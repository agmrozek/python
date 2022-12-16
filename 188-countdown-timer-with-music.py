import sys
import time

from playsound import playsound  # on Mac this requires PyObjC


def countdown(seconds: int) -> None:
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f'{mins:02}:{secs:02}', end="\r")
        time.sleep(1)
        seconds -= 1
    print("00:00", end="\r")
    playsound('alarm.mp4')


if __name__ == '__main__':
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        script = sys.argv[0]
        print(f"Usage: {script} <minutes_till_alarm:int>")
        sys.exit()

    seconds = int(sys.argv[1]) * 60
    countdown(seconds)