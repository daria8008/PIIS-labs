(import [pandas :as pd])
(import [numpy :as np])

(setv path "data.csv")
(setv data (pd.read_csv path))

(setv time (get data "time"))
(print "Time expected value:" (.mean time))

(setv score (get data "score"))
(print "Score variance:" (.var score))