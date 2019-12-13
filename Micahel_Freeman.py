
import Metashape
import os
import time

#start headless photoscan from command line prompt and save the new project
project = Metashape.app.document
project.save(r'C:\Users\Civil\Desktop\Iteration Test\Model\IterationRunmodel.psx')


#add new chunk to project
chunk = project.addChunk()
chunk.label = "new_chunk"
#chunk = PhotoScan.app.document.chunk
project.save()


#create list of all photos in a folder
images_path = r'C:\Users\Civil\Desktop\Iteration Test\Images'
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


#Aligning Photos
print("Aligning Photots")
chunk.matchPhotos(accuracy=Metashape.LowAccuracy, generic_preselection=True, reference_preselection=True, filter_mask=False, mask_tiepoints=False, keypoint_limit=500000, tiepoint_limit=40000, keep_keypoints=True)
chunk.alignCameras()
project.save()
print("Finished Photo Alignment")


#Build Model
print("Building Model")
chunk.buildModel(surface=Metashape.Arbitrary, interpolation=Metashape.EnabledInterpolation, face_count=Metashape.MediumFaceCount, source=Metashape.PointCloudData, vertex_colors=True, quality=Metashape.HighQuality, volumetric_masks=False, keep_depth=False, reuse_depth=False)
print("Finished Model Construction")


#Export PLY File
print("Exporting .PLY Model")
chunk.exportModel(r'C:\Users\Civil\Desktop\Iteration Test\Export_PLY\Iteration1.ply', binary=True, precision=6, texture_format=Metashape.ImageFormatJPEG, texture=False, normals=True, colors=True, cameras=False, markers=False, udim=False, alpha=False, strip_extensions=False, raster_transform=Metashape.RasterTransformNone, colors_rgb_8bit=True, format=Metashape.ModelFormatPLY, projection=Metashape.CoordinateSystem("EPSG::4326"))
project.save()
print("Finished Exporing .PLY Model")
	
