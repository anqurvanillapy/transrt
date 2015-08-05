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

Type the command below and specify your file name

```
$ transrt <filename>
```

And the manual translating will be in process,  
The built-in commands are shown below

```
Commmands     Functions
---------     --------------------------
    'f'       Forwarding
    'b'       Backwarding
    'r'       Restarting one line
    's'       Shutting Down,
              or Skipping to Next Result
---------     --------------------------
```

After translating, the default output file `a.srt` will be generated

### Example ###

Choose a SRT file to translate and type

```
$ transrt example.srt -o translated.srt
```

And `example.srt` will be initialized, on terminal displaying

```
$ transrt example.srt -o translated.srt
Packing file...
Success

Commmands     Functions
---------     --------------------------
    'f'       Forwarding
    'b'       Backwarding
    'r'       Restarting one line
    's'       Shutting Down,
              or Skipping to Next Result
---------     --------------------------

1
00:00:00,000 --> 00:00:01,00
Hello, world!

(Next line is
        Aloha, jerk!
)
>>> 
```
Now you can manually translate the script, press `Enter` to add a
newline, type `f` to go forwards, skipping to the second line

```
$ transrt example.srt -o translated.srt
Packing file...
Success

Commmands     Functions
---------     --------------------------
    'f'       Forwarding
    'b'       Backwarding
    'r'       Restarting one line
    's'       Shutting Down,
              or Skipping to Next Result
---------     --------------------------

1
00:00:00,000 --> 00:00:01,00
Hello, world!

(Next line is
        Aloha, jerk!
)
>>> 你好, 世界!
>>> f

2
00:00:01,000 --> 00:00:02,000
Aloha, jerk!

(This is the last line.)
>>> s
```

As above, if now type `s` to shut down translating, the output file
`translated.srt` will be like

```
1
00:00:00,000 --> 00:00:01,000
你好, 世界!
Hello, world!
```

The second line will not be written in the output file,  
And now, enjoy your translating!

### Search ###

- `-kn`, `--keynumber`
    + The SRT file will be seperated into different dicts, and every
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

TODO
----

* [x] Add a feature of restarting the translation of a certain line by
typing command `r`
* [x] Make it available to preview the next line to better work in
context

Support
-------

It's just a very simple tool, TBH. If you got any questions, bugs or
further features for this repo, please feel free to raise your issues
or pull your requests.