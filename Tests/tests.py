from FooEtAl import RadVol

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
assert RadVol(0.01) == 0.000004189, "should be 0.000004189"
#testing a large number
assert RadVol(150) == 14137166.941155, "should be 14137166.94155"