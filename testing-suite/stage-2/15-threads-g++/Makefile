executable_name = output

full: build run

fullclean: clean build run

build:
		g++ -o $(executable_name) *.cpp -lpthread

run:
		./$(executable_name)

clean:
		rm -f ./$(executable_name)

memleaktest:
		valgrind --tool=memcheck ./$(executable_name)
