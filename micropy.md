# Micropy CLI

## Using the Stubs
### First use on your computer

Having already [installed micropy-cli](https://github.com/BradenM/micropy-cli#getting-started), clone or [download](https://github.com/cpwood/Pico-Stub/archive/main.zip) this repo and issue the following command:

```
micropy stubs add "<path to dist/micropy-cli folder in this repo>"
```

For example:

```
micropy stubs add "C:\Pico-Stub\dist\micropy-cli"
```

If you haven't already installed [Pylint](https://www.pylint.org/), do so as follows:

```
pip install pylint
```

### When starting new projects

Just follow the [instructions](https://github.com/BradenM/micropy-cli#creating-a-project) over on the Micropy CLI readme!

The recommended `micropy init` templates are:

* `VSCode Settings for Autocompletion/Intellisense`
* `Pylint MicroPython Settings`

Optionally, if your project will end up in a Git repository, add `Git Ignore Template` too.

