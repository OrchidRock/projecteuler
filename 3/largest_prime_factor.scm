;:
;: Algorithm 1:
;:      The  useful of prime table very obvious when n not too big.
;:      But how can we judge the size of prime table when n hasn't a limition ?
;: Algorithm 2:
;:      2 and odd table
;:
;:

(define PRIMES_TABLE_FILE "../lib/primes_table.txt")
(define (load-primes-table filename)
    (with-input-from-file filename
                          (lambda ()
                                (let loop ((lines '())
                                           (next-line (read-line)))
                                  (if (eof-object? next-line)
                                    (reverse lines)
                                    (loop (cons (string->number next-line) lines)
                                          (read-line)))))))
(define (solve n)
    (define primes-table (load-primes-table PRIMES_TABLE_FILE))
    (define (iter n pt)
        (cond ((null? pt) (display "The primes-table is too small"))
              ((= n 1) (car pt))
              ((= (remainder n (car pt)) 0)
                (iter (/ n (car pt)) pt))
              (else (iter n (cdr pt)))))
    (iter n primes-table))
