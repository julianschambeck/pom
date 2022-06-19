#!/usr/bin/env python3
import time
import datetime
import os
import platform

if __name__ == "__main__":
    
    # 25 minutes in seconds.
    seconds_left = 60 * 25
    while seconds_left > 0:
        # Only print remaining time after every whole minute.
        if (seconds_left % 60) == 0:
            # Remaining time.
            timer = datetime.timedelta(seconds=seconds_left)
            # Only print minutes and seconds.
            time_left = str(timer)[2:]
            print(time_left)
        
        time.sleep(1)
        seconds_left -= 1

    # Pomodoro is over.

    # OS is Mac OSX.
    if platform.system() == "Darwin":
        title = "Pomodoro"
        message = "Pomodoro has finished. Time to take a break!"

        os.system("""
            osascript -e 'display notification "{}" with title "{}"'
            """.format(message, title))

    # OS is Linux.
    if platform.system() == "Linux":
        # TODO: Notification suitable for linux os.
        print("Linux OS here")

