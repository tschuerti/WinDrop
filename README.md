![WinDrop](https://raw.githubusercontent.com/tschuerti/WinDrop/refs/heads/main/logo.png)

WinDrop is a simple Flask application that allows you to transfer URLs, text, and media files to your Windows machine via HTTP requests.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using pip:
    ```sh
    pip install flask
    ```
3. Run the application:
    ```sh
    python main.py
    ```

4. Install the following shortcut on your iOS device to easily send data to your Windows machine:
    [iCloud Shortcut](https://www.icloud.com/shortcuts/dbd1977c628040b6a1c62d7a387cc59b)

## Usage

1. Run the application on your Windows machine.
2. Run the iCloud Shortcut on your iOS
3. Enter the IP address of your Windows machine and the port number (default is 5000).
4. Add to sharefeed in Shortcuts
5. Share anything and select WinDrop

## License
Distributed under the MIT License. See `LICENSE` for more information.