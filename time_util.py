#time manage tool

#input usage
#example: selected_time
from datetime import datetime, timedelta

month_list = {
        1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
        5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
        9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec",
        }

def grads_time(year, month, date, hour):
    return f"{hour:02d}z{date:02d}{month_list[month]}{year}"

#JST --> UTC
def grads_time_from_jst(year, month, day, hour_jst):
    dt_jst = datetime(year, month, day, hour_jst)
    dt_utc = dt_jst - timedelta(hours=9)

    return(
        f"{dt_utc.hour:02d}z"
        f"{dt_utc.day:02d}"
        f"{month_list[dt_utc.month]}"
        f"{dt_utc.year}"
    )
