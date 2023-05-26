from ina219 import INA219
from ina219 import DeviceRangeError
import time
import zenoh
import os

class PowerMonitor:
    def __init__(self, session, name, shunt, address):
        self.name = name
        self.ina = INA219(shunt, address=address)
        self.ina.configure()
        self.pub_current = session.declare_publisher(os.path.join("sensors", name, "current"))
        self.pub_voltage = session.declare_publisher(os.path.join("sensors", name, "voltage"))

    def pub(self):
        self.pub_voltage.put(f"{self.ina.voltage():5.3f}")
        try:
            self.pub_current.put(f"{self.ina.current():5.3f}")
        except DeviceRangeError:
            self.pub_current.put(f"high")

session = zenoh.open()

m1_mon = PowerMonitor(session, "motor1", 0.001, 0x41)
m2_mon = PowerMonitor(session, "motor2", 0.001, 0x42)
pi_mon = PowerMonitor(session, "rpi", 0.1, 0x40)

while True:
    m1_mon.pub()
    m2_mon.pub()
    pi_mon.pub()
    time.sleep(0.1)

