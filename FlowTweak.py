#Name: FlowTweak
#Info: Change Flow % on skin/skirt over a range of layers

from ..Script import Script

class FlowTweak(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name":"Flow Tweak",
            "key": "FlowTweak",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "start_layer":
                {
                    "label": "Start Layer",
                    "description": "Layer no. to start",
                    "unit": "",
                    "type": "int",
                    "default_value": 0
                },
                "layer_count":
                {
                    "label": "Layer Count",
                    "description": "Number of layers to apply flow rate change",
                    "unit": "",
                    "type": "int",
                    "default_value": 2
                },
                "skin_flow_rate":
                {
                    "label": "Skin Flow %",
                    "description": "Flow rate when printing Skin",
                    "unit": "%",
                    "type": "int",
                    "default_value": 80
                },
                "skirt_flow_rate":
                {
                    "label": "Skirt Flow %",
                    "description": "Flow rate when printing Skirt",
                    "unit": "%",
                    "type": "int",
                    "default_value": 100
                },
                "default_flow_rate":
                {
                    "label": "Default Flow %",
                    "description": "Flow rate when printing anything else",
                    "unit": "%",
                    "type": "int",
                    "default_value": 100
                }
            }
        }"""

    def execute(self, data: list):

        """data is a list. Each index contains a layer"""

        currentLayer = 0
        startL = self.getSettingValueByKey("start_layer")
        twLayers = self.getSettingValueByKey("layer_count")
        twSkinFlow = self.getSettingValueByKey("skin_flow_rate")
        twSkirtFlow = self.getSettingValueByKey("skirt_flow_rate")
        defFlow = self.getSettingValueByKey("default_flow_rate")

        modFlow = False

        myfile = open("C:\\Users\\gharr_000\\Documents\\GitHub\\FlowTweak\\tw.log", "w")
        myfile.write("Processing...\n")

        for layer in data:
            lines = layer.split("\n")
            index = data.index(layer)
            myfile.write("Processing layer index %i\n" % (index))
            modified_gcode = ""
            for line in lines:
                prepend_gcode = ""
                if line.startswith(';'):
                    if ";Generated with Cura_SteamEngine" in line:
                        prepend_gcode += "; FlowTweak\n"
                        prepend_gcode += "; Params startL: %i\n" % (startL)
                        prepend_gcode += "; Params twLayers: %i\n" % (twLayers)
                        prepend_gcode += "; Params twSkinFlow: %i\n" % (twSkinFlow)
                        prepend_gcode += "; Params twSkirtFlow: %i\n" % (twSkirtFlow)
                        prepend_gcode += "; Params defFlow: %i\n" % (defFlow)

                    if line.startswith(';LAYER:'):
                        currentLayer = int(line[7:].strip())
                        myfile.write("Found layer %i\n" % (currentLayer))

                        if currentLayer == 0:
                            # start off at default flow rate
                            prepend_gcode += "; FlowTweak - Print Layers %i-%i at Skin:%i%%/Skirt:%i%% -- start at %i%%\n" % ( startL, (startL+twLayers), twSkinFlow, twSkirtFlow, defFlow )
                            prepend_gcode += "M221 T0 S%f\n" % (defFlow)

                    if currentLayer >= startL and currentLayer < ( startL + twLayers ):
                        if line.startswith(";TYPE:SKIN"):  #Enable flow tweaks on SKIN type only
                            prepend_gcode += "; FlowTweak - Reduce SKIN flow to %i%%\n" % (twSkinFlow)
                            prepend_gcode += "M221 T0 S%f\n" % (twSkinFlow)
                            modFlow = True

                        if line.startswith(";TYPE:SKIRT"):  #Enable flow tweaks on SKIRT type only
                            prepend_gcode += "; FlowTweak - Reduce SKIRT flow to %i%%\n" % (twSkirtFlow)
                            prepend_gcode += "M221 T0 S%f\n" % (twSkirtFlow)
                            modFlow = True

                    if line.startswith(";TYPE:") and not ( line.startswith(";TYPE:SKIN") or line.startswith(";TYPE:SKIRT") ) and modFlow == True:  #Restore default flow for other types
                        prepend_gcode += "; FlowTweak - Reset flow to %i%%\n" % (defFlow)
                        prepend_gcode += "M221 T0 S%f\n" % (defFlow)
                        modFlow = False

                    if currentLayer == ( startL + twLayers ) and modFlow == True:
                        prepend_gcode += "; FlowTweak - Reset flow to %i%%\n" % (defFlow)
                        prepend_gcode += "M221 T0 S%f\n" % (defFlow)
                        modFlow = False
                modified_gcode += prepend_gcode + line + "\n"

            if modFlow:
                # reset to default flow at the end of the layer
                modified_gcode += "; FlowTweak - Reset flow to %i%%\n" % (defFlow)
                modified_gcode += "M221 T0 S%f\n" % (defFlow)
                modFlow = False

            layer = modified_gcode
            data[index] = layer

        myfile.close()

        return data
