executable_name = output

full: build run

fullclean: clean build run

build:
		gcc -o $(executable_name) *.c -lpthread

run:
		./$(executable_name)

clean:
		rm -f ./$(executable_name)

memleaktest:
		valgrind --tool=memcheck ./$(executable_name)
