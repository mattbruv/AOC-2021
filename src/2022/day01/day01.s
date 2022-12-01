.data
ans:
.long 0
.long 0
.long 0

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

    # check if new sum is > ans[0] through ans[2]
    movl ans(%rip), %ebx
    cmpl %ebx, %edx # compare ans[0] to accumulator
    jle .Ans1
    movl %edx, ans(%rip)
    jmp .ResetAndAdd
    .Ans1:
    movl 4+ans(%rip), %ebx
    cmpl %ebx, %edx # compare ans[1] to accumulator
    jle .Ans2
    movl %edx, 4+ans(%rip)
    jmp .ResetAndAdd
    .Ans2:
    movl 8+ans(%rip), %ebx
    cmpl %ebx, %edx # compare ans[2] to accumulator
    jle .ResetAndAdd
    movl %edx, 8+ans(%rip)
    jmp .ResetAndAdd


.Finish:
    movl ans(%rip), %eax
    ret

.global part2
part2:
    movl $0, %eax
    addl ans(%rip), %eax
    addl 4+ans(%rip), %eax
    addl 8+ans(%rip), %eax
    ret


