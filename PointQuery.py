# Customize this starter script by adding code
# to the run_script function. See the Help for
# complete information on how to create a script
# and use Script Runner.

""" Your Description of the script goes here """

# Some commonly used imports

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
#import resources
# Import the code for the dialog
from vector_selectbypointdialog import vector_selectbypointDialog
class Loader:
    def __init__(self, iface):
        """Initialize using the qgis.utils.iface
        object passed from the console.
        """

        self.iface = qgis.utils.iface

    def load_shapefiles(self, shp_path):
        """Load all shapefiles found in shp_path"""
        print "Loading shapes from %s" % path.join(shp_path, "*.shp")
        shps = glob(path.join(shp_path, "*.shp"))
        for shp in shps:
            (shpdir, shpfile) = path.split(shp)
            print "Loading %s" % shpfile
            lyr = QgsVectorLayer(shp, shpfile, 'ogr')
            QgsMapLayerRegistry.instance().addMapLayer(lyr)




class vector_selectbypoint:
    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # self.iface = qgis.utils.iface
        # refernce to map canvas
        self.canvas = self.iface.mapCanvas()
        # out click tool will emit a QgsPoint on every click
        self.clickTool = QgsMapToolEmitPoint(self.canvas)
        # create our GUI dialog
        self.dlg = vector_selectbypointDialog()

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/vector_selectbypoint/icon.png"), \
            "some text that appears in the menu", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&some text that appears in the menu", self.action)

        # connect our custom function to a clickTool signal that the canvas was clicked
        result = QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.handleMouseDown)
        #QMessageBox.information( self.iface.mainWindow(),"Info", "connect = %s"%str(result) )

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&some text that appears in the menu",self.action)
        self.iface.removeToolBarIcon(self.action)

    def handleMouseDown(self, point, button):
        self.dlg.clearTextBrowser()
        self.dlg.setTextBrowser( str(point.x()) + " , " +str(point.y()) )
        #QMessageBox.information( self.iface.mainWindow(),"Info", "X,Y = %s,%s" % (str(point.x()),str(point.y())) )

    # run method that performs all the real work
    def run(self):
        # make our clickTool the tool that we'll use for now
        self.canvas.setMapTool(self.clickTool)

        # show the dialog
        self.dlg.show()
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass

def run_script(iface):
    selecltbypoint = vector_selectbypoint(iface)
    print "Loading .."
    selecltbypoint.run()

