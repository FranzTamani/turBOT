executable_name = output

full: build run

fullclean: clean build run

build:
		rustc \
			-C codegen-units=16 \
			-C opt-level=3 \
			-o $(executable_name) \
			main.rs

run:
		./$(executable_name)

clean:
		rm -f ./$(executable_name)

memleaktest:
		valgrind --tool=memcheck ./$(executable_name)
