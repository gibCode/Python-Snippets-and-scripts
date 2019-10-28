# For interaction with QGIS environment, there is a iface variable,
# which is an instance of QgsInterface. This interface allows access to the map canvas, menus, toolbars and
# other parts of the QGIS application.

lyr = iface.activeLayer()
lyr.name()  //u'NZ_road'
#-----------------------------
lyr.geometryType()
# 0:point ;#1:line  ; #2:polygon


lyr.selectAll() # --- > open attribute table ; all rows are selected

lyr.select(0) # by index
lyr.removeSeelction()

iface.showAttributeTable(lyr)

#pendingFields : FEATURES table columns
for field in lyr.pendingFields():
    print field.typeName(), field.name()




ADDING AND REMOVING FIELDS

#To add fields(attributes) specify a list of fiel definitions
#For deletion provide index

# _________          QVariant for datatype.

dataProv = lyr.dataProvider()
dataProv.featureCount() # number in attribute tab;e
-------------------------------------------
#to add attributes ---> 
dataProv.addAttributes([QgsField ("isActive", QVariant.String)])
#-------------------------------------------------------

lyr.updateFields()
#==========================================

dataProv.fieldNameIndex("isActive")  #Result : 4

#DELETE command
dataProv.deleteAttributes([4])


				if caps & QgsVectorDataProvider.AddAttributes:
					res = layer.dataProvider().addAttributes( [ QgsField("mytext", \
					QVariant.String), QgsField("myint", QVariant.Int) ] )
				if caps & QgsVectorDataProvider.DeleteAttributes:
					res = layer.dataProvider().deleteAttributes( [ 0 ] )



#FEATURES
 features = lyr.getFeatures()   #result : featureIteratorObject
#Make sure to add 2 spaces before typing the second line
for f in features:
  g = features.geometry()
  attr=features.Attributes()
  print g, attr
#======================================================================

			Change Attribute values
#----------------------------------------------
#create json variable:
		attr ={dataProv.fieldNameIndex("Id"):100, 1:"MW002", 2:"0" }
#Commit changes based on index of row to modify

		dataProv.changeAttributeValues({8:attr})


#       To change the point geometry position
#---------------------------------------------------------------
geom =QgsGeometry.fromPoint(QgsPoint(111,222))
dataProv.changeGeometryValues({8:geom})

lyr.triggerRepaint()
#===============================================================


feat = QgsFeature(lyr.pendingFields())
feat.setAttributes([9,"MW009"])
feat.setGeometry(QgsGeometry.fromPoint(QgsPoint(111,222)))
dataProv.addFeatures([feat])




SYMBOLOGY

#renderers determine what symbol will be used for a particular feature.

renderer = layer.rendererV2()
renderer.symbol().setColor(QColor.fromRGB(244,244,244))

#creates a simple marker

symbol = QgsMarkerSymbolV2.createSimple({'name':'square','color':'red'})



							GUI
#==============================================================
from qgis.gui import *
canvas = QgsMapCanvas()
canvas.show()

