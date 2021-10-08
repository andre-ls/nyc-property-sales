config_point = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "x1e71e",
          "type": "point",
          "config": {
            "dataId": "NY Properties",
            "label": "Properties",
            "color": [
              201,
              0,
              0
            ],
            "columns": {
              "lat": "Y Coordinate",
              "lng": "X Coordinate",
              "altitude": None
            },
            "isVisible": True,
            "visConfig": {
              "radius": 10,
              "fixedRadius": False,
              "opacity": 0.8,
              "outline": False,
              "thickness": 2,
              "strokeColor": None,
              "colorRange": {
                "name": "Uber Viz Diverging 1.5",
                "type": "diverging",
                "category": "Uber",
                "colors": [
                  "#00939C",
                  "#5DBABF",
                  "#BAE1E2",
                  "#F8C0AA",
                  "#DD7755",
                  "#C22E00"
                ]
              },
              "strokeColorRange": {
                "name": "Global Warming",
                "type": "sequential",
                "category": "Uber",
                "colors": [
                  "#5A1846",
                  "#900C3F",
                  "#C70039",
                  "#E3611C",
                  "#F1920E",
                  "#FFC300"
                ]
              },
              "radiusRange": [
                0,
                50
              ],
              "filled": True
            },
            "hidden": False,
            "textLabel": [
              {
                "field": {
                  "name": "Sale Price",
                  "type": "real"
                },
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 13,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": None,
            "colorScale": "quantile",
            "strokeColorField": None,
            "strokeColorScale": "quantile",
            "sizeField": None,
            "sizeScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "NY Properties": [
              {
                "name": "Address",
                "format": None
              },
              {
                "name": "Gross Square Feet",
                "format": None
              },
              {
                "name": "Building Class Category",
                "format": None
              }
            ]
          },
          "compareMode": False,
          "compareType": "absolute",
          "enabled": True
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": -7.114285714285717,
      "dragRotate": True,
      "latitude": 40.66392735209681,
      "longitude": -74.00693389551695,
      "pitch": 48.87078527062999,
      "zoom": 10.106531408747953,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "muted_night",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}

config_hex = {
  "version": "v1",
  "config": {
    "visState": {
      "filters": [],
      "layers": [
        {
          "id": "s0dqf6q",
          "type": "hexagon",
          "config": {
            "dataId": "NY Properties",
            "label": "Properties",
            "color": [
              201,
              0,
              0
            ],
            "columns": {
              "lat": "Y Coordinate",
              "lng": "X Coordinate"
            },
            "isVisible": True,
            "visConfig": {
              "opacity": 0.8,
              "worldUnitSize": 1,
              "resolution": 8,
              "colorRange": {
                "name": "Uber Viz Diverging 1.5",
                "type": "diverging",
                "category": "Uber",
                "colors": [
                  "#00939C",
                  "#5DBABF",
                  "#BAE1E2",
                  "#F8C0AA",
                  "#DD7755",
                  "#C22E00"
                ]
              },
              "coverage": 1,
              "sizeRange": [
                0,
                500
              ],
              "percentile": [
                0,
                100
              ],
              "elevationPercentile": [
                0,
                100
              ],
              "elevationScale": 17.5,
              "colorAggregation": "average",
              "sizeAggregation": "average",
              "enable3d": True
            },
            "hidden": False,
            "textLabel": [
              {
                "field": {
                  "name": "Sale Price",
                  "type": "real"
                },
                "color": [
                  255,
                  255,
                  255
                ],
                "size": 13,
                "offset": [
                  0,
                  0
                ],
                "anchor": "start",
                "alignment": "center"
              }
            ]
          },
          "visualChannels": {
            "colorField": {
              "name": "Sale Price",
              "type": "real"
            },
            "colorScale": "quantile",
            "sizeField": {
              "name": "Sale Price",
              "type": "real"
            },
            "sizeScale": "linear"
          }
        }
      ],
      "interactionConfig": {
        "tooltip": {
          "fieldsToShow": {
            "NY Properties": []
          },
          "compareMode": False,
          "compareType": "relative",
          "enabled": False
        },
        "brush": {
          "size": 0.5,
          "enabled": False
        },
        "geocoder": {
          "enabled": False
        },
        "coordinate": {
          "enabled": False
        }
      },
      "layerBlending": "normal",
      "splitMaps": [],
      "animationConfig": {
        "currentTime": None,
        "speed": 1
      }
    },
    "mapState": {
      "bearing": -7.114285714285717,
      "dragRotate": True,
      "latitude": 40.66392735209681,
      "longitude": -74.00693389551695,
      "pitch": 48.87078527062999,
      "zoom": 10.106531408747953,
      "isSplit": False
    },
    "mapStyle": {
      "styleType": "muted_night",
      "topLayerGroups": {},
      "visibleLayerGroups": {
        "label": True,
        "road": True,
        "border": False,
        "building": True,
        "water": True,
        "land": True,
        "3d building": False
      },
      "threeDBuildingColor": [
        9.665468314072013,
        17.18305478057247,
        31.1442867897876
      ],
      "mapStyles": {}
    }
  }
}