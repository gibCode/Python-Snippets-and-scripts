import gdal.sys

from gdalconst import *

gdal.AllRegister()
filename =r"alberta_2011/tiff"

ds = gdal.Open(ilename, GA_Readonly)

if ds is None:
print 'could not open' + filename
sys.exit(1)

cols = ds.RasterXSize
rows = ds.RasterYSize

bands = ds.RasterCount
print cols, rows, bands

 