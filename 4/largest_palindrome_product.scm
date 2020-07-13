;:
;:
;:

(define (reverse num)
  (define (iter n res)
    (if (<= n 0)
      res
      (iter (quotient n 10) (+ (* 10 res) (remainder n 10)))))
  (iter num 0))

(define (is_palindrome num)
  (= (reverse num) num))


(define (solve)
  (define (iter2 a b db largeat_palindrome)
    (if (>= b a)
      (if (<= (* a b) largeat_palindrome)
        largeat_palindrome
        (if (is_palindrome (* a b))
          (iter2 a (- b db) db (* a b))
          (iter2 a (- b db) db largeat_palindrome)))
      largeat_palindrome))
  (define (iter1 a largeat_palindrome)
    (if (>= a 100)
      (if (= (remainder a 11) 0)
        (iter1 (- a 1) (iter2 a 999 1 largeat_palindrome))
        (iter1 (- a 1) (iter2 a 990 11 largeat_palindrome)))
      largeat_palindrome))
  (iter1 999 0))

(solve)
