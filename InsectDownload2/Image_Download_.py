import pandas as pd
import re
import os
import urllib.request
import requests, urllib
import numpy as np

# Parent Directories

parent_dir = "C:/Users/rbknight/Desktop/PythonProjects/InsectRecognition/InsectImages/InsectImages/"

df = pd.read_excel('multimedia.xlsx')

df['species'] = df.apply(lambda _: '', axis=1)
df['downloadFlag'] = df.apply(lambda _: '', axis=1)

for i in df.index:

    url = (df['identifier'][i])
    pattern = re.compile(r'[A-Z]{1}[a-z]+_[a-z]+')
    breeds = pattern.finditer(url)

    for breed in breeds:

        df['species'][i] = breed.group(0)



unique_species =df['species'].unique().tolist()

ncounts = np.zeros(len(unique_species))

for i ,ulab in enumerate(unique_species):

    val s =df.loc[df['species' ]= =ulab ,'gbifID']
    ncounts[i ] =len(vals.unique())

    if ncounts[i ]> =5:

        df.loc[df['species' ]= =ulab ,'downloadFlag' ] ='yes'

    else:

        df.loc[df['species' ]= =ulab ,'downloadFlag' ] ='no'


counter = 0
totalDownloaded = 0



for i in df.index:

    url = (df['identifier'][i])
    downloadFlag =df['downloadFlag'][i]

    if ((downloadFlag= ='no')):

        continue

    # check if item is label image
    pattern = re.compile(r'[lL]abel')
    labels = pattern.finditer(url)

    isLabel = False
    for label in labels:

        if label != None:

            isLabel = True


    if ((isLabe l= =True)):

        continue

    # gets taxonomy name, sets it as path
    pattern = re.compile(r'[A-Z]{1}[a-z]+_[a-z]+')
    breeds = pattern.finditer(url)

    for breed in breeds:

        match_breed = breed.group(0)

        breed_path = os.path.join(parent_dir, match_breed)

    # checks if path exists and creates if not

    isExist = os.path.exists(breed_path)
    if not isExist:

        os.makedirs(breed_path)
        print(totalDownloaded)

    # gets id number, set it as path

    pattern = re.compile(r'\d{3,7}_')
    id_nums = pattern.finditer(url)

    for id in id_nums:

        match_id = id.group(0)

        if match_id == None:

            continue

        id_path = os.path.join(breed_path, match_id)

    # checks if path exists, if not creates path
    isExist = os.path.exists(id_path)

    if not isExist:

        os.makedirs(id_path)

    # renames file to id name
    new_image_name = match_id + ".jpg"

    # new_image_name = new_image_
    imagePath = os.path.join(id_path, new_image_name)
    imageExists = os.path.isfile(imagePath)


    image_num = 0
    keepGoing = True

    # checks if id file exists, if so, adds -image_num, where image_num is iteration of while loop
    while keepGoing:

        if imageExists:

            image_num += 1
            str_image = str(image_num)
            new_image_name = match_id + "-" + str_image + ".jpg"


            imagePath = os.path.join(id_path, new_image_name)
            imageExists = os.path.isfile(imagePath)

        else:

            keepGoing = False

            '''

            if imageExists:

                new_image_name = match_id + "-2" + ".jpg"

                imagePath = os.path.join(id_path, new_image_name)

                imageExists = os.path.isfile(imagePath)



                if imageExists:

                    print(totalDownloaded)

                    totalDownloaded += 1



                    continue

                '''

            # creates image path, retrieves image and saves into path

        image_save = os.path.join(id_path, new_image_name)
        urllib.request.urlretrieve(url, image_save)

    # tracker of current position in excel sheet
    totalDownloaded += 1