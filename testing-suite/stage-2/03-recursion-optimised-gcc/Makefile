executable_name = output

full: build run

fullclean: clean build run

build:
		gcc -O3 -o $(executable_name) *.c

run:
		./$(executable_name)

clean:
		rm -f ./$(executable_name)
