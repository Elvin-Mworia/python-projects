#!/usr/bin/env python3
import psutil
import time
import subprocess

# =============================
# Configuration
# =============================
THRESHOLD = 30        # Battery percentage to trigger alert
CHECK_INTERVAL = 30   # How often to check battery status (seconds)
BEEP_INTERVAL = 5     # How often to beep while low battery (seconds)
BEEP_SOUND = '/usr/share/sounds/freedesktop/stereo/dialog-warning.oga'
# =============================


def play_alert():
    """Play an alert sound."""
    subprocess.run(['paplay', BEEP_SOUND], check=False)


def main():
    print("🔋 Continuous Battery Monitor started...")
    low_battery = False

    while True:
        battery = psutil.sensors_battery()
        if battery is None:
            print("❌ No battery detected. Exiting.")
            break

        percent = battery.percent
        plugged = battery.power_plugged

        # Low battery + not plugged in → continuous beep mode
        if not plugged and percent <= THRESHOLD:
            if not low_battery:
                print(f"⚠️  Battery low ({percent}%). Starting continuous alert...")
                subprocess.run([
                    'notify-send',
                    '⚠️ Battery Low',
                    f'Battery below {THRESHOLD}%! Plug in your charger!'
                ])
                low_battery = True

            # Keep beeping every few seconds until charger is plugged in
            play_alert()
            time.sleep(BEEP_INTERVAL)
            continue

        # When plugged in or battery recovers → stop alert
        if low_battery and (plugged or percent > THRESHOLD):
            print(f"🔌 Charger connected or battery above {THRESHOLD}%. Stopping alert.")
            subprocess.run([
                'notify-send',
                '🔋 Charging',
                'Battery level safe, alert stopped.'
            ])
            low_battery = False

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
