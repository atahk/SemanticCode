#!/bin/sh
GLYPH="$1"
if [ -z "$GLYPH" ]
then
    echo "No glyph specified"
    exit 1
fi

FILE="$GLYPH.glif"
for DIR in RomanMasters/SourceCodePro_0.ufo \
	       RomanMasters/SourceCodePro_2.ufo \
	       ItalicMasters/SourceCodePro-Italic_0.ufo \
	       ItalicMasters/SourceCodePro-Italic_2.ufo
do
    cd $DIR/glyphs
    grep -q "<key>$GLYPH</key>" contents.plist
    if [ "$?" -gt "0" ]
    then
	LINENUM=`grep "<key>LIG</key>" contents.plist -n | cut -d : -f1`
	gawk -i inplace -v "n=$LINENUM" -v "s=\t\t<string>${GLYPH}.glif</string>" '(NR==n) { print s } 1' contents.plist
	gawk -i inplace -v "n=$LINENUM" -v "s=\t\t<key>${GLYPH}</key>" '(NR==n) { print s } 1' contents.plist
	echo "Added to contents.plist for $DIR"
    else
	# echo "Already in contents.plist for $DIR"
    fi
    if [ -f "$GLYPH.glif" ]
    then
	FILE="../../../$DIR/glyphs/$GLYPH.glif"
	grep -q "<glyph name=\"$GLYPH\"" "$GLYPH.glif"
	if [ "$?" -gt "0" ]
	then
	    sed -i "s/^<glyph name=\"[_a-zA-Z]\+\"/<glyph name=\"$GLYPH\"/" "$GLYPH.glif"
	    echo "Glyph name fixed"
	fi
    elif [ -f "$FILE" ]
    then
	cp "$FILE" "$GLYPH.glif"
	FILE="../../../$DIR/glyphs/$GLYPH.glif"
	echo "Glyph copied to $DIR"
    fi
    cd ../../..
done
