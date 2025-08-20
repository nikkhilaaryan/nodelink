# Connection setup/teardown

import bluetooth

def client_mode(address: str, port: int = 3):

    """
    Attempt to connect to a remote Bluetooth device as a client.

    Args:
        address (str): The Bluetooth MAC address of the remote device.
        port (int): The RFCOMM port number (default: 3).

    Returns:
        socket.socket: A connected RFCOMM socket object if successfull.
    """
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    try:
        sock.connect((address, port))
        return sock
    except bluetooth.btcommon.BluetoothError as e:
        print(f"[ERROR]: Failed to connect to {address} on port {port} → {e}")
        sock.close()
        return None

def server_mode(port: int = 3):

    """
    Start a Bluetooth server socket and wait for a client to connect.

    Args:
        port (int): The RFCOMM port number to bind to (default: 3).

    Returns:
        tuple: (client_socket, client_info)
            - client_socket: connected RFCOMM socket object
            - client_info: tuple containing client address info
    """
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    try:
        server_sock.bind(("", port))
        server_sock.listen(1)

        print(f"[SYSTEM]: Listening for RFCOMM connections on port {port}...")
        client_sock, client_info = server_sock.accept()
        print(f"[SYSTEM]: Accepted connection from {client_info}")

        return client_sock, client_info
    except bluetooth.btcommon.BluetoothError as e:
        print(f"[ERROR]: Server failed on port {port} → {e}")
        server_sock.close()
        return None