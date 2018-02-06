#!/bin/sh
GLYPH="$1"
OLDGLYPH="$2"
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
    ROMANDIR=`echo $DIR | sed 's/-Italic//' | sed 's/^Italic/Roman/'`
    ROMANFILE="../../../$ROMANDIR/glyphs/$GLYPH.glif"
    grep -q "<key>$GLYPH</key>" contents.plist
    if [ "$?" -gt "0" ]
    then
        LINENUM=`grep "<key>LIG</key>" contents.plist -n | cut -d : -f1`
        gawk -i inplace -v "n=$LINENUM" -v "s=\t\t<string>${GLYPH}.glif</string>" '(NR==n) { print s } 1' contents.plist
        gawk -i inplace -v "n=$LINENUM" -v "s=\t\t<key>${GLYPH}</key>" '(NR==n) { print s } 1' contents.plist
        echo "Added to contents.plist for $DIR"
    else
        echo "Already in contents.plist for $DIR"
    fi
    if [ -f "$GLYPH.glif" ]
    then
        grep -q "<glyph name=\"$GLYPH\"" "$GLYPH.glif"
        if [ "$?" -gt "0" ]
        then
            sed -i "s/^<glyph name=\"[_a-zA-Z0-9]\+\"/<glyph name=\"$GLYPH\"/" "$GLYPH.glif"
            sed -i "/<unicode hex=/d" "$GLYPH.glif"
            echo "Glyph name fixed in $DIR"
        fi
        grep -Eq '(.*)(x|y)="(-?[0-9]+[-+*][-+0-9]*[0-9]+)"(.*)' "$GLYPH.glif"
        if [ "$?" -eq "0" ]
        then
            sed -i 's/"/<DBLQUO>/g' "$GLYPH.glif"
            sed -i -r 's/(.*)(x|y)=<DBLQUO>(-?[0-9]+[-+*][-+0-9]*[0-9]+)<DBLQUO>(.*)/echo "\1\2=<DBLQUO>$((\3))<DBLQUO>\4"/ge' "$GLYPH.glif"
            sed -i 's/<DBLQUO>/"/g' "$GLYPH.glif"
            echo "Glyph math substitution in $DIR"
        fi
        FILE="../../../$DIR/glyphs/$GLYPH.glif"
    elif [ -f "$OLDGLYPH.glif" ]
    then
        cp "$OLDGLYPH.glif" "$GLYPH.glif"
        sed -i "s/^<glyph name=\"[_a-zA-Z0-9]\+\"/<glyph name=\"$GLYPH\"/" "$GLYPH.glif"
        sed -i "/<unicode hex=/d" "$GLYPH.glif"
        echo "Old glyph copied and name fixed in $DIR"
        FILE="../../../$DIR/glyphs/$GLYPH.glif"
    elif [ -f "$ROMANFILE" ]
    then
        cp "$ROMANFILE" "$GLYPH.glif"
        echo "Glyph copied to $DIR"
    elif [ -f "$FILE" ]
    then
        cp "$FILE" "$GLYPH.glif"
        echo "Glyph copied to $DIR"
        FILE="../../../$DIR/glyphs/$GLYPH.glif"
    fi
    cd ../../..
done
