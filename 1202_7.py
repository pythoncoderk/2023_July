from datetime import datetime, timedelta

# 時間の文字列を定義
time_str1 = "0:08:00"
time_str2 = "0:15:00"

# 文字列を時間オブジェクトに変換
time_format = "%H:%M:%S"
time1 = datetime.strptime(time_str1, time_format)
time2 = datetime.strptime(time_str2, time_format)

# 時間を足し算
result_time = time1 + timedelta(hours=time2.hour, minutes=time2.minute, seconds=time2.second)

# 結果を出力
result_time_str = result_time.strftime(time_format)
print(result_time_str)
