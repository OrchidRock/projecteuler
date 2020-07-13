
;: enumerater
(define (enumerate-interval low high)
    (if (> low high)
        '()
        (cons low (enumerate-interval (+ low 1) high))))

;: recursive
(define (accumulate-stream op initial stream)
    (if (stream-null? stream)
        initial
        (op (stream-car stream) (accumulate-stream op 
                                                   initial 
                                                   (stream-cdr stream)))))

;: iterative
(define (accumulate-stream-iter op initial stream)
    (define (iter stream result)
        (if (stream-null? stream)
            result
            (iter (stream-cdr stream) (op result (stream-car stream)))))
    (iter stream initial))
