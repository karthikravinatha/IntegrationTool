import time
import requests
from rest_framework.views import APIView
from django.http import JsonResponse
from utils.sms_helper import SmsHelperInfobip

from IntegrationTool import settings


class TriggerOtp(APIView):
    def post(self, request, *args, **kwargs):
        # Initialize the SMS channel with your credentials.
        message = request.POST.get("message")
        recipient = request.POST.get("to")
        type = request.POST.get("type")
        # r = self.temp()
        if type == "1":
            response = self.send_whatsapp_message(recipient)
            return JsonResponse(response, safe=False)
        else:
            response = SmsHelperInfobip().send_sms(recipient=recipient, message=message)
            return JsonResponse(response.status_code, safe=False)

    def send_whatsapp_message(self, receiver):
        BASE_URL = settings.INFOBIP_BASE_URL
        API_KEY = settings.INFOBIP_API_KEY_WHATSAPP
        SENDER = "447860099299"
        RECIPIENT = receiver
        payload = {
            "messages":
                [
                    {
                        "from": SENDER,
                        "to": RECIPIENT,
                        "content": {
                            "templateName": "registration_success",
                            "templateData": {
                                "body": {
                                    "placeholders": [
                                        "Hello",
                                        "How",
                                        "Are",
                                        "You"
                                    ]
                                },
                                "header": {
                                    "type": "IMAGE",
                                    "mediaUrl": "https://api.infobip.com/ott/1/media/infobipLogo"
                                },
                                "buttons": [
                                    {
                                        "type": "QUICK_REPLY",
                                        "parameter": "yes-payload"
                                    },
                                    {
                                        "type": "QUICK_REPLY",
                                        "parameter": "no-payload"
                                    },
                                    {
                                        "type": "QUICK_REPLY",
                                        "parameter": "later-payload"
                                    }
                                ]
                            },
                            "language": "en"
                        }
                    }
                ]
        }
        headers = {
            'Authorization': API_KEY,
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        response = requests.post(BASE_URL + "/whatsapp/1/message/template", json=payload, headers=headers)
        return response.json()


