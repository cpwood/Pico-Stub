# Micropython-Stubber

## Generating the Stubs

The stub content is generated using [Josverl/micropython-stubber](https://github.com/Josverl/micropython-stubber) using the [minified version of `createstubs.py`](https://github.com/Josverl/micropython-stubber/blob/master/minified/createstubs.py). Some polyfilling and post-processing is required since the Pico board doesn't support `ujson` which is used by `createstubs.py`.

To generate the stub files, copy all the files within the `board` folder to your Pico and then reboot it. You can do this either via [Pico-Go](https://marketplace.visualstudio.com/items?itemName=ChrisWood.pico-go) or via [Thonny](https://thonny.org/).

Upon reboot, you will see that the stub generation begins after a short delay.

Once complete, you'll need to copy all the generated files back to your computer. 

Copy the "micropython" folder that's been created on your Pico back to your computer.

Then run the `post/post-process.py` script. This will create sub-folders within the `/dist` folder for both Micropy-CLI and Pylance.
