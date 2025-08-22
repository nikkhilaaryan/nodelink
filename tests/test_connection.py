from core.connection import client_mode, server_mode
import sys

"""
Usage:
  On one laptop (server): python test_connection.py server
  On the other (client): python test_connection.py client <SERVER_BLUETOOTH_MAC>
"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_connection.py [server|client] [address_if_client]")
        sys.exit(1)

    mode = sys.argv[1].lower()

    if mode == "server":
        result = server_mode()
        if result:
            sock, client_info = result
            print(f"[TEST]: Server started, waiting for connection...")
            print(f"[TEST]: Connected with {client_info}")
            sock.close()
        else:
            print("[TEST]: Server failed.")

    elif mode == "client":
        if len(sys.argv) < 3:
            print("Usage: python test_connection.py client <SERVER_BLUETOOTH_MAC>")
            sys.exit(1)

        address = sys.argv[2]
        sock = client_mode(address)
        if sock:
            print(f"[TEST]: Connected to server at {address}")
            sock.close()
        else:
            print("[TEST]: Client failed to connect.")
