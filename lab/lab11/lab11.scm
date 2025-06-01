(define (if-program condition if-true if-false)
  `(if ,condition ,if-true ,if-false))


(define (square n) (* n n))

(define (pow-expr base exp) 
  (cond 
    ; base case
    ((= exp 0) 1)
    ; exp is 1
    ((= exp 1) `(* ,base ,exp))
    ; even case
    ((even? exp) `(square ,(pow-expr base (/ exp 2))))
    ; odd case
    (else `(* ,base (square ,(pow-expr base (/ (- exp 1) 2)))))
  )
)

(define-macro (repeat n expr)
  ; need lambda or else will immediately return a value back from function call
  ; BUT we want to call function n times
  `(repeated-call ,n (lambda () ,expr)))

; Call zero-argument procedure f n times and return the final result.
(define (repeated-call n f)
  (if (= n 1)
    ; return final call to f
      (f)
      ; call f n number of times
      (begin (f) (repeated-call (- n 1) f))))
