# scenarios.py

from devices import Device


def smart_home():
    return [
        Device("Thermostat", 0.05, 3),
        Device("Camera", 0.1, 4),
        Device("Smart Lock", 0.07, 5),
        Device("Network", 0.2, 5)
    ]


def smart_city():
    return [
        Device("Traffic Sensor", 0.1, 4),
        Device("Street Light", 0.08, 3),
        Device("Air Sensor", 0.06, 2),
        Device("Central Network", 0.25, 5)
    ]


def industrial_iot():
    return [
        Device("PLC Controller", 0.12, 5),
        Device("Robot Arm", 0.1, 5),
        Device("Sensor Unit", 0.08, 4),
        Device("Industrial Network", 0.3, 5)
    ]