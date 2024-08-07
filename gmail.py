import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email server credentials
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'guruveeraprasath322@gmail.com'
EMAIL_PASSWORD = 'gmgvp@322'
TOEMAIL_ADDRESS = 'guruveeraprasath786@gmail.com'

def generate_report():
    # Your logic to generate the report
    report = "This is a daily report."
    return report

def send_email(report):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TOEMAIL_ADDRESS  # You can also add multiple recipients
    msg['Subject'] = 'Daily Report'

    msg.attach(MIMEText(report, 'plain'))

    # Connect to the server and send the email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

def job():
    report = generate_report()
    send_email(report)

# Schedule the job every day at 8 AM
schedule.every().day.at("19:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
