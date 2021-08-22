all: build inject run

build:
	g++ -o empty.out empty.cpp

inject:
	./turbot.sh empty.out

run:
	./empty.out

clean:
	rm ./empty.out
