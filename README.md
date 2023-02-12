<H1>Network Monitoring Tool</H1>
A basic network monitoring tool that tracks the number of established network connections and sends an email alert if the number of connections exceeds a set threshold. The tool is designed to continuously monitor network activity and provide real-time information on established connections.<br><br>

<H2>Features</H2>
-> Encrypted email password for added security<br>
-> Threshold for number of connections can be set by the administrator<br>
-> Sends an email alert if the number of established connections exceeds the set threshold<br>
-> Monitors network activity continuously and provides real-time information on established connections<br>
-> User-friendly and easy to use<br><br>

<H2>Requirements</H2>
-> Python 3<br>
-> psutil library<br>
-> cryptography library<br><br>
<H2>Installation</H2>
1. Clone the repository to your local machine<br>
2. Install the dependencies by running the following command:<br>
pip install -r requirements.txt<br>
3. Replace the values in the code with your own email settings and encrypted email password.<br>
4. Run the script by executing the following command:<br>
python network_monitor.py<br><br>
<H2>Configuration</H2>
The tool can be configured by changing the following values in the code:<br>

-> SMTP_SERVER: The address of the SMTP server to be used to send the email alert<br>
-> SMTP_PORT: The port number of the SMTP server<br>
-> FROM_ADDRESS: The email address from which the alert will be sent<br>
-> TO_ADDRESS: The email address to which the alert will be sent<br>
-> SUBJECT: The subject of the email alert<br>
-> PASSWORD: The encrypted email password<br>
-> THRESHOLD: The number of established connections beyond which an email alert will be sent<br>
-> SLEEP_INTERVAL: The interval (in seconds) at which the script checks for established connections<br><br>
<H2>Usage</H2>
The tool will start monitoring the network activity and print the number of established connections every 5 seconds (by default). If the number of connections exceeds the set threshold, an email alert will be sent to the administrator. The tool can be stopped by pressing Ctrl + C on the keyboard.<br>

<H1>Note</H1>
The encrypted email password provided in the code is for demonstration purposes only and should be replaced with your own encrypted password. It is recommended to encrypt the password using the 'cryptography' library before using it in the code.<br>
