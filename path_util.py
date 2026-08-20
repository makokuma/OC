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

def get_dset_from_ctl(ctl_path: Path) -> str:
    with ctl_path.open() as f:
        for line in f:
            line = line.strip()

            if line.lower().startswith("dset "):
                return line.split(maxsplit=1)[1]

    raise ValueError(f"dset not found: {ctl_path}")


def resolve_dset_path(ctl_path: Path) -> Path:
    dset = get_dset_from_ctl(ctl_path)

    # CTL基準の相対パス
    if dset.startswith("^"):
        return ctl_path.parent / dset[1:]

    path = Path(dset)

    # 絶対パス
    if path.is_absolute():
        return path

    raise ValueError(f"Unsupported relative dset: {dset}")
