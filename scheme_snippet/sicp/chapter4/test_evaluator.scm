
(define (append x y)
  (if (null? x)
    y
    (cons (car x) (append (cdr x) y))))


(append '(a b c) '(d e f))


; start exercise 4.5
(define (cadr x) (car (cdr x)))
(cond ((assoc 'b '((a 1) (b 2))) => cadr)
      (else false))
; end exercise 4.5

; start exercise 4.6
(let ((a (cons 3 4)) (b 2))
  (+ (car a) b))
; end exercise 4.6

; start exercise 4.7
(let* ((x 3) (y (+ x 2)) (z (+ x y 5)))
  (* x z))
; end exercise 4.7
