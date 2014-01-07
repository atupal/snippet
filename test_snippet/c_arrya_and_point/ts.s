	.file	"ts.c"
	.text
	.globl	main
	.type	main, @function
main:
.LFB2:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%rbx
	subq	$56, %rsp
	.cfi_offset 3, -24
	movq	%rsp, %rax
	movq	%rax, %rbx
	movl	-20(%rbp), %eax
	movslq	%eax, %r8
	subq	$1, %r8
	movq	%r8, -32(%rbp)
	movslq	%eax, %r8
	movq	%r8, %rsi
	movl	$0, %edi
	movslq	%eax, %rsi
	movq	%rsi, %rdx
	movl	$0, %ecx
	cltq
	salq	$2, %rax
	leaq	3(%rax), %rdx
	movl	$16, %eax
	subq	$1, %rax
	addq	%rdx, %rax
	movl	$16, %ecx
	movl	$0, %edx
	divq	%rcx
	imulq	$16, %rax, %rax
	subq	%rax, %rsp
	movq	%rsp, %rax
	addq	$3, %rax
	shrq	$2, %rax
	salq	$2, %rax
	movq	%rax, -40(%rbp)
	movl	$888, %edi
	call	malloc
	movq	%rax, -48(%rbp)
	movl	$444, %edi
	call	malloc
	movq	%rax, -56(%rbp)
	movq	-56(%rbp), %rax
	addq	$4, %rax
	movl	$1314, (%rax)
	movq	-40(%rbp), %rax
	movl	$13, 4(%rax)
	movq	-48(%rbp), %rax
	addq	$4, %rax
	movl	$14, (%rax)
	movl	$0, %eax
	movq	%rbx, %rsp
	movq	-8(%rbp), %rbx
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE2:
	.size	main, .-main
	.ident	"GCC: (GNU) 4.8.2"
	.section	.note.GNU-stack,"",@progbits
