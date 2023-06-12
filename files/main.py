from auxFunctions import *
import json
from PIL import Image

def mainProcess(browserPath, editedSuffix):
    piexifCodecs = [k.casefold() for k in ['TIF', 'TIFF', 'JPEG', 'JPG']]

    mediaMoved = []  # array with names of all the media already matched
    path = browserPath  # source path
    fixedMediaPath = path + "\MatchedMedia"  # destination path
    nonEditedMediaPath = path + "\EditedRaw"
    errorCounter = 0
    successCounter = 0
    editedWord = editedSuffix or "editado"
    print(editedWord)

    try:
        obj = list(os.scandir(path))  #Convert iterator into a list to sort it
        obj.sort(key=lambda s: len(s.name)) #Sort by length to avoid name(1).jpg be processed before name.jpg
        createFolders(fixedMediaPath, nonEditedMediaPath)
    except Exception as e:
        print("Choose a valid directory")
        return

    for entry in obj:
        if entry.is_file() and entry.name.endswith(".json"):  # Check if file is a JSON
            print(entry)
            with open(entry, encoding="utf8") as f:  # Load JSON into a var
                data = json.load(f)

            progress = round(obj.index(entry)/len(obj)*100, 2)
            print(str(progress) + "%")

            #SEARCH MEDIA ASSOCIATED TO JSON

            titleOriginal = data['title']  # Store metadata into vars

            try:
                title = searchMedia(path, titleOriginal, mediaMoved, nonEditedMediaPath, editedWord)

            except Exception as e:
                print("Error on searchMedia() with file " + titleOriginal)
                errorCounter += 1
                continue

            filepath = path + "/" + title
            if title == "None":
                print(titleOriginal + " not found")
                errorCounter += 1
                continue

            # METADATA EDITION
            timeStamp = int(data['photoTakenTime']['timestamp'])  # Get creation time
            print(filepath)

            if title.rsplit('.', 1)[1].casefold() in piexifCodecs:  # If EXIF is supported
                try:
                    im = Image.open(filepath)
                    rgb_im = im.convert('RGB')
                    os.replace(filepath, filepath.rsplit('.', 1)[0] + ".jpg")
                    filepath = filepath.rsplit('.', 1)[0] + ".jpg"
                    rgb_im.save(filepath)

                except ValueError as e:
                    print("Error converting to JPG in " + title)
                    errorCounter += 1
                    continue

                try:
                    set_EXIF(filepath, data['geoData']['latitude'], data['geoData']['longitude'], data['geoData']['altitude'], timeStamp)

                except Exception as e:  # Error handler
                    print("Inexistent EXIF data for " + filepath)
                    print(str(e))
                    errorCounter += 1
                    continue

            os.utime(filepath, (timeStamp, timeStamp)) # Set Unix creation and modification time

            #MOVE FILE AND DELETE JSON

            os.replace(filepath, fixedMediaPath + "/" + title)
            os.remove(path + "/" + entry.name)
            mediaMoved.append(title)
            successCounter += 1

    sucessMessage = " successes"
    errorMessage = " errors"

    #UPDATE INTERFACE
    if successCounter == 1:
        sucessMessage = " success"

    if errorCounter == 1:
        errorMessage = " error"

    print("100% complete!")
    print("Matching process finished with " + str(successCounter) + sucessMessage + " and " + str(errorCounter) + errorMessage + ".")

