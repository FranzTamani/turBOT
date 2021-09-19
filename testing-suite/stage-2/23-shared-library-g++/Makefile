project_dir = $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
executable_name = output

full: build run

fullclean: clean build run

build:
		g++ -o $(executable_name) *.cpp \
			-I./include/ \
			-L./include/ \
			-lhello

run: export LD_LIBRARY_PATH = $(project_dir)include
run:
		./$(executable_name)

clean:
		rm -f ./$(executable_name)

memleaktest:
		valgrind --tool=memcheck ./$(executable_name)
