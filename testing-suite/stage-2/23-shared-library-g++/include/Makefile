obj_name = hello

full: build

fullclean: clean build

build:
		g++ -c -fPIC -o $(obj_name).o hello.cpp
		g++ -shared $(obj_name).o -o lib$(obj_name).so

clean:
		rm -f ./$(obj_name).o
		rm -f ./lib$(obj_name).so
