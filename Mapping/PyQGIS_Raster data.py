#========================================================
#           Loading a raster layer
#========================================================
#create the layer by specifying the source file and a layer name:
rasterLyr = QgsRasterLayer("/qgis_data/rasters/SatImage.tif","Gulf Coast")
# Next, ensure that the layer is created as expected. The following command should
return True:
rasterLyr.isValid()
# Finally, add the layer to the layer registry:
QgsMapLayerRegistry.instance().addMapLayers([rasterLyr])

#========================================================
#       Getting the cell size of a raster layer
#========================================================

#Load the layer and validate it:
rasterLyr = QgsRasterLayer("/qgis_data/rasters/satimage.tif","Sat Image")
rasterLyr.isValid()
# Now, call the x distance method, which should return 0.00029932313140079714:
rasterLyr.rasterUnitsPerPixelX()
# Then, call the y distance, which should be 0.00029932313140079714:
rasterLyr.rasterUnitsPerPixelY()

#========================================================
#       Obtaining the width and height of a raster
#========================================================

#In the Python Console, load the layer and ensure that it is valid:
rasterLyr = QgsRasterLayer("/qgis_data/rasters/satimage.tif","satimage")
rasterLyr.isValid()
#Check the name of SatImage after unzipping.
# Obtain the layer's width, which should be 2592:
rasterLyr.width()
# Now, get the raster's height, which will return 2693:
rasterLyr.height()

#========================================================
#       Counting raster bands
#========================================================
#In the Python Console, load the layer and ensure that it is valid:
rasterLyr = QgsRasterLayer("/qgis_data/rasters/satimage.tif","Sat Image")
rasterLyr.isValid()
# Now, get the band count, which should be 3 in this case:
rasterLyr.bandCount()

#========================================================
#       Swapping raster bands
#========================================================

#load the layer and ensure that it is valid:
rasterLyr =QgsRasterLayer("/qgis_data/rasters/FalseColor.tif", "BandSwap")
rasterLyr.isValid()
# Now, we must access the layer renderer in order to manipulate the order of the
#bands displayed. Note that this change does not affect the underlying data:
ren = rasterLyr.renderer()
# Next, we will set the red band to band 2:
ren.setRedBand(2)
# Now, we will set the green band to band 1:
ren.setGreenBand(1)
# Finally, add the altered raster layer to the map:
QgsMapLayerRegistry.instance().addMapLayers([rasterLyr])

#========================================================
#       Querying the value of a raster at a specified point
#========================================================
# A common remote sensing operation is to get the raster data value at a specified coordinate.


#First, load and validate the layer:
rasterLyr = QgsRasterLayer("/qgis_data/rasters/satimage.tif","Sat Image")
rasterLyr.isValid()

#Next, get the layer's center point from its QgsRectangle extent object, which will
#return a tuple with the x and y values:
c = rasterLyr.extent().center()
# Now, using the layer's data provider, we can query the data value at that point using
#the identify() method:
qry = rasterLyr.dataProvider().identify(c,
QgsRaster.IdentifyFormatValue)
# Because a query error won't throw an exception, we must validate the query:
qry.isValid()
# Finally, we can view the query results, which will return a Python dictionary with each
#band number as the key pointing to the data values in that band:
qry.results()
# Verify that you get the following output:
{1: 17.0, 2: 66.0, 3: 56.0}

#========================================================
#       Reprojecting a raster
#========================================================
#The first line of code is used to import the processing module:
import processing
# Next, we load our raster layer and validate it:
rasterLyr = QgsRasterLayer("/qgis_data/rasters/SatImage.tif","Reproject")
rasterLyr.isValid()
# Finally, we run the gdal warp algorithm by inserting the correct parameters,
#including the layer reference, current projection, desired projection, None for changes
##to the resolution, 0 to represent nearest neighbor resampling, None for additional
#parameters, 0 –Byte output raster data type (1 for int16), and an output name
#for the reprojected image:
processing.runalg("gdalogr:warpreproject", rasterLyr,"EPSG:4326", "EPSG:3722", None, 0, None, "/0,qgis_data/rasters/warped.tif")
# Verify that the output image, warped.tif, was properly created in the filesystem.

#========================================================
#       Creating an elevation hillshade
#========================================================

#Import the processing module:
import processing
# Load and validate the layer:
rasterLyr = QgsRasterLayer("/qgis_data/rasters/dem.asc","Hillshade")
rasterLyr.isValid()

#Run the Hillshade algorithm, providing the algorithm name, layer reference,
#band number, compute edges option, zevenbergen option for smoother terrain,
#z-factor elevation exaggeration number, scaling ratio of vertical to horizontal units,
#azimuth (angle of the light source), altitude (height of the light source), and output
#image's name:
processing.runandload("gdalogr:hillshade", rasterLyr, 1,False, False, 1.0, 1.0, 315.0, 45.0,"/qgis_data/rasters/hillshade.tif")
# Verify that the output image, hillshade.tif, looks similar to the following
#image in QGIS. It should be automatically


#========================================================
#       Creating vector contours from elevation data
#========================================================


#Import the processing module.
import processing
# Load and validate the DEM:
rasterLyr = QgsRasterLayer("/qgis_data/rasters/dem.asc","DEM")
rasterLyr.isValid()
# Add the DEM to the map using the mapLayerRegistry method:
QgsMapLayerRegistry.instance().addMapLayers([rasterLyr])
# Run the contour algorithm and draw the results on top of the DEM layer, specifying
#the algorithm name, layer reference, interval between contour lines in map units,
#name of the vector data attribute field that will contain the elevation value, any extra
#parameters, and output filename:
processing.runandload("gdalogr:contour", rasterLyr, 50.0,"Elv", None, "/qgis_data/rasters/contours.shp")


#========================================================
#       Sampling a raster dataset using a regular grid
#========================================================



#========================================================

#  Adding elevation data to line vertices usinga digital elevation model
#========================================================

#If you have a transportation route through some terrain, it is useful to know the elevation
#profile of that route.

#Import the processing module:
import processing
# Set up the filenames as variables, so they can be used throughout the script:
pth = "/qgis_data/rasters/path/"
rasterPth = pth + "elevation.asc"
vectorPth = pth + "path.shp"
pointsPth = pth + "points.shp"
elvPointsPth = pth + "elvPoints.shp"
# Load and validate the source layers:
rasterLyr = QgsRasterLayer(rasterPth, "Elevation")
rasterLyr.isValid()
vectorLyr = QgsVectorLayer(vectorPth, "Path", "ogr")
vectorLyr.isValid()
#Add the layers to the map:
QgsMapLayerRegistry.instance().addMapLayers([vectorLyr,rasterLyr])
# Create an intermediate point dataset from the line using a SAGA algorithm in the
#Processing Toolbox:
processing.runalg("saga:convertlinestopoints", vectorLyr,False, 1, pointsPth)
# Finally, use another processing algorithm from SAGA to create the final dataset with
#the grid values assigned to the points:
processing.runandload("saga:addgridvaluestopoints", pointsPth,rasterPth, 0, elvPointsPth)

#========================================================

#  Creating a common extent for rasters
#========================================================

#Import the processing module:
import processing
# Run the newly added processing algorithm, specifying the algorithm name, path to
# the two images, an optional no data value, an output directory for the unified images,
#and a Boolean flag to load the images into QGIS:
processing.runalg("script:unifyextentandresolution","/qgis_data/rasters/Image2.tif;/qgis_data/rasters/Image1.tif",-9999,"/qgis_data/rasters",True)
# In the QGIS table of contents, verify that you have two images named:
Image1_unified.tif
Image2_unfied.tif


#========================================================

# Resampling raster resolution
#========================================================
#Resampling to a lower resolution, also known as downsampling, requires you to
#remove pixels from the image while maintaining the geospatial referencing integrity of thedataset.

#Import the processing module:
import processing
# Load and validate the raster layer:
rasterLyr = QgsRasterLayer("/qgis_data/rasters/SatImage.tif","Resample")
rasterLyr.isValid()
# The algorithm requires projection information. We are not changing it, so just
#assign the current projection to a variable:
epsg = rasterLyr.crs().postgisSrid()
srs = "EPSG:%s" % epsg
# Get the current pixel's ground distance and multiply it by 2 to calculate half the
#ground resolution. We only use the X distance because in this case, it is identical
#to the Y distance:
res = rasterLyr.rasterUnitsPerPixelX() * 2
# Run the resampling algorithm, specifying the algorithm name, layer reference, input
#and then output spatial reference system, desired resolution, resampling algorithm
#(0 is the nearest neighbor), any additional parameters, 0 for output raster data type,
#and the output filename:
processing.runalg("gdalogr:warpreproject", rasterLyr, srs,srs, res, 0, None, 0, "/qgis_data/rasters/resampled.tif")
# Verify that the resampled.tif image was created in your /qgis_data/rasters directory.

#========================================================
#               Resampling raster resolution
#========================================================
#Remotely-sensed images are not just pictures; they are data. The value of the pixels has
#meaning that can be automatically analyzed by a computer

#Numpy can be accessed through the GDAL package's gdalnumeric module.

#we must import the bridge module called gdalnumeric, which connects GDAL
#to Numpy in order to perform an array math on geospatial images:
import gdalnumeric
# Now, we will load our raster image directly into a multidimensional array:
a = gdalnumeric.LoadFile("/qgis_data/rasters/satimage.tif")
# The following code counts the number of pixel combinations in the image:
b = a.T.ravel()
c=b.reshape((b.size/3,3))
order = gdalnumeric.numpy.lexsort(c.T)
c = c[order]
diff = gdalnumeric.numpy.diff(c, axis=0)
ui = gdalnumeric.numpy.ones(len(c), 'bool')
ui[1:] = (diff != 0).any(axis=1)
u = c[ui]

#  Now, we can take a look at the size of the resulting one-dimensional array to get the unique values count:
u.size

#========================================================
#               Mosaicing rasters
#========================================================


#Run the gdalogr:merge algorithm, specifying the process name, two images,
#a boolean to use the pseudocolor palette from the first image, a boolean to stack
#each image into a separate band, and the output filename:


processing.runalg("gdalogr:merge","C:/qgis_data/rasters/Image2.tif;C:/qgis_data/rasters/Image1.tif",False,False,"/qgis_data/rasters/merged.tif")

# Verify that the merged.tif image has been created and displays the two images as
#a single raster within QGIS.



#========================================================
#               Converting a TIFF image to a JPEG image
#========================================================
#Import the gdal module:
from osgeo import gdal
# Get a GDAL driver for our desired format:
drv = gdal.GetDriverByName("JP2OpenJPEG")
#Open the source image:
src = gdal.Open("/qgis_data/rasters/satimage.tif")
# Copy the source dataset to the new format:
tgt = drv.CreateCopy("/qgis_data/rasters/satimage.jp2", src)


#========================================================
#               Creating pyramids for a raster
#========================================================

#Import the processing module:
import processing
#Run the gdalogr:overviews algorithm, specifying the process name, input
#image, overview levels, the option to remove existing overviews, resampling method
#(0 is the nearest neighbor), and overview format (1 is internal):
processing.runalg("gdalogr:overviews","/qgis_data/rasters/FalseColor.tif","2 4 8 16",True,0,1)


#Now, load the raster into QGIS by dragging and dropping it from the filesystem
#onto the map canvas.
# Double-click on the layer name in the map's legend to open the Layer
#Properties dialog.
# In the Layer Properties dialog, click on the Pyramids tab and verify that the layer
# has multiple resolutions listed.


#========================================================
#               Converting a pixel location to a map coordinate
#========================================================

# We need to import the gdal module:
from osgeo import gdal
# Then, we need to define the reusable function that does the conversion accepting a
# GDAL GeoTransform object containing the raster georeferencing information and
# the pixel's x,y values:
def Pixel2world(geoMatrix, x, y):
	ulX = geoMatrix[0]
	ulY = geoMatrix[3]
	xDist = geoMatrix[1]
	yDist = geoMatrix[5]
	coorX = (ulX + (x * xDist))
	coorY = (ulY + (y * yDist))
	return (coorX, coorY)
# Now, we'll open the image in GDAL
src = gdal.Open("/qgis_data/rasters/Satimage.tif")
# Next, get the GeoTransform object from the image:
geoTrans = src.GetGeoTransform()
# Now, calculate the center pixel of the image:
centerX = src.RasterXSize/2
centerY = src.RasterYSize/2
# Finally, perform the conversion by calling our function:
Pixel2world(geoTrans, centerX, centerY)
# Verify the coordinates returned are close to the following output:
(-89.59486002580364, 30.510227817850406)


#========================================================
#          Converting a map coordinate to a pixel location
#========================================================
#We need to import the gdal module:
from osgeo import gdal
# Then, we need to define the reusable function that does the coordinate to pixel
#conversion. We get the GDAL GeoTransform object containing the raster
#georeferencing information and the map x,y coordinates:
def world2Pixel(geoMatrix, x, y):
	ulX = geoMatrix[0]
	ulY = geoMatrix[3]
	xDist = geoMatrix[1]
	yDist = geoMatrix[5]
	rtnX = geoMatrix[2]
	rtnY = geoMatrix[4]
	pixel = int((x - ulX) / xDist)
	line = int((y - ulY) / yDist)
	return (pixel, line)

#Next, we open the source image:
src = gdal.Open("/qgis_data/rasters/satimage.tif")
# Now, get the GeoTransform object:
geoTrans = src.GetGeoTransform()
# Finally, perform the conversion:
world2Pixel(geoTrans, -89.59486002580364, 30.510227817850406)
# Verify your output is the following:
(1296, 1346)


#========================================================
#          Classifying a raster
#========================================================



















