;:
;: The sieve method of Eratosthenes.
;:

(load "../lib/streams.scm")
(load "../lib/common.scm")

(define LIMIT 2000000)


;: slow
(define (solve n)
  (define (iter series res)
    (if (or (null? series) (>= (car series) n))
      res
      (iter (filter (lambda (x) (not (= (remainder x (car series)) 0)))
                    series)
            (+ res (car series)))))
  (iter (enumerate-interval 2 (- n 1)) 0))

(define (solve2 n)
  (define (iter stream res)
    (if (or (stream-null? stream) (>= (stream-car stream) n))
        res
        (iter (stream-filter (lambda (x) (not (= (remainder x (stream-car stream)) 0)))
                             stream)
              (+ res (stream-car stream)))))
  (iter (stream-enumerate-interval 2 (- n 1)) 0))

; (solve LIMIT)
