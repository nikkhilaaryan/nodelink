# Connection setup/teardown
# core/connection.py
import bluetooth

def client_mode(address: str, psm: int = 0x1001):
    """
    Connect to a remote Bluetooth device using L2CAP (Windows-friendly).

    Args:
        address (str): The Bluetooth MAC address of the remote device.
        psm (int): The L2CAP PSM to connect to (default: 0x1001).

    Returns:
        socket.socket: Connected L2CAP socket if successful, else None.
    """
    sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)

    try:
        sock.connect((address, psm))
        return sock
    except bluetooth.btcommon.BluetoothError as e:
        print(f"[ERROR]: Failed to connect to {address} on PSM {psm} → {e}")
        sock.close()
        return None

def server_mode(psm: int = 0x1001):
    """
    Start a Bluetooth server socket and wait for a client to connect (Windows).

    Args:
        psm (int): The L2CAP PSM to bind to (default: 0x1001).

    Returns:
        tuple: (client_socket, client_info) if successful, else None.
    """
    server_sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)

    try:
        server_sock.bind(("00:00:00:00:00:00", psm))
        server_sock.listen(1)

        print(f"[SYSTEM]: Listening for L2CAP connections on PSM {psm}...")
        client_sock, client_info = server_sock.accept()
        print(f"[SYSTEM]: Accepted connection from {client_info}")

        return client_sock, client_info
    except bluetooth.btcommon.BluetoothError as e:
        print(f"[ERROR]: Server failed on PSM {psm} → {e}")
        server_sock.close()
        return None
