TARGET_BASE=~/Dropbox/Personal/Fonts
UFO_FILE=ufo/glyphs/contents.plist

all: $(TARGET_BASE)/Semantic/

$(TARGET_BASE)/Semantic/: config.dill build.py
	python build.py -t $(TARGET_BASE)/Semantic/

config.dill: Roman/Black/font.$(UFO_FILE) Italic/BlackIt/font.$(UFO_FILE) configure.py
	python configure.py

Roman/Black/font.$(UFO_FILE): RomanMasters/SourceCodePro_0.$(UFO_FILE) RomanMasters/SourceCodePro_2.$(UFO_FILE)
	makeInstancesUFO -d RomanMasters/SourceCodePro.designspace

Italic/BlackIt/font.$(UFO_FILE): ItalicMasters/SourceCodePro-Italic_0.$(UFO_FILE) ItalicMasters/SourceCodePro-Italic_2.$(UFO_FILE)
	makeInstancesUFO -d ItalicMasters/SourceCodePro-It.designspace

clean:
	rm -rf config.dill Roman/*/font.ufo Italic/*/font.ufo
