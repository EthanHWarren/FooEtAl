from FooEtAl import *
import argparse
import sys

if not len(sys.argv) > 1:
    print("Please type 'FooCLI.py -h' or 'FooCLI.py -help' for a list of available options.")
else:
    parser = argparse.ArgumentParser(description = "Foo is a software package for Foo Physics operations")

    parser.add_argument("-rv", "--radVol", nargs = 1, type = float, metavar = "num", 
                        help = "Takes the radius of a sphere, returns it's volume")
 

    args = parser.parse_args()

 
    if len(args.radVol) != 0:
        print(RadVol(args.radVol[0]))