import smtplib #  Simple Mail Transfer Protocol library, used to send emails
from email import encoders # encodes attachments
from email.mime.text import MIMEText # to write the body of the email
from email.mime.base import MIMEBase # to represent the attachment before encoding and sending it
from email.mime.multipart import MIMEMultipart # to combine multiple parts of an email (e.g., body + attachment)

try:
    # setup connection
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('senderemail@gmail.com', 'senderemailpassword')
    # NOTE: if you get error that your credentials are not correct even though they are,
    # then go to your google account > manage your google account > security >
    # enable 2-step verification > home > search for 'app passwords' > create app pawwords >
    # copy / paste your password to senderemailpassword above

    # create email
    email = MIMEMultipart()

    # sender / recipient / subject information
    email['From'] = 'senderemail@gmail.com' # sender@example.com
    email['To'] = 'receiveremail@gmail.com' # recipient@example.com
    email['Subject'] = 'Test Email from Python via Mailtrap'

    # create body and add it to the email
    with open('message.txt', 'r') as f:
        body = f.read()

    email.attach(MIMEText(body, 'plain'))

    # create image attachment and add it to the email
    filename = 'successImage.jpg'
    imageAttachment = open(filename, 'rb') # rb because it's an image and not just text

    emailAttachment = MIMEBase('application', 'octet-stream') # p is a container for imageAttachment before it gets encoded and attached
    # 'octet-stream' means "generic binary data" and it's used for files that don't have a specific MIME type (like .png, .pdf, .zip, etc.)
    # you can also use image/jpeg in this case

    emailAttachment.set_payload(imageAttachment.read()) # reads the binary content from imageAttachment

    # encode and add headers
    encoders.encode_base64(emailAttachment)
    emailAttachment.add_header('Content-Disposition', f'imageAttachment; filename={filename}')
    email.attach(emailAttachment)

    # take whole email as string
    text = email.as_string()

    # send email
    server.sendmail('senderemail@gmail.com', 'receiveremail@gmail.com', text)
    server.quit()
except Exception as e:
    print(f"Error: {e}'")