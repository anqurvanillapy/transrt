transrt
=======

**transrt** meaning **Translator of SubRip File**, a tool used to
productively translate (manually) the subtile files from Google
Developer Group Youtube video channel, as my contributing to GDG
Zhuhai Subtitle Fanclub.

Installation
------------

Simply clone this repo

```
$ git clone git@github.com:anqurvanillapy/transrt.git
```

And run the code

```
$ python setup.py install
```

Usage
-----

### Help Message ###

Type `transrt -h` to display help mesage, as follows

```
usage: transrt.py [-h] [-o filename] [-kn keynumber | -kwd keyword] filename

A simple manual translator of SubRip file

positional arguments:
  filename              input file name

optional arguments:
  -h, --help            show this help message and exit
  -o filename, --output filename
                        output file name
  -kn keynumber, --keynumber keynumber
                        the key number to search for
  -kwd keyword, --keyword keyword
                        the keyword to search for

```

### Normal Usage ###

Type the command below and specify your file names

```
transrt <filename>
```

And the manual translating will be in process,
The built-in commands are shown below

```
Commmands     Functions
---------     --------------------------
    'f'       Forwarding
    'b'       Backwarding
    's'       Shutting Down,
              or Skipping Search Results
---------     --------------------------
```

After translating, the default output file `a.srt` will be generated

### Search ###

- `-kn`, `--keynumber`
    + The SRT file will be seperated into several dicts, and every
    dict is numbered by its top figure of a certain block, as you can
    open a SRT file to see its file content structure
    + Give `int`-typed arguments to `-kn` or `--keynumber` option, to
    search for a certain piece of subtitle numbered by the given
    argument
    + When searching is done, the process will be similar to normal
    usage
- `-kwd`, `--keyword`
    + Search for the keyword you give in the content of **every dict**
    of the SRT file, but you just can type **only one** keyword
    without any spaces
    + When searching is not over, type `s` will be skipping into the
    next search result
    + Commands in normal usage like `f` and `b` are also available

Known Issues
------------

* [ ] In Python 2.7.6 interpretor, using `raw_input()` and deleting
**fullwidth** characters will not cause any errors, but in script the
**fullwidth** ones will not be deleted completely on the terminal, but
actually deleted if I print them

Support
-------

It's just a very simple tool, TBH. If you got any questions, bugs or
further features for this repo, please feel free to raise your issues
or pull your requests.