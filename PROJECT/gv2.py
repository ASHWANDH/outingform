import fpdf
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def fill_pdf(pdf_file, data):
    # create PDF object
    pdf = fpdf.FPDF()
    pdf.add_page()
    # add text to the PDF
    for key, value in data.items():
        pdf.set_font("Arial", style='U', size=14)
        pdf.cell(190, 10, txt=key, ln=1, align="L")
        pdf.set_font("Arial", size=12)
        pdf.cell(190, 10, txt=value, ln=1, align="L")
    # save PDF
    pdf.output(pdf_file, "F")

def send_email(pdf_file, recipient, sender, password):
    # create message object
    msg = MIMEMultipart()
    # add PDF as attachment
    with open(pdf_file, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={pdf_file}")
    msg.attach(part)
    # add recipient, sender, and subject
    msg["To"] = recipient
    msg["From"] = sender
    msg["Subject"] = "PDF document"
    # send email
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(msg)

# get data from user
data = {}
keys = ["Name", "Age", "Address", "Phone Number"]
for key in keys:
    value = input(f"Enter {key}: ") 
    data[key] = value
# create PDF and send email
pdf_file = "details.pdf"
fill_pdf(pdf_file, data)
recipient = input("Enter recipient email: ")
sender = input("Enter sender email: ")
password = input("Enter sender email password: ")
send_email(pdf_file, recipient, sender, password)
