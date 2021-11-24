(setv maze [[0 0 0 0 0 0 0] [0 0 1 1 1 0 0] [0 1 1 0 1 0 0] [0 1 0 0 1 1 0] [0 1 1 1 1 1 0] [0 0 0 1 1 0 0] [0 0 0 0 0 0 0]])

(setv pacman_pos [1 3])
(setv ghost_pos [4 3])

(defn calculate_heuristic [p_x p_y g_x g_y]
    (+ (abs (- p_x g_x)) (abs (- p_y g_y))))

(defn a[] -1)

(defn ghost_step [pacman_pos ghost_pos maze] 
    (setv heur_with_best_coord [100 []])

    (if (= (get maze (get ghost_pos 0) (+ (get ghost_pos 1) 1)) 1)
        (if (< (calculate_heuristic (get ghost_pos 0) (+ (get ghost_pos 1) 1) (get pacman_pos 0) (get pacman_pos 1)) (get heur_with_best_coord 0))
            (setv heur_with_best_coord [(calculate_heuristic (get ghost_pos 0) (+ (get ghost_pos 1) 1) (get pacman_pos 0) (get pacman_pos 1)) [(get ghost_pos 0) (+ (get ghost_pos 1) 1)]])
            (setv a 0))
        (setv a 0))

    (if (= (get maze (get ghost_pos 0) (- (get ghost_pos 1) 1)) 1)
        (if (< (calculate_heuristic (get ghost_pos 0) (- (get ghost_pos 1) 1) (get pacman_pos 0) (get pacman_pos 1)) (get heur_with_best_coord 0))
            (setv heur_with_best_coord [(calculate_heuristic (get ghost_pos 0) (- (get ghost_pos 1) 1) (get pacman_pos 0) (get pacman_pos 1)) [(get ghost_pos 0) (- (get ghost_pos 1) 1)]])
            (setv a 0))
        (setv a 0))

    (if (= (get maze (+ (get ghost_pos 0) 1) (get ghost_pos 1)) 1)
        (if (< (calculate_heuristic (+ (get ghost_pos 0) 1) (get ghost_pos 1) (get pacman_pos 0) (get pacman_pos 1)) (get heur_with_best_coord 0))
            (setv heur_with_best_coord [(calculate_heuristic (- (get ghost_pos 1) 0) (get ghost_pos 1) (get pacman_pos 0) (get pacman_pos 1)) [(- (get ghost_pos 1) 0) (get ghost_pos 1)]])
            (setv a 0))
        (setv a 0))

    (if (= (get maze (- (get ghost_pos 0) 1) (get ghost_pos 1)) 1)
        (if (< (calculate_heuristic (- (get ghost_pos 0) 1) (get ghost_pos 1) (get pacman_pos 0) (get pacman_pos 1)) (get heur_with_best_coord 0))
            (setv heur_with_best_coord [(calculate_heuristic (- (get ghost_pos 1) 0) (get ghost_pos 1) (get pacman_pos 0) (get pacman_pos 1)) [(- (get ghost_pos 1) 0) (get ghost_pos 1)]])
            (setv a 0))
        (setv a 0))
    
    (setv best_coordinates (get heur_with_best_coord 1))
    (return best_coordinates)
)

(defn pacman_step [ghost_pos pacman_pos maze] 
    (setv heur_with_best_coord [0 []])

    (if (= (get maze (- (get ghost_pos 0) 1) (get ghost_pos 1)) 1)
        (if (> (calculate_heuristic (- (get ghost_pos 0) 1) (get ghost_pos 1) (get pacman_pos 0) (get pacman_pos 1)) (get heur_with_best_coord 0))
            (setv heur_with_best_coord [(calculate_heuristic (- (get ghost_pos 1) 0) (get ghost_pos 1) (get pacman_pos 0) (get pacman_pos 1)) [(- (get ghost_pos 1) 0) (get ghost_pos 1)]])
            (print 0))
        (setv a 0))

    (if (= (get maze (+ (get ghost_pos 0) 1) (get ghost_pos 1)) 1)
        (if (> (calculate_heuristic (+ (get ghost_pos 0) 1) (get ghost_pos 1) (get pacman_pos 0) (get pacman_pos 1)) (get heur_with_best_coord 0))
            (setv heur_with_best_coord [(calculate_heuristic (- (get ghost_pos 1) 0) (get ghost_pos 1) (get pacman_pos 0) (get pacman_pos 1)) [(- (get ghost_pos 1) 0) (get ghost_pos 1)]])
            (setv a 0))
        (setv a 0))

    (if (= (get maze (get ghost_pos 0) (+ (get ghost_pos 1) 1)) 1)
        (if (> (calculate_heuristic (get ghost_pos 0) (+ (get ghost_pos 1) 1) (get pacman_pos 0) (get pacman_pos 1)) (get heur_with_best_coord 0))
            (setv heur_with_best_coord [(calculate_heuristic (get ghost_pos 0) (+ (get ghost_pos 1) 1) (get pacman_pos 0) (get pacman_pos 1)) [(get ghost_pos 0) (+ (get ghost_pos 1) 1)]])
            (setv a 0))
        (setv a 0))

    (if (= (get maze (get ghost_pos 0) (- (get ghost_pos 1) 1)) 1)
        (if (> (calculate_heuristic (get ghost_pos 0) (- (get ghost_pos 1) 1) (get pacman_pos 0) (get pacman_pos 1)) (get heur_with_best_coord 0))
            (setv heur_with_best_coord [(calculate_heuristic (get ghost_pos 0) (- (get ghost_pos 1) 1) (get pacman_pos 0) (get pacman_pos 1)) [(get ghost_pos 0) (- (get ghost_pos 1) 1)]])
            (setv a 0))
        (setv a 0))
    
    (return (get heur_with_best_coord 1))
)

(print "Start ghost pos: " ghost_pos)
(print "Start pacman pos: " pacman_pos)
(print "\n")

(setv ghost_pos (ghost_step pacman_pos ghost_pos maze))
(print "Best ghost step" ghost_pos)
(setv pacman_pos (pacman_step pacman_pos ghost_pos maze))
(print "Best pacman step" pacman_pos)