#========================================================
#           Creating a vector layer in memory
#========================================================


# First, you need to import the OrderedDict container, which remembers the order in
#which keys are inserted:
from collections import OrderedDict
# Then, build an ordered dictionary that contains attribute names and types:
fields =OrderedDict([('city','str(25)'),('population','int')])
# Next, build a string by joining the output of a Python list comprehension that loops
#through the ordered dictionary:
path = '&'.join(['field={}:{}'.format(k,v) for k,v in
fields.items()])
# Finally, use this string to define the layer:
vectorLyr = QgsVectorLayer('Point?crs=epsg:4326&' + path, 'Layer 1' , "memory")


#========================================================
#           Adding a point feature to a vector layer
#========================================================
#  First, load the layer:
vectorLyr =QgsVectorLayer('/qgis_data/nyc/NYC_MUSEUMS_GEO.shp', 'Museums', "ogr")
#  Now, will access the layer's data provider:
vpr = vectorLyr.dataProvider()
#   Next, create a new point using the QgsGeometry object:
pnt = QgsGeometry.fromPoint(QgsPoint(-74.80,40.549))
#   Now, will create a new QgsFeature object to house the geometry:
f = QgsFeature()
#   Next, set the geometry of the feature using our point:
f.setGeometry(pnt)
#   Then, place the features into the layer's feature list:
vpr.addFeatures([f])
#  Finally, update the layer's extent to complete the addition:
vectorLyr.updateExtents()


#========================================================
#           Adding a line feature to a vector layer
#========================================================

#First, load the line layer and ensure that it is valid:
vectorLyr = QgsVectorLayer('/qgis_data/paths/paths.shp','Paths' , "ogr")
vectorLyr.isValid()

# Next, access the layer's data provider:
vpr = vectorLyr.dataProvider()
# Now, build our list of points for a new line:
points = []
points.append(QgsPoint(430841,5589485))
points.append(QgsPoint(432438,5575114))
points.append(QgsPoint(447252,5567663))
# Then, create a geometry object from the line:
line = QgsGeometry.fromPolyline(points)
# Create a feature and set its geometry to the line:
f = QgsFeature()
f.setGeometry(line)
# Finally, add the feature to the layer data provider and update the extent:
vpr.addFeatures([f])
vectorLyr.updateExtents()

#========================================================
#           Adding a polygon feature to a vector layer
#========================================================

# First, load the layer and validate it:
vectorLyr =QgsVectorLayer('/qgis_data/polygon/polygon.shp', 'Polygon', "ogr")
vectorLyr.isValid()
# Next, access the layer's data provider:
vpr = vectorLyr.dataProvider()
# Now, build a list of points for the polygon:
points = []
points.append(QgsPoint(-123.26,49.06))
points.append(QgsPoint(-127.19,43.07))
points.append(QgsPoint(-120.70,35.21))
points.append(QgsPoint(-115.89,40.02))
points.append(QgsPoint(-113.04,48.47))
points.append(QgsPoint(-123.26,49.06))
# Next, create a geometry object and ingest the points as a polygon. We nest our list
#of points in another list because a polygon can have inner rings, which will consist of
#additional lists of points being added to this list:
poly = QgsGeometry.fromPolygon([points])
# Next, build the feature object and add the points:
f = QgsFeature()
f.setGeometry(poly)
# Finally, add the feature to the layer's data provider and update the extents:
vpr.addFeatures([f])

#========================================================
#           Adding a set of attributes to a vector layer
#========================================================

#First, load the layer and validate it:
vectorLyr = QgsVectorLayer('/qgis_data/nyc/NYC_MUSEUMS_GEO.shp','Museums' , "ogr")
vectorLyr.isValid()
# Next, access the layer's data provider so that we can get the list of fields:
vpr = vectorLyr.dataProvider()
# Now, create a point geometry, which in this case is a new museum:
pnt = QgsGeometry.fromPoint(QgsPoint(-74.13401,40.62148))
# Next, get the fields object for the layer that we'll need to create a new feature for:
fields = vpr.fields()

#then, create a new feature and initialize the attributes:
f = QgsFeature(fields)
# Now, set the geometry of our new museum feature:
f.setGeometry(pnt)
# Now, we are able to add a new attribute. Adding an attribute is similar to updating a
#Python dictionary, as shown here:
f['NAME'] = 'Python Museum'
# Finally, we add the feature to the layer and update the extents:
vpr.addFeatures([f])
vectorLyr.updateExtents()


#========================================================
#           Adding a field to a vector layer
#========================================================

#First, you must import the Qt library's data types, which PyQGIS uses to specify the
#layer field's data types:
from PyQt4.QtCore import QVariant
# Next, load and validate the layer:
vectorLyr =QgsVectorLayer('/qgis_data/nyc/NYC_MUSEUMS_GEO.shp', 'Museums', "ogr")
vectorLyr.isValid()
# Then, access the layer data provider:
vpr = vectorLyr.dataProvider()
# Now, add a Python list of QgsField objects, which defines the field name and type.
#In this case, we'll add one field named Admission as a Double:
vpr.addAttributes([QgsField("Admission", QVariant.Double)])
# Finally, update the fields to complete the change:
vectorLyr.updateFields()


#========================================================
#           Joining a shapefile attribute table to
#                   a CSV file
#========================================================

#First, load the county's census track layer and validate it:
vectorLyr =QgsVectorLayer('/qgis_data/census/hancock_tracts.shp','Hancock' , "ogr")
vectorLyr.isValid()
# Now, load the CSV file as a layer and validate it as well:
infoLyr =QgsVectorLayer('/qgis_data/census/ACS_12_5YR_S1901_with_ann.csv', 'Census' , "ogr")
infoLyr.isValid()

#Once this is done, you must add both the layers to the map registry for the two layers
#to interact for the join. However, set the visibility to False, so the layers do not
#appear on the map:
QgsMapLayerRegistry.instance().addMapLayers([vectorLyr,infoLyr], False)
# Next, you must create a special join object:
info = QgsVectorJoinInfo()
# The join object needs the layer ID of the CSV file:
info.joinLayerId = infoLyr.id()
# Next, specify the key field from the CSV file whose values correspond to the
#values in the shapefile:
info.joinFieldName = "GEOid2"
# Then, specify the corresponding field in the shapefile:
info.targetFieldName = "GEOID"
# Set the memoryCache property to True in order to speed up access to the
#joined data:
info.memoryCache = True
# Add the join to the layer now:
vectorLyr.addJoin(info)
# Next, write out the joined shapefile to a new file on disk:
QgsVectorFileWriter.writeAsVectorFormat(vectorLyr,"/qgis_data/census/joined.shp", "CP120", None, "ESRIShapefile")
# Now, load the new shapefile back in as a layer for verification:
joinedLyr = QgsVectorLayer('/qgis_data/census/joined.shp','Joined' , "ogr")
# Verify that the field count in the original layer is 12:
vectorLyr.dataProvider().fields().count()
# Finally, verify that the new layer has a field count of 142 from the join:
joinedLyr.dataProvider().fields().count()


#========================================================
#           Moving vector layer geometry
#========================================================


# First, load the layer and validate it:
vectorLyr =QgsVectorLayer('/qgis_data/nyc/NYC_MUSEUMS_GEO.shp','Museums' , "ogr")
vectorLyr.isValid()
# Next, define the feature ID we are interested in changing:
feat_id = 22
# Now, create the new point geometry, which will become the new location:
geom = QgsGeometry.fromPoint(QgsPoint(-74.20378,40.89642))
# Finally, change the geometry and replace it with our new geometry, specifying the feature ID:
vectorLyr.dataProvider().changeGeometryValues({feat_id : geom})


#========================================================
#           Changing a vector layer feature's attribute
#========================================================

# First, load the layer and validate it:
vectorLyr =QgsVectorLayer('/qgis_data/nyc/NYC_MUSEUMS_GEO.shp','Museums' , "ogr")
vectorLyr.isValid()
# Next, define the feature IDs you want to change:
fid1 = 22
fid2 = 23
# Then, get the index of the fields you want to change, which are the telephone
# number and city name:
tel = vectorLyr.fieldNameIndex("TEL")
city = vectorLyr.fieldNameIndex("CITY")
# Now, create the Python dictionary for the attribute index and the new value,
# which in this case is an imaginary phone number:
attr1 = {tel:"(555) 555-1111", city:"NYC"}
attr2 = {tel:"(555) 555-2222", city:"NYC"}
# Finally, use the layer's data provider to update the fields:
vectorLyr.dataProvider().changeAttributeValues({fid1:attr1,fid2:attr2})


#========================================================
#           Deleting a vector layer feature
#========================================================

#First, load and validate the layer:
vectorLyr =QgsVectorLayer('/qgis_data/nyc/NYC_MUSEUMS_GEO.shp','Museums' , "ogr")
vectorLyr.isValid()
# Next, specify a Python list containing feature IDs. In this case, we have two:
vectorLyr.dataProvider().deleteFeatures([ 22, 95 ])

#========================================================
#           Reprojecting a vector layer
#========================================================

# First, you need to import the processing module:
import processing
# Next, run the reprojection alogoritm, as follows:
processing.runalg("qgis:reprojectlayer","/qgis_data/ms/MSCities_MSTM.shp", "epsg:4326","/qgis_data/ms/MSCities_MSTM_4326.shp")


#========================================================
#           Converting a shapefile to KML
#========================================================

#First load the layer and validate it:
vectorLyr =QgsVectorLayer('/qgis_data/hancock/hancock.shp', 'Hancock', "ogr")
vectorLyr.isValid()
# Then, establish the destination CRS. KML should always be in EPS:4326:
dest_crs = QgsCoordinateReferenceSystem(4326)
# Next, use the file writer to save it as a KML file by specifying the file type as KML:
QgsVectorFileWriter.writeAsVectorFormat(vectorLyr,"/qgis_data/hancock/hancock.kml", "utf-8", dest_crs, "KML")


#========================================================
#           Merging shapefiles
#========================================================

# Import the Python glob module for wildcard file matching:
import glob
# Next, import the processing module for the merge algorithm:
import processing
# Now, specify the path of our data directory:
pth = "/qgis_data/tiled_footprints/"
# Locate all the .shp files:
files = glob.glob(pth + "*.shp")
# Then, specify the output name of the merged shapefile:
out = pth + "merged.shp"
# Finally, run the algorithm that will load the merged shapefile on to the map:
processing.runandload("saga:mergeshapeslayers",files.pop(0),";".join(files),out)


#========================================================
#           Splitting a shapefile
#========================================================






#========================================================
#          Generalizing a vector layer
#========================================================

#Generalizing is native to QGIS, but we will access it in PyQGIS through the Processing Toolbox
#using the qgis:simplifygeometries algorithm, as follows:
# Import the processing module:
import processing
# Now, run the processing algorithm, specifying the algorithm name, input data,
#tolerance value, spacing between points — which defines how close two points are in
#map units before one is deleted — and the output dataset's name:
processing.runandload("qgis:simplifygeometries","/qgis_data/ms/mississippi.shp",0.3,"/qgis_data/ms/generalize.shp")


#========================================================
#          Dissolving vector shapes
#========================================================
#Dissolve:you cam combine a group of adjoining shapesby the outermost boundary of the entire dataset, 
#or you can also group the adjoining shapeswith the same attribute value.

#Import the processing module:
import processing
# Next, run the dissolve algorithm, specifying the input data—False to specify that
#we don't want to dissolve all the shapes into one but to use an attribute instead—the
#attribute we want to use, and the output filename:
processing.runandload("qgis:dissolve","/qgis_data/censusGIS_CensusTract_poly.shp",False,"COUNTY_8","/qgis_data/census/dissovle.shp")


#========================================================
#          Performing a union on vector shapes
#========================================================
#A union turns two overlapping shapes into one.

#Import the processing module:
import processing

#Now, run the algorithm by specifying the two input shapes and a single output file:
processing.runandload("qgis:union","/qgis_data/union/building.shp","/qgis_data/union/walkway.shp","/qgis_data/union/union.shp")


#========================================================
#          Rasterizing a vector layer
#========================================================
#Sometimes, a raster dataset is the most efficient way to display a complex vector that is
#merely a backdrop in a map.
#Import the processing module:
import processing
# Run the algorithm, specifying the input data, the attribute from which raster
#values need to be drawn, 0 in order to specify pixel dimensions for the output
#instead of map dimensions, width and height, and finally the output raster name:
processing.runalg("gdalogr:rasterize","/qgis_data/rasters/contour.shp","ELEV",0,1000,1000,"/qgis_data/rasters/contour.tif")

#========================================================
#          Rasterizing a vector layer
#========================================================

















