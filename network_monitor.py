import psutil
import time
import smtplib
import base64
import os
from cryptography.fernet import Fernet

# Threshold for number of connections
connection_threshold = 100

# Email notification settings
email_recipient = 'recipient@example.com'
email_sender = 'sender@example.com'

def get_email_password():
    # Encrypted email password
    encrypted_email_password = b'gAAAAABcKj7VuLX9z35-Vr-vqqdP_o0aZJjKq3p4I4-5y5b5G9f5K2S5SzwJQZBlOPhlKlCgpm1jK6-Jy6_9d6OmpU6exYUw=='

    # Decrypt the encrypted email password
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    email_password = cipher_suite.decrypt(encrypted_email_password)
    return email_password.decode('utf-8')

def send_email_alert(subject, message):
    email_password = get_email_password()
    email_server = 'smtp.example.com'
    email_port = 587
    try:
        smtp_server = smtplib.SMTP(email_server, email_port)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(email_sender, email_password)
        smtp_server.sendmail(email_sender, email_recipient,
                             f'Subject: {subject}\n\n{message}')
        smtp_server.quit()
        print(f'Successfully sent email alert to {email_recipient}')
    except Exception as e:
        print(f'Failed to send email alert: {e}')

def monitor_network():
    print("Monitoring network activity...")
    while True:
        # Get the list of network connections
        connections = psutil.net_connections()

        # Count the number of established connections
        established_count = 0
        for connection in connections:
            if connection.status == 'ESTABLISHED':
                established_count += 1

        # Check if the number of established connections is greater than the threshold
        if established_count > connection_threshold:
            subject = "High number of established connections alert"
            message = f"The number of established connections is currently at {established_count}. This is above the threshold of {connection_threshold}."
            print(f"Number of established connections: {established_count}")
            print("Warning: High number of established connections!")
            send_email_alert(subject, message)
        else:
            print(f"Number of established connections: {established_count}")

        # Wait for 5 seconds before checking again
        time.sleep(5)

if __name__ == '__main__':
    monitor_network()
