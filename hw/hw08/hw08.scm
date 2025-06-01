(define (ascending? s)   
  ;cdr checks rest of list, whereas car (cdr s) checks second element
  (cond ((or (null? s) (null? (cdr s))) #t)
        ((> (car s) (car (cdr s))) #f)
        (else (ascending? (cdr s)))
  )
)

(define (my-filter pred s) 
;pred should apply to current element, not entire list'
  (cond 
    ;check if list is empty'
    ((or (null? s)) '())
    ;elif predicate works on current element'
    ((pred (car s)) 
      (cons (car s) (my-filter pred (cdr s))))
    ;predicate doesn't work on current element'
    (else (my-filter pred (cdr s)))
  )
)


(define (interleave lst1 lst2) 
  (cond 
    ((null? lst1) lst2)
    ((null? lst2) lst1)
    (else 
      (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2))))
    )
  )
)


(define (no-repeats s) 
  ; check if s is empty
  (cond
    ((null? s) '())

    (else
      ; compare current value of s
      (let ((a (car s)))
      ; add onto existing list with cons
      ; use filter to filter through non-repeat elements
      (cons a (no-repeats (filter (lambda (x) (not (= x a))) (cdr s)))))
    )
  )
)