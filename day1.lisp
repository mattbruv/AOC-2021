(load "helpers.lisp")

(defparameter *i* (mapcar #'parse-integer (readlines (open "data/day1.txt"))))

(defun increases (value remainder collection)
    (if (eql (car remainder) nil)
        collection
        (increases (car remainder) (cdr remainder)
            (if (> (car remainder) value)
                (cons (car remainder) collection)
                collection))))

(defun slidings (remainder collection)
    (let ((group (take-first-n remainder 3)))
        (if (eql group nil)
            collection
            (slidings (cdr remainder) (append collection (list (apply '+ group)))))))

(defparameter *incs* (increases (car *i*) *i* '()))
(defparameter *slides* (slidings *i* '()))

(print (length *incs*))
(print (length (increases (car *slides*) *slides* '())))