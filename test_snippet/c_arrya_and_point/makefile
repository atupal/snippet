
main:ts.c
	gcc -c -g -Wa,-adlhn $< > ts.s

ass: ts.c
	gcc -S

clean:
	rm ts.s -f
