global _start
section .text
_start:
    mov rax, 1          ; sys_write
    mov rdi, 1          ; stdout
    mov rsi, message    ; message to write
    mov rdx, 13         ; message length
    syscall

    mov rax, 60         ; sys_exit
    mov rdi, 0          ; exit status
    syscall

section .data
message db "Hello, World!", 10
