.text


.global part1
part1:
    movl $0, %ebx # highestSoFar
    movl $0, %ecx # counter

.ResetAndAdd:
    movl $0, %edx # accumulator

.AddNext:
    leaq nums(%rip), %rax
    addq %rcx,  %rax 
    movl (%rax), %eax
    addl $4, %ecx

    cmpl $-1, %eax
    je .NextElf

    addl %eax, %edx
    jmp .AddNext

.NextElf:
    # iif we have looked through all the numbers, return
    cmpl $8948, %ecx
    jge .Finish

    # check if new sum is > ebx
    cmpl %ebx, %edx
    jle .ResetAndAdd

    # it's greater than
    movl %edx, %ebx
    jmp .ResetAndAdd

.Finish:
    movl %ebx, %eax
    ret

.global part2
part2:
    movl $0, %eax
    ret


