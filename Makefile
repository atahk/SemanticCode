TARGET_BASE=~/Dropbox/Personal/Fonts

all: $(TARGET_BASE)/Semantic/

$(TARGET_BASE)/Semantic/: config.dill
	python build.py -t $(TARGET_BASE)/Semantic/

config.dill: Roman/Black/font.ufo Italic/Black/font.ufo
	python configure.py

Roman/Black/font.ufo:
	makeInstancesUFO -d RomanMasters/SourceCodePro.designspace

Italic/Black/font.ufo:
	makeInstancesUFO -d ItalicMasters/SourceCodePro-It.designspace

clean:
	rm -rf config.dill Roman/*/font.ufo Italic/*/font.ufo
