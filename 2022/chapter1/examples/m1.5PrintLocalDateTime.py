from datetime import datetime
type(datetime)

now = datetime.now()
print(now)

day = now.strftime('%x')
print(day)

time = now.strftime('%X')
print(time)
