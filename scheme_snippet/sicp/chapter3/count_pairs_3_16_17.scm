
(define (count-pairs x)
  (if (not (pair? x))
    0
    (+ (count-pairs (car x))
       (count-pairs (cdr x))
       1)))


(define l (list 'a 'b 'c))

; 3
(display (count-pairs l))
(display "\n")

(define second (cons 'a 'b))
(define third (cons 'c 'd))
(define first (cons second third))
(set-car! second third)

; 4
(display (count-pairs first))
(display "\n")

(define second (cons 'a 'b))
(define third (cons second second))
(define first (cons third third))

; 7
(display (count-pairs first))
(display "\n")

(define loop (cons 'a 'b))
(set-car! loop loop)
; never return: stackoverflow
; (count-pairs loop)


;; correct:

(define s '())
(define (visited? pair)
  (define (look t)
    (if (eq? t '())
      (begin
        (set! s (cons pair s))
        0)
      (if (eq? pair (car t))
        1
        (look (cdr t)))))
  (look s))

(define (count-pairs-2 x)
  (if (or (not (pair? x)) (eq? (visited? x) 1))
    0
    (+ (count-pairs-2 (car x))
       (count-pairs-2 (cdr x))
       1)))


(display "correct:\n")
(define l (list 'a 'b 'c))

; 3
(display (count-pairs-2 l))
(display "\n")

(define second (cons 'a 'b))
(define third (cons 'c 'd))
(define first (cons second third))
(set-car! second third)

; 4
(display (count-pairs-2 first))
(display "\n")

(define second (cons 'a 'b))
(define third (cons second second))
(define first (cons third third))

; 7
(display (count-pairs-2 first))
(display "\n")
