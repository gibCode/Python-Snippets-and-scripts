
from osgeo import osr

spatialReference = osr.patialReference()
spatialReference.ImportFromEPSG(4326)





#Declare path where to save the shapefile
path = 'c:\\temp\\essai.shp

driver = ogr.GetDriverByName('ESRI SHapefile')

#I create a datasource for my data
shapeData = driver.CreateDataSource(path)


#Create a points layer
layer =shapeData.CreateLayer('customs',spatialReference, ogr.wkbPoint)

#Layer definition attributs
layer_def= laye.GetLayerDefn()

#Define an attribut(name and type)
new_field =ogr.FieldDefn('nom', ogr.PFTString)

#Add field to layer
layer,CreateField(new_field)



# ADDING ENTITIES
#..................................................

#declare a point object
point = ogr.Geometry(ogr.wkbPoint)

#add first point
point.AddPoint(7,7)

#Feature index
featureIndex = 0
#entity with attribut definition
feature = ogr.Feature(layer_def)
#associate feature to geometry
feature.SetGeometry(point)

# define index
feature.SetFID(featureIndex)
#add values to the attribute
feature.SetField("nom","coucou")
#add to layer
layer.CreateFeature(feature)





#terminates the shapefile creation
shapeData,Destroy()






#ogr.wkbPoint
#ogr.wkbLineString
#ogr.wkbLinearString
#ogr.wkbMultiPoint
#ogr.wkbMultiLineString
#ogr.wkbMultiPolygon
