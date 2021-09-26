executable_name = output

full: build run

fullclean: clean build run

build:
		clang++ -o $(executable_name) *.cpp -lpthread
		../../bin/upx/upx -9 $(executable_name)

run:
		./$(executable_name)

clean:
		rm -f ./$(executable_name)

memleaktest:
		valgrind --tool=memcheck ./$(executable_name)
