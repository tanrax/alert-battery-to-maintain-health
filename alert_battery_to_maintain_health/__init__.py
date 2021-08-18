__version__ = '0.1.0'

from notifypy import Notify
import psutil

if __name__ == '__main__':
    # Variables
    battery = psutil.sensors_battery()

    if battery:
        notification = Notify()
        notification.title = "Cool Title"
        notification.message = "Even cooler message."
        notification.send()

        print(battery)
        plugged = battery.power_plugged
        percent = str(battery.percent)
        plugged = "Plugged In" if plugged else "Not Plugged In"
        print(percent+'% | '+plugged)

