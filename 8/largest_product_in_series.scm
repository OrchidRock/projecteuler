;:
;:
;:

(define ADJ_LEN 13)
(define SERIES_FILE "series.txt")

(define (load-series filename)
  (with-input-from-file filename
                        (lambda ()
                          (let loop ((series '())
                                     (next-char (read-char)))
                            (if (eof-object? next-char)
                              (reverse series)
                              (if (char->digit next-char)
                                (loop (cons (char->digit next-char) series)
                                      (read-char))
                                (loop series (read-char))))))))


(define series (load-series SERIES_FILE))

(define (solve n series)
  (define (get-initial-gpa series n)
    (define (iter product res n series)
      (if (= n 0)
        (list series product (reverse res))
        (iter (* product (car series))
              (cons (car series) res)
              (- n 1)
              (cdr series))))
    (iter 1 '() n series))
  (define (get-next-gpa gpa series)
    (if (null? series)
      gpa
      (if (= (caadr gpa) 0)
        (list (cadr (get-initial-gpa (append (cdadr gpa) series)
                                     n))
              (append (cdadr gpa) (list (car series))))
        (list (* (/ (car gpa) (caadr gpa)) (car series))
              (append (cdadr gpa) (list (car series)))))))
  (define (iter greatest-product-adj next series)

    (display greatest-product-adj)
    (display next)
    (newline)
    (if (null? series)
      greatest-product-adj
      (if (> (car next) (car greatest-product-adj))
        (iter next (get-next-gpa next series) (cdr series))
        (iter greatest-product-adj
              (get-next-gpa next series)
              (cdr series)))))
  (let ((initial-gpa (get-initial-gpa series n)))
    (let ((next-gpa (get-next-gpa (cdr initial-gpa)
                                  (car initial-gpa))))
        ;(display (cdr initial-gpa))
        ;(display (car initial-gpa))
        ;(display next-gpa)
        (iter (cdr initial-gpa) next-gpa (cdr (car initial-gpa)))
      )))

(solve ADJ_LEN series)

