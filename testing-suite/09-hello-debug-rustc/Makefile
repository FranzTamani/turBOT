executable_name = output

full: build run

fullclean: clean build run

build:
		rustc -g -C opt-level=0 -o $(executable_name) main.rs

run:
		./$(executable_name)

clean:
		rm -f ./$(executable_name)
