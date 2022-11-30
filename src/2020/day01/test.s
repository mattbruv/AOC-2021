	.file	"test.c"
	.text
	.globl	foo
	.data
	.align 8
foo:
	.long	1974
	.long	3259
	.globl	idx
	.align 4
idx:
	.long	1
	.def	__main;	.scl	2;	.type	32;	.endef
	.text
	.globl	main
	.def	main;	.scl	2;	.type	32;	.endef
	.seh_proc	main
main:
	pushq	%rbp
	.seh_pushreg	%rbp
	movq	%rsp, %rbp
	.seh_setframe	%rbp, 0
	subq	$32, %rsp
	.seh_stackalloc	32
	.seh_endprologue
	call	__main
	movl	idx(%rip), %eax
	cltq
	leaq	0(,%rax,4), %rdx
	leaq	foo(%rip), %rax
	movl	(%rdx,%rax), %eax
	addq	$32, %rsp
	popq	%rbp
	ret
	.seh_endproc
	.ident	"GCC: (Rev2, Built by MSYS2 project) 11.2.0"
