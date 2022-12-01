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
    addl %eax, %edx
    addl $4, %ecx

    cmpl $-1, %eax
    je .NextElf
    jmp .AddNext

.NextElf:
    # iif we have looked through all the numbers, return
    cmpl (4 * 2237), %ecx
    jge .Finish

    # check if new sum is > ebx
    cmpl %edx, %ebx
    jle .ResetAndAdd

    # it's greater than
    movl %edx, %ebx


    # highest = EBX
    # accumulator

    # iif n = -1, accumulator > highest? highest = acc
    # return highest

.Finish:
    movl %ebx, %eax
    ret

.global part2
part2:
    movl $0, %eax
    ret


