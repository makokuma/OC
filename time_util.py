#time manage tool

#input usage
#example: selected_time

def grads_time(year, month, date, hour):
    month_list = {
            1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
            5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
            9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec",
            }

    return f"{hour:02d}z{date:02d}{month_list[month]}{year}"


