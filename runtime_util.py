#for setting config information
import os
from pathlib import Path

def get_daterange():
    value1 = os.environ.get("OC_DATE_MIN")
    value2 = os.environ.get("OC_DATE_MAX")
    value3 = os.environ.get("OC_DATE_DEFAULT")

    return value1, value2, value3

def parse_date(value):
    YY = value[0:4]
    MM = value[5:7]
    DD = value[8:10]

    return YY, MM, DD

