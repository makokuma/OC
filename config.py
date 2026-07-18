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

EVENT_CONFIG = {
    "kyushu_heavy_rain_2020": {
        "label": "2020年7月豪雨",
        "date": (2020, 7, 4),
        "hour": 9,
        "plot_key": "rain",
        "lat_range": (30, 36),
        "lon_range": (128, 134),
        "description": "九州地方の各地で大雨となった事例です。h",
    },
    "wide_japan_rain": {
        "label": "西日本豪雨",
        "date": (2018, 7, 6),
        "hour": 2,
        "plot_key": "rain",
        "lat_range": (20, 50),
        "lon_range": (120, 150),
        "description": "西日本の各地で記録的な大雨となった事例です。",
    },
    "heat_day": {
        "label": "猛暑の日",
        "date": (2018, 7, 23),
        "hour": 20,
        "plot_key": "temp",
        "lat_range": (30, 42),
        "lon_range": (130, 145),
        "description": "2018年に埼玉県で猛暑日となった事例です。",
    },
}
