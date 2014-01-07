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
  11 0000 55       		pushq	%rbp
  12              		.cfi_def_cfa_offset 16
  13              		.cfi_offset 6, -16
  14 0001 4889E5   		movq	%rsp, %rbp
  15              		.cfi_def_cfa_register 6
  16 0004 53       		pushq	%rbx
  17 0005 4883EC38 		subq	$56, %rsp
  18              		.cfi_offset 3, -24
  19 0009 4889E0   		movq	%rsp, %rax
  20 000c 4889C3   		movq	%rax, %rbx
   5:ts.c          ****   int n;
   6:ts.c          **** 
   7:ts.c          ****   int fuuuuuuuuuuuck[n];
  21              		.loc 1 7 0
  22 000f 8B45EC   		movl	-20(%rbp), %eax
  23 0012 4C63C0   		movslq	%eax, %r8
  24 0015 4983E801 		subq	$1, %r8
  25 0019 4C8945E0 		movq	%r8, -32(%rbp)
  26 001d 4C63C0   		movslq	%eax, %r8
  27 0020 4C89C6   		movq	%r8, %rsi
  28 0023 BF000000 		movl	$0, %edi
  28      00
  29 0028 4863F0   		movslq	%eax, %rsi
  30 002b 4889F2   		movq	%rsi, %rdx
  31 002e B9000000 		movl	$0, %ecx
  31      00
  32 0033 4898     		cltq
  33 0035 48C1E002 		salq	$2, %rax
  34 0039 488D5003 		leaq	3(%rax), %rdx
  35 003d B8100000 		movl	$16, %eax
  35      00
  36 0042 4883E801 		subq	$1, %rax
  37 0046 4801D0   		addq	%rdx, %rax
  38 0049 B9100000 		movl	$16, %ecx
  38      00
  39 004e BA000000 		movl	$0, %edx
  39      00
  40 0053 48F7F1   		divq	%rcx
  41 0056 486BC010 		imulq	$16, %rax, %rax
  42 005a 4829C4   		subq	%rax, %rsp
  43 005d 4889E0   		movq	%rsp, %rax
  44 0060 4883C003 		addq	$3, %rax
  45 0064 48C1E802 		shrq	$2, %rax
  46 0068 48C1E002 		salq	$2, %rax
  47 006c 488945D8 		movq	%rax, -40(%rbp)
   8:ts.c          ****   int *heheheheheheheh;
   9:ts.c          ****   heheheheheheheh = (int *) malloc (888);  // 为了方便观测设置为 888 (4,8的倍数) 了，
  48              		.loc 1 9 0
  49 0070 BF780300 		movl	$888, %edi
  49      00
  50 0075 E8000000 		call	malloc
  50      00
  51 007a 488945D0 		movq	%rax, -48(%rbp)
  10:ts.c          **** 
  11:ts.c          ****   int * const nima = (int *) malloc (444);  // 同上
  52              		.loc 1 11 0
  53 007e BFBC0100 		movl	$444, %edi
  53      00
  54 0083 E8000000 		call	malloc
  54      00
  55 0088 488945C8 		movq	%rax, -56(%rbp)
  12:ts.c          ****   nima[1] = 1314;
  56              		.loc 1 12 0
  57 008c 488B45C8 		movq	-56(%rbp), %rax
  58 0090 4883C004 		addq	$4, %rax
  59 0094 C7002205 		movl	$1314, (%rax)
  59      0000
  13:ts.c          **** 
  14:ts.c          **** 
  15:ts.c          ****   fuuuuuuuuuuuck[1] = 13;
  60              		.loc 1 15 0
  61 009a 488B45D8 		movq	-40(%rbp), %rax
  62 009e C740040D 		movl	$13, 4(%rax)
  62      000000
  16:ts.c          ****   heheheheheheheh[1] = 14;
  63              		.loc 1 16 0
  64 00a5 488B45D0 		movq	-48(%rbp), %rax
  65 00a9 4883C004 		addq	$4, %rax
  66 00ad C7000E00 		movl	$14, (%rax)
  66      0000
  17:ts.c          **** 
  18:ts.c          ****   return 0;
  67              		.loc 1 18 0
  68 00b3 B8000000 		movl	$0, %eax
  68      00
  69 00b8 4889DC   		movq	%rbx, %rsp
  19:ts.c          **** }
  70              		.loc 1 19 0
  71 00bb 488B5DF8 		movq	-8(%rbp), %rbx
  72 00bf C9       		leave
  73              		.cfi_def_cfa 7, 8
  74 00c0 C3       		ret
  75              		.cfi_endproc
  76              	.LFE2:
  78              	.Letext0:
