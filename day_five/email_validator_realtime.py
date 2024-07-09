import re
import dns.resolver
import smtplib

def validator(email):
    pattern = r"^(?:[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?\.)+[a-zA-Z0-9](?:[a-zA-Z0-9-]*[a-zA-Z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-zA-Z0-9-]*[a-zA-Z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)])$"
    return re.match(pattern, email) is not None

def check_mx_record(domain):
    try:
        records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(records[0].exchange)
        return mx_record
    except Exception:
        return None

def check_email_exists(email):
    domain = email.split('@')[1]
    mx_record = check_mx_record(domain)
    if not mx_record:
        return False
    
    # Connect to the mail server
    server = smtplib.SMTP()
    server.set_debuglevel(0)
    
    try:
        server.connect(mx_record)
        server.helo(server.local_hostname)  # local host name
        server.mail('test@example.com')
        code, message = server.rcpt(email)
        server.quit()
        if code == 250:
            return True
        else:
            return False
    except Exception:
        return False

while True:
    email = input("Enter your email address to validate or 'exit' to terminate: ")

    if email.lower() == "exit":
        break

    if not validator(email):
        print("Invalid email address format")
        continue

    if check_email_exists(email):
        print("Valid email address")
    else:
        print("Invalid or non-existent email address")
