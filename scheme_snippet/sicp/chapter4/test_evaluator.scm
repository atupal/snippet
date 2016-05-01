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

; start exercise 4.21
((lambda (n)
   ((lambda (fact) (fact fact n))
    (lambda (ft k) (if (= k 1) 1 (* k (ft ft (- k 1)))))))
 10)
; end exercise 4.21

; start exercise 4.25
(unless (= 0 0)
  (/ 0 0)
  (begin (display "exception: returning 0") 0))
(define (factorial n)
  (unless (= n 1)
    (* n (factorial (- n 1)))
    1))
(factorial 10)
; end exercise 4.25

; 4.2.2 lazy evaluation
; (define (try a b) (if (= a 0) 1 b))
(define (try a (b lazy)) (if (= a 0) 1 b))
(try 0 (/ 1 0))


; start exercise 4.27
(define count 0)

(define (id x)
  (set! count (+ count 1)) x)

(define w (id (id 10)))

count

w

count

; end exercise 4.27


; start exercise 4.29
(define count 0)

(define (square x) (* x x))

(square (id 10))

count
; end exercise 4.29

; start exercise 4.30
(define (for-each proc items)
  (if (null? items)
    'done
    (begin (proc (car items))
           (for-each proc (cdr items)))))


(for-each (lambda (x) (newline) (display x))
          (list 57 321 88))

(define (p1 x)
  (set! x (cons x '(2)))
  x)


(define (p2 x)
  (define (p e)
    e
    x)
  (p (set! x (cons x '(2)))))

(p1 1)

(p2 1)
; end exercise 4.30

; start exercise 4.31
; commented for large output
; (define count 0)
; 
; (define (square x) (* x x))
; 
; (square (id 10))
; 
; count ; 1
; 
; (define count 0)
; 
; (define (square (x lazy)) (* x x))
; 
; (square (id 10))
; 
; count ; 2
; 
; (define count 0)
; 
; (define (square (x lazy-memo)) (* x x))
; 
; (square (id 10))
; 
; count ; 1
; end exercise 4.31

; start 4.2.3 Streams as Lazy Lists
(define cons-system cons)
(define car-system car)
(define cdr-system cdr)

(define (cons x y) (lambda (m) (m x y)))
(define (car z) (z (lambda (p q) p)))
(define (cdr z) (z (lambda (p q) q)))

(define (list-ref items n)
  (if (= n 0)
    (car items)
    (list-ref (cdr items) (- n 1))))

(define (map proc items)
  (if (null? items)
    '()
    (cons (proc (car items)) (map proc (cdr items)))))

(define (scale-list items factor)
  (map (lambda (x) (* x factor)) items))

(define (add-lists list1 list2)
  (cond ((null? list1) list2)
        ((null? list2) list1)
        (else (cons (+ (car list1) (car list2))
                    (add-lists (cdr list1) (cdr list2))))))

(define ones (cons 1 ones))

(define integers (cons 1 (add-lists ones integers)))

(list-ref integers 17)


(define (integral integrand initial-value dt)
  (define int
    (cons initial-value
          (add-lists (scale-list integrand dt) int)))
  int)

(define (solve f y0 dt)
  (define y (integral dy y0 dt))
  (define dy (map f y))
  y)

; these will cause stack overflow of guile vm, but mit-scheme works
;(list-ref (solve (lambda (x) x) 1 0.001) 1000)

(define cons cons-system)
(define car car-system)
(define cdr cdr-system)
