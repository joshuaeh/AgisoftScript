#1. to run this script open command prompt and type the following line 
### cd ../..
#2. hit enter then type the following line
### cd Program Files\Agisoft\PhotoScan Pro 
#2. hit enter then type the folloring command and hit enter
### photoscan -r C:\Users\Civil\Desktop\Agisoft_Script\start_photoscan.py
#3. the script will run and create a new photoscan file named test.psx in the Agisoft_Script folder on the desktop

import Metashape
import os
import time

#start headless photoscan from command line prompt and save the new project
project = Metashape.app.document
project.save(r'E:\Practice Models\Rock_Canyon_Spillway_06Aug2019\model.psx')


#add new chunk to project
chunk = project.addChunk()
chunk.label = "new_chunk"
#chunk = PhotoScan.app.document.chunk
project.save()


#create list of all photos in a folder
images_path = r'E:\Practice Models\Rock_Canyon_Spillway_06Aug2019\Pictures'
images_list = os.listdir(images_path)
project.save()

#add each photo to the chunk
for image in images_list:
	try:
		chunk.addPhotos([images_path + "\\" + image]) 
	except:
		print("Some photos were not loaded correctly")
		continue

print("Finished loading pictures")
chunk.matchPhotos(accuracy=PhotoScan.HighAccuracy, preselection=PhotoScan.GenericPreselection)
chunk.alignCameras()
project.save()

##chunk.buildDepthMaps()
##chunk.buildDenseCloud()
##project.save()
##
##chunk.buildModel(surface=PhotoScan.Arbitrary, interpolation=PhotoScan.EnabledInterpolation, face_count=5000, vertex_colors=True)

project.save()
print("Code ran without any exceptions")
	
