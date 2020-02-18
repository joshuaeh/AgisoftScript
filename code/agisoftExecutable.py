import Metashape
import os
import sys
import math
from pathlib import Path


#Arguments that need to be passed
results_folder = sys.argv[1]  											 				# first argument: cwd
iteration_number = sys.argv[2]  										 	# Second argument: iteration number
project_name = os.path.join(results_folder, r'metashape\model.psx')
subfolder = os.path.join(working_folder, r'iteration_' + str(iteration_number))
cwd = Path.cwd()
print('Passed to Methashape:')
print(f'''project name: {project_name}
subfolder: {subfolder}
current working directory: {cwd}
''')

# 
# #Save new project
# doc = Metashape.app.document
# doc.open(project_name, read_only = False)
# #Load the photos
# images_list = os.listdir(photos_location)
# chunk = doc.chunk
# #Change reference coordinate system temporarily to import photos
# temp_crs = Metashape.CoordinateSystem("EPSG::4326")
# chunk.crs = temp_crs
# chunk.updateTransform
# doc.read_only = False
# doc.save()
# 
# #add each photo to the chunk
# for image in images_list:
# 	try:
# 		chunk.addPhotos([photos_location + "\\" + image]) 
# 	except:
# 		print("Some photos were not loaded correctly")
# 		continue
# 
# #Change reference coordinate system to Local Coordinates
# out_crs = Metashape.CoordinateSystem('LOCAL_CS["Local Coordinates",LOCAL_DATUM["Local Datum",0],UNIT["metre",1,AUTHORITY["EPSG","9001"]]]')
# 
# # for camera in chunk.cameras:
# #     if camera.reference.location:
# #         camera.reference.location = Metashape.CoordinateSystem.transform(camera.reference.location, chunk.crs, out_crs)
# 
# chunk.crs = out_crs
# chunk.updateTransform()
# 
# chunk.matchPhotos(accuracy=Metashape.HighAccuracy, preselection=Metashape.GenericPreselection)
# chunk.alignCameras()
# chunk.optimizeCameras(fit_f=True, fit_cxcy=True, fit_aspect=True, fit_skew=True, fit_k1k2k3=True, fit_p1p2=True, fit_k4=False)
# doc.save()
# #Generate DenseCloud
# chunk.buildDepthMaps()
# chunk.buildDenseCloud()
# chunk.buildDem()
# chunk.buildOrthomosaic()
# res1 = round(chunk.orthomosaic.resolution,4)
# res2 = round(chunk.elevation.resolution,4)
# print('----RESOLUTION : ' + str(res1) + '/pixel')
# print('----RESOLUTION : ' + str(res2) + '/pixel')
# 
# res_file = open(os.path.join(subfolder,'resolution.txt'),'w')
# res_file.write(str(res1) + '\n')
# res_file.write(str(res2))
# res_file.close()
# 
# #Export
# chunk.exportPoints(points_location, normals = False,colors=False,format = Metashape.PointsFormatXYZ)
# print('Point Clouds ready')
# chunk.exportReport(report_location)
# print('Report ready')
# doc.save()
# Metashape.app.quit()
# print('Metashape save and exit : Successfull')