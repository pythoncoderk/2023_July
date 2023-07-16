import psutil
print(psutil.cpu_times())

for i in range(3):
    psutil.cpu_times_percent(interval=1, percpu=False)