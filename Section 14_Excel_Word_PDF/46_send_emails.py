# Emails

import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)
# <class 'smtplib.SMTP'>
conn
# <smtplib.SMTP object at 0x03314580>
conn.ehlo()
# (250, b'smtp.gmail.com at your service, [172.112.32.253]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
conn.starttls()
# (220, b'2.0.0 Ready to start TLS')
conn.login('mahzindraco@gmail.com', 'MahZin1326')
# used app password to make ^ work
conn.sendmail('mahzindraco@gmail.com', 'mahzindraco@gmail.com', '''Subject: So \n\nlong
,\nSo Long, and thanks.\n\n-Mason''')

conn.quit()
