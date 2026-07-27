#for setting config information
import os
from pathlib import Path

def get_date(name: str) -> date:
    value = os.environ.get(name)

    if not value:
        raise RuntimeError(
            f"{name} is not set. "
            "Check ~/.config/oc/server.conf."
        )

    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise RuntimeError(
            f"{name} must be YYYY-MM-DD: {value!r}"
        ) from exc

def get_daterange() -> tuple[date, date, date]:
    date_min = get_date("OC_DATE_MIN")
    date_max = get_date("OC_DATE_MAX")
    date_default = get_date("OC_DATE_DEFAULT")

    if date_min > date_max:
        raise RuntimeError(
            "OC_DATE_MIN must not be later than OC_DATE_MAX."
        )

    if not date_min <= date_default <= date_max:
        raise RuntimeError(
            "OC_DATE_DEFAULT must be between "
            "OC_DATE_MIN and OC_DATE_MAX."
        )

    return date_min, date_max, date_default
