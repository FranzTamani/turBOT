logstring:  
    # This is the string we are writing
    .asciz "Hello World\n"
    # This calculates and saves the length of the above string
    logstringLen = .- logstring
logfile:
    # This is the path to the file to write to
    .asciz "./test.log"

# This is effectively the "main" of this payload
# Accoring to the current CLI implementation of BOT, must be named the same as the file minus the prefix
# i.e.
# [main_func_name].S
# contains:
# [main_func_name]:
logTamperInject:
    # syscall 2 is open
    mov rax, 2
    # provide filepath
    lea rdi, [logfile + rip]
    # specify open mode
    # 0x441 = O_CREAT| O_WRONLY | O_APPEND
    # meaning open as write only, create the file if it doesn't exist, append to the file if it does exist
    mov rsi, 0x441
    # Provide file permissions in case we need to create the file
    mov edx, 0666
    # Open it
    syscall
    # rax is now the file descriptor for the file we just opened, save it for later
    mov r8, rax

    # syscall 1 is write
    mov rax, 1
    # rdi is where to write to. The previously opened file, in our case
    mov rdi, r8
    # rsi is the string to write. [hello + rip] is  PIC reference to it
    lea rsi, [logstring + rip]
    # rdx is length of the string. A previously defined constant
    mov rdx, logstringLen
    # Do the write
    syscall

    # If you want to do more writing, here's where to to it
    
    # syscall 3 is close
    mov rax, 3
    # Close what? The open file we wrote to
    mov rdi, r8
    # Close it
    syscall
    # Return to caller
    ret
