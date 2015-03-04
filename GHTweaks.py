#Name: GH Tweaks
#Info: My customizations
#Depend: GCode
#Type: postprocess
#Param: startL(int:0) Layer no. to start
#Param: twLayers(int:3) No. of layers to change
#Param: twFill(int:90) Change Fill %
#Param: defFill(int:100) Default/Normal Fill %

startL = int(startL)
twLayers = int(twLayers)
twFill = int(twFill)
defFill = int(defFill)

with open(filename, "r") as f:
	lines = f.readlines()

with open(filename, "w") as f:

	for lIndex in xrange(len(lines)):
		line = lines[lIndex]

		f.write(line)

		if line.startswith(';'):
			if line.startswith(';LAYER:'):
				currentLayer = int(line[7:].strip())

				if currentLayer == 0:
					f.write("; GH Tweaks\n")
					f.write("; Params startL: %s %i\n" % (type(startL), startL))
					f.write("; Params twLayers: %s %i\n" % (type(twLayers), twLayers))
					f.write("; Params twFill: %s %i\n" % (type(twFill), twFill))
					f.write("; Params defFill: %s %i\n" % (type(defFill), defFill))

				if currentLayer >= startL and currentLayer < ( startL + twLayers ):
					f.write("; GH Tweaks - Print Layers %i-%i (+%i) at %i%%\n" % ( startL, (startL+twLayers), twLayers, twFill))
					f.write("M221 T0 S%f\n" % (twFill))

				if currentLayer == ( startL + twLayers ):
					f.write("; GH Tweaks - Print Layers %i-%i (+%i) at (%i)%% -- reset to %i\n" % ( startL, (startL+twLayers), twLayers, twFill, defFill ))
					f.write("M221 T0 S%f\n" % (defFill))
