(load "eval_apply.scm")
(load "utils.scm")


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

; start 4.3.3 Implementing the amb Evaluator
(define (amb? exp) (tagged-list? exp 'amb))
(define (amb-choices exp) (cdr exp))

(define (analyze-4.3.3 exp)
  (cond ((self-evaluating? exp) (analyze-self-evaluating exp))
        ((quoted? exp) (analyze-quoted exp))
        ((variable? exp) (analyze-variable exp))
        ((assignment? exp) (analyze-assignment exp))
        ((definition? exp) (analyze-definition exp))
        ((if? exp) (analyze-if exp))
        ((let? exp) (analyze (let->combination exp)))
        ((let*? exp) (analyze (let*->nested-lets exp)))
        ((letrec? exp) (analyze (letrec->let exp)))
        ((for? exp) (analyze (for->procedure-calls exp)))
        ((unless? exp) (analyze (unless->if exp)))
        ((lambda? exp) (analyze-lambda exp))
        ((begin? exp) (analyze-sequence (begin-actions exp)))
        ((cond? exp) (analyze (cond->if exp)))
        ((amb? exp) (analyze-amb exp))   ; dispatch amb
        ((application? exp) (analyze-application exp))
        (else (error "Unknow expression type: ANALYZE" exp))))
(define analyze analyze-4.3.3)

(define (ambeval exp env succeed fail)
  ((analyze exp) env succeed fail))

; simple expressions
(define (analyze-self-evaluating exp)
  (lambda (env succeed fail)
    (succeed exp fail)))
(define (analyze-quoted exp)
  (let ((qval (text-of-quotation exp)))
    (lambda (env succeed fail)
      (succeed qval fail))))
(define (analyze-variable exp)
  (lambda (env succeed fail)
    (succeed (lookup-variable-value exp env) fail)))
(define (analyze-lambda exp)
  (let ((vars (lambda-parameters exp))
        (bproc (analyze-sequence (lambda-body exp))))
    (lambda (env succeed fail)
      (succeed (make-procedure vars bproc env) fail))))

; conditionals and sequences
(define (analyze-if exp)
  (let ((pproc (analyze (if-predicate exp)))
        (cproc (analyze (if-consequent exp)))
        (aproc (analyze (if-alternative exp))))
    (lambda (env succeed fail)
      (pproc env
             ;; success continuation for evaluating the predicate
             ;; to obtain pred-value
             (lambda (pred-value fail2)
               (if (true? pred-value)
                 (cproc env succeed fail2)
                 (aproc env succeed fail2)))
             ;; failure continuation for evaluating thepredicate
             fail))))
(define (analyze-sequence exps)
  (define (sequentially a b)
    (lambda (env succeed fail)
      (a env
         ;; success continuatoin for calling a
         (lambda (a-value fail2)
           (b env succeed fail2))
         ;; failure continuation for calling a
         fail)))
  (define (loop first-proc rest-procs)
    (if (null? rest-procs)
      first-proc
      (loop (sequentially first-proc
                          (car rest-procs))
            (cdr rest-procs))))
  (let ((procs (map analyze exps)))
    (if (null? procs)
      (error "Empty sequence: ANALYZE"))
    (loop (car procs) (cdr procs))))

; definitions and assignments
(define (analyze-definition exp)
  (let ((var (definition-variable exp))
        (vproc (analyze (definition-value exp))))
    (lambda (env succeed fail)
      (vproc env
             (lambda (val fail2)
               (define-variable! var val env)
               (succeed 'ok fail2))
             fail))))
(define (analyze-assignment exp)
  (let ((var (assignment-variable exp))
        (vproc (analyze (assignment-value exp))))
    (lambda (env succeed fail)
      (vproc env
             (lambda (val fail2)        ; *1*
               (let ((old-value
                       (lookup-variable-value var env)))
                 (set-variable-value! var val env)
                 (succeed 'ok
                          (lambda ()    ; *2*
                            (set-variable-value!
                              var old-value env)
                            (fail2)))))
             fail))))

; procedure applications
(define (analyze-application exp)
  (let ((fproc (analyze (operator exp)))
        (aprocs (map analyze (operands exp))))
    (lambda (env succeed fail)
      (fproc env
             (lambda (proc fail2)
               (get-args aprocs
                         env
                         (lambda (args fail3)
                           (execute-application
                             proc args succeed fail3))
                         fail2))
             fail))))
(define (get-args aprocs env succeed fail)
  (if (null? aprocs)
    (succeed '() fail)
    ((car aprocs)
     env
     ;; success continuation for this aproc
     (lambda (arg fail2)
       (get-args
         (cdr aprocs)
         env
         ;; success continuation for
         ;; recursive call to get-args
         (lambda (args fail3)
           (succeed (cons arg args) fail3))
         fail2))
     fail)))
(define (execute-application proc args succeed fail)
  (cond ((primitive-procedure? proc)
          (succeed (apply-primitive-procedure proc args)
                   fail))
         ((compound-procedure? proc)
          ((procedure-body proc)
           (extend-environment
             (procedure-parameters proc)
             args
             (procedure-environment proc))
           succeed
           fail))
         (else
           (error "Unknown procedure type: EXECUTE-APPLICATION"
                  proc))))

; evaluating amb expressions
(define (analyze-amb exp)
  (let ((cprocs (map analyze (amb-choices exp))))
    (lambda (env succeed fail)
      (define (try-next choices)
        (if (null? choices)
          (fail)
          ((car choices)
           env
           succeed
           (lambda () (try-next (cdr choices))))))
      (try-next cprocs))))

; driver loop
(define input-prompt  ";;; Amb-Eval input:")
(define output-prompt ";;; Amb-Eval value:")
(define (driver-loop-amb)
  (define (internal-loop try-again)
    (prompt-for-input input-prompt)
    (let ((input (read)))
      (if (eof-object? input)
        (exit))
      (if (eq? input 'try-again)
        (try-again)
        (begin
          (newline) (display ";;; Staring a new problem ")
          (ambeval
            input
            the-global-environment
            ;; ambeval success
            (lambda (val next-alternative)
              (announce-output output-prompt)
              (user-print val)
              (internal-loop next-alternative))
            ;; ambeval failure
            (lambda ()
              (announce-output
                ";;; There are no more values of")
              (user-print input)
              (driver-loop-amb)))))))
  (internal-loop
    (lambda ()
      (newline) (display ";;; There is no current problem")
      (driver-loop-amb))))
(define driver-loop driver-loop-amb)

; end 4.3.3 Implementing the amb Evaluator

;;
;; end 4.3 Variations on a Scheme - Condeterministic Computing
;;



(driver-loop)
