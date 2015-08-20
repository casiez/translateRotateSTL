#!/usr/bin/python

# translateRotateSTL
# Gery Casiez - 2015

import sys, getopt
import numpy
from stl import mesh
import math

def usage():
	print 'translateRotateSTL.py -i <inputfile> -o <outputfile> -t <x>,<y>,<z> -r <x>,<y>,<z>'
	print 'Example: translateRotateSTL.py -i model.stl -t 0,50,0 -r 0,0,45'
	print 'Rotations are defined in degrees'

def main(argv):
	inputfile = ''
	outputfile = ''
	tx = 0
	ty = 0
	tz = 0
	rx = 0
	ry = 0
	rz = 0

	try:
		opts, args = getopt.getopt(argv,"hi:o:t:r:")
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			usage()
			sys.exit()
		elif opt == '-i':
			inputfile = arg
		elif opt == '-o':
			outputfile = arg
		elif opt == '-t':
			xyz = arg.split(',')
			tx = float(xyz[0])
			ty = float(xyz[1])
			tz = float(xyz[2])
		elif opt == '-r':
			xyz = arg.split(',')
			rx = float(xyz[0])
			ry = float(xyz[1])
			rz = float(xyz[2])

	your_mesh = mesh.Mesh.from_file(inputfile)

	if outputfile == '':
		outputfile = inputfile[:-4] + '-modified.stl'

	for i in range(0, len(your_mesh.vectors)):
		for j in range(0, len(your_mesh.vectors[i])):
			your_mesh.vectors[i][j] = your_mesh.vectors[i][j] + numpy.array([tx, ty, tz])

	if (rx != 0.0):
		your_mesh.rotate([1.0, 0.0, 0.0], math.radians(rx))

	if (ry != 0.0):
		your_mesh.rotate([0.0, 1.0, 0.0], math.radians(ry))

	if (rz != 0.0):
		your_mesh.rotate([0.0, 0.0, 1.0], math.radians(rz))

	your_mesh.save(outputfile)

if __name__ == "__main__":
	if (len(sys.argv) == 1):
		usage()
		exit(1)
	main(sys.argv[1:])