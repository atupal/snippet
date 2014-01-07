
main:ts.c
	gcc -c -g -Wa,-adlhn $< > ts.comment.s

ass: ts.c
	gcc -S -o ts.s $<

obj: ts.c
	gcc -g -c $<  # And then  usx 'objdump -d -M intel -S ts.o'
	@objdump -d -M intel -S ts.o > objdump.out

clean:
	rm ts.s -f
