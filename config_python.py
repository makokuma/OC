#for python

PLOT_CONFIG = {
    "rain": {
        "label": "降水",
        "shortName": "twatp",
        "typeOfLevel": "surface",
        "level": 0,
    },

    "temp": {
        "label": "気温(2m)",
        "shortName": "t",
        "typeOfLevel": "heightAboveGround",
        "level": 2,
    },
}

OVERLAY_CONFIG = {
    "slp_contour": {
        "label": "海面更正気圧",
        "shortName": "prmsl",
        "typeOfLevel": "meanSea",
        "level": 0,
    },

    "wind_vector": {
        "label": "地上風",
        "u_shortName": "10u",
        "v_shortName": "10v",
        "typeOfLevel": "heightAboveGround",
        "level": 10,
    },
}
