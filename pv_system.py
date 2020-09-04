{                                                     # start configuration
  "transformers": [
    {
      "name": "<str>",
      "transformer spec ID": "<enum>",                # all of the specs are enumerated below
      "inverters": [
        {
          "name": "<str>",
          "inverter count": "<int>",
          "inverter spec ID": "<enum>",
          "layouts": [                                # number of layouts per inverter must be <= number of MPPTs
            {
              "name": "<str>",
              "thermal parameters": "<thermal model: {Uv: <float>, Uc: <float>}>",
              "row in front of PV system": "<bool>",  # is this in the middle of the system or not
              "row in back of PV system": "<bool>",   # useful for bifacial
              "number strings per row": "<int>",      # total size of layout must be a multiple of this
              "system azimuth": "<float[degrees]>",
              "module tilt": "<float[degrees]>",
              "gcr": "<float>",
              "PV module spec ID": "<enum>",          # only one module allowed per layout
              "PV modules per string": "<int>",
              "mounting type ID": "<enum>",
              "number of strings": "<int>",
              "DC collection loss": "<float[%]>",
              "etc": "<...>"
            },
            {                                         # next inverter 1 layout
              "name": "<str>",
              "etc": "<...>"
            }
        ],                                            # end inverter 1 layouts
        "AC collection loss": "<float[%]>",
        "etc": "<..>",
        },
        {                                             # next transformer 1 inverter
          "name": "<str>",
          "etc": "<...>"
        }
      ],                                              # end transformer 1 inverters
      "etc": "<...>"
    },                                                # end trasnformer 1
    {                                                 # next transformer
      "name": "<str>",
      "etc": "<...>"
    }  
  ],                                                  # end transformers
  "PV module specs": {                                # enumerate the PV module specs by ID
    "<PV module ID>": "<ModuleSpec>",
    "etc": "<...>"
  },
  "inverter specs": {                                 # enumerate the inverter specs by ID
    "<inverter ID>": "<InverterSpec>",
    "etc": "<...>"
  },
  "transformer specs": {                              # enumerate the xfmr specs by ID
    "<xfmr ID>": "<TransformerSpec>",
    "etc": "<...>"
  },
  "mounting type specs": {                            # end of configuration
    "<mounting type ID>": "<RackSpec>|<TrackerSpec>",
    "etc": "<...>"
  },
"tmy weather dat file path": "<filepath>",
"soiling per month": "<array of floats [1x12]>",
"albedo per month": "<array of floats [1x12]>",
"latitude": "<float[degrees]>",
"longitude": "<float[degrees]>",
"elevation": "<float[meters]>",
"etc": "<...>"
}                                                     # end of configuration
