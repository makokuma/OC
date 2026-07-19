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

    #accumulate rain
    "rain_accum_24h": {
        "label": "24時間積算降水量",
        "ctrl_grp": "fcst_sfc",
        "grads_var": "APCPsfc",
        "gxout": "shaded",
        "lat_range": (20, 50),
        "lon_range": (120, 150),
        "accum_hours": 24,
    },

    "rain_accum_6h": {
        "label": "6時間積算降水量",
        "ctrl_grp": "fcst_sfc",
        "grads_var": "APCPsfc",
        "gxout": "shaded",
        "lat_range": (20, 50),
        "lon_range": (120, 150),
        "accum_hours": 24,
    },

    "rain_accum_3h": {
        "label": "3時間積算降水量",
        "ctrl_grp": "fcst_sfc",
        "grads_var": "APCPsfc",
        "gxout": "shaded",
        "lat_range": (20, 50),
        "lon_range": (120, 150),
        "accum_hours": 24,
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
        "date": (2018, 7, 5),
        "hour": 9,
        "plot_key": "rain",
        "lat_range": (20, 50),
        "lon_range": (120, 150),
        "description": "西日本の各地で記録的な大雨となった事例です。",
    },
    "heat_day": {
        "label": "猛暑の日",
        "date": (2018, 7, 23),
        "hour": 14,
        "plot_key": "temp",
        "lat_range": (30, 42),
        "lon_range": (130, 145),
        "description": "2018年に埼玉県で猛暑日となった事例です。",
    },
}

#region tub
REGION_CONFIG = {
    "japan": {
        "label": "日本周辺",
        "lat_range": (20, 50),
        "lon_range": (120, 150),
    },
    "kyushu": {
        "label": "九州",
        "lat_range": (30, 35),
        "lon_range": (128, 133),
    },
    "kanto": {
        "label": "関東",
        "lat_range": (34, 37),
        "lon_range": (138, 141),
    },
    "kinki": {
        "label": "近畿",
        "lat_range": (33, 37),
        "lon_range": (134, 137),
    },
    "shikoku": {
        "label": "四国",
        "lat_range": (32, 34.5),
        "lon_range": (131.5, 135.5),
    },
    "hokuriku": {
        "label": "北陸",
        "lat_range": (35, 39),
        "lon_range": (135, 141),
    },
    "tohoku": {
        "label": "東北",
        "lat_range": (36.5, 42),
        "lon_range": (138.5, 142.5),
    },
    "hokkaido": {
        "label": "北海道",
        "lat_range": (41, 46),
        "lon_range": (139, 147),
    },
}
