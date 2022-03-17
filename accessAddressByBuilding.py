####Description: Streamlines workflow after building polygons are sliced (USE SLICE ON STEROIDS TOOL IN CUSTOM PLUGINS)"
###Author: Darren Guthrie 


import time
tmStart = time.time()



#CHANGE HERE:
building_path = "C:\\Users\\dguthrie\\Desktop\\buildings\\C328050001_buildings.geojson"
### File path to polygon
layer_name = "buildings"
###layer name for polygon
vlyr = QgsVectorLayer(building_path, layer_name, "ogr")

QgsProject.instance().addMapLayer(vlyr)
###Adds file to map

adp_path = "C:\\Users\\dguthrie\\Desktop\\buildings\\C328050001_units.geojson"
###address point file path
point_layer_name = "ADPs"
###layer name for address points
adplayer = QgsVectorLayer(adp_path, point_layer_name, "ogr")

QgsProject.instance().addMapLayer(adplayer)
###adds address layer to map

ac_path = "C:\\Users\\dguthrie\\Desktop\\buildings\\C328050001_access_points.geojson"
###access point file path
ac_layer = "access_points"
### access point layer name
access_points = QgsVectorLayer(ac_path, ac_layer, "ogr")

QgsProject.instance().addMapLayer(access_points)
### add access points to map

#Hardcoded inputs (change to variables later)
processing.run("native:selectbylocation",\
{'INPUT':'C:\\Users\\dguthrie\\Desktop\\buildings\\C328050001_units.geojson',\
'PREDICATE':[0,1],\
'INTERSECT':'C:\\Users\\dguthrie\\Desktop\\buildings\\C328050001_buildings.geojson',\
'METHOD':0})
###Select from location of APD where building polygons present
##Spatial Join ADPs to building polygons


layer = adplayer
###layer
ex_layer = 'C:\\Users\\dguthrie\\Desktop\\buildings\\exADPs.geojson'
###New exported file CHANGE NAME AFTER RUNNING SCRIPT

writer = QgsVectorFileWriter.writeAsVectorFormat(layer, ex_layer, 'utf-8', driverName= 'geojson', onlySelected=True)
selected_ADP = iface.addVectorLayer(ex_layer, '', 'ogr')
##### selected and export features





##CHANGE HERE:
fnpoly = 'C:\\Users\\dguthrie\\Desktop\\buildings\\C328050001_buildings.geojson'
fnpts = 'C:\\Users\\dguthrie\\Desktop\\buildings\\C328050001_units.geojson'
polyADP = 'buildingsADPJoined.geojson'
#####Defines input units and building, and lastly output file

processing.run("native:joinattributesbylocation", {'INPUT': fnpoly,\
'JOIN':fnpts,\
'PREDICATE':[1,5],\
'JOIN_FIELDS':['addr:unit'],\
'METHOD':0,'DISCARD_NONMATCHING':False,\
'PREFIX':'joined_','OUTPUT':'polyADP'})
####adds Spatial join output







processing.run("native:joinattributesbylocation", {'INPUT': access_points,\
'JOIN':fnpoly,\
'PREDICATE':[1,5],\
'JOIN_FIELDS':['BLD_ID'],\
'METHOD':0,'DISCARD_NONMATCHING':False,\
'PREFIX':'','OUTPUT':'TEMPORARY_OUTPUT'})
###Spatial Join Buildings to AC


tmEnd = time.time()
print("Run time: {0:3f} seconds".format(tmEnd-tmStart))


