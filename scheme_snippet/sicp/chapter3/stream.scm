
;; definition
(define the-empty-stream '())
(define stream-null? null?)

(define (memo-proc proc)
  (let ((already-run? #f) (result #f))
    (lambda ()
      (if (not already-run?)
        (begin (set! result (proc))
               (set! already-run? #t)
               result)
        result))))

;(define (delay exp)
  ;(memo-proc (lambda () exp)))


;(define (force delayed-object) (delayed-object))

;(define (cons-stream a b)
  ;(cons a (delay b)))

(define (stream-car stream) (car stream))
(define (stream-cdr stream) (force (cdr stream)))



;; util functions 
(define (stream-ref s n)
  (if (= n 0)
    (stream-car s)
    (stream-ref (stream-cdr s) (- n 1))))

(define (stream-take s n)
  (if (= n 0)
    '()
    (cons (stream-car s) (stream-take (stream-cdr s) (- n 1)))))

(define (stream-slice s n)
  (if (= n 0)
    '()
    (cons-stream (stream-car s) (stream-slice (stream-cdr s) (- n 1)))))

(define (stream-map proc s)
  (if (stream-null? s)
    the-empty-stream
    (cons-stream (proc (stream-car s))
                 (stream-map proc (stream-cdr s)))))

(define (stream-for-each proc s)
  (if (stream-null? s)
    'done
    (begin (proc (stream-car s))
           (stream-for-each proc (stream-cdr s)))))
(define (stream-filter pred stream)

  (cond ((stream-null? stream) the-empty-stream)
        ((pred (stream-car stream))
         (cons-stream (stream-car stream)
                      (stream-filter
                        pred
                        (stream-cdr stream))))
        (else (stream-filter pred (stream-cdr stream)))))

(define (stream-map proc . argstreams)
  (if (stream-null? (car argstreams))
    the-empty-stream
    (cons-stream
      (apply proc (map stream-car argstreams))
      (apply stream-map
             (cons proc (map stream-cdr argstreams))))))

(define (display-stream s)
  (stream-for-each display-line s))
(define (display-line x) (newline) (display x))

(define (stream-enumerate-interval low high)
  (if (> low high)
    the-empty-stream
    (cons-stream
      low
      (stream-enumerate-interval (+ low 1) high))))


;; ex 3.51
#|
(define (show x)
  (display-line x)
  x)

(define x
  (stream-map show
              (stream-enumerate-interval 0 10)))

(display "stream-ref x 5")
(stream-ref x 5)
(display "stream-ref x 7")
(stream-ref x 7)
|#
;; end ex 3.51

;; ex 3.52
(define sum 0)
;(display-line sum)
(define (accum x) (set! sum (+ x sum)) sum)
;(display-line sum)
(define seq
  (stream-map accum
              (stream-enumerate-interval 1 20)))
;(display-line sum)
(define y (stream-filter even? seq))
;(display-line sum)
(define z
  (stream-filter (lambda (x) (= (remainder x 5) 0))
                 seq))
;(display-line sum)
(stream-ref y 7)
;(display-line sum)
;(display-stream z)
;; end ex 3.52


(define (integers-starting-from n)
  (cons-stream n (integers-starting-from (+ n 1))))
(define integers (integers-starting-from 1))
(define (divisible? x y) (= (remainder x y) 0))
(define (sieve stream)
  (cons-stream
    (stream-car stream)
    (sieve (stream-filter
             (lambda (x)
               (not (divisible? x (stream-car stream))))
             (stream-cdr stream)))))
(define primes (sieve (integers-starting-from 2)))

(define ones (cons-stream 1 ones))
(define (add-streams s1 s2) (stream-map + s1 s2))
(define integers
  (cons-stream 1 (add-streams ones integers)))

(define (scale-stream stream factor)
  (stream-map (lambda (x) (* x factor))
              stream))

(define double (cons-stream 1 (scale-stream double 2)))

;(display-line (stream-ref double 10))

(define primes
  (cons-stream
    2
    (stream-filter prime? (integers-starting-from 3))))

(define (prime? n)jk
  (define (iter ps)
    (cond ((> (square (stream-car ps)) n) #t)
          ((divisible? n (stream-car ps)) #f)
          (else (iter (stream-cdr ps)))))
  (iter primes))

;(display-line (stream-take primes 3))


; ex 3.54
(define (mul-streams s1 s2) (stream-map * s1 s2))

; factorails count from 0
(define factorials
  (cons-stream 1 (mul-streams factorials integers)))

;(display (stream-take factorials 10))

; end ex 3.54
; ex 3.55
(define (partial-sums s)
  (add-streams s (cons-stream 0 (partial-sums s))))

;(display-line (stream-take integers 10))
;(display-line (stream-take (partial-sums integers) 10))


; ex 3.56
; merge that combines two ordered streams into one ordered result stream, eliminating repetitions:
(define (merge s1 s2)
  (cond ((stream-null? s1) s2)
        ((stream-null? s2) s1)
        (else
          (let ((s1car (stream-car s1))
                (s2car (stream-car s2)))
            (cond ((< s1car s2car)
                   (cons-stream
                     s1car
                     (merge (stream-cdr s1) s2)))
                  ((> s1car s2car)
                   (cons-stream
                     s2car
                     (merge s1 (stream-cdr s2))))
                  (else
                    (cons-stream
                      s1car
                      (merge (stream-cdr s1)
                             (stream-cdr s2)))))))))

(define S (cons-stream 1 (merge (scale-stream S 2) (merge (scale-stream S 3) (scale-stream S 5)))))

;(display-line (stream-take S 10))
; end ex 3.56


; ex 3.58
(define (expand num den radix)
  (cons-stream
    (quotient (* num radix) den)
    (expand (remainder (* num radix) den) den radix)))
;(display-line (stream-take (expand 1 7 10) 10))
;(display-line (stream-take (expand 3 8 10) 10))
; end ex 3.58

;; ex 3.59
(define (integrate-series s)
  (stream-map (lambda (x y) (* x (/ 1 y))) s integers))

(define exp-series
  (cons-stream 1 (integrate-series exp-series)))

;(display-line (stream-take exp-series 10))
(define cosine-series (cons-stream 1 (scale-stream (integrate-series sine-series) -1)))
(define sine-series (cons-stream 0 (integrate-series cosine-series)))

;(display-line (stream-take cosine-series 10))
;(display-line (stream-take sine-series 10))
;; end ex 3.59

;; ex 3.60
(define (mul-series s1 s2)
  (cons-stream
    (* (stream-car s1) (stream-car s2))
    (add-streams (add-streams (scale-stream (stream-cdr s1) (stream-car s2)) 
                              (scale-stream (stream-cdr s2) (stream-car s1)))
                 (cons-stream 0 (mul-series (stream-cdr s1) (stream-cdr s2))))))

; A shorter version:
(define (mul-series s1 s2)
  (cons-stream (* (stream-car s1) (stream-car s2))
               (add-streams (scale-stream (stream-cdr s2) (stream-car s1))
                            (mul-series (stream-cdr s1) s2))))

(define S (add-streams (mul-series sine-series sine-series) (mul-series cosine-series cosine-series)))
;(display-line (stream-take S 10))
;; end ex 3.60

;; ex 3.61
(define (invert-unit-series s)
  (define x
    (cons-stream 1 (scale-stream (mul-series (stream-cdr s) x) -1)))
  x)

; bellow version is not memorized
;(define (invert-unit-series s)
    ;(cons-stream 1 (scale-stream (mul-series (stream-cdr s) (invert-unit-series s)) -1)))
;; end ex 3.61

;; ex 3.62

(define (div-series s1 s2)
  (mul-series s1 (invert-unit-series s2)))
(define tangent (div-series sine-series cosine-series))
;(display-line (stream-take tangent 10))
;; end ex 3.62

(define (average a b)
  (/ (+ a b) 2))

(define (sqrt-improve guess x)
  (average guess (/ x guess)))

(define (sqrt-stream x)
  (define guesses
    (cons-stream
      1.0
      (stream-map (lambda (guess) (sqrt-improve guess x))
                  guesses)))
  guesses)

;(display-stream (stream-slice (sqrt-stream 2) 10))


