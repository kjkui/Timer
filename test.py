import time

tm = 300
now = time.time() + tm

while True:
    CurrentTime = int(now - time.time())
    if CurrentTime <= 0:
        print("Время вышло")
        break
    time.sleep(1)