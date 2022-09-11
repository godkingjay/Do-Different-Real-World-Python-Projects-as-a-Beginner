# import psutil
import psutil

CPU = psutil.cpu_count()

print(CPU)

while True:
    CPU_Percent = psutil.cpu_percent(1)
    print(CPU_Percent)