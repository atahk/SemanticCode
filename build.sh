#!/bin/sh

family=SemanticCode
languages='haskell javascript'
romanWeights='Black Bold ExtraLight Light Medium Regular Semibold'
italicWeights='BlackIt BoldIt ExtraLightIt LightIt MediumIt It SemiboldIt'

# path to Python script that adds the SVG table
addSVG=$(cd $(dirname "$0") && pwd -P)/addSVGtable.py

# path to UVS file
UVS=$(cd $(dirname "$0") && pwd -P)/uvs.txt

# clean existing build artifacts
rm -rf target/
rm ligatures.fea

for l in $languages
do
  otfDir="target/$l/"
  mkdir -p $otfDir

  # copy the desired ligature definitions into place
  cp ligatures.$l.fea ligatures.fea

  for w in $romanWeights
  do
    outputFile=$otfDir/$family-$l-$w.otf
    makeotf -f Roman/$w/font.ufo -r -ci "$UVS" -o $outputFile
    rm Roman/$w/current.fpr # remove default options file from the source tree after building
    "$addSVG" $outputFile svg
  done

  for w in $italicWeights
  do
    outputFile=$otfDir/$family-$l-$w.otf
    makeotf -f Italic/$w/font.ufo -r -ci "$UVS" -o $outputFile
    rm Italic/$w/current.fpr # remove default options file from the source tree after building
    "$addSVG" $outputFile svg
  done

  rm ligatures.fea # remove temporary ligatures definition
done