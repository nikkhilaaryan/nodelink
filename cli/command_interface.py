import time
from unittest import result
from core.discovery import scan_bluetooth_devices
from core.connection import client_mode, server_mode

def main_command_interface():
    while True:
        print("\nnodelink Command Interface")
        print("1. Initiate Device Scan")
        print("2. Establish Secure Bluetooth Link")
        print("3. Standby for Incoming Transmission")
        print("4. Terminate NodeLink Session")

        choice = input("Confirm Selection ID: ")

        if choice == "1":
            print("[SYSTEM]: Initiating Bluetooth scan. Please wait.")

            bluetooth_devices = scan_bluetooth_devices()

            if not bluetooth_devices:
                print("[ALERT]: No Bluetooth devices discovered. Please ensure Bluetooth is enabled and try again.")
            else:
                # Blinking effect
                print("[SYSTEM]: Scanning", end="", flush=True)
                for _ in range(5):  
                    print(".", end="", flush=True)
                    time.sleep(0.5)
                    print("\b \b", end="", flush=True)
                    time.sleep(0.5)

                print("\n[SYSTEM]: Discovered Bluetooth devices:")
                for idx, device in enumerate(bluetooth_devices, 1):
                    print(f"  - {idx}. {device.name} ({device.address})")

        elif choice == "2":
            #client_mode
            address = input("Enter the Bluetooth MAC address of the remote device: ")
            print(f"[SYSTEM]: Attempting to connect to {address}.")
            sock = client_mode(address)
            if sock:
                print("[SYSTEM]: Connection Established (placeholder).")

            else: 
                print("[ALERT]: Connection Failed (placeholder).")

        elif choice == "3":
            #server_mode
            print("[SYSTEM]: Attempting to start server.")
            time.sleep(3)
            print("[SYSTEM]: Waiting for the incoming Bluetooth connection.")
            result= server_mode()
            if result:
                sock, client_info = result
                print(f"[SYSTEM]: Channel established with {client_info} (placeholder).")
            else:
                print("[ALERT]: Failed to establish channel (placeholder).")

        elif choice == "4":
            print("[SYSTEM]: Terminating NodeLink Session.")
            break

        else:
            print("[ALERT]: Invalid Selection. Try again.")
