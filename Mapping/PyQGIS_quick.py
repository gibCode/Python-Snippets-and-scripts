Add a single point to a map
-----------------------------------
#
#First, create a layer that is of the type geometry
layer = QgsVectorLayer('Point?crs=epsg:4326', 'MyPoint' ,'memory') #you can define the geometry and the attributes inline
                                                                   #in the code rather than in an external data source
#set up a data provider to accept the data source.
pr = layer.dataProvider()
#create a generic feature object
pt = QgsFeature()
#create a point
point1 = QgsPoint(20,20)
#stack the objects together
pt.setGeometry(QgsGeometry.fromPoint(point1))
pr.addFeatures([pt])
layer.updateExtents()
#add them to the map.
QgsMapLayerRegistry.instance().addMapLayers([layer])




ADDING A POLYGON
==================================================================
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *


def run_script(iface):
    layer = QgsVectorLayer('Polygon?crs=epsg:4326', 'Mississippi', "memory")
    pr = layer.dataProvider()
    poly = QgsFeature()
    geom = QgsGeometry.fromWkt("POLYGON ((-88.82 34.99,-88.09 34.89,-88.39 30.34,-89.57 30.18,-89.73 31,-91.63 30.99,-90.87 32.37,-91.23 33.44,-90.93 34.23,-90.30 34.99,-88.82 34.99))")
    poly.setGeometry(geom)
    pr.addFeatures([poly])
    layer.updateExtents()
    QgsMapLayerRegistry.instance().addMapLayers([layer] 
 --------------------------------------------------------------------------


#=================================================================================
#                Loading a vector layer from a file sample
#=================================================================================

layer = QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp", "New York City Museums", "ogr")
# ensure that the layer was created as expected:
if not layer.isValid():
print "Layer %s did not load" % layer.name()
# Finally, add the layer to the layer registry:
QgsMapLayerRegistry.instance().addMapLayers([layer])

#=================================================================================
#                Loading a vector layer from a spatial database
#=================================================================================








#=================================================================================
#               Examining vector layer features
#=================================================================================

#First, load the layer:
layer =QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp", "New York City Museums", "ogr")
# Next, get an iterator of the layer's features:
features = layer.getFeatures()
# Now, get the first feature from the iterator:
f = features.next()
#Then, get the feature's geometry:
g = f.geometry()
#Finally, get the point's values:
g.asPoint()
#Verify that the Python console output is similar to the following QgsPoint object:
(-74.0138,40.7038)

#=================================================================================
#               Examining vector layer attributes
#=================================================================================
#First, load the layer:
layer =QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp", "New York City Museums", "ogr")

#Next, get the features iterator:
features = layer.getFeatures()
# Now, grab the first feature from the iterator:
f = features.next()
#Finally, examine the attributes as a Python list:
f.attributes()
#Verify that the Python console's output resembles the following list:
[u'Alexander Hamilton U.S. Custom House', u'(212) 514-3700',u'http://www.oldnycustomhouse.gov/', u'1 Bowling Grn', NULL, u'New
York', 10004.0, -74.013756, 40.703817]

#=================================================================================
#               Filtering a layer by geometry
#=================================================================================
 # First, load the point layer:
lyrPts = QgsVectorLayer("/qgis_data/ms/MSCities_Geo_Pts.shp","MSCities_Geo_Pts", "ogr")
 # Next, load the polygon layer:
lyrPoly = QgsVectorLayer("/qgis_data/ms/GIS_CensusTract_poly.shp", "GIS_CensusTract_poly", "ogr")
 # Add the layers to the map using a list:
QgsMapLayerRegistry.instance().addMapLayers([lyrPts,lyrPoly])
 #  Access the polygon layer's features:
ftsPoly = lyrPoly.getFeatures()
 # Now, iterate through the polygon's features:
for feat in ftsPoly:
 	#  Grab each feature's geometry:
	geomPoly = feat.geometry()
	 # 7. Access the point features and filter the point features by the polygon's bounding box:
	featsPnt = lyrPts.getFeatures(QgsFeatureRequest()self.setFilterRect(geomPoly.boundingBox()))
 	#  Iterate through each point and check whether it's within the polygon itself:
	for featPnt in featsPnt:
		if featPnt.geometry().within(geomPoly):
 		#  If the polygon contains the point, print the point's ID and select the point:
		print featPnt.id()
		lyrPts.select(featPnt.id())
 #  Now, set the polygon layer as the active map layer:
iface.setActiveLayer(lyrPoly)
 #  Zoom to the polygon layer's maximum extent:
iface.zoomToActiveLayer()


#=================================================================================
#               Filtering a layer by attributes
#=================================================================================

# First, we load the point layer:
lyrPts = QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp","Museums", "ogr")
# Next, we add the layer to the map in order to visualize the points:
QgsMapLayerRegistry.instance().addMapLayers([lyrPts])
#Now, we filter the point layer to points with attributes that match a specific zip code:
selection = lyrPts.getFeatures(QgsFeatureRequest().
setFilterExpression(u'"ZIP" = 10002'))
# Then, we use a list comprehension to create a list of feature IDs that are fed to the
feature selection method:
lyrPts.setSelectedFeatures([s.id() for s in selection])
#Finally, we zoom to the selection:
iface.mapCanvas().zoomToSelected()


#=================================================================================
#               Buffering a feature intermediate
#=================================================================================

#  First, load the layer:
lyr = QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp", "Museums", "ogr")
#   Next, visualize the layer on the map:
QgsMapLayerRegistry.instance().addMapLayers([lyr])
#   Access the layer's features:
fts = lyr.getFeatures()
#   Grab the first feature:
ft = fts.next()
#   Select this feature:
lyr.setSelectedFeatures([ft.id()])
#   Create the buffer:
buff = ft.geometry().buffer(.2,8)
#   Set up a memory layer for the buffer's geometry:
buffLyr = QgsVectorLayer('Polygon?crs=EPSG:4326', 'Buffer' ,'memory')
#  Access the layer's data provider:
pr = buffLyr.dataProvider()
#   Create a new feature:
b = QgsFeature()
#   Set the feature's geometry with the buffer geometry:
b.setGeometry(buff)
#   Add the feature to the data provider:
pr.addFeatures([b])
#   Update the buffer layer's extents:
buffLyr.updateExtents()
#   Set the buffer layer's transparency so that you can see other features as well:
buffLyr.setLayerTransparency(70)
#   Add the buffer layer to the map:
QgsMapLayerRegistry.instance().addMapLayers([buffLyr])

#=================================================================================
#               Measuring the distance between two points
#=================================================================================
# First, import the library that contains the QGIS contents:
from qgis.core import QGis
# Then, load the layer:
lyr = QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp","Museums", "ogr")
# Access the features:
fts = lyr.getFeatures()
# Get the first feature:
first = fts.next()
#  Set a placeholder for the last feature:
last = fts.next()
#  Iterate through the features until you get the last one:
for f in fts:
    last = f
#  Create a measurement object:
d = QgsDistanceArea()
#  Measure the distance:
m = d.measureLine(first.geometry().asPoint(),
last.geometry().asPoint())
#  Convert the measurement value from decimal degrees to meters:
d.convertMeasurement(m, 2, 0, False)
#  Ensure that your Python console output looks similar to this tuple:
(4401.1622240174165, 0)



#=================================================================================
#               Measuring the distance along a line sample
#=================================================================================
#  First, we must load the QGIS constants library:
from qgis.core import QGis
#  Load the line layer:
lyr = QgsVectorLayer("/qgis_data/shapes/paths.shp", "Route", "ogr")
#   Grab the features:
fts = lyr.getFeatures()
#   Get the first feature:
route = fts.next()
#   Create the measurement object instance:
d = QgsDistanceArea()
#   Then, we must configure the QgsDistanceArea object to use the ellipsoidal mode for
accurate measurements in meters:
d.setEllipsoidalMode(True)
#   Pass the line's geometry to the measureLine method:
m = d.measureLine(route.geometry().asPolyline())
#   Convert the measurement output to miles:
d.convertMeasurement(m, QGis.Meters, QGis.NauticalMiles, False)


#=================================================================================
#               Calculating the area of a polygon
#=================================================================================

# First, import the QGIS constants library, as follows:
from qgis.core import QGis
#  Load the layer:
lyr = QgsVectorLayer("/qgis_data/ms/mississippi.shp", "Mississippi", "ogr")
#  Access the layer's features:
fts = lyr.getFeatures()
#  Get the boundary feature:
boundary = fts.next()
# Create the measurement object instance:
d = QgsDistanceArea()
# Pass the polygon list to the measureArea() method:
m = d.measurePolygon(boundary.geometry().asPolygon()[0])
#  Convert the measurement from decimal degrees to miles:
d.convertMeasurement(m, QGis.Degrees, QGis.NauticalMiles, True)
#  Verify that your output looks similar to the following:
(42955.47889640281, 7)

#=================================================================================
#               Creating a spatial index
#=================================================================================


# Load the layer:
lyr = QgsVectorLayer("/qgis_data/nyc/NYC_MUSEUMS_GEO.shp", "Museums", "ogr")
#  Get the features:
fts = lyr.getFeatures()

#   Get the first feature in the set:
first = fts.next()
#   Now, create the spatial index:
index = QgsSpatialIndex()
#   Begin loading the features:
index.insertFeature(first)
#   Insert the remaining features:
for f in fts:
    index.insertFeature(f)
#   Now, select the IDs of 3 points nearest to the first point. We use the number 4
#  because the starting point is included in the output:
hood = index.nearestNeighbor(first.geometry().asPoint(), 4)

#=================================================================================
#               Loading data from a spreadsheet
#=================================================================================

#First, we build the base URI string with the filename:
uri="""file:///qgis_data/ms/MS_Features.txt?"""
#Next, we tell QGIS that the file is a CSV file:
uri += """type=csv&"""
# Now, we specify our delimiter, which is a pipe ("|"), as a URL-encoded value:
uri += """delimiter=%7C&"""
#Next, we tell QGIS to trim any spaces at the ends of the fields:
uri += """trimFields=Yes&"""
# Now, the most important part, we specify the x field:
uri += """xField=PRIM_LONG_DEC&"""
#  Then, we specify the y field:
uri += """yField=PRIM_LAT_DEC&"""
#  We decline the spatial index option:
uri += """spatialIndex=no&"""
# We decline the subset option:
uri += """subsetIndex=no&"""
# We tell QGIS not to watch the file for changes:
uri += """watchFile=no&"""
# Finally, we complete the uri with the CRS of the layer:
uri += """crs=epsg:4326"""
# We load the layer using the delimitedtext data provider:
layer=QgsVectorLayer(uri,"MS Features","delimitedtext")
# Finally, we add it to the map:
QgsMapLayerRegistry.instance().addMapLayers([layer])
