.intel_syntax noprefix

.text
hello: .asciz "Hello World\n"
        helloLen = .- hello
logfile:
        .asciz "./test.log"

.globl main
main:
    mov rax, 2
    lea rdi, [logfile + rip]
    mov rsi, 0x441
    mov edx, 0666 # For some fucking reason, octal is represented in GAS with just a leading '0'
    syscall
    mov r8, rax
    mov rax, 1
    mov rdi, r8
    lea rsi, [hello + rip]
    mov rdx, helloLen
    syscall
    mov rax, 3
    mov rdi, r8
    syscall
    mov rax, 60
    mov rdi, 0
    syscall
