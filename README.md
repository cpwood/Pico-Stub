# Pico-Stub

## Introduction
This repository contains MicroPython stubs for the Raspberry Pi Pico, allowing you to benefit from Python code linting and autocompletion in Visual Studio Code.

## Using the stubs
### First use on your computer
Clone this repository to your computer. 

### When starting a new project
1. In your project root, create a `.vscode` folder (note the preceding `.`).
2. Copy the contents of this repository's `vscode` folder to the `.vscode` folder you just created.
3. Update the two paths to `micropython-rp2-1_13-290` in `settings.json` as appropriate.
4. Copy the `.pylintrc` file in this repository's `pylint` folder to the root of your project.
5. Update the path to `micropython-rp2-1_13-290` in `.pylintrc` as appropriate.

## Generating the stubs
### Prerequisites
You'll need to be able to copy files to and from your Pico board and also have Node installed on your computer.

### Steps
The stub content is generated using [Josverl/micropython-stubber](https://github.com/Josverl/micropython-stubber) using the [minified version of `createstubs.py`](https://github.com/Josverl/micropython-stubber/blob/master/minified/createstubs.py). Some pollyfilling and post-processing is required since the Pico board doesn't support `ujson` which is used by `createstubs.py`.

To generate the stub files, copy all the files within the `board` folder to your Pico and then reboot it. Upon reboot, you will see that the stub generation begins after a short delay.

Once complete, you'll need to copy all the generated files back to your computer. Although this project is aimed at VS Code, copying the files is actually easiest using [Thonny's](https://thonny.org/) file manager at the moment!

When you've copied the "micropython" folder back, place it in this repo's `stub` folder.

Then run prettify.js using node:

```
node prettify.js
```

You may need to modify the path to `modules.json` within `prettify.js`.

This will post-process the `modules.json` file within the "micropython" folder in two ways:

1. it will change the single-quotes to standard JSON double-quotes; and
2. it will generally prettify the file, ensuring the JSON is properly nested with indentation.
