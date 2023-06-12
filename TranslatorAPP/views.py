from django.shortcuts import render
from rest_framework.views import APIView
import ast


# Create your views here.
class TranslatorViews(APIView):
    def post(self, request, *args, **kwargs):
        ss = request.POST
        hd = ss.get("hidden_f")
        v3 = self.translate_text_v3(hd)
        # data = ast.literal_eval(hd)
        # return_dict = {}
        # for i in data:
        #     for k, v in i.items():
        #         return_dict[k] = self.translate_v2(v, "kn")
        return render(request, "index.html", context={"translated_data": v3})

    def get(self, request, *args, **kwargs):
        return render(request, "index.html", context={"translated_data": ""})

    def translate_v2(self, text, target):
        from google.cloud import translate_v2 as translate

        translate_client = translate.Client()
        if isinstance(text, bytes):
            text = text.decode("utf-8")

        # Text can also be a sequence of strings, in which case this method
        # will return a sequence of results for each text.
        result = translate_client.translate(text, target_language=target)

        print("Text: {}".format(result["input"]))
        print("Translation: {}".format(result["translatedText"]))
        print("Detected source language: {}".format(result["detectedSourceLanguage"]))
        return result["translatedText"]

    def translate_text_v3(self, text, project_id="august-victor-389603"):
        from google.cloud import translate
        client = translate.TranslationServiceClient()
        location = "global"
        parent = f"projects/{project_id}/locations/{location}"
        response = client.translate_text(
            request={
                "parent": parent,
                "contents": [text],
                "mime_type": "text/html",
                # "mime_type": "text/plain",
                # "source_language_code": "en-US",
                "target_language_code": "kn",
            })

        for translation in response.translations:
            # print("Translated text: {}".format(translation.translated_text))
            return translation.translated_text
        # return response.translations[0]["translated_text"]