;:
;:
;:

(load "../lib/common.scm")
(load "../lib/streams.scm")

(define (fibs-stream limit) 
    (define (get-fibs a b)
        (if (<= a limit)
            (cons-stream a 
                        (get-fibs b (+ a b)))
            '()))
    (get-fibs 0 1))

(define (solve limit)
    (accumulate-stream + 0 (stream-filter even? 
                                          (fibs-stream limit))))
