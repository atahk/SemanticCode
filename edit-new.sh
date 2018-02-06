#!/bin/sh
GLYPH="$1"
EDITOR="$2"
if [ -z "$GLYPH" ]
then
    echo "No glyph specified"
    exit 1
fi

if [ -z "$EDITOR" ]
then
    echo "No editor specified"
    exit 1
fi

FILE="$GLYPH.glif"
for DIR in RomanMasters/SourceCodePro_0.ufo \
	       RomanMasters/SourceCodePro_2.ufo \
	       ItalicMasters/SourceCodePro-Italic_0.ufo \
	       ItalicMasters/SourceCodePro-Italic_2.ufo
do
    FILE="$DIR/glyphs/$GLYPH.glif"
    if [ -f "$FILE" ]
    then
        "$EDITOR" "$FILE"
    else
        echo "Missing glyph: $FILE"
    fi
done
