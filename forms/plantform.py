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

MoistureLevel = {1: 'Dry',
                 2: 'Moist',
                 3: 'Wet',
                 4: 'Water'}

MoistureLevel_reverse = dict(reversed(item) for item in MoistureLevel.items())

SoilTexture = {1: 'Light (sandy) soil',
               2: 'Medium (loamy) soil',
               3: 'Heavy (clay) soil'}

SoilTexture_reverse = dict(reversed(item) for item in SoilTexture.items())

SalinityLevel = {
        1: 'Low 2-4 dS/m',
        2: 'Medium 4-8 dS/m',
        3: 'High 8+ dS/m'
}

SalinityLevel_reverse = dict(reversed(item) for item in SalinityLevel.items())

MonthRange ={
    0: 'December',
    1: 'January',
    2: 'Feburary',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

MonthRange_reverse = dict(reversed(item) for item in MonthRange.items())

Symbol = {
        'Spike_1': 'Spiked Form 1',
        'Spike_2': 'Spiked Form 2',
        'Spike_3': 'Spiked Form 3',
        'Spike_4': 'Spiked Form 4',
        'Mounded_1': 'Mounded Form 1',
        'Mounded_2': 'Mounded Form 2',
        'Prostrate_1': 'Prostrate Form 1',
        'Prostrate_2': 'Prostrate Form 2',
        'Prostrate_3': 'Prostrate Form 3',
        'Prostrate_4': 'Prostrate Form 4',
        'Fountain_1': 'Fountain Form 1',
        'Fountain_2': 'Fountain Form 2',
        'Columnar_1': 'Columnar Form 1',
        'Oval_1': 'Oval Form 1',
        'Pyramidal_1': 'Pyramidal Form 1',
        'Rounded_1': 'Rounded Form 1',
        'Rounded_2': 'Rounded Form 2',
        'Spreading_1': 'Spreading Form 1',
        'Spreading_2': 'Spreading Form 2',
        'Vase_1': 'Vase Form 1',
        'Vase_2': 'Vase Form 2',
        'Vase_3': 'Vase Form 3',
        'Vase_4': 'Vase Form 4',
        'Weeping_1': 'Weeping Form 1'
}

Symbol_reverse = dict(reversed(item) for item in Symbol.items())

Form = {
        12: 'Large Tree',
        11: 'Medium Tree',
        10: 'Small Tree',
        9: 'Bamboo',
        8: 'Shrub',
        7: 'Fern',
        6: 'Prostrate Shrub',
        5: 'Vine',
        4: 'Herbaceous Species',
        3: 'Corm/Bulb',
        2: 'Biennial',
        1: 'Annual Species'
}

Form_reverse = dict(reversed(item) for item in Form.items())

PlantFunction = {
        1: 'Productive Species',
        2: 'Support Species',
        3: 'Weed/Volunteer Species',
        4: 'Native Species'
}

PlantFunction_reverse = dict(reversed(item) for item in PlantFunction.items())

WindLevel = {
        0: 'Calm',
        1: 'Near Calm',
        2: 'Light Air',
        3: 'Light Breeze',
        4: 'Gentle Breeze',
        5: 'Moderate Breeze',
        6: 'Fresh Breeze',
        7: 'Strong Breeze',
        8: 'Near Gale',
        9: 'Gale',
        10: 'Severe Gale',
        11: 'Storm'
}

WindLevel_reverse = dict(reversed(item) for item in WindLevel.items())

LightLevel = {
            3: 'Full Sun',
            2: 'Partial Shade',
            1: 'Deep Shade',
}

LightLevel_reverse = dict(reversed(item) for item in LightLevel.items())

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

        self.symbolcombo = self.dlg.findChild(QComboBox, "symbolcombo")

        self.formcombo = self.dlg.findChild(QComboBox, "formcombo")
        self.functioncombo = self.dlg.findChild(QComboBox, "functioncombo")
        self.wind_lower = self.dlg.findChild(QComboBox, "wind_lower")
        self.wind_upper = self.dlg.findChild(QComboBox, "wind_upper")
        self.light_lower = self.dlg.findChild(QComboBox, "light_lower")
        self.light_upper = self.dlg.findChild(QComboBox, "light_upper")

        self.production_start = self.dlg.findChild(QComboBox, "production_start")
        self.production_end = self.dlg.findChild(QComboBox, "production_end")
        self.leaf_start = self.dlg.findChild(QComboBox, "leaf_start")
        self.leaf_end = self.dlg.findChild(QComboBox, "leaf_end")
        self.flower_start = self.dlg.findChild(QComboBox, "flower_start")
        self.flower_end = self.dlg.findChild(QComboBox, "flower_end")
        self.seed_start = self.dlg.findChild(QComboBox, "seed_start")
        self.seed_end = self.dlg.findChild(QComboBox, "seed_end")

        self.moisture_lower = self.dlg.findChild(QComboBox, "moisture_lower")
        self.moisture_upper = self.dlg.findChild(QComboBox, "moisture_upper")
        self.soil_lower = self.dlg.findChild(QComboBox, "soil_lower")
        self.soil_upper = self.dlg.findChild(QComboBox, "soil_upper")
        self.salinity_lower = self.dlg.findChild(QComboBox, "salinity_lower")
        self.salinity_upper = self.dlg.findChild(QComboBox, "salinity_upper")
        self.grafted = self.dlg.findChild(QCheckBox, "grafted")
        self.buttonBox = self.dlg.findChild(QDialogButtonBox, "buttonBox")

        self.vegetationpk = self.dlg.findChild(QLineEdit, "vegetationid")
        self.plantpk = self.dlg.findChild(QLineEdit, "plantid")
        self.cultivarpk = self.dlg.findChild(QLineEdit, "cultivarid")
        self.rootstockpk = self.dlg.findChild(QLineEdit, "rootstockid")

        self.symbol = self.dlg.findChild(QLineEdit, "symbol")

        self.form = self.dlg.findChild(QLineEdit, "form")
        self.plant_function = self.dlg.findChild(QLineEdit, "plant_function")
        self.wind_lower_limit = self.dlg.findChild(QLineEdit, "wind_lower_limit")
        self.wind_upper_limit = self.dlg.findChild(QLineEdit, "wind_upper_limit")
        self.light_lower_limit = self.dlg.findChild(QLineEdit, "light_lower_limit")
        self.light_upper_limit = self.dlg.findChild(QLineEdit, "light_upper_limit")

        self.production_startmonth = self.dlg.findChild(QLineEdit, "production_startmonth")
        self.production_endmonth = self.dlg.findChild(QLineEdit, "production_endmonth")
        self.leaf_startmonth = self.dlg.findChild(QLineEdit, "leaf_startmonth")
        self.leaf_endmonth = self.dlg.findChild(QLineEdit, "leaf_endmonth")
        self.flower_startmonth = self.dlg.findChild(QLineEdit, "flower_startmonth")
        self.flower_endmonth = self.dlg.findChild(QLineEdit, "flower_endmonth")
        self.seed_startmonth = self.dlg.findChild(QLineEdit, "seed_start_month")
        self.seed_endmonth = self.dlg.findChild(QLineEdit, "seed_endmonth")

        self.moisture_lower_level = self.dlg.findChild(QLineEdit, "moisture_lower_limit")
        self.moisture_upper_level = self.dlg.findChild(QLineEdit, "moisture_upper_limit")
        self.soiltexture_lower_limit = self.dlg.findChild(QLineEdit, "soiltexture_lower_limit")
        self.soiltexture_upper_limit = self.dlg.findChild(QLineEdit, "soiltexture_upper_limit")
        self.ph_lower_limit = self.dlg.findChild(QLineEdit, "pH_lower_limit")
        self.ph_upper_limit = self.dlg.findChild(QLineEdit, "pH_upper_limit")
        self.salinity_lower_limit = self.dlg.findChild(QLineEdit, "salinity_lower_limit")
        self.salinity_upper_limit = self.dlg.findChild(QLineEdit, "salinity_upper_limit")
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
            QMessageBox.information(None, "DEBUG:", 'row number: '+str(row))
            self.mapper.submit()
            self.model.insertRow(row)
            self.mapper.setCurrentIndex(row)
            self.vegetationpk.setText(str(row))

            self.plantid.setCurrentIndex(self.plantid.findText('Malus Domestica', Qt.MatchExactly))

        if currentplant != '':
            # QMessageBox.information(None, "DEBUG:", 'plant primary key: '+str(currentplant))
            query = QSqlQuery()
            query.prepare('select common_name from plantdb_plant where id = ?')
            query.addBindValue(str(currentplant))
            query.exec_()
            if query.next():
                currentname = str(query.value(0))
                # QMessageBox.information(None, "DEBUG:", 'plant common name: '+str(currentname))
                # cnindex = self.commonnamemodel.createIndex(currentplant, 0)
                if currentname != '':
                    self.commonname.setCurrentIndex(self.commonname.findText(currentname, Qt.MatchExactly))
        # Symbol combobox
        self.symbolcombo.addItems(Symbol.values())
        if self.symbol.text() != '':
            self.symbolcombo.setCurrentIndex(self.symbolcombo.findText(Symbol[self.symbol.text()], Qt.MatchExactly))
        # Form combobox
        self.formcombo.addItems(Form.values())
        if self.form.text() != '':
            self.formcombo.setCurrentIndex(self.formcombo.findText(Form[int(self.form.text())], Qt.MatchExactly))
        # Function combobox
        self.functioncombo.addItems(PlantFunction.values())
        if self.plant_function.text() != '':
            self.functioncombo.setCurrentIndex(self.functioncombo.findText(PlantFunction[int(self.plant_function.text())], Qt.MatchExactly))
        # Wind level comboboxes
        self.wind_lower.addItems(WindLevel.values())
        self.wind_upper.addItems(WindLevel.values())
        if self.wind_lower_limit.text() != '':
            self.wind_lower.setCurrentIndex(self.wind_lower.findText(WindLevel[int(self.wind_lower_limit.text())], Qt.MatchExactly))
        if self.wind_upper_limit.text() != '':
            self.wind_upper.setCurrentIndex(self.wind_upper.findText(WindLevel[int(self.wind_upper_limit.text())], Qt.MatchExactly))
        # Light level comboboxes
        self.light_lower.addItems(LightLevel.values())
        self.light_upper.addItems(LightLevel.values())
        if self.light_lower_limit.text() != '':
            self.light_lower.setCurrentIndex(self.light_lower.findText(LightLevel[int(self.light_lower_limit.text())], Qt.MatchExactly))
        if self.light_upper_limit.text() != '':
            self.light_upper.setCurrentIndex(self.light_upper.findText(LightLevel[int(self.light_upper_limit.text())], Qt.MatchExactly))

        # Moisture comboboxes
        MoistureOptions = MoistureLevel.values()
        self.moisture_lower.addItems(MoistureOptions)
        self.moisture_upper.addItems(MoistureOptions)
        # QMessageBox.information(None, "DEBUG:", 'moisture lower level: '+str(MoistureLevel[int(self.moisture_lower_level.text())]))
        if self.moisture_lower_level.text() != '':
            self.moisture_lower.setCurrentIndex(self.moisture_lower.findText(MoistureLevel[int(self.moisture_lower_level.text())], Qt.MatchExactly))
        if self.moisture_upper_level.text() != '':
            self.moisture_upper.setCurrentIndex(self.moisture_upper.findText(MoistureLevel[int(self.moisture_upper_level.text())], Qt.MatchExactly))
        # Soil Texture comboboxes
        SoilOptions = SoilTexture.values()
        self.soil_lower.addItems(SoilOptions)
        self.soil_upper.addItems(SoilOptions)
        # QMessageBox.information(None, "DEBUG:", 'soil lower level: '+str(self.soiltexture_lower_limit.text()))
        if self.soiltexture_lower_limit.text() != '':
            self.soil_lower.setCurrentIndex(self.soil_lower.findText(SoilTexture[int(self.soiltexture_lower_limit.text())], Qt.MatchExactly))
        if self.soiltexture_upper_limit.text() != '':
            self.soil_upper.setCurrentIndex(self.soil_upper.findText(SoilTexture[int(self.soiltexture_upper_limit.text())], Qt.MatchExactly))
        # Soil Salinity comboboxes
        SalinityOptions = SalinityLevel.values()
        self.salinity_lower.addItems(SalinityOptions)
        self.salinity_upper.addItems(SalinityOptions)
        # QMessageBox.information(None, "DEBUG:", 'soil lower level: '+str(self.soiltexture_lower_limit.text()))
        if self.salinity_lower_limit.text() != '':
            self.salinity_lower.setCurrentIndex(self.salinity_lower.findText(SalinityOptions[int(self.salinity_lower_limit.text())], Qt.MatchExactly))
        if self.salinity_upper_limit.text() != '':
            self.salinity_upper.setCurrentIndex(self.salinity_upper.findText(SalinityOptions[int(self.salinity_upper_limit.text())], Qt.MatchExactly))
        # Cultivar production comboboxes
        MonthOptions = MonthRange.values()
        self.production_start.addItems(MonthOptions)
        self.production_end.addItems(MonthOptions)
        # QMessageBox.information(None, "DEBUG:", 'soil lower level: '+str(self.soiltexture_lower_limit.text()))
        if self.production_startmonth.text() != '':
            self.production_start.setCurrentIndex(self.production_start.findText(MonthRange[int(self.production_startmonth.text())], Qt.MatchExactly))
        if self.production_endmonth.text() != '':
            self.production_end.setCurrentIndex(self.production_end.findText(MonthRange[int(self.production_endmonth.text())], Qt.MatchExactly))
        # Cultivar leaf comboboxes
        self.leaf_start.addItems(MonthOptions)
        self.leaf_end.addItems(MonthOptions)
        # QMessageBox.information(None, "DEBUG:", 'soil lower level: '+str(self.soiltexture_lower_limit.text()))
        if self.leaf_startmonth.text() != '':
            self.leaf_start.setCurrentIndex(self.leaf_start.findText(MonthRange[int(self.leaf_startmonth.text())], Qt.MatchExactly))
        if self.leaf_endmonth.text() != '':
            self.leaf_end.setCurrentIndex(self.leaf_end.findText(MonthRange[int(self.leaf_endmonth.text())], Qt.MatchExactly))
        # Cultivar flower comboboxes
        self.flower_start.addItems(MonthOptions)
        self.flower_end.addItems(MonthOptions)
        # QMessageBox.information(None, "DEBUG:", 'soil lower level: '+str(self.soiltexture_lower_limit.text()))
        if self.flower_startmonth.text() != '':
            self.flower_start.setCurrentIndex(self.flower_start.findText(MonthRange[int(self.flower_startmonth.text())], Qt.MatchExactly))
        if self.flower_endmonth.text() != '':
            self.flower_end.setCurrentIndex(self.flower_end.findText(MonthRange[int(self.flower_endmonth.text())], Qt.MatchExactly))
        # Cultivar seed comboboxes
        self.seed_start.addItems(MonthOptions)
        self.seed_end.addItems(MonthOptions)
        # QMessageBox.information(None, "DEBUG:", 'soil lower level: '+str(self.soiltexture_lower_limit.text()))
        if self.seed_startmonth.text() != '':
            self.seed_start.setCurrentIndex(self.seed_start.findText(MonthRange[int(self.seed_startmonth.text())], Qt.MatchExactly))
        if self.seed_endmonth.text() != '':
            self.seed_end.setCurrentIndex(self.seed_end.findText(MonthRange[int(self.seed_endmonth.text())], Qt.MatchExactly))



        pid = self.plantingid.text()
        # QMessageBox.information(None, "DEBUG:", 'final row number: '+pid)

    def create_connections(self):
        self.plantid.currentIndexChanged.connect(self.updateComboboxes)
        self.cultivarid.currentIndexChanged.connect(self.updateRootstocklist)
        self.grafted.stateChanged.connect(self.updateGrafted)
        self.commonname.currentIndexChanged.connect(self.updatefromCommonname)

        self.formcombo.currentIndexChanged.connect(self.updateform)
        self.symbolcombo.currentIndexChanged.connect(self.updatesymbol)
        self.functioncombo.currentIndexChanged.connect(self.updatefunction)
        self.wind_lower.currentIndexChanged.connect(self.updatelowerwind)
        self.wind_upper.currentIndexChanged.connect(self.updateupperwind)
        self.light_lower.currentIndexChanged.connect(self.updatelowerlight)
        self.light_upper.currentIndexChanged.connect(self.updateupperlight)

        self.moisture_lower.currentIndexChanged.connect(self.updatelowermoisture)
        self.moisture_upper.currentIndexChanged.connect(self.updateuppermoisture)
        self.soil_lower.currentIndexChanged.connect(self.updatelowersoil)
        self.soil_upper.currentIndexChanged.connect(self.updateuppersoil)
        self.salinity_lower.currentIndexChanged.connect(self.updatelowersalinity)
        self.salinity_upper.currentIndexChanged.connect(self.updateuppersalinity)

        self.production_start.currentIndexChanged.connect(self.updateproductionstart)
        self.production_end.currentIndexChanged.connect(self.updateproductionend)
        self.leaf_start.currentIndexChanged.connect(self.updateleafstart)
        self.leaf_end.currentIndexChanged.connect(self.updateleafend)
        self.flower_start.currentIndexChanged.connect(self.updateflowerstart)
        self.flower_end.currentIndexChanged.connect(self.updateflowerend)
        self.seed_start.currentIndexChanged.connect(self.updateseedstart)
        self.seed_end.currentIndexChanged.connect(self.updateseedend)

    def updateform(self):
        self.form.setText(str(Form_reverse[self.formcombo.currentText()]))

    def updatesymbol(self):
        self.symbol.setText(str(Symbol_reverse[self.symbolcombo.currentText()]))

    def updatefunction(self):
        self.plant_function.setText(str(PlantFunction_reverse[self.functioncombo.currentText()]))

    def updatelowerwind(self):
        self.wind_lower_limit.setText(str(WindLevel_reverse[self.wind_lower.currentText()]))

    def updateupperwind(self):
        self.wind_upper_limit.setText(str(WindLevel_reverse[self.wind_upper.currentText()]))

    def updatelowerlight(self):
        self.light_lower_limit.setText(str(LightLevel_reverse[self.light_lower.currentText()]))

    def updateupperlight(self):
        self.light_upper_limit.setText(str(LightLevel_reverse[self.light_upper.currentText()]))

    def updatelowermoisture(self):
        currentlowermoisturetext = self.moisture_lower.currentText()
        self.moisture_lower_level.setText(str(MoistureLevel_reverse[currentlowermoisturetext]))

    def updateuppermoisture(self):
        currentuppermoisturetext = self.moisture_upper.currentText()
        self.moisture_upper_level.setText(str(MoistureLevel_reverse[currentuppermoisturetext]))

    def updatelowersoil(self):
        currentlowersoiltext = self.soil_lower.currentText()
        self.soiltexture_lower_limit.setText(str(SoilTexture_reverse[currentlowersoiltext]))

    def updateuppersoil(self):
        currentuppersoiltext = self.soil_upper.currentText()
        self.soiltexture_upper_limit.setText(str(SoilTexture_reverse[currentuppersoiltext]))

    def updatelowersalinity(self):
        currentlowersalinitytext = self.salinity_lower.currentText()
        self.salinity_lower_limit.setText(str(SalinityLevel_reverse[currentlowersalinitytext]))

    def updateuppersalinity(self):
        currentuppersalinitytext = self.salinity_upper.currentText()
        self.salinity_upper_limit.setText(str(SalinityLevel_reverse[currentuppersalinitytext]))

    def updateproductionstart(self):
        self.production_startmonth.setText(str(MonthRange_reverse[self.production_start.currentText()]))

    def updateproductionend(self):
        self.production_endmonth.setText(str(MonthRange_reverse[self.production_end.currentText()]))

    def updateleafstart(self):
        self.leaf_startmonth.setText(str(MonthRange_reverse[self.leaf_start.currentText()]))

    def updateleafend(self):
        self.leaf_endmonth.setText(str(MonthRange_reverse[self.leaf_end.currentText()]))

    def updateflowerstart(self):
        self.flower_startmonth.setText(str(MonthRange_reverse[self.flower_start.currentText()]))

    def updateflowerend(self):
        self.flower_endmonth.setText(str(MonthRange_reverse[self.flower_end.currentText()]))

    def updateseedstart(self):
        self.seed_startmonth.setText(str(MonthRange_reverse[self.seed_start.currentText()]))

    def updateseedend(self):
        self.seed_endmonth.setText(str(MonthRange_reverse[self.seed_end.currentText()]))

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
            newname = str(query.value(0))
            if newname is not None:
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


        #self.dlg.accept()
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
