#Name: GH Tweaks
#Info: My customizations - Change Flow % on skin for the specified layers
#Depend: GCode
#Type: postprocess
#Param: startL(int:0) Layer no. to start
#Param: twLayers(int:3) No. of layers to change
#Param: twFlow(int:90) Change Flow %
#Param: defFlow(int:100) Default/Normal Flow %

startL = int(startL)
twLayers = int(twLayers)
twFlow = int(twFlow)
defFlow = int(defFlow)

modFlow = False
currentLayer = 0

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
					f.write("; Params twFlow: %s %i\n" % (type(twFlow), twFlow))
					f.write("; Params defFlow: %s %i\n" % (type(defFlow), defFlow))

			if currentLayer >= startL and currentLayer < ( startL + twLayers ):
				if line.startswith(";TYPE:SKIN"):  #Enable flow tweaks on SKIN type only
					f.write("; GH Tweaks - Print Layers %i-%i (+%i) at %i%%\n" % ( startL, (startL+twLayers), twLayers, twFlow))
					f.write("M221 T0 S%f\n" % (twFlow))
					modFlow = True

			if line.startswith(";TYPE:") and not line.startswith(";TYPE:SKIN") and modFlow == True:  #Restore default flow for other types
				f.write("; GH Tweaks - Print Layers %i-%i (+%i) at (%i)%% -- reset to %i\n" % ( startL, (startL+twLayers), twLayers, twFlow, defFlow ))
				f.write("M221 T0 S%f\n" % (defFlow))
				modFlow = False

			if currentLayer == ( startL + twLayers ) and modFlow == True:
				f.write("; GH Tweaks - Print Layers %i-%i (+%i) at (%i)%% -- reset to %i\n" % ( startL, (startL+twLayers), twLayers, twFlow, defFlow ))
				f.write("M221 T0 S%f\n" % (defFlow))
				modFlow = False
