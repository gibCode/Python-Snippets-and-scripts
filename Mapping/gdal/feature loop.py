

feature = layer.GetNextFeature()

while feature:
    #print the name value of the current entity
    print feature.GetField("name")

    <-- area to include code below -->
    #request nect entity
    feature = layer. GetNextfeature()


GEOMETRY
	to get geometry add code to loop
<--
geography - feature.GetGeometryRef()
print geography
-->