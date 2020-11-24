import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
n = int(input("nhập n ="))
for i in range(n):
 fromaddr = "tha1242002@gmail.com"
 toaddr = "nguyenhuukieutrinh@gmail.com"
 msg = MIMEMultipart()
 msg['From'] = fromaddr
 msg['To'] = toaddr
 msg['Subject'] = "Chào chi :3"
 body = "Em yêu chị "
 msg.attach(MIMEText(body, 'plain'))
 server = smtplib.SMTP('smtp.gmail.com', 587)
 server.starttls()
 server.login(fromaddr, "thang1242002")
 text = msg.as_string()
 server.sendmail(fromaddr, toaddr, text)
 server.quit()
