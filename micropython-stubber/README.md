# Micropython-Stubber

## Using the Stubs

### First use on your computer

Clone or [download](https://github.com/cpwood/Pico-Stub/archive/main.zip) this repo to your computer. 

### When starting new projects

1. In your project root, create a `.vscode` folder (note the preceding `.`).
2. Copy the contents of this repository's `vscode` folder to the `.vscode` folder you just created.
3. Update the two paths to `micropython-rp2-1_13-290` in `settings.json` as appropriate.
4. Copy the `.pylintrc` file in this repository's `pylint` folder to the root of your project.
5. Update the path to `micropython-rp2-1_13-290` in `.pylintrc` as appropriate.

## Generating the Stubs

The stub content is generated using [Josverl/micropython-stubber](https://github.com/Josverl/micropython-stubber) using the [minified version of `createstubs.py`](https://github.com/Josverl/micropython-stubber/blob/master/minified/createstubs.py). Some polyfilling and post-processing is required since the Pico board doesn't support `ujson` which is used by `createstubs.py`.

To generate the stub files, copy all the files within the `board` folder to your Pico and then reboot it. Upon reboot, you will see that the stub generation begins after a short delay.

Once complete, you'll need to copy all the generated files back to your computer. Although this project is aimed at VS Code, copying the files is actually easiest using [Thonny's](https://thonny.org/) file manager at the moment!

Copy the "micropython" folder that's been created on your Pico back to your computer.

>  If you're preparing a pull request for this repo, place the folder you copied back within the `micropython-stubber` folder. Overwrite any existing folders, but don't delete anything.