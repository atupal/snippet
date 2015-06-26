
(define x (list 'a 'b))
(define y (list 'c 'd))

(define z (append x y))

(display (cdr x))

(define w (append! x y))

(display "\n")

(display (cdr x))
