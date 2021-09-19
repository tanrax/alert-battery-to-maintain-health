__version__ = '1.0.0'

# Dependencies
import os
from tempfile import gettempdir
from notifypy import Notify
import psutil

# Variables
LIMIT_ABOVE_BATTERY = 85
MESSAGE_LIMIT_ABOVE_BATTERY = "Disconnect your charger, has enough 🌹"
LIMIT_BELOW_BATTERY = 15
MESSAGE_LIMIT_BELOW_BATTERY = "Connect your charger, needs energy 🥀"
FILE_NAME_TEMP = "alert_battery_to_maintain_health"
PATH_FILE_NAME_TEMP = os.path.join(gettempdir(), FILE_NAME_TEMP)


def get_sensor_battery():
    """Get object data sensor battery"""
    return psutil.sensors_battery()


def send_notification(message, title="🔋Battery🔋"):
    """Send native notification"""
    os.system(f"echo '{title}: {message}' > /dev/pts/0" 
)


def create_file_block():
    """Make temp file not repeat notification"""
    open(PATH_FILE_NAME_TEMP, 'w').close()


def get_battery_percent():
    """Gets the percentage of battery charge"""
    return int(get_sensor_battery().percent)


def is_plugged():
    """It tells you if it is charging or not."""
    return get_sensor_battery().power_plugged


if __name__ == '__main__':

    # Is battery
    if get_sensor_battery() :

        # It has not been previously warned
        if not os.path.exists(PATH_FILE_NAME_TEMP):

            # Below
            if LIMIT_BELOW_BATTERY > get_battery_percent() and not is_plugged():
                send_notification(MESSAGE_LIMIT_BELOW_BATTERY)
                create_file_block()

            # Above
            if LIMIT_ABOVE_BATTERY < get_battery_percent() and is_plugged():
                send_notification(MESSAGE_LIMIT_ABOVE_BATTERY)
                create_file_block()

        # Unlock to warned
        elif LIMIT_BELOW_BATTERY < get_battery_percent() < LIMIT_ABOVE_BATTERY:
            os.remove(PATH_FILE_NAME_TEMP)
