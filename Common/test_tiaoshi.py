
import time

end_date = "2023-08-21"
time2 = "2023-08-18"
start_sec = time.mktime(time.strptime(time2, '%Y-%m-%d'))
end_sec = time.mktime(time.strptime(end_date, '%Y-%m-%d'))
days = int((end_sec - start_sec) / 86400)
print(days)