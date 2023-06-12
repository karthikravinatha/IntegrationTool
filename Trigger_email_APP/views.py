from rest_framework.views import APIView
from django.http import JsonResponse
from utils.email_helper import EmailHelperSendGrid


# Create your views here.
class TriggerEmail(APIView):
    def post(self, request, *args, **kwargs):
        response = EmailHelperSendGrid(recipient="karthik@appinessworld.com", email_subject="Email Test",
                                       email_body="Hello Welcome Karthik").send_email()
        return JsonResponse(response, safe=False)
