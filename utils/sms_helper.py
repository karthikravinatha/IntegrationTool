from infobip_channels.sms.channel import SMSChannel
from IntegrationTool import settings


class SmsHelperInfobip():
    def send_sms(self, recipient, message):
        try:
            channel = SMSChannel.from_auth_params(
                {
                    "base_url": settings.INFOBIP_BASE_URL,
                    "api_key": settings.INFOBIP_API_KEY,
                }
            )
            # Send a message with the desired fields.
            sms_response = channel.send_sms_message(
                {
                    "messages": [
                        {
                            "destinations": [{"to": recipient}],
                            "text": message,
                        }
                    ]
                }
            )
            # Get delivery reports for the message. It may take a few seconds show the just-sent message.
            return sms_response
        except Exception() as ex:
            raise ex
        # query_parameters = {"limit": 10}
        # delivery_reports = channel.get_outbound_sms_delivery_reports(query_parameters)
        # delivery_reports = channel.get_inbound_sms_messages(query_parameters)
        # # See the delivery reports.
        # print(delivery_reports)
