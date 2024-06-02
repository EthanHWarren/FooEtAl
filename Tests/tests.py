from FooEtAl import *

#"correct" answers are from Desmos online graphing calculator. They use pi to the 11th place, or 3.14159265359.
#testing random value
assert RadVol(4) == 268.082573106, "should be 268.082573106"
#testing plugging in 0
assert RadVol(0) == 0, "should be 0"
#testing a negative number
assert RadVol(-5) == 0, "should be 0"
#testing a floating point number
assert RadVol(5.76) == 800.490273974, "should be 800.490273974"
#testing a small value
assert RadVol(0.001) == 0.00000418879020479, "should be 0.00000418879020479"
#testing a large number
assert RadVol(150) == 14137166.9412, "should be 14137166.9412"