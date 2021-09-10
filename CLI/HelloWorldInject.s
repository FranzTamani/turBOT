hello:      .asciz "Hello World\n"
            helloLen = .- hello
HelloWorldInject:
            mov rax, 1
            mov rdi, 1
            lea rsi, [hello + rip]
            mov rdx, helloLen
            syscall
            ret
