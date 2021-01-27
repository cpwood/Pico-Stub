import getopt
import json
import os
import sys

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

    # We need to remove any reference to errno or ujson since
    # neither are included on the Pico. We just provided some
    # pollyfills to get the stub generation to work.

    # Remove 'errno' and 'ujson' modules from two JSON files
    process_json(folder + '/info.json')
    process_json(folder + '/stubs/modules.json')

    # Remove the corresponding .py files
    delete_file(folder + '/stubs/errno.py')
    delete_file(folder + '/stubs/ujson.py')

def process_json(file):
   print('  ' + file)
   
   data = None

   with open(file) as input_file:
    data = json.load(input_file)

    for a in data['modules'][:]:
        if (a['module'] == u'errno' or a['module'] == u'ujson'):
            print('    Removed ' + a['module'] + ' ..')
            data['modules'].remove(a)

   with open(file, 'w+') as output_file:
    json.dump(data, output_file)

def delete_file(file):
    if os.path.exists(file):
        print('  Deleting ' + file)
        os.remove(file)

if __name__ == "__main__":
    main(sys.argv[1:])