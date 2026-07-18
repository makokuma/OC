#config

PLOT_CONFIG = {
    #rain
    "rain": {
        "label": "降水",
        "ctrl_grp": "fcst_sfc", #fcst_sfc anl_sfc, fcst_p, anl_p
        "grads_var": "APCPsfc",
        "gxout": "shaded",
        "lat_range": (20, 50),
        "lon_range": (120, 150),
    },

    #temperature
    "temp": {
        "label": "気温(2m)",
        "ctrl_grp": "fcst_sfc", #fcst_sfc anl_sfc, fcst_p, anl_p
        "grads_var": "TMP2m",
        "gxout": "shaded",
        "lat_range": (20, 50),
        "lon_range": (120, 150),
    },

    #wind

    #pressure
    "prs": {
        "label": "海面更正気圧",
        "ctrl_grp": "fcst_sfc", #fcst_sfc anl_sfc, fcst_p, anl_p
        "grads_var": "PRMSLmsl",
        "gxout": "shaded",
        "lat_range": (20, 50),
        "lon_range": (120, 150),
    },
}

