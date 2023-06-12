# 日付表示と計算

import datetime

# 年 月 日 時 分 秒
# 2023/6/12 9:00:00
day_string = input('Y/m/d H:M:S の形式で >>> ')
day_dt = datetime.datetime.strptime(day_string, '%Y/%m/%d %H:%M:%S')

twenty_days_after = day_dt + datetime.timedelta(days=20)
print(twenty_days_after)

now = datetime.datetime.now()  # 現在の日付・時刻
today = datetime.date.today()  # 今日の日付

print(now)
print(today)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

now_time = f'{now.year}/{now.month}/{now.day} {now.hour}:{now.minute}:{now.second}'
print(now_time)

# 2023年06月12日 16時26分40秒
text = now.strftime('%Y年%m月%d日 %H時%M分%S秒')
print(text)