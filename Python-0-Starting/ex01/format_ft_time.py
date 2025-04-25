import time

seconds_since_epoch = time.time()

current_time = time.localtime(seconds_since_epoch)
month = time.strftime("%b", current_time)
day = time.strftime("%d", current_time)
year = time.strftime("%Y", current_time)
date_format = f"{month} {day} {year}"

print(f"Seconds since January 1, 1970: {seconds_since_epoch:,.4f} or {seconds_since_epoch:.2e} in scientific notation")
print(date_format)
