import json
import os
import sys
import shutil
from pathlib import Path

def main():
    folder_path = Path(os.path.dirname(os.path.realpath(__file__))).parent
    print('  Working with ' + folder_path + ' ...')

    folder_name = folder_path.name
    
    generated_path = folder_path.joinpath("generated")
    frozen_path = folder_path.joinpath("frozen")
    dist_path = folder_path.joinpath("dist")
    micropy_path = dist_path.joinpath("micropy-cli")
    pylance_path = dist_path.joinpath("pylance")

    print('  Processing Micropy-CLI ...')

    if os.path.exists(micropy_path):
        os.rmdir(micropy_path)

    os.mkdir(micropy_path)
    os.mkdir(micropy_path.joinpath("stubs"))

    # Create info.json by copying modules.json
    shutil.copyfile(generated_path.joinpath("modules.json"), micropy_path.joinpath("info.json"))

    # Set a "firmware/firmware" value in the JSON
    process_json(str(micropy_path.joinpath("info.json")))

    # Copy the frozen modules
    shutil.copytree(folder_path.joinpath("frozen"), micropy_path.joinpath("frozen"))

    # Create version.json by copying from the root of the repo
    shutil.copyfile(folder_path.joinpath("version.json"), micropy_path.joinpath("version.json"))

    print('  Processing Pylance ...')

    if os.path.exists(pylance_path):
        os.rmdir(pylance_path)

    os.mkdir(pylance_path)
    os.mkdir(pylance_path.joinpath("stdlib"))
    os.mkdir(pylance_path.joinpath("stubs"))

    # Create version.json by copying from the root of the repo
    shutil.copyfile(folder_path.joinpath("version.json"), pylance_path.joinpath("version.json"))

    # Copy frozen items to their respective destinations
    # stdlib
    shutil.copytree(frozen_path.joinpath("_typeshed"), pylance_path.joinpath("stdlib", "_typeshed"))
    shutil.copytree(frozen_path.joinpath("collections"), pylance_path.joinpath("stdlib", "collections"))
    shutil.copytree(frozen_path.joinpath("importlib"), pylance_path.joinpath("stdlib", "importlib"))
    shutil.copyfile(frozen_path.joinpath("_ast.pyi"), pylance_path.joinpath("_ast.pyi"))
    shutil.copyfile(frozen_path.joinpath("_collections_abc.pyi"), pylance_path.joinpath("_collections_abc.pyi"))
    shutil.copyfile(frozen_path.joinpath("_importlib_modulespec.pyi"), pylance_path.joinpath("_importlib_modulespec.pyi"))
    shutil.copyfile(frozen_path.joinpath("_thread.pyi"), pylance_path.joinpath("_thread.pyi"))
    shutil.copyfile(frozen_path.joinpath("abc.pyi"), pylance_path.joinpath("abc.pyi"))
    shutil.copyfile(frozen_path.joinpath("array.pyi"), pylance_path.joinpath("array.pyi"))
    shutil.copyfile(frozen_path.joinpath("ast.pyi"), pylance_path.joinpath("ast.pyi"))
    shutil.copyfile(frozen_path.joinpath("binascii.pyi"), pylance_path.joinpath("binascii.pyi"))
    shutil.copyfile(frozen_path.joinpath("builtins.pyi"), pylance_path.joinpath("builtins.pyi"))
    shutil.copyfile(frozen_path.joinpath("gc.pyi"), pylance_path.joinpath("gc.pyi"))
    shutil.copyfile(frozen_path.joinpath("io.pyi"), pylance_path.joinpath("io.pyi"))
    shutil.copyfile(frozen_path.joinpath("math.pyi"), pylance_path.joinpath("math.pyi"))
    shutil.copyfile(frozen_path.joinpath("mmap.pyi"), pylance_path.joinpath("mmap.pyi"))
    shutil.copyfile(frozen_path.joinpath("os.pyi"), pylance_path.joinpath("os.pyi"))
    shutil.copyfile(frozen_path.joinpath("random.pyi"), pylance_path.joinpath("random.pyi"))
    shutil.copyfile(frozen_path.joinpath("select.pyi"), pylance_path.joinpath("select.pyi"))
    shutil.copyfile(frozen_path.joinpath("struct.pyi"), pylance_path.joinpath("struct.pyi"))
    shutil.copyfile(frozen_path.joinpath("sys.pyi"), pylance_path.joinpath("sys.pyi"))
    shutil.copyfile(frozen_path.joinpath("time.pyi"), pylance_path.joinpath("time.pyi"))
    shutil.copyfile(frozen_path.joinpath("types.pyi"), pylance_path.joinpath("types.pyi"))
    shutil.copyfile(frozen_path.joinpath("typing.pyi"), pylance_path.joinpath("typing.pyi"))
    shutil.copyfile(frozen_path.joinpath("uarray.pyi"), pylance_path.joinpath("uarray.pyi"))
    shutil.copyfile(frozen_path.joinpath("uasyncio"), pylance_path.joinpath("uasyncio"))
    shutil.copyfile(frozen_path.joinpath("ubinascii.pyi"), pylance_path.joinpath("ubinascii.pyi"))
    shutil.copyfile(frozen_path.joinpath("uio.pyi"), pylance_path.joinpath("uio.pyi"))
    shutil.copyfile(frozen_path.joinpath("uos.pyi"), pylance_path.joinpath("uos.pyi"))
    shutil.copyfile(frozen_path.joinpath("urandom.pyi"), pylance_path.joinpath("urandom.pyi"))
    shutil.copyfile(frozen_path.joinpath("uselect.pyi"), pylance_path.joinpath("uselect.pyi"))
    shutil.copyfile(frozen_path.joinpath("ustruct.pyi"), pylance_path.joinpath("ustruct.pyi"))
    shutil.copyfile(frozen_path.joinpath("usys.pyi"), pylance_path.joinpath("usys.pyi"))
    shutil.copyfile(frozen_path.joinpath("utime.pyi"), pylance_path.joinpath("utime.pyi"))

    # stubs
    copy_to_pylance_folder(frozen_path.joinpath("btree.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("ds18x20.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("framebuf.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("machine.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("micropython.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("onewire.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("rp2.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("typing_extensions.pyi"), pylance_path)

def process_json(file):
    print('  Writing ' + file)

    data = None

    with open(file) as input_file:
        data = json.load(input_file)

    data['firmware']['firmware'] = data['firmware']['platform'] + ' v' + data['firmware']['version']

    with open(file, 'w+') as output_file:
        json.dump(data, output_file)

def copy_to_pylance_folder(frozen_file: Path, pylance_path: Path):
    folder_name = frozen_file.name.replace(".pyi", "")
    os.mkdir(pylance_path.joinpath("stubs", folder_name))
    shutil.copyfile(frozen_file, pylance_path.joinpath("stubs", folder_name, frozen_file.name))

if __name__ == "__main__":
    main()