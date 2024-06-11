import time
import winsound
import tqdm
import os
import select
import sys

# Function to convert time format to seconds
def get_seconds(timer_str):
    try:
        h, m, s = map(int, timer_str.split(":"))
        return h * 3600 + m * 60 + s
    except ValueError:
        print("Invalid time format. Please enter time in the format HH:MM:SS.")
        return None

# Countdown function
def countdown(t_second, message, period_type):
    print("At any time during timer, press ---p--- to pause timer")
    while t_second:
        mins, secs = divmod(t_second, 60) 
        hours, mins = divmod(mins, 60)
        if period_type == 'work':
            timeformat = 'Work time remaining: {:02d}:{:02d}:{:02d}'.format(hours, mins, secs) 
        else:
            timeformat = 'Rest time remaining: {:02d}:{:02d}:{:02d}'.format(hours, mins, secs) 
        print(timeformat, end='\r')
        time.sleep(1)
        t_second -= 1
        if kbhit():
            key = getch()

            if key.lower() == 'p':
                input("Timer paused. Press Enter to continue...")

                #print("Remaining...")

    print(message)
    winsound.PlaySound("piano_alarm", winsound.SND_ASYNC + winsound.SND_LOOP)

def kbhit():
    """ Returns True if Keyboard character was hit, False otherwise."""
    
    if sys.platform == 'win32':
        import msvcrt
        return msvcrt.kbhit()
    else:
        import tty
        import termios
        dr, dw, de = select.select([sys.stdin], [], [], 0)
        return dr != []
    
def getch():
    """Waits for a key press and returns a single character string."""
    if sys.platform == 'win32':
        import msvcrt
        return msvcrt.getch().decode()    
    else:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

#Function to stop Alarm
def stop_alarm():

    input("Press Enter to stop the alarm.")
    winsound.PlaySound(None, winsound.SND_ASYNC)

def cycle(work_seconds, rest_seconds, cycles):
    for _ in range(cycles):
        # Running the work timer
        countdown(work_seconds, "Work Session Over. Time to rest!", 'work')
        stop_alarm()

        # Running the rest timer
        countdown(rest_seconds, "Rest Session Over. Time to get back to work!", 'rest')
        stop_alarm()

def timer_input(prompt):
    while True:
        
        time_str = input(prompt)
        seconds = get_seconds(time_str)
        if seconds is not None:
            return seconds

# Asking user for timer input in hour, minutes, and seconds
def wk_timer_rest_timer_input():
    while True:
        wk_timer = input("Set Work Timer: Enter a time to work in the format HH:MM:SS\n")
        rest_timer = input("Set Rest Timer: Enter a time to rest in the format HH:MM:SS\n")
        if get_seconds(wk_timer) is not None and get_seconds(rest_timer) is not None:
            return wk_timer, rest_timer
        else:
            print("One or both of the times were invalid. Please try again.")
            
work_time, rest_time = wk_timer_rest_timer_input()
print(f"Work Time: {work_time}, Rest Time: {rest_time}")

#Asking for number of cycle
while True:
    try:
        cycle_input = int(input("Enter number of cycle: "))
        break
    except ValueError:
        print("Please enter a valid integer for the # of cycles.")
        
# Converting time format to seconds
work_seconds = get_seconds(work_time)
rest_seconds = get_seconds(rest_time)

# Starting the Pomodoro cycles
cycle(work_seconds, rest_seconds, cycle_input)