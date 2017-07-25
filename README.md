_N.B. This is a fork of the_ [Source Code Pro repository](https://github.com/adobe-fonts/source-code-pro)

### SemanticCode – _Ligatures for code_

Inspired by the excellent Hasklig font, SemanticCode is a modification of Hasklig (and by extension, Source Code Pro) to cover ligatures for a wide variety of programming languages. 

The main idea is to substitute operators which have a multi-character representation, such as `!=` and `->`, with more readable equivalents that have the same semantic meaning, and the same width. 
For example, in languages where `!=` represents 'not equal' we have a ligature corresponding to a slashed equal sign that is two characters wide. 
The benefit of the substitutions are most noticible in languages such as Haskell which have many complicated operators, e.g. `=>` `-<` `>>=`.

The goals of SemanticCode differ slightly from Hasklig in two ways. 
Firstly, versions of the font are available for different programming languages, each with a set of ligatures defined that is intended to correspond with common operator usage in that programming language. 
Secondly, the ligatures themselves are intended to correspond more closely to the _semantic meaning_ of the operator than the multi-character representation. 
For example in the Haskell variant of the font, SemanticCode has a glyph for `/=` in which the slash is centred, whereas the Hasklig glyph has the slash toward the left, as in the multi-character representation.

[**Download SemanticCode Font Family v0.1**](TODO)

#### SemanticCode
![SemanticCode Sample](SemanticCode_example.png?raw=true)

#### Hasklig
![Hasklig Sample](hasklig_example.png?raw=true)

#### Source Code Pro
![Source Code Pro Sample](SourceCodeProSample.png?raw=true)

### Release notes
+ [v0.1](https://github.com/i-tu/Hasklig/releases/tag/1.1)
    + Initial version with Javascript and Haskell variants
    + Javascript: Basic support for common non-assignment operators
    + Haskell: As Hasklig, except the slash for `/=` is centred, and `===` has three strokes

### Currently implemented symbols

#### Haskell
`<*` `<*>` `<+>` `<$>` `***` `<|` `|>`  `<|>` `!!` `||` `===` `==>` `<<<` `>>>` `<>` `+++` `<-` `->` `=>` `>>` `<<` `>>=` `=<<` `..` `...` `::` `-<` `>-` `-<<` `>>-` `++` `/=` `==`

#### Javascript
`===` `!==` `<<<` `>>>` `==` `!=` `=>` `<<` `>>` `++` `||`


### Building the fonts from source

#### Requirements

To build the binary font files from source, you need to have installed the
[Adobe Font Development Kit for OpenType](http://www.adobe.com/devnet/opentype/afdko.html) (AFDKO). The AFDKO
tools are widely used for font development today, and are part of most font
editor applications.

Some SVG glyphs are inserted into the fonts using Python [FontTools](https://pypi.python.org/pypi/FontTools).

#### Building font instances from masters

This repository only includes so-called *master* weights of the fonts (effectively extralight and black).
The shapes of the weights in between these extremities are calculated by `makeInstancesUFO` supplied with `.designspace` files.
For convenience, the shell script **buildInstances** is provided, which  executes `makeInstancesUFO`, calculating all the italic and regular font weight shapes.

```sh
$ ./buildInstances.sh
```

#### Building all fonts

To build for each language, a shell script named **build** is provided in the root directory.
It builds all OTFs and TTFs for each language, and can be executed by typing:

```sh
$ ./build.sh
```

### Credits
Original idea, design and implementation of code ligatures by Ian Tuomi 2014-2015. 
This typeface extends [Source Code Pro](https://github.com/adobe-fonts/source-code-pro) with ligatures.
