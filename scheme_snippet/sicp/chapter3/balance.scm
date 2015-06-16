
(define (make-withdraw balance)
  (lambda (amount)
    (if (>= balance amount)
      (begin (set! balance (- balance amount))
             balance)
      "Insufficeent funds")))


(define w1 (make-withdraw 25))
(display (w1 20))
(display "\n")
(display (w1 20))
