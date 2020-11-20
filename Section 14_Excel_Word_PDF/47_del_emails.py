import imapclient
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('mahzindraco@gmail.com', 'hmfwqpjutywtdmms')
# ^ using an app password
conn.select_folder('INBOX', readonly=True)
conn.search(['SINCE 20-Aug-2015'])
UIDs = conn.search(['SINCE 20-Aug-2015']) # how to get this to work?
rawMessage = conn.fetch([47474], ['BODY[]', 'FLAGS'])

# sparse
import pyzmail
message = pyzmail.PyzMessage.factory(rawMessage[47474][b'BODY[]'])
message.get_subject()
meessage.get_addresses('from')
meessage.get_addresses('to')
message.get_addresses('bcc')

# check if email is txt, html, both or none
message.text_part
message.html_part == None
message.text_part.get_payload().decode('UTF-8') # results in a string

# encoding the message 
message.text_part.charset
message.text_part.charset == None

# checking other folders (spam, draft, etc.)
conn.list_folders()
conn.select_folder('INBOX', readonly=False)
UIDs = conn.search(['ON 24-Aug-2015'])
UIDS
# conn.delete_messages(UIDs)
