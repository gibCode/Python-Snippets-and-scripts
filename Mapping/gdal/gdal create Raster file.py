import numpy, sys
from osgeo import gdal
from osgeo.gdalconst import *


gdalAllRegister()


driver = gdal.GetDriverByName("GTiff")


rows =50
cols=50


image =driver.Create("c:temp/test.tif", cols, rows,1 GDT_Int32)

band = image.GetRasterBand(1)

data = numpy.zeros((rows,cols), numpy.int16)

band.WriteArray(data,0,0)

band.FlushCache()
band.SetNoDataValue(-99)

del data