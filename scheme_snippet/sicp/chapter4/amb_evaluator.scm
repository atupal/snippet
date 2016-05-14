(load "eval_apply.scm")


;;
;; Start 4.3 Variations on a Scheme - Nondeterministic Computing
;;

; start 4.3.1 Amb and Search
(define (require p) (if (not p) (amb)))
(define (an-element-of items)
  (require (not (null? items)))
  (amb (car items) (an-element-of (cdr items))))
(define (an-integer-starting-from n)
  (amb n (an-integer-starting-from (+ n 1))))
; start exercise 4.35
(define (an-integer-between low high)
  (require (<= low high))
  (amb low (an-integer-between (+ low 1) high)))
; end exercise 4.35

; start exercise 4.36
; end exercise 4.36

; start exercise 4.37
; end exercise 4.37

; end 4.3.1 Amb and Search

;;
;; end 4.3 Variations on a Scheme - Condeterministic Computing
;;



(driver-loop)
