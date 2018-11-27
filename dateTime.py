# coding:utf-8

# 获取当前日期和时间
from datetime import datetime
now = datetime.now()
print(now)

# 获取指定日期和时间
dt = datetime(2015, 3, 19, 12, 20, 21)
print(dt)

# 将日期和时间以数字表示（即将datetime转换为timestamp）
dt1 = datetime(2015, 3, 19, 12, 20, 21)
print(dt1.timestamp())
# 将timestamp转换为datetime
dt2 = 1426738821.0
print(datetime.fromtimestamp(dt2))

# 将字符串日期，转换为datetime
s1 = '2018-02-20 18:19:20'
print(datetime.strptime(s1, '%Y-%m-%d %H:%M:%S'))

# 将datetime转换成str（通过导入datetime导入）
now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
# 通过导入time将datetime转换成str
import time
print(time.strftime("%Y%m%d-%H%M%S", time.localtime()))


# datetime加减
from datetime import timedelta
print(now + timedelta(hours=2))
print(now - timedelta(days=1))
print(now - timedelta(days=1, hours=3))

# 把时间从UTC+0时区转换为UTC+8
from datetime import timezone
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('UTC+0:00 now = ', utc_dt)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+8:00 now =', utc8_dt)