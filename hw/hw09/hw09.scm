(define (curry-cook formals body) 
  ; base case
  (if (= (length formals) 1)
    (list 'lambda formals body)

    ; multiple elements in list
    ; local bindings
    (let ((first (car formals))
         (rest (cdr formals)))

      ; recursively curry rest of list
      (list 'lambda (list first) (curry-cook rest body))
    )
  )
)

(define (curry-consume curry args)
  ; base case, args is empty list
  (if (null? args)
    curry

    ; args is not empty
    ; recursively call curry on first element
    (curry-consume (curry (car args)) (cdr args))
    
  )
)



(define-macro (switch expr options)
  (switch-to-cond (list 'switch expr options)))

(define (switch-to-cond switch-expr)
  (cons 'cond
        (map (lambda (option)
               (cons (list 'equal? (car (cdr switch-expr)) (car option)) (cdr option)))
             (car (cdr (cdr switch-expr))))))
