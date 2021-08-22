hello:      .asciz "Hello World\n"
            helloLen = .- hello
HelloWorld:
            mov rax, 1
            mov rdi, 1
            lea rsi, [hello + rip]
            mov rdx, helloLen
            syscall
            ret