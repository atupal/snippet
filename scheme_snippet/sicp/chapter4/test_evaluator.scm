
(define (append x y)
  (if (null? x)
    y
    (cons (car x) (append (cdr x) y))))


(append '(a b c) '(d e f))


(define (cadr x) (car (cdr x)))
(cond ((assoc 'b '((a 1) (b 2))) => cadr)
      (else false))
