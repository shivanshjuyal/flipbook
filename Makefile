DISTPATH=.

build: clean
	pyinstaller src/fc.py --onefile --distpath $(DISTPATH)

clean:
	rm -rf build/ fc  *.spec
