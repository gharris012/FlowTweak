# FlowTweak
This is basically a simplified and customized TweakAtZ. It allows you to change the flow rate for a range of layers and only apply them to the skin and skirt.
Parameters:
- Layer Number: The first layer to apply the adjusted flow rate. Default: 0
- Number of Layers: The number of layers to apply the adjusted flow rate. Default: 3
- Change Flow %: The adjusted flow rate to use. Default: 90
- Normal Flow %: The flow to use for the rest of the print. Default: 100

Using the default settings, the skin and skirt sections of the first 3 layers will be printed at 90% flow rate.

The first couple of layers tend to glob a little on my Printrbot Simple Metal when using Cura, but the rest of the print goes well. Reducing the flow rate on the skin and skirt for the first few layers results in a much cleaner print.

# Installation
Add to Cura as a plugin:

- Open Cura
- Go to the Plugins tab
- Click on "Open plugin location"
- Drag FlowTweak.py into plugin location
- Restart Cura
*Written for Cura 15.02

# Todo
Future plans (might) include:
- add 'type' specific settings (such as a separate flow for Skin and Skirt).
- move 'reset' gcode placement to the end of the modified section rather than the beginning of the next one.
