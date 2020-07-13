;:
;: This problem is a change by which we can 
;: use the lazy-value of Scehme.
;:

;: Firstly, we justly use the filter
(load "../lib/common.scm")

(define (pred? x)
    (or (= (remainder x 3) 0) 
        (= (remainder x 5) 0)))

(define (solve n)
    (fold-left + 0 (filter pred?
                         (enumerate-interval 1 n))))

;: Stream
(load "../lib/streams.scm")
(define (solve2 n)
    ( accumulate-stream + 0 (stream-filter pred? (stream-enumerate-interval 1 n))))

(define (solve3 n)
    ( accumulate-stream-iter + 0 (stream-filter pred? (stream-enumerate-interval 1 n))))


