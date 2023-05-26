import zenoh
import time
import subprocess

def handle_new_battery_voltage(sample):
    try:
        battery_voltage = float(sample.payload)
    except:
        battery_voltage = 0.0
        print(f"Battery voltage unreadable ({sample.payload!r})")
    if battery_voltage < 9.9:       # 3.3v per cell quite a generous cutoff
        print(f"Battery dangerously low, shutting down")
        subprocess.call(["sudo", "halt"])

session = zenoh.open()

sub = session.declare_subscriber("sensors/motor1/voltage", handle_new_battery_voltage)

while True:
    time.sleep(1.0)
