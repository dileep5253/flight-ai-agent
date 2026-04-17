import smtplib
from email.mime.text import MIMEText


def send_email(receiver_email, airline, price):
    # 🔹 Your Gmail (must match app password account)
    sender_email = "your_email@gmail.com"
    
    # 🔹 App Password (16 characters, no spaces)
    password = "ujpzmughkvoerquc"

    # 🔹 Email content
    body = f"""
Flight Booking Confirmation

Airline: {airline}
Price: ₹{price}

Status: CONFIRMED
PNR: AI12345
"""

    # 🔹 Create message
    msg = MIMEText(body)
    msg['Subject'] = "Flight Ticket Confirmation"
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        # 🔹 Connect to Gmail SMTP
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.ehlo()

        # 🔹 Login
        server.login(sender_email, password)

        # 🔹 Send mail
        server.send_message(msg)
        server.quit()

        print("✅ Email sent successfully")

    except smtplib.SMTPAuthenticationError:
        print("❌ Authentication failed → Check App Password / Gmail")
    
    except Exception as e:
        print("❌ Error:", e)