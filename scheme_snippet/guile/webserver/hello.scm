

(use-modules (web server))

(define (handler request request-body)
  (values '((content-type . (text/plain)))
          "Hello world!"))


(run-server handler)
