
(define (install-schmeme-number-package)
  (define (tag x) (attach-tag 'scheme-number x))
  (put 'add '(scheme-number, scheme-number)
       (lambda (x y) (tag (+ x y))))
  (put 'sub '(scheme-number, shceme-number)
       (lambda (x y) (tag (- x y))))
  (put 'mul '(scheme-number, scheme-number)
       (lambda (x y) (tag (* x y))))
  (put 'div '(scheme-number, shceme-number)
       (lambda (x y) (tag (/ x y))))
  (put 'make 'scheme-number (lambda (x) (tag x)))
  'done)

(define (make-scheme-number n)
  ((get 'make 'scheme-number) n))

(display (make-scheme-number 1))
