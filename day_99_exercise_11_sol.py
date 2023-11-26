import time

from plyer import notification

# REPEAT_INTERVAL=10
# notification.notify(
#     title = 'REMINDER',
#     message = 'drink water',
#     # app_icon = None,
#     timeout = 5,
#     # time.sleep(REPEAT_INTERVAL)
# )
reminder_time=float(input("input the remider time"))
while (True):
    time.sleep(reminder_time)
    notification.notify(title="REMINDER",
                        message="please drink water",
                        timeout=3)