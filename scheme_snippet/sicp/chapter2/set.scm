
(define (entry tree) (car tree))
(define (left-branch tree) (cadr tree))
(define (right-branch tree) (caddr tree))
(define (make-tree entry left right)
  (list entry left right))

(define (adjoin-set x set)
  (cond ((null? set) (make-tree x '() '()))
        ((= x (entry set)) set)
        ((< x (entry set))
         (make-tree (entry set)
                    (adjoin-set x (left-branch set))
                    (right-branch set)))
        ((> x (entry set))
         (make-tree (entry set) (left-branch set)
                    (adjoin-set x (right-branch set))))))


(define (tree->list-1 tree)
  (if (null? tree)
  '()
  (append (tree->list-1 (left-branch tree))
          (cons (entry tree)
                (tree->list-1
                  (right-branch tree))))))

(define (tree->list-2 tree)
  (define (copy-to-list tree result-list)
    (if (null? tree)
      result-list
      (copy-to-list (left-branch tree)
                    (cons (entry tree)
                          (copy-to-list
                            (right-branch tree)
                            result-list)))))
  (copy-to-list tree '()))



(define tree
  (adjoin-set 4
              (adjoin-set 5
                          (adjoin-set 2
                                      (adjoin-set 0 
                                                  (adjoin-set 1 
                                                              (make-tree 3 '() '())))))))

(display (tree->list-1 tree))  ; O(nlgn)
(display "\n")
(display (tree->list-2 tree))  ; O(n)
