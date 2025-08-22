# nodelink
a peer-to-peer offline messaging tool using bluetooth for secure, direct device-to-device text communication.

## Development Status

**nodelink** development is currently **paused for Windows platforms** due to limitations with Bluetooth RFCOMM/L2CAP support:

- The `pybluez2` library **does not provide RFCOMM or L2CAP functionality on Windows 10/11**, preventing cross-platform peer-to-peer Bluetooth messaging.
- The original `PyBluez` library **supports RFCOMM on Linux**, so nodelink is fully functional on Linux environments.
- Development for Linux **will be resumed later**, leveraging PyBluez to implement full P2P messaging capabilities.
- Windows support would require either:
  - A different Bluetooth stack/library with RFCOMM/L2CAP support, or  
  - Custom native bindings to Windows Bluetooth APIs.
  
>**Note:** nodelink remains a **Linux-compatible experimental P2P Bluetooth CLI tool** until cross-platform RFCOMM support is available.
