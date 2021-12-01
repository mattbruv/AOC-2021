(defun readlines (s)
    (loop for line = (read-line s nil)
        while line
        collect line))

(defun take-first-n (collection limit)
    (let ((diff (- (length collection) limit)))
        (butlast collection
            (if (< diff 0) (+ limit diff) diff))))