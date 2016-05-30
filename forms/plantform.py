# -*- encoding: utf-8 -*-

from PyQt4.QtCore import (QDate, QDateTime, QFile, QVariant, Qt, QEvent, SIGNAL)
from PyQt4.QtGui import (QApplication, QComboBox, QCursor,
        QDataWidgetMapper, QDateTimeEdit, QDialog, QGridLayout,
        QHBoxLayout, QIcon, QLabel, QLineEdit, QMessageBox, QPixmap,
        QPushButton, QVBoxLayout, QWidget, QCheckBox, QDialogButtonBox)
from PyQt4.QtSql import (QSqlDatabase, QSqlQuery, QSqlRelation, QSqlTableModel, QSqlQuery,
        QSqlRelationalDelegate, QSqlRelationalTableModel, QSqlIndex, QSqlField)
from qgis.core import *

import sys
#import vegetation
try:
    from PyQt4.QtCore import QString
except ImportError:
    QString = str
__author__ = 'max'
myDialog = None

ROWNUMBER, ID, PLANTID, ROOTSTOCKID, CULTIVARID, LATINNAME, FAMILY, GENUS, SPECIES, SSP, COMMONNAME, FUNCTION, BORDER, \
    FILL, SYMBOL, FORM, LOCATIONS, WIDTH, HEIGHT, GRAFTED, COMMENT,  GERMINATIONDATE = range(22)


def formOpen(dialog, layer, feature):
    mydialog = myDialog(dialog, layer, feature)


class myDialog:
    def __init__(self, dialog, layer, feature):
        self.dlg = dialog
        self.layerid = layer
        self.featureid = feature
        self.create_model()
        self.create_connections()
        self.validate_data()

    def create_model(self):
        provider = self.layerid.dataProvider()
        if provider.name() == 'postgres':
            # get the URI containing the connection parameters
            uri = QgsDataSourceURI(provider.dataSourceUri())
            #QMessageBox.information(None, "DEBUG:", str(uri.uri()))
            # create a PostgreSQL connection using QSqlDatabase
            #QSqlDatabase.__init__(QSqlDatabase, "QPSQL")
            db = QSqlDatabase.addDatabase('QPSQL')
            #QMessageBox.information(None, "DEBUG:", str(db.isValid()))
            # check to see if it is valid
            if db.isValid():
                print "QPSQL db is valid"
                # set the parameters needed for the connection
                db.setHostName(uri.host())
                #QMessageBox.information(None, "DEBUG:", str(uri.host()))
                db.setDatabaseName(uri.database())
                db.setPort(int(uri.port()))
                db.setUserName(uri.username())
                db.setPassword(uri.password())
                db.authcfg = None
                self.db = db
                self.db.open()
            else:
                QMessageBox.information(None, "DEBUG:", str('Add the qt postgresql driver with  apt-get install libqt4-sql-psql'))

        # Attach form widget
        self.plantingid = self.dlg.findChild(QLineEdit, "row_number")
        self.plantid = self.dlg.findChild(QComboBox, "plantcomboBox")
        self.cultivarid = self.dlg.findChild(QComboBox, "cultivarcomboBox")
        self.rootstockid = self.dlg.findChild(QComboBox, "rootstockcomboBox")
        self.commonname = self.dlg.findChild(QComboBox, "name")
        self.grafted = self.dlg.findChild(QCheckBox, "grafted")
        self.buttonBox = self.dlg.findChild(QDialogButtonBox, "buttonBox")

        self.plantpk = self.dlg.findChild(QLineEdit, "plantid")
        self.cultivarpk = self.dlg.findChild(QLineEdit, "cultivarid")
        self.rootstockpk = self.dlg.findChild(QLineEdit, "rootstockid")
        try:
            currentplantingindex = int(self.plantingid.text())-1
        except ValueError:
            currentplantingindex = ''
        try:
            currentplant = int(self.plantpk.text())
        except ValueError:
            currentplant = ''
        # currentplantingindex = int(self.plantingid.text())-1
        currentcomboindex = self.plantid.currentText()
        currentcultivarindex = self.cultivarid.currentText()
        currentrootstockindex = self.rootstockid.currentText()

        # Store original qcombobox models

        # self.originalplantmodel = self.plantid.model()
        # self.originalcultivarmodel = self.cultivarid.model()
        # self.originalrootstockmodel = self.rootstockid.model()

        #QMessageBox.information(None, "DEBUG:", 'planting id: '+str(currentplantingindex))
        #QMessageBox.information(None, "DEBUG:", 'plantid: '+str(currentcomboindex))
        #QMessageBox.information(None, "DEBUG:", 'cultivarid: '+str(currentcultivarindex))
        #QMessageBox.information(None, "DEBUG:", 'rootstockid: '+str(currentrootstockindex))

        self.model = QSqlRelationalTableModel(self.dlg, self.db)
        self.model.setTable("plantdb_vegetationview")

        self.model.setRelation(PLANTID, QSqlRelation("plantdb_plant", "id", "legacy_pfaf_latin_name"))
        self.model.setRelation(CULTIVARID, QSqlRelation("plantdb_cultivar", "id", "name"))
        self.model.setRelation(ROOTSTOCKID, QSqlRelation("plantdb_rootstock", "id", "rootstockname"))

        pk = QSqlIndex("cursor", "idxName")
        pk.append(QSqlField("row_number"))
        self.model.setPrimaryKey(pk)
        self.model.setSort(ROWNUMBER, Qt.AscendingOrder)
        self.model.select()

        # define the relation models
        self.plantmodel = self.model.relationModel(PLANTID)
        self.cultivarmodel = self.model.relationModel(CULTIVARID)
        self.rootstockmodel = self.model.relationModel(ROOTSTOCKID)

        # define mapper
        # establish ties between underlying database model and data widgets on form
        self.mapper = QDataWidgetMapper(self.dlg)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.plantingid, ROWNUMBER)
        plantDelegate = GenericDelegate(self.dlg)
        plantDelegate.insertColumnDelegate(CULTIVARID, CultivarComboBoxDelegate(self.dlg, self))
        plantDelegate.insertColumnDelegate(ROOTSTOCKID, RootstockComboBoxDelegate(self.dlg, self))
        self.mapper.setItemDelegate(plantDelegate)

        # Plant combobox
        self.plantid.setModel(self.plantmodel)
        self.plantid.setModelColumn(
                self.plantmodel.fieldIndex("legacy_pfaf_latin_name"))
        self.mapper.addMapping(self.plantid, PLANTID)

        # Common Name combobox
        self.commonnamemodel = QSqlTableModel(self.dlg, self.db)
        self.commonnamemodel.setTable("plantdb_plant")
        self.commonnamemodel.setSort(7, Qt.AscendingOrder)
        self.commonnamemodel.select()
        self.commonnamemapper = QDataWidgetMapper(self.dlg)
        self.commonnamemapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.commonnamemapper.setModel(self.commonnamemodel)
        self.commonnamemapper.addMapping(self.commonname, 7)
        # self.commonnamemapper.toFirst()
        self.commonname.setModel(self.commonnamemodel)
        self.commonname.setModelColumn(7)

        # Cultivar combobox
        self.cultivarid.setModel(self.cultivarmodel)
        self.cultivarid.setModelColumn(
                self.cultivarmodel.fieldIndex("name"))
        self.mapper.addMapping(self.cultivarid, CULTIVARID)

        # Rootstock combobox
        self.rootstockid.setModel(self.rootstockmodel)
        self.rootstockid.setModelColumn(
                self.rootstockmodel.fieldIndex("rootstockname"))
        self.mapper.addMapping(self.rootstockid, ROOTSTOCKID)
        self.rootstockid.readonly = False
        self.rootstockid.installEventFilter(self.dlg)
        self.mapper.addMapping(self.grafted, GRAFTED)

        self.mapper.toFirst()
        # pid = self.plantingid.text()
        # QMessageBox.information(None, "DEBUG:", 'initial row number: '+pid)
        # row = self.mapper.currentIndex()
        if currentplantingindex != '':
            row = currentplantingindex
            self.mapper.setCurrentIndex(row)
        else:
            row = self.model.rowCount()
            self.mapper.submit()
            self.model.insertRow(row)
            self.mapper.setCurrentIndex(row)
            self.plantid.setCurrentIndex(self.plantid.findText('Malus Domestica', Qt.MatchExactly))

        if currentplant != '':
            # QMessageBox.information(None, "DEBUG:", 'plant primary key: '+str(currentplant))
            query = QSqlQuery()
            query.prepare('select common_name from plantdb_plant where id = ?')
            query.addBindValue(str(currentplant))
            query.exec_()
            if query.next():
                currentname = query.value(0)
                # QMessageBox.information(None, "DEBUG:", 'plant common name: '+str(currentname))
                # cnindex = self.commonnamemodel.createIndex(currentplant, 0)
                self.commonname.setCurrentIndex(self.commonname.findText(currentname, Qt.MatchExactly))


        pid = self.plantingid.text()
        # QMessageBox.information(None, "DEBUG:", 'final row number: '+pid)

    def create_connections(self):
        self.plantid.currentIndexChanged.connect(self.updateComboboxes)
        self.cultivarid.currentIndexChanged.connect(self.updateRootstocklist)
        self.grafted.stateChanged.connect(self.updateGrafted)
        self.commonname.currentIndexChanged.connect(self.updatefromCommonname)

    def updateGrafted(self):
        # get grafted state
        pid = int(self.plantingid.text())-1
        graftedindex = self.model.createIndex(pid, GRAFTED)
        isgrafted = self.model.data(graftedindex, Qt.DisplayRole)
        self.rootstockid.blockSignals(True)
        self.rootstockmodel.setFilter("")
        if self.grafted.isChecked():
            plantIndex = self.plantid.currentIndex()
            plant_id = self.plantmodel.record(plantIndex).value("id")
            # QMessageBox.critical(self, 'Grafted: filter', "plant_id = {}".format(plant_id), str(self.grafted.isChecked()))
            self.rootstockmodel.setFilter("plant_id = {}".format(plant_id))
            rootstockIndex = self.rootstockid.currentIndex()
            rootstock_id = self.rootstockmodel.record(rootstockIndex).value("id")
            self.rootstockpk.setText(str(rootstock_id))
        else:
            cultivarIndex = self.cultivarid.currentIndex()
            native_rootstock = self.cultivarmodel.record(cultivarIndex).value("native_rootstock_id")

            # QMessageBox.critical(self, 'Not Grafted: filter', "id = {}".format(native_rootstock))
            self.rootstockmodel.setFilter("id = {}".format(native_rootstock))
            self.rootstockpk.setText(str(native_rootstock))
        self.rootstockid.blockSignals(False)

    def updatefromCommonname(self):
        # get plantid

        # QMessageBox.information(None, "DEBUG:", 'commonname  text: '+str(self.commonname.currentText()))
        commonnameIndex = self.commonname.currentIndex()
        plant_id = self.commonnamemodel.record(commonnameIndex).value("id")
        # QMessageBox.information(None, "DEBUG:", 'commonname  text: '+str(plant_id))
        #
        self.plantid.blockSignals(True)
        self.cultivarid.blockSignals(True)
        self.rootstockid.blockSignals(True)
        self.plantpk.setText(str(plant_id))
        query = QSqlQuery()
        query.prepare('select legacy_pfaf_latin_name from plantdb_plant where id = ?')
        query.addBindValue(str(plant_id))
        query.exec_()
        if query.next():
            newname = query.value(0)
            self.plantid.setCurrentIndex(self.plantid.findText(newname, Qt.MatchExactly))
        self.cultivarmodel.setFilter("")
        self.rootstockmodel.setFilter("")
        # QMessageBox.critical(self, 'filter', "plant_id = {}".format(plant_id))
        self.cultivarmodel.setFilter("plant_id = {}".format(plant_id))
        cultivarIndex = self.cultivarid.currentIndex()
        cultivar_id = self.cultivarmodel.record(cultivarIndex).value("id")
        self.cultivarpk.setText(str(cultivar_id))

        pid = int(self.plantingid.text())-1
        graftedindex = self.model.createIndex(pid, GRAFTED)
        isgrafted = self.model.data(graftedindex, Qt.DisplayRole)

        if self.grafted.isChecked():
            self.rootstockmodel.setFilter("plant_id = {}".format(plant_id))
            rootstockIndex = self.rootstockid.currentIndex()
            rootstock_id = self.rootstockmodel.record(rootstockIndex).value("id")
            self.rootstockpk.setText(str(rootstock_id))
        else:
            cultivarIndex = self.cultivarid.currentIndex()
            native_rootstock = self.cultivarmodel.record(cultivarIndex).value("native_rootstock_id")
            self.rootstockmodel.setFilter("id = {}".format(native_rootstock))
            self.rootstockpk.setText(str(native_rootstock))

        self.plantid.blockSignals(False)
        self.cultivarid.blockSignals(False)
        self.rootstockid.blockSignals(False)

    def updateComboboxes(self):
        # get plantid
        plantIndex = self.plantid.currentIndex()
        plant_id = self.plantmodel.record(plantIndex).value("id")
        #QMessageBox.information(None, "DEBUG:", 'plant primary key: '+str(self.plantpk.text()))
        self.plantpk.setText(str(plant_id))
        #QMessageBox.critical(self, 'Results', str(plant_id))
        self.commonname.blockSignals(True)
        self.cultivarid.blockSignals(True)
        self.rootstockid.blockSignals(True)

        query = QSqlQuery()
        query.prepare('select common_name from plantdb_plant where id = ?')
        query.addBindValue(str(plant_id))
        query.exec_()
        if query.next():
            newname = query.value(0)
            self.commonname.setCurrentIndex(self.commonname.findText(newname, Qt.MatchExactly))

        self.cultivarmodel.setFilter("")
        self.rootstockmodel.setFilter("")
        # QMessageBox.critical(self, 'filter', "plant_id = {}".format(plant_id))
        self.cultivarmodel.setFilter("plant_id = {}".format(plant_id))
        cultivarIndex = self.cultivarid.currentIndex()
        cultivar_id = self.cultivarmodel.record(cultivarIndex).value("id")
        self.cultivarpk.setText(str(cultivar_id))

        pid = int(self.plantingid.text())-1
        graftedindex = self.model.createIndex(pid, GRAFTED)
        isgrafted = self.model.data(graftedindex, Qt.DisplayRole)

        if self.grafted.isChecked():
            self.rootstockmodel.setFilter("plant_id = {}".format(plant_id))
            rootstockIndex = self.rootstockid.currentIndex()
            rootstock_id = self.rootstockmodel.record(rootstockIndex).value("id")
            self.rootstockpk.setText(str(rootstock_id))
        else:
            cultivarIndex = self.cultivarid.currentIndex()
            native_rootstock = self.cultivarmodel.record(cultivarIndex).value("native_rootstock_id")
            self.rootstockmodel.setFilter("id = {}".format(native_rootstock))
            self.rootstockpk.setText(str(native_rootstock))
        self.commonname.blockSignals(False)
        self.cultivarid.blockSignals(False)
        self.rootstockid.blockSignals(False)

    def updateRootstocklist(self):
        # get plantid
        plantIndex = self.plantid.currentIndex()
        plant_id = self.plantmodel.record(plantIndex).value("id")
        # QMessageBox.critical(self, 'Results', str(plant_id))

        self.rootstockid.blockSignals(True)


        cultivarIndex = self.cultivarid.currentIndex()
        cultivar_id = self.cultivarmodel.record(cultivarIndex).value("id")
        self.cultivarpk.setText(str(cultivar_id))

        self.rootstockmodel.setFilter("")

        pid = int(self.plantingid.text())-1
        graftedindex = self.model.createIndex(pid, GRAFTED)
        isgrafted = self.model.data(graftedindex, Qt.DisplayRole)

        if self.grafted.isChecked():
            #QMessageBox.critical(self, 'rootstock filter', "plant_id = {}".format(plant_id))
            self.rootstockmodel.setFilter("plant_id = {}".format(plant_id))
            rootstockIndex = self.rootstockid.currentIndex()
            rootstock_id = self.rootstockmodel.record(rootstockIndex).value("id")
            self.rootstockpk.setText(str(rootstock_id))
        else:
            cultivarIndex = self.cultivarid.currentIndex()
            native_rootstock = self.cultivarmodel.record(cultivarIndex).value("native_rootstock_id")
            #QMessageBox.critical(self, 'Not grafted: rootstock filter', "id = {}".format(native_rootstock))
            self.rootstockmodel.setFilter("id = {}".format(native_rootstock))
            self.rootstockpk.setText(str(native_rootstock))
        #QMessageBox.critical(self, 'Current rootstock filter', str(self.rootstockmodel.filter()))
        self.rootstockid.blockSignals(False)

    def validate_data(self):
        # Disconnect the signal that QGIS has wired up for the dialog to the button box.

        self.buttonBox.accepted.disconnect(self.dlg.accept)
        self.buttonBox.accepted.connect(self.validate)
        self.buttonBox.rejected.connect(self.dlg.reject)

    def validate(self):
        # Make sure that the name field isn't empty.

        # get final plantid
        plantIndex = self.plantid.currentIndex()
        plant_id = self.plantid.model().record(plantIndex).value("id")
        # get final cultivarid
        cultivarIndex = self.cultivarid.currentIndex()
        cultivar_id = self.cultivarid.model().record(cultivarIndex).value("id")
        # get final rootstockid
        rootstockIndex = self.rootstockid.currentIndex()
        rootstock_id = self.rootstockid.model().record(rootstockIndex).value("id")
        # self.mapper.submit()
        # QMessageBox.information(None, "DEBUG:", 'plantid: '+str(plant_id))
        # QMessageBox.information(None, "DEBUG:", 'cultivarid: '+str(cultivar_id))
        # QMessageBox.information(None, "DEBUG:", 'rootstockid: '+str(rootstock_id))
        self.mapper.removeMapping(self.plantid)
        self.mapper.removeMapping(self.cultivarid)
        self.mapper.removeMapping(self.rootstockid)
        # self.plantid.currentIndexChanged.disconnect()
        # self.cultivarid.currentIndexChanged.disconnect()
        # self.grafted.stateChanged.disconnect()
        # self.plantid.setModel(self.originalplantmodel)
        # self.cultivarid.setModel(self.originalcultivarmodel)
        # self.rootstockid.setModel(self.originalrootstockmodel)

        # newplantindex = self.plantid.findText(str(plant_id))
        # newcultivarindex = self.plantid.findText(str(cultivar_id))
        # newrootstockindex = self.plantid.findText(str(rootstock_id))

        # if newplantindex >= 0:
        #     self.plantid.setCurrentIndex(newplantindex)
        # if newcultivarindex >= 0:
        #     self.cultivarid.setCurrentIndex(newcultivarindex)
        # if newrootstockindex >= 0:
        #     self.rootstockid.setCurrentIndex(newrootstockindex)
        # currentcomboindex = self.plantid.currentText()
        # currentcultivarindex = self.cultivarid.currentText()
        # currentrootstockindex = self.rootstockid.currentText()
        # QMessageBox.information(None, "DEBUG:", 'plant text: '+str(currentcomboindex))
        # QMessageBox.information(None, "DEBUG:", 'cultivar text: '+str(currentcultivarindex))
        # QMessageBox.information(None, "DEBUG:", 'rootstock text: '+str(currentrootstockindex))

        self.dlg.accept()
        # if not self.plantingid.text().length() == 0:
        #     msgBox = QMessageBox()
        #     msgBox.setText("Name field can not be null.")
        #     msgBox.exec_()
        # else:
        #     # Return the form as accpeted to QGIS.
        #     self.dlg.accept()


class CultivarComboBoxDelegate(QSqlRelationalDelegate):
    """Implements custom delegate for Cultivar combobox in the Plant dialog.

    Filters the cultivar combobox to show the cultivars relevant to the selected plant table.

    Inherits QSqlRelationalDelegate.
    """

    def __init__(self, parent, parentinst):
        """Constructor for RootstockComboBoxDelegate class."""
        super(CultivarComboBoxDelegate, self).__init__(parent)
        self.plantid = parentinst.plantid

    def setEditorData(self, editor, index):
        """Writes current data from model into editor.

        Filters contents of combobox so that only options are the shootout rounds not referenced
        twice in the Penalty Shootout table.

        Arguments:
            editor -- ComboBox widget
            index -- current index of database table model for the cultivar column

        """
        plantingModel = index.model()
        cultivarModel = editor.model()
        plantModel = self.plantid.model()
        # block signals from player combobox so that EnableWidget() is not called multiple times
        editor.blockSignals(True)
        # clear filters
        cultivarModel.setFilter(QString())
        # current plant name and ID
        cultivarName = plantingModel.data(index, Qt.DisplayRole)
        # get plantid
        plantIndex = self.plantid.currentIndex()
        plant_id = plantModel.record(plantIndex).value("id")

        cultivarModel.select()
        # cultivarText = plantingModel.data(index, Qt.DisplayRole).toString()
        cultivarModel.setFilter("plant_id = {}".format(plant_id))
        try:
            editor.setCurrentIndex(editor.findText(cultivarName, Qt.MatchExactly))
        except TypeError:
            pass
        editor.blockSignals(False) # unblock signals from player combobox

    def setModelData(self, editor, model, index):
        """Maps round name to ID number in Rounds model, and writes ID to the current entry in the database table.

        Arguments:
            editor -- ComboBox widget
            model -- underlying database table model
            index -- current index of database table model

        """
        cultivarIndex = editor.currentIndex()
        value = editor.model().record(cultivarIndex).value("id")
        model.setData(index, value)


class RootstockComboBoxDelegate(QSqlRelationalDelegate):
    """Implements custom delegate for Rootstock combobox in the Plant dialog.

    Filters the rootstock combobox to show the rootstocks relevant to the selected plant table.

    Inherits QSqlRelationalDelegate.
    """

    def __init__(self, parent, parentinst):
        """Constructor for RootstockComboBoxDelegate class."""
        super(RootstockComboBoxDelegate, self).__init__(parent)
        self.plantid = parentinst.plantid
        self.grafted = parentinst.grafted
        self.cultivarid = parentinst.cultivarid
        self.parent = parentinst

    def setEditorData(self, editor, index):
        """Writes current data from model into editor.

        Filters contents of combobox so that only options are the shootout rounds not referenced
        twice in the Penalty Shootout table.

        Arguments:
            editor -- ComboBox widget
            index -- current index of database table model for the rootstock column

        """
        plantingModel = index.model()
        rootstockModel = editor.model()
        cultivarmodel = self.cultivarid.model()
        plantModel = self.plantid.model()

        # block signals from player combobox so that EnableWidget() is not called multiple times
        editor.blockSignals(True)

        # clear filters
        rootstockModel.setFilter(QString())

        # current plant name and ID
        rootstockName = plantingModel.data(index, Qt.DisplayRole)
        pid = int(self.parent.plantingid.text())-1
        graftedindex = self.parent.model.createIndex(pid, GRAFTED)
        isgrafted = self.parent.model.data(graftedindex, Qt.DisplayRole)
        # get plantid
        plantIndex = self.plantid.currentIndex()
        plant_id = plantModel.record(plantIndex).value("id")
        # get native rootstock
        cultivarIndex = self.cultivarid.currentIndex()
        native_rootstock = cultivarmodel.record(cultivarIndex).value("native_rootstock_id")

        rootstockModel.select()

        # get Grafted status
        if isgrafted:
            print "Model Grafted"
            rootstockModel.setFilter("plant_id = {}".format(plant_id))
            try:
                editor.setCurrentIndex(editor.findText(rootstockName, Qt.MatchExactly))
            except TypeError:
                pass
        else:
            print "Model Not Grafted"
            rootstockModel.setFilter("id = {}".format(native_rootstock))
            try:
                editor.setCurrentIndex(editor.findText(rootstockName, Qt.MatchExactly))
            except TypeError:
                pass

        # unblock signals from player combobox
        editor.blockSignals(False)

    def setModelData(self, editor, model, index):
        """Maps round name to ID number in Rounds model, and writes ID to the current entry in the database table.

        Arguments:
            editor -- ComboBox widget
            model -- underlying database table model
            index -- current index of database table model

        """

        plantingModel = index.model()
        cultivarmodel = self.cultivarid.model()
        pid = int(self.parent.plantingid.text())-1
        # print int(self.parent.plantingid.text())-1, self.parent.plantingid.text().toInt()[0]-1
        graftedindex = self.parent.model.createIndex(pid, GRAFTED)
        isgrafted = self.parent.model.data(graftedindex, Qt.DisplayRole)
        cultivarIndex = self.cultivarid.currentIndex()
        native_rootstock = cultivarmodel.record(cultivarIndex).value("native_rootstock_id")

        rootstockIndex = editor.currentIndex()
        value = editor.model().record(rootstockIndex).value("id")
        # model.setData(index, value)
        if isgrafted:
           model.setData(index, value)
        else:
           model.setData(index, native_rootstock)


class GenericDelegate(QSqlRelationalDelegate):
    """Implements generic components of UI delegates.

    This class is designed to accommodate a list of custom column delegates.
    Can implement either baseclass paint(), createEditor(), setEditorData() and
    setModelData() methods or custom methods if defined by the subclass.

    Source: "Rapid GUI Programming with Python and Qt" by Mark Summerfield,
    Prentice-Hall, 2008, pg. 483-486.

    Inherits QSqlRelationalDelegate.

    """

    def __init__(self, parent=None):
        """Constructor for GenericDelegate class.

        Defines delegates member as empty dictionary.  Keys will be column numbers.

        """
        super(GenericDelegate, self).__init__(parent)
        self.delegates = {}

    def insertColumnDelegate(self, column, delegate):
        """Inserts delegate and column number in delegate dictionary."""
        delegate.setParent(self)
        self.delegates[column] = delegate

    def removeColumnDelegate(self, column):
        """Removes delegate from delegate dictionary."""
        if column in self.delegates:
            del self.delegates[column]

    def paint(self, painter, option, index):
        """Calls either custom or baseclass paint methods for widget.

        Custom method is called if delegate is defined for the column.
        Base class method is called otherwise.

        """
        delegate = self.delegates.get(index.column())
        if delegate is not None:
            delegate.paint(painter, option, index)
        else:
            QSqlRelationalDelegate.paint(self, painter, option, index)

    def createEditor(self, parent, option, index):
        """Calls either custom or baseclass editor creation methods for widget.

        Custom method is called if delegate is defined for the column.
        Base class method is called otherwise.

        """
        delegate = self.delegates.get(index.column())
        if delegate is not None:
            return delegate.createEditor(parent, option, index)
        else:
            return QSqlRelationalDelegate.createEditor(self, parent, option, index)

    def setEditorData(self, editor, index):
        """Calls either custom or standard models to write data from database model to editor.

        Custom method is called if delegate is defined for the column.
        Base class method is called otherwise.

        """
        delegate = self.delegates.get(index.column())
        if delegate is not None:
            delegate.setEditorData(editor, index)
        else:
            QSqlRelationalDelegate.setEditorData(self, editor, index)

    def setModelData(self, editor, model, index):
        """Calls either custom or standard methods to write data from editor to database model.

        Custom method is called if delegate is defined for the column.
        Base class method is called otherwise.

        """
        delegate = self.delegates.get(index.column())
        if delegate is not None:
            delegate.setModelData(editor, model, index)
        else:
            QSqlRelationalDelegate.setModelData(self, editor, model, index)
