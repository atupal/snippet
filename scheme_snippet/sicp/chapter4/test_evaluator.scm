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

; start exercise 4.8
(define (fib n)
  (let fib-iter ((a 1)
                 (b 0)
                 (count n))
    (if (= count 0)
      b
      (fib-iter (+ a b) a (- count 1)))))

(fib 10)
; end exercise 4.8

; start exercise 4.9
(for 0 10 display)
; endt exercise 4.9

(define (f x)
  (define (even? n) (if (= n 0) true  (odd?  (- n 1))))
  (define (odd? n)  (if (= n 0) false (even? (- n 1))))
  (even? x))

(f 12)

; start exercise 4.20
(letrec
  ((fact (lambda (n)
           (if (= n 1) 1 (* n (fact (- n 1)))))))
  (fact 10))
; end exercise 4.20
