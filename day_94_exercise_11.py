# ***drink water reminder***
"""
time: This module works with the time object and is installed by default
Plyer: Plyer module is used to access the features of the hardware. This module does not comes built-in with Python.
 We need to install it externally.
 Step 1) Import the notification class from the plyer module
  step2)After that you just need to call the notify method of this class.
Syntax: notify(title=”, message=”, app_name=”, app_icon=”, timeout=10, ticker=”, toast=False)

Parameters:
=>title (str) – Title of the notification
=>message (str) – Message of the notification
=>app_name (str) – Name of the app launching this notification
=>app_icon (str) – Icon to be displayed along with the message
=>timeout (int) – time to display the message for, defaults to 10
=>ticker (str) – text to display on status bar as the notification arrives
=>toast (bool) – simple Android message instead of full notification

Step 3) Add the sleep function to show that notification again.
"""
import time
from plyer import notification




