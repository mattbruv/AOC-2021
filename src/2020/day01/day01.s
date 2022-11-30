.data
.align 4
value:
    .long 1974
    .long 3259


.text
.global main
main:
    movl $69, 4+value(%rip)
    movl 4+value(%rip), %eax
    ret



