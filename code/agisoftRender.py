import Metashape
import os
import time



def firefly(
        project_path='',
        Iteration=0,
        Images_path=r'..\rawImageBin',
        export_location='',
        export_path=''
):
    '''
    :param project_path: Path within results folder that will save the project
    :param Iteration
    :param Images_path:
    :return:
    '''


    #date system for tagging
    today = date.today()
    day = today.day
    month = today.month
    year = today.year

    # folder for results
    if project_path == '':
        results_folder_name = f"{day}.{month}.{year}"
        results_folder_dir = "../Results/" + results_folder_name + f"/iteration {Iteration}"
        Path(results_folder_dir).mkdir(parents=True, exist_ok=True)
    else:
        results_folder_dir = project_path + f"/iteration {Iteration}"
        Path(results_folder_dir).mkdir(parents=True, exist_ok=True)

    # start timing of process
    start_time = time.clock()

    #save the project
    print('Creating Project')
    project = Metashape.app.document
    project.save(results_folder_dir)

    # add new chunk to above project
    print('Adding Chunk')
    chunk = project.addChunk()
    chunk.label = "new_chunk"
    project.save()

    # create list of all photos in a folder
    print('Creating List of Photos')
    images_list = os.listdir(images_path)
    project.save()

    # add each photo to the chunk
    print('Adding Images to Chunk')
    for image in images_list:
        try:
            chunk.addPhotos([images_path + "\\" + image])
        except
            print("---some photos were not loaded correctly---")
            continue

    # align photos
    print('Aligning photos')
    chunk.matchPhotos(
        accuracy=Metashape.LowAccuracy,
        generic_preselection=True,
        reference_preselection=True,
        filter_mask=False,
        mask_tiepoints=False,
        keypoint_limit=500000,
        tiepoint_limit=40000,
        keep_keypoints=True
        )
    chunk.alignCameras()
    project.save()
    print('Finished Photo Alignment')

    # Build Model
    print('Building Model')
    chunk.buildModel(
        surface=Metashape.Arbitrary,
        interpolation=Metashape.EnabledInterpolation,
        face_count=Metashape.MediumFaceCount,
        source=Metashape.PointCloudData,
        vertex_colors=True,
        quality=Metashape.HighQuality,
        volumetric_masks=False,
        keep_depth=False,
        reuse_depth=False
    )
    print('Finished Building Model')

    # Export PLY File
    print("Exporting .PLY Model")
    chunk.exportModel(
        export_location,
        binary=True,
        precision=6,
        texture_format=Metashape.ImageFormatJPEG,
        texture=False,
        normals=True,
        colors=True,
        cameras=False,
        markers=False,
        udim=False,
        alpha=False,
        strip_extensions=False,
        raster_transform=Metashape.RasterTransformNone,
        colors_rgb_8bit=True,
        format=Metashape.ModelFormatPLY,
        projection=Metashape.CoordinateSystem("EPSG::4326"))
    project.save()
    print("Finished Exporting .PLY Model")

    # show model creation time
    end_agisoft = clock.time
    time_agisoft = end_agisoft - start_time
    print(f'Time in Agisoft: {time_agisoft}')

    # Begin omega calculation



