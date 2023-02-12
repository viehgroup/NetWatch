<H1>Network Monitoring Tool</H1>
A basic network monitoring tool that tracks the number of established network connections and sends an email alert if the number of connections exceeds a set threshold. The tool is designed to continuously monitor network activity and provide real-time information on established connections.<br><br>

<H2>Features</H2>
Encrypted email password for added security
Threshold for number of connections can be set by the administrator
Sends an email alert if the number of established connections exceeds the set threshold
Monitors network activity continuously and provides real-time information on established connections
User-friendly and easy to use
Requirements
Python 3
psutil library
cryptography library
Installation
Clone the repository to your local machine
Install the dependencies by running the following command:
Copy code
pip install -r requirements.txt
Replace the values in the code with your own email settings and encrypted email password.
Run the script by executing the following command:
Copy code
python network_monitor.py
Configuration
The tool can be configured by changing the following values in the code:

SMTP_SERVER: The address of the SMTP server to be used to send the email alert
SMTP_PORT: The port number of the SMTP server
FROM_ADDRESS: The email address from which the alert will be sent
TO_ADDRESS: The email address to which the alert will be sent
SUBJECT: The subject of the email alert
PASSWORD: The encrypted email password
THRESHOLD: The number of established connections beyond which an email alert will be sent
SLEEP_INTERVAL: The interval (in seconds) at which the script checks for established connections
Usage
The tool will start monitoring the network activity and print the number of established connections every 5 seconds (by default). If the number of connections exceeds the set threshold, an email alert will be sent to the administrator. The tool can be stopped by pressing Ctrl + C on the keyboard.

Note
The encrypted email password provided in the code is for demonstration purposes only and should be replaced with your own encrypted password. It is recommended to encrypt the password using the cryptography library before using it in the code.

License
This network monitoring tool is open-source software licensed under the MIT License.
