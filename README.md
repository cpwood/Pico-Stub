# Pico-Stub

This repository contains MicroPython stubs for the Raspberry Pi Pico, allowing you to benefit from Python code linting and autocompletion in Visual Studio Code.

![alt text](https://raw.githubusercontent.com/cpwood/Pico-Stub/main/screenshot.png "Screenshot")

## Using the Stubs

You can set up Visual Studio Code to use these stubs manually or using [Micropy CLI](https://github.com/BradenM/micropy-cli) (recommended). 

* [Using Micropy CLI](micropy.md#using-the-stubs) (recommended)
* [Manual Instructions](micropython-stubber.md#using-the-stubs) 

This two-part series will get you going with development for the Pico in MicroPython using VS Code:

* [Part One - Setting up your environment](https://medium.com/all-geek-to-me/developing-for-the-raspberry-pi-pico-in-vs-code-getting-started-6dbb3da5ba97)
* [Part Two - Start coding!](https://medium.com/all-geek-to-me/developing-for-the-raspberry-pi-pico-in-vs-code-start-coding-bb3834233eff)

## Generating the Stubs

This isn't something you *need* to do; the stubs are already included in this repository within the `stubs` directory.

However, if you want to do this yourself, you can do so using [Micropython-Stubber](https://github.com/Josverl/micropython-stubber).

* [Using Micropython-Stubber](micropython-stubber.md#generating-the-stubs)