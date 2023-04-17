import schedule
import time
from datetime import datetime


def tarefa():
    print("Estou ocupado! Volte mais tarde")
    print(datetime.now())


schedule.every(2).seconds.do(tarefa)

while True:
    schedule.run_pending()
    time.sleep(1)