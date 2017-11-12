# FlowTweak
This is basically a simplified and customized TweakAtZ. It allows you to change the flow rate for a range of layers and only apply them to the skin and/or skirt.

Parameters:
- Layer Number: The first layer to apply the adjusted flow rate. Default: 1
- Number of Layers: The number of layers to apply the adjusted flow rate. Default: 2
- Change Skin Flow %: The adjusted flow rate to use for skin. Default: 80
- Change Skirt Flow %: The adjusted flow rate to use for skin. Default: 100
- Normal Flow %: The flow to use for the rest of the print. Default: 100

Note that the layer count starts at 0.

Using the default settings, the skin will be printed at 80% and the skirt be printed at 100% flow rate on the second layer.

The first couple of layers tend to glob a little on my Printrbot Simple Metal when using Cura, but the rest of the print goes well.
Reducing the flow rate on the skin on the second layer results in a much cleaner print that still adheres well to the print bed.

# Installation
Add to Cura as a post-processing script:

- Copy FlowTweak.py to C:\Program Files\Ultimaker Cura 3.0\plugins\PostProcessingPlugin\scripts (or wherever you installed Cura - prior to 3.0.4 the default was C:\Program Files\Cura 3.0\plugins\PostProcessingPlugin\scripts)
- Restart Cura

# Usage
- Load a model into Cura
- Click on Extensions -> Post Processing -> Modify G-Code
- Click Add a Script -> Flow Tweak
- Change settings as necessary
- Save gcode
- Review gcode
- Print

*Written for Cura 3.0+
