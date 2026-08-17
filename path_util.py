import os
from pathlib import Path


def get_data_root() -> Path:
    value = os.environ.get("OC_DATA_ROOT")

    if not value:
        raise RuntimeError(
            "OC_DATA_ROOT is not set. "
            "Check ~/.config/oc/server.conf."
        )

    return Path(value).expanduser()


def get_ctl_path(yyyy: int, mm: int, ctrl_grp: str) -> Path:
    data_year = yyyy if mm in {7, 8, 9, 10, 11, 12} else yyyy - 1

    return (
        get_data_root()
        / str(data_year)
        / f"{ctrl_grp}_LL.ctl"
    )

def get_grib_path(yyyy: int, mm: int, dd:int, hh:int ctrl_grp: str) -> Path:
    data_year = yyyy if mm in {7, 8, 9, 10, 11, 12} else yyyy - 1

    return (
        get_data_root()
        / str(data_year)
        / ctrl
        / f"{ctrl_grp}_{yyyy}{mm}{dd}{hh}00.grib2"
