_N.B. This is a fork of the_ [Hasklig repository](https://github.com/i-tu/Hasklig)

### SemanticCode – _Ligatures for code_

This is a fork of SemanticCode to cover R, C++, Python and Julia. SemanticCode is a modification of Hasklig (and by extension, Source Code Pro) to cover ligatures for a variety of programming languages. 

The main idea is to substitute operators which have a multi-character representation, such as `!=` and `->`, with more readable equivalents that have the same semantic meaning, and the same width. 
For example, in languages where `!=` represents 'not equal' we show a glyph corresponding to a slashed equal sign that is two characters wide. 
The benefits of these substitutions are most noticible in languages such as Haskell which have many mathematical operators, e.g. `=>` `-<` `>>=`.

The goals of SemanticCode differ slightly from Hasklig in two ways. 
Firstly, versions of the font are available for different programming languages, each with a set of ligatures defined that is intended to correspond with common operator usage in that programming language. 
Secondly, the ligatures themselves are intended to correspond more closely to the _semantic meaning_ of the operator than the multi-character representation. 
For example, in the SemanticHaskell variant SemanticCode has a glyph for `/=` with the slash centred, whereas the Hasklig glyph has the slash toward the left, as in the multi-character representation.

### TODO

+ add R comment glyph `##`
+ add R glyph `%in%`
+ improve R glyph `<<-` and C++ glyph `<<`
+ add R glyphs `%%`, `%*%`, `%/%`, `%o%`, `%x%`, `%+%` and `%-%`
+ add C++ operator glyphs `+=`, `-=`, `*=`, `/=`, `%=`, `&=`, `|=`, `^=`, `<<=` and `>>=`
+ add Python
+ add Julia

### Release notes
+ forked version
    + Added R, C++ and a combination of the two
	+ Added inequalities `<=` and `>=`
	+ added C++ comment glyphs `//`, `/*`, `*/`
	+ added R glyph `<<-`
	+ Fixed build from scratch
	+ Added Makefile
+ v2.2
    + The entire build system is now written in python
    + Build system improvements means each variant is called `Semantic<Language>` 
    + Added MATLAB with `==` and `~=` glyphs
+ v2.1
    + Initial version with Javascript and Haskell variants
    + Javascript: Basic support for common non-assignment operators
    + Haskell: As Hasklig, except the slash for `/=` is centred, and `===` has three strokes

### Currently implemented symbols

#### Haskell
`***` `:::` `===` `==>` `=<<` `>=>` `>>=` `>>>` `>>-` `->>` `-<<`
`<*>` `<|>` `<$>` `<=>` `<=<` `<->` `<+>` `<<<` `...` `+++`
`*>` `\\` `||` `|>` `::` `==` `=>` `!!` `>>` `>-` `->` `-<` `<*`
`<>` `<|` `<-` `<<` `..` `++` `/=`

#### Javascript
`===` `!==` `>>>` `<<<` `||` `==` `=>` `!=` `>>` `<<` `++`

#### MATLAB
`==` `~=`

### Building the fonts from source

#### Requirements

The build system requires [Python](https://www.python.org/), and is tested with version 2.7.

To build the binary font files from source, you need to have installed the
[Adobe Font Development Kit for OpenType](http://www.adobe.com/devnet/opentype/afdko.html) (AFDKO). 
The AFDKO tools are widely used for font development today, and are part of most font
editor applications.

Some SVG glyphs are inserted into the fonts using Python [FontTools](https://pypi.python.org/pypi/FontTools), 
and the build system needs [dill](https://pypi.python.org/pypi/dill)

#### Configure

To configure the build, use `configure.py`, suppying the desired options.

The repository only includes so-called *master* weights of the fonts (effectively extralight and black).
The shapes of the weights in between these extremities are calculated by `makeInstancesUFO` supplied with 
`.designspace` files. This needs to be done initally, and only needs to be repeated when new glyphs are 
added to the master fonts. 
The configure script automatically makes the instances if one of the required `font.ufo` directories are 
missing, and if any glyphs have been added the `-bi` option forces a rebuild. 

By default the configure script enables all supported languages, in the future options for 
controlling enabled languages will be added.

#### Building

Once the confugure script has been run, use `build.py` to build the fonts.

### Credits
Original idea, design and implementation of code ligatures by Ian Tuomi 2014-2015. 
This typeface extends [Source Code Pro](https://github.com/adobe-fonts/source-code-pro) with ligatures.
