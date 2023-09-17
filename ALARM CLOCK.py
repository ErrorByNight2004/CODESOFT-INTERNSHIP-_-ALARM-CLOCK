import datetime
import time
import winsound  # For playing sound on Windows

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now()
        if current_time >= alarm_time:
            print("Time to wake up!")
            play_alarm_sound()
            break
        time.sleep(60)  # Check every minute

def play_alarm_sound():
    frequency = 2500  # Frequency in Hertz
    duration = 3000  # Duration in milliseconds
    winsound.Beep(frequency, duration)

def main():
    try:
        alarm_hour = int(input("Enter the hour for the alarm (0-23): "))
        alarm_minute = int(input("Enter the minute for the alarm (0-59): "))

        if alarm_hour < 0 or alarm_hour > 23 or alarm_minute < 0 or alarm_minute > 59:
            print("Invalid input. Please enter a valid time.")
            return

        alarm_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, 
                            datetime.datetime.now().day, alarm_hour, alarm_minute)
        set_alarm(alarm_time)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
    