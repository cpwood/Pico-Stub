import getopt
import json
import os
import sys
import shutil
from pathlib import Path

def main(argv):
    folder = ""

    try:
        opts, args = getopt.getopt(argv,"i:",["folder="])
    except getopt.GetoptError:
        print('post-process.py -i <stubfolder>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-i"):
            folder = arg

    print('  Working with ' + folder + ' ...')

    folder_path = Path(folder)

    folder_name = folder_path.name
    parent_path = folder_path.parent
    temp_path = parent_path.joinpath('temp')

    print('  Arranging directories ...')

    # Create destination folder with name of "temp" (for now)
    if os.path.exists(temp_path):
        os.rmdir(temp_path)

    os.mkdir(temp_path)
    os.mkdir(temp_path.joinpath('stubs'))

    # Move the content of the source folder under temp/stubs
    shutil.move(folder, temp_path)
    os.rename(temp_path.joinpath(folder_name), temp_path.joinpath('stubs'))

    # Now rename "temp" back to the name of the original folder
    os.rename(temp_path, folder)

    # Create info.json by copying modules.json
    shutil.copyfile(folder_path.joinpath('stubs', 'modules.json'), folder_path.joinpath('info.json'))
    
    # Set a "firmware/firmware" value in the JSON
    process_json(str(folder_path.joinpath('info.json')))

def process_json(file):
    print('  Writing ' + file)

    data = None

    with open(file) as input_file:
        data = json.load(input_file)

    data['firmware']['firmware'] = data['firmware']['platform'] + ' v' + data['firmware']['version']

    with open(file, 'w+') as output_file:
        json.dump(data, output_file)

if __name__ == "__main__":
    main(sys.argv[1:])