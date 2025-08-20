from dataclasses import dataclass
import bluetooth  # from PyBluez

@dataclass
class BluetoothDevice:
    name: str
    address: str

def scan_bluetooth_devices(scan_timeout: int = 10) -> list[BluetoothDevice]:
    """
    Discover nearby Classic Bluetooth devices using PyBluez.

    Args:
        scan_timeout (int): Duration of the scan in seconds.

    Returns:
        list[BluetoothDevice]: List of discovered devices.
    """
    devices = bluetooth.discover_devices(duration=scan_timeout, lookup_names=True)
    result: list[BluetoothDevice] = []

    for addr, name in devices:
        device_name = name or "Unidentified Device"
        result.append(BluetoothDevice(device_name, addr))

    return result
