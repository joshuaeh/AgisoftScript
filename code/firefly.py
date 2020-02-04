import Metashape
import os
import time



def firefly(
        project_path='',
        Iteration=0,
        Images_path=r'..\rawImageBin'


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

    # start timing of process
    start_time = time.clock()

    #save the project
    project = Metashape.app.document
    project.save(project_path)

    # add new chunk to above project
    chunk = project.addChunk()
    chunk.label = "new_chunk"
    project.save()

    # create list of all photos in a folder
    images_list = os.listdir(images_path)
    project.save()

    # add each photo to the chunk
    for image in images_list:
        try:
            chunk.addPhotos([images_path + "\\" + image])
        except *:
            print("some photos were not loaded correctly")
            continue
