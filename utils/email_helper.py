import base64
import json
import magic
import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content, HtmlContent, Attachment, FileContent, FileName, FileType, \
    Disposition, MailSettings, BccSettingsEmail, Cc
from sendgrid import SendGridException
from django.http import JsonResponse
from IntegrationTool import settings



class EmailHelperSendGrid:
    def __init__(self, recipient=None, email_subject=None, email_body=None, email_template=None, recipient_cc=None,
                 recipient_bcc=None, attachments=None, scheduled=None):
        self.recipient = recipient
        self.email_subject = email_subject
        self.email_body = email_body
        self.email_template = email_template
        self.recipient_cc = recipient_cc
        self.recipient_bcc = recipient_bcc
        self.attachments = attachments
        self.scheduled = scheduled

    def send_email(self):
        try:
            sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)
            from_email = Email(settings.FROM_EMAIL)
            to_email = To(self.recipient)
            content = Content("text/plain", self.email_body)
            mail = Mail(from_email, to_email, self.email_subject, content, self.email_template)
            # adding cc email
            if self.recipient_cc:
                mail.add_cc(To(self.recipient_cc))

            # adding BCC email
            if self.recipient_bcc:
                mail_settings = MailSettings()
                mail_settings.bcc_settings = BccSettingsEmail(self.recipient_bcc)
                mail.mail_settings = mail_settings

            if self.attachments:
                self.attachments = self.build_email_attachments(self.attachments)
                mail.attachment = self.attachments

            response = sg.send(message=mail)
            # ss = sendgrid.TrackingSettings(click_tracking="ClickTracking")
            return response.status_code
        except SendGridException as ex:
            return ex

    def build_email_attachments(self, attachments):
        if attachments:
            attachments_list = []
            for each_attachments in attachments:
                with open(each_attachments, 'rb') as f:
                    data = f.read()
                file_name = each_attachments.split("/")[-1]
                encoded = base64.b64encode(data).decode('ascii')
                attachment = Attachment(FileContent(encoded), FileName(file_name),
                                        FileType(self.get_file_mime_type(each_attachments)),
                                        Disposition('attachment'))
                attachments_list.append(attachment)
            return attachments_list

    @staticmethod
    def get_file_mime_type(file_path):
        if file_path:
            mime = magic.Magic(mime=True)
            return mime.from_file(file_path)

msg_body = "When you send an SMS to a phone number belonging to an end user's device you are sending an Outbound SMS. Historically, this was and still is referred to as a Mobile Terminated (MT) SMS, though nowadays an SMS is not always sent to a mobile device. In an Outbound SMS you can set the From or Sender field with whatever you have registered or purchased with Infobip, either a Long Number, Short Code, or text based Sender. " \
           "99% of all use cases can be achieved by using this API method. Everything from sending a simple single message to a single destination, up to batch sending of personalized messages to the thousands of recipients with a single API request. Language, transliteration, scheduling and every advanced feature you can think of is supported."
ob = EmailHelperSendGrid("karthik@appinessworld.com", "Test", msg_body, None, "karthikravinatha@gmail.com")
#                          # , None,
#                          # [os.path.join(settings.BASE_DIR, "Django Middleware.pdf"),
#                          #  os.path.join(settings.BASE_DIR, "manage.py")])
ob.send_email()
