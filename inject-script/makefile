lazy: build inject_lazy run

no_call: build inject_no_call run

build:
	g++ -o empty.out empty.cpp

inject_lazy:
	./turbot-lazy.sh empty.out

inject_no_call:
	./turbot-no-call.sh empty.out

run:
	./empty.out

clean:
	rm ./empty.out
