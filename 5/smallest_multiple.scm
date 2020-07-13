
(define (is-prime n prefix_primes_table)

  (define (div num prime)
    (if (= (remainder num prime) 0)
      (div (/ num prime) prime)
      num))

  (if (null? prefix_primes_table)
    (not (= n 1))
    (is-prime (div n (car prefix_primes_table)) (cdr prefix_primes_table))))

(define (solve n)

  (define (next-factor factor)
    (if (= factor 2)
      3
      (+ factor 2)))

  (define (iter factor prefix_primes_table res)
    (if (> factor n)
      res
      (if (is-prime factor prefix_primes_table)
        (let ((expont (floor (/ (log n) (log factor)))))
          (let ((k (expt factor expont)))
            (iter (next-factor factor)
                  (append prefix_primes_table (list factor))
                  (* res k))))
        (iter (next-factor factor) prefix_primes_table res))))
  (iter 2 '() 1))

