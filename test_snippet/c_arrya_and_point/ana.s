   1              		.file	"ts.c"
   2              		.text
   3              	.Ltext0:
   4              		.globl	main
   6              	main:
   7              	.LFB2:
   8              		.file 1 "ts.c"
   1:ts.c          **** #include <stdlib.h>
   2:ts.c          **** 
   3:ts.c          **** 
   4:ts.c          **** int main() {
   9              		.loc 1 4 0
  10              		.cfi_startproc
  11 0000 55       		pushq	%rbp  // saves the base pointer to the stack so that is can be restored later(popq %rbp)
  12              		.cfi_def_cfa_offset 16
  13              		.cfi_offset 6, -16
  14 0001 4889E5   		movq	%rsp, %rbp  // copy rsp to rbp setting the base pointer(temporarily for out function) to the stack pointer That way we can push variables to the stack if out function requires it.
  15              		.cfi_def_cfa_register 6
  16 0004 4881EC00 		subq	$512, %rsp  // Grow our stack 48 bytes upward, The compiler evidently concluded that our function may nedd 512 bytes of stack space for its use.
  16      020000
   5:ts.c          ****   int fuuuuuuuuuuuck[123];
   6:ts.c          ****   int *heheheheheheheh;
   7:ts.c          ****   heheheheheheheh = (int *) malloc (888);  // 为了方便观测设置为 888 (4,8的倍数) 了，
  17              		.loc 1 7 0
  18 000b BF780300 		movl	$888, %edi
  18      00
  19 0010 E8000000 		call	malloc
  19      00
  20 0015 488945F8 		movq	%rax, -8(%rbp)
   8:ts.c          **** 
   9:ts.c          **** 
  10:ts.c          ****   fuuuuuuuuuuuck[1] = 13;
  21              		.loc 1 10 0
  22 0019 C78504FE 		movl	$13, -508(%rbp)  // 数组寻址
  22      FFFF0D00 
  22      0000
  11:ts.c          ****   heheheheheheheh[1] = 14;
  23              		.loc 1 11 0
  24 0023 488B45F8 		movq	-8(%rbp), %rax  // 指针的寻址
  25 0027 4883C004 		addq	$4, %rax
  26 002b C7000E00 		movl	$14, (%rax)
  26      0000
  12:ts.c          **** 
  13:ts.c          ****   return 0;
  27              		.loc 1 13 0
  28 0031 B8000000 		movl	$0, %eax
  28      00
  14:ts.c          **** }
  29              		.loc 1 14 0
  30 0036 C9       		leave
  31              		.cfi_def_cfa 7, 8
  32 0037 C3       		ret
  33              		.cfi_endproc
  34              	.LFE2:
  36              	.Letext0:
