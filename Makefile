DIST=./dist

build:
		mkdir $(DIST)
		cp -r app config test $(DIST)
		cp Dockerfile $(DIST)
		cp run.py main.py Pip* $(DIST)
		ls -la $(DIST)
		cd $(DIST) && docker build --rm -t apiorbit:1.0.0 .

clean:
		rm -rf $(DIST)