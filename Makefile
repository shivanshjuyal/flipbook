DISTPATH=.
SRC=src/fc.py
ARGS=--onefile 
CLEAN=build/ fc *.spec


build: clean
	pyinstaller $(SRC) $(ARGS) --distpath $(DISTPATH)

clean:
	rm -rf $(CLEAN)
