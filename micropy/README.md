# Micropy CLI

## Using the Stubs
### First use on your computer

Having already [installed micropy-cli](https://github.com/BradenM/micropy-cli#getting-started), clone or [download](https://github.com/cpwood/Pico-Stub/archive/main.zip) this repo and issue the following command:

```
micropy stubs add "<path to pico micropy folder in this repo>"
```

For example:

```
micropy stubs add "C:\Pico-Stub\micropy\rp2-1.13.0\"
```

### When starting new projects

Just follow the [instructions](https://github.com/BradenM/micropy-cli#creating-a-project) over on the Micropy CLI readme!

## Generating the Stubs

In addition to having [installed micropy-cli](https://github.com/BradenM/micropy-cli#getting-started), you'll also need to install the prerequisites for stub generation. You do this using the following command:

```
pip install micropy-cli[create_stubs]
```

You will need to copy `errno.py` and `ujson.py` from the `board` folder to the Pico prior to generating the stubs. The stub generation code in Micropy CLI uses both modules but neither are present on the Pico out-of-the-box, so these polyfills will substitute the real deal. 

You can then generate the stubs using the following command:

```
micropy stubs create COM3
```

Change the COM port or path to `/dev/something-or-other` as appropriate for your machine.

At the conclusion of the stub generation process, you'll find the stubs within your `$HOME` folder in a `.micropy/stubs` sub-folder, for example:

```
C:\Users\chris.wood\.micropy\stubs\rp2-1.13.0
```

You'll then need to run the `post-process.py` script as follows (using the above path as an example):

```
py post-process.py -i "C:\Users\chris.wood\.micropy\stubs\rp2-1.13.0"
```

This will remove any references to `errno` and `ujson` from the stubs. These were only included because of our polyfills; we don't want them to be included in the stubs.

>  If you're preparing a pull request for this repo, place the folder with the stubs within the `micropy` folder. Overwrite any existing folders, but don't delete anything.