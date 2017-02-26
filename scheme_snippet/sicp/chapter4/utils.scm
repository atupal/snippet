(use-modules (srfi srfi-19))

(define (debug message)
  (newline)
  (display "[DEBUG] ")
  (display (date->string (current-date) "~4"))
  (display ": ")
  (display message))
