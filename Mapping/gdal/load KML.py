from osgeo import ogr

kmlfile='baloon.kml'

driver = ogr.GetDriverByName('KML')
datasource =driver.Open(kmlfile)

layer = datasource.GetLayer()

nbFeat = layer.GetFeatureCount()
print nbFeat


