import fpdf
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def fill_pdf(pdf_file, data):
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=21, style='BU')
    pdf.cell(190, 20, txt="R.M.K College Of Engineering And Technology", ln=1, align="C")
    pdf.cell(190, 20, txt="Outing Form", ln=3, align="C")
    pdf.cell(190, 13, txt="", ln=4, align="C")
    for key, value in data.items():
        pdf.set_font("Times", style='BU', size=17)
        pdf.cell(77, 14, txt=key, ln=0, align="L")
        pdf.set_font("Times", size=15)
        pdf.cell(73, 14, txt=value, ln=1, align="L")
    pdf.cell(220, 50, txt="", ln=3, align="C")
    pdf.set_font("Times", style='B', size=17)
    pdf.cell(50, 8, txt="HoD", ln=0, align="C")
    pdf.set_font("Times", style='B', size=17)
    pdf.cell(65, 8, txt="Counselor /", ln=0, align="C")
    pdf.set_font("Times", style='B', size=17)
    pdf.cell(75, 8, txt="Principal", ln=1, align="C")
    pdf.set_font("Times", style='B', size=17)
    pdf.cell(50, 8, txt="", ln=0, align="C")
    pdf.set_font("Times", style='B', size=17)
    pdf.cell(65, 8, txt="Branch Co-Ordinator", ln=0, align="C")
    pdf.set_font("Times", style='B', size=17)
    pdf.output(pdf_file, "F")



def send_email(pdf_file, recipient, sender, password):
    msg = MIMEMultipart()
    with open(pdf_file, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={pdf_file}")
    msg.attach(part)
    msg["To"] = recipient
    msg["From"] = sender
    msg["Subject"] = "Outing Form"
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender, password)
        smtp.send_message(msg)

data = {}
keys = ["Name", "Registeration Number", "Phone Number", "Email", "Department", "Address","Date Of Leaving","Time Of Leaving","Date Of Arriving","Time Of Arriving"]
for key in keys:
    value = input(f"Enter {key}: ")
    data[key] = value
pdf_file = "Outing Form.pdf"
fill_pdf(pdf_file, data)
recipient = data['Email']
sender = "ganessh7114@gmail.com"
password = "krvqssopqhulecul"
send_email(pdf_file, recipient, sender, password)
print("\"Successfully Sent the E-mail\"")
