executable_name = output

full: build run

fullclean: clean build run

build:
		clang -O0 -g -o $(executable_name) *.c

run:
		./$(executable_name)

clean:
		rm -f ./$(executable_name)
