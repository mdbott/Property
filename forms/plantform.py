# -*- encoding: utf-8 -*-

from PyQt4.QtCore import *
from qgis.core import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *
try:
    from PyQt4.QtCore import QString
except ImportError:
    QString = str
__author__ = 'max'
myDialog = None


def formOpen(dialog, layer, feature):
    mydialog = myDialog(dialog, layer, feature)


class myDialog:
    def __init__(self, dialog, layer, feature):
        self.dlg = dialog
        self.layerid = layer
        self.featureid = feature

        provider = layer.dataProvider()
        #app = QtCore.QCoreApplication(sys.argv)
        #QMessageBox.information(None, "DEBUG:", str(provider.name()))
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
                #query = QSqlQuery("""select genus,species from plantdb_plant where genus = 'Prunus'""")
                query = db.exec_("""select genus,species from plantdb_plant where genus = 'Prunus'""")
                #QMessageBox.information(None, "DEBUG:", str(query.record().count()))
            else:
                QMessageBox.information(None, "DEBUG:", str('Add the qt postgresql driver with  apt-get install libqt4-sql-psql'))
            # database = 'plantdb'
            # username = 'postgres'
            # password = ''
            # table = 'testing'
            # srid = 4326
            # dimension = 2
            # typmod = 'POINT'
            #
            # db2 = QSqlDatabase.addDatabase('QPSQL')
            #
            # uri = QgsDataSourceURI()
            # uri.setConnection('192.168.1.100', '5432', database, username, password)
            # uri.setDataSource('public', table, 'the_geom', '')
            #
            # db2.setHostName(uri.host())
            # db2.setPort(int(uri.port()))
            # db2.setDatabaseName(uri.database())
            # db2.setUserName(uri.username())
            # db2.setPassword(uri.password())
            # QMessageBox.information(None, "DEBUG:", str(db2.isValid()))

        # Create plantcombobox model
        self.plantcombobox = self.dlg.findChild(QComboBox, "plantid")
        self.cultivarcombobox = self.dlg.findChild(QComboBox, "cultivarid")
        self.rootstockcombobox = self.dlg.findChild(QComboBox, "rootstockid")

        currentcomboindex = self.plantcombobox.currentText()
        currentcultivarindex = self.cultivarcombobox.currentText()
        currentrootstockindex = self.rootstockcombobox.currentText()
        QMessageBox.information(None, "DEBUG:", 'plantid: '+str(currentcomboindex))
        QMessageBox.information(None, "DEBUG:", 'cultivarid: '+str(currentcultivarindex))
        QMessageBox.information(None, "DEBUG:", 'rootstockid: '+str(currentrootstockindex))
        self.plantingmodel = QSqlRelationalTableModel(self.dlg, self.db)
        self.plantingmodel.setTable('plantdb_vegetation')
        self.plantingmodel.setRelation(2, QSqlRelation("plantdb_plant", "id", "legacy_pfaf_latin_name"))
        self.plantingmodel.setRelation(3, QSqlRelation("plantdb_cultivar", "id", "name"))
        self.plantingmodel.setRelation(4, QSqlRelation("plantdb_rootstock", "id", "rootstockname"))
        self.plantingmodel.setSort(1, Qt.AscendingOrder)
        self.plantingmodel.select()
        index = self.plantingmodel.index(0,0)
        self.plantingmodel.setCurrentIndex(index)
        #self.dlg.setItemDelegate(QSqlRelationalDelegate(self.dlg))
        #self.dlg.setCurrentIndex(self.plantingmodel.index(0))

        self.mapper = QDataWidgetMapper(self.dlg)
        self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
        self.mapper.setModel(self.plantingmodel)
        row = self.plantingmodel.rowCount()
        self.mapper.setItemDelegate(QSqlRelationalDelegate(self.dlg))

        plantrelationModel = self.plantingmodel.relationModel(2)
        cultivarrelationModel = self.plantingmodel.relationModel(3)
        rootstockrelationModel = self.plantingmodel.relationModel(4)

        self.plantcombobox.setModel(plantrelationModel)
        self.plantcombobox.setModelColumn(plantrelationModel.fieldIndex("legacy_pfaf_latin_name"))
        self.mapper.addMapping(self.plantcombobox, 3)


        self.cultivarcombobox.setModel(cultivarrelationModel)
        #self.dlg.cultivarcombomodel = cultivarrelationModel
        self.cultivarcombobox.setModelColumn(cultivarrelationModel.fieldIndex("name"))
        self.mapper.addMapping(self.cultivarcombobox, 5)

        self.rootstockcombobox.setModel(rootstockrelationModel)
        self.plantcombobox.setModelColumn(rootstockrelationModel.fieldIndex("rootstockname"))
        self.mapper.addMapping(self.rootstockcombobox, 6)











        # self.plantcombomodel = QSqlTableModel(self.plantCombobox, self.db)
        # self.plantcombomodel.setTable('plantdb_plant')
        # self.plantcombomodel.select()
        # newcombobox_query = QSqlQuery(db=self.db)
        # newcombobox_query.prepare("SELECT legacy_pfaf_latin_name FROM plantdb_plant WHERE id=:id")
        # newcombobox_query.bindValue(":id", currentcomboindex)
        # newcombobox_query.exec_()
        # QMessageBox.information(None, "DEBUG:", str(newcombobox_query.first()))
        # # self.plantcombomodel.data(self.plantcombomodel.index(currentcomboindex, self.plantcombomodel.fieldIndex("id"))).toString()
        #
        # self.plantCombobox.setModel(self.plantcombomodel)
        # self.plantCombobox.setModelColumn(self.plantcombomodel.fieldIndex("legacy_pfaf_latin_name"))
        # currentplantid = str(self.plantCombobox.itemData(self.plantCombobox.currentIndex()))
        #
        #
        #
        #
        #
        # # Create cultivarcombobox model
        # self.cultivarCombobox = self.dlg.findChild(QComboBox, "cultivarid")
        # self.cultivarcombomodel = QSqlTableModel(self.cultivarCombobox, self.db)
        # self.cultivarcombomodel.setTable("plantdb_cultivar")
        # cultivarfilter = QString('plant_id = ' + currentplantid)
        # self.cultivarcombomodel.setFilter(cultivarfilter)
        #
        # self.cultivarcombomodel.select()
        #
        # # Create rootstockcombobox model
        # self.rootstockCombobox = self.dlg.findChild(QComboBox, "rootstockid")
        # self.rootstockcombomodel = QSqlTableModel(self.rootstockCombobox, self.db)
        # self.rootstockcombomodel.setTable("plantdb_rootstock")
        # rootstockfilter = QString('plant_id = ' + currentplantid)
        # self.rootstockcombomodel.setFilter(rootstockfilter)
        # self.rootstockcombomodel.select()
        #
        #
        #
        #
        # self.cultivarCombobox.setModel(self.cultivarcombomodel)
        # self.cultivarCombobox.setModelColumn(self.cultivarcombomodel.fieldIndex("name"))
        # self.rootstockCombobox.setModel(self.rootstockcombomodel)
        # self.rootstockCombobox.setModelColumn(self.rootstockcombomodel.fieldIndex("name"))
        self.plantcombobox.currentIndexChanged[str].connect(self.printMsg)
        self.plantcombobox.highlighted[int].connect(self.printMsg)
        self.mapper.setCurrentIndex(row)
        QMessageBox.information(None, "DEBUG:", 'current index: '+str(self.mapper.currentIndex()))

        currentcomboindex = self.plantcombobox.currentText()
        currentcultivarindex = self.cultivarcombobox.currentText()
        currentrootstockindex = self.rootstockcombobox.currentText()
        QMessageBox.information(None, "DEBUG:", 'plantid: '+str(currentcomboindex))
        QMessageBox.information(None, "DEBUG:", 'cultivarid: '+str(currentcultivarindex))
        QMessageBox.information(None, "DEBUG:", 'rootstockid: '+str(currentrootstockindex))

        # When you change the value for plant widget, change the content of the cultivar widget
        #self.plantcombobox.currentIndexChanged.connect(lambda: self.populateDependantCombobox(self.cultivarcombobox, self.plantcombobox))



    def getDistrictCeiRoute(self):
        db = spatialite_utils.GeoDB(sqlitePath)
        sql = """SELECT * FROM reseau_metadata"""
        cursor = db.con.cursor()
        db._exec_sql(cursor,sql)
        return cursor.fetchall()

    def printMsg(self):
        QgsMessageLog.logMessage(str(self.plantcombobox.count()), "essai", 0)

    def populateDependantCombobox(self, widget, parent_widget):
        """Generic function to manage cascading QComboBox.
           * widget: widget object (QComboBox) to control
           * parent_widget: get the value from the parent QComboBox widget"""

        # Get the value of the parent QComboBox
        newplantid = str(parent_widget.itemData(parent_widget.currentIndex()))
        cultivarfilter = QString('plant_id = ' + newplantid)
        rootstockfilter = QString('plant_id = ' + newplantid)
        self.cultivarcombomodel.setFilter(cultivarfilter)
        self.rootstockcombomodel.setFilter(rootstockfilter)


class Delegate(QSqlRelationalDelegate):
    """
    Delegate class handles the delegate. This allows for custom editing within
    the GUI. QtSql.QSqlRelationalDelegate is being subclassed to support custom editing.

    Methods that are being overridden are:
        createEditor
        setEditorData
        setModelData
    """

    def __init__(self, parent = None):
        """Class constructor."""

        super(Delegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        """
        This creates the editors in the delegate, which is reimplemented from
        QAbstractItemDelegate::createEditor(). It returns the widget used to edit
        the item specified by index for editing. The parent widget and style option
        are used to control how the editor widget appears.
        """

        column = index.column()

        if column == 1:
            editor = QtGui.QLineEdit(parent)
            regex = QtCore.QRegExp(r"[a-zA-Z][a-zA-Z0-9_]{3,60}")
            validator = QtGui.QRegExpValidator(regex,parent)
            editor.setValidator(validator)
            return editor

        # Else return the base editor. This will handle all other columns.
        else:
            return super(AppDelegate, self).createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        """
         Once the editor has been created and given to the view, the view calls
         setEditorData(). This gives the delegate the opportunity to populate the
         editor with the current data, ready for the user to edit.

        Sets the contents of the given editor to the data for the item
        at the given index.

        Note that the index contains information about the model being used.

        The base implementation does nothing.
        If you want custom editing you will need to reimplement this function.
        """

        column = index.column()

        # Get the data value from the model.
        text = index.model().data(index, QtCore.Qt.DisplayRole).toString()

        # Set the editors text to be the text from the model.
        if column == 1:
            editor.setText(text)

        # Else return the base setEditorData method.
        # This is not strictly needed because in flags the ID column is set
        # to be selectable only so it should never call setEditorData.
        else:
            return super(AppDelegate, self).setEditorData(self, editor, index)

    def setModelData(self, editor, model, index):
        """
        Sets the data for the item at the given index in the model
        to the contents of the given editor. The base implementation does
        nothing.
        If you want custom editing you will need to reimplement this method.

        If the user confirms their edit the editor's data must be written
        back to the model. The model will then notify the views that the item
        has changed, and those views that are showing the item
        will request fresh data to display.

        In each case we simply retrieve the value from the appropriate editor,
        and call setData (), passing the values as QVariants.
        """

        column = index.column()

        # Test if the editor has been modified.
        if not editor.isModified():
            return

        # This ensure that validation passes.
        text = editor.text()
        validator = editor.validator()
        if validator is not None:
            state, text = validator.validate(text, 0)
            if state != QtGui.QValidator.Acceptable:
                return

        if column == 1:
            # Call model.setData and set the data to the text in the QLineEdit.
            # After the user confirms the edit then set the model data to the
            # new user input.
            model.setData(index, QtCore.QVariant(editor.text()))

        # else return the base setModelData method.
        else:
            super(AppDelegate, self).setModelData(self, editor, model, index)


