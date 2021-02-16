# Pico-Stub

This repository contains MicroPython stubs for the Raspberry Pi Pico, allowing you to benefit from Python code linting and autocompletion in Visual Studio Code.

![alt text](https://raw.githubusercontent.com/cpwood/Pico-Stub/main/screenshot.png "Screenshot")

## Using the Stubs

The easiest way to use these stubs is by installing the [Pico-Go extension]() and then choosing `Pico-Go > Configure project` from the command palette. This will configure your project for auto-completion and linting. Linting is performed by [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance).

Alternatively, if you'd prefer to use [Micropy CLI](https://github.com/BradenM/micropy-cli) with [Pylint](https://www.pylint.org/), follow [these instructions](micropy.md#using-the-stubs).

## About the Stubs

Any of the stubs located in the `/dist` folder are copied from the `/frozen` folder and are re-arranged for the target linter (Pylint or Pylance).

These stubs are **_not_** generated. They're hand-written and maintained.

The `/generated` folder contains stubs that have been generated on a Pico board. These are solely used to spot changes between firmware releases using diffs. Once a change has been spotted, the frozen stubs are manually updated accordingly.

The stubs _aren't_ perfect and issues and pull requests are welcomed to improve accuracy and fuller class and method documentation.

## Generating the Stubs

This isn't something you *need* to do; the stubs are already included in this repository within the `/generated` directory.

However, if you want to do this yourself, you can do so using [Micropython-Stubber](https://github.com/Josverl/micropython-stubber).

* [Using Micropython-Stubber](micropython-stubber.md#generating-the-stubs)