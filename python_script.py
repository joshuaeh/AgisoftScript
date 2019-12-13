import PhotoScan
import os
import time

#this is just a built in python method for keeping track of processing time
start = time.time()


#path_save: path to folder where we want to save our project
path_save=r'C:\Users\Civil\Desktop\test_agisoft_script.psx'
#path_photos: path to where the folder containing our photos
path_photos=r'C:\Users\Civil\Desktop\Agisoft_Script\RCP_20m-80m\20m'
#path_points: path where we want to save our .ply file including file save name and .ply
path_points=r'C:\Users\Civil\Desktop\test_points.ply' 
#path_report: path to where we want to save our report as well as the name and .pdf
#path_report=r'E:\Algorithm Developments\Iterative Model Refinement\RCP Jul 4 2017\RC1_7.4.17\RC1_flights_7.5.17\script_test_file\report_60m-MM.pdf' 


###All of the following 5 variables can be changed to increase accuracy of the model
model_quality=PhotoScan.MediumQuality
photo_accuracy = PhotoScan.MediumAccuracy
num_faces = 5000
texture_size = 4096
coordinate_system = "EPSG::3742"


#create a save name for project and save it
doc = PhotoScan.app.document
doc.save(path_save)

#create chunk, name the chunk, set the chunk to active 
chunk = PhotoScan.app.document.addChunk()
chunk.label= "new_chunk"

#populate a list with the photos from path_photos
photo_list = os.listdir(path_photos)

#for each member in the list try to add it to our active chunk 
###the try except is very important because the list goes one beyond our photos and returns an error
for photo_name in photo_list:
	try:
		chunk.addPhotos([path_photos + "\\" + photo_name]) 
	except:
		continue

#match, align, and optimize photos that have been added		
chunk.matchPhotos(accuracy=photo_accuracy, preselection=PhotoScan.GenericPreselection)
chunk.alignCameras()
chunk.optimizeCameras(fit_f=True, fit_cxcy=True, fit_aspect=True, fit_skew=True, fit_k1k2k3=True, fit_p1p2=True, fit_k4=False)

#set coordinate system for each camera
n_crs = PhotoScan.CoordinateSystem(coordinate_system)
for camera in chunk.cameras:
	camera.reference.location = PhotoScan.CoordinateSystem.transform(camera.reference.location, chunk.crs, n_crs)

#build the dense cloud and then build the model
doc.save
chunk.buildDenseCloud()
chunk.buildModel(surface=PhotoScan.Arbitrary, interpolation=PhotoScan.EnabledInterpolation, face_count=num_faces, vertex_colors=True)

#build UV has to be done before the texture can be built
#chunk.buildUV(mapping=PhotoScan.GenericMapping)
#chunk.buildTexture(blending=PhotoScan.MosaicBlending, size=texture_size, fill_holes=True)

#generate the .ply for the points and the .pdf for the report
###photoscan requires the project is aved before a report can be generated
doc.save()
chunk.exportPoints(path_points, binary = False, precision = 6, normals= True, colors= True, source = PhotoScan.DataSource.PointCloudData, format = PhotoScan.PointsFormatPLY, projection=PhotoScan.CoordinateSystem("EPSG::3742"))
#chunk.exportReport(path_report)

end = time.time()
print("Total program run time: ", end-start)
resolution = PhotoScan.Elevation.resolution

#print(resolution)

doc.save
#app.quit()



