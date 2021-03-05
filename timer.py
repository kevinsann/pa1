import time

def create_countdown_timer(time):
    print(time,"......")

time_in_sec=3

def display():
    for times in range(time_in_sec):
        create_countdown_timer(time_in_sec-times)
        time.sleep(1)

    print("Computer has moved.")
