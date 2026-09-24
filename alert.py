import time
import winsound
import threading


last_alert_time = 0

ALERT_COOLDOWN = 5


def ring_alarm():

    # Ring for 10 seconds
    winsound.Beep(1000, 10000)


def send_alert():

    global last_alert_time

    current_time = time.time()

    if current_time - last_alert_time >= ALERT_COOLDOWN:

        print("🚨 SECURITY ALERT: PERSON DETECTED!")

        # Start the alarm without freezing the camera
        alarm_thread = threading.Thread(target=ring_alarm)
        alarm_thread.start()

        last_alert_time = current_time