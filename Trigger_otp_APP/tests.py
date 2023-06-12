from google.cloud import translate


def translate_text(text="<h5>The Adult cardiology treatments and services</h5>", project_id="august-victor-389603"):

    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{project_id}/locations/{location}"
    response = client.translate_text(
    request={
        "parent": parent,
        "contents": [text],
        "mime_type": "text/html",
        # "mime_type": "text/plain",
        "source_language_code": "en-US",
        "target_language_code": "kn",
    })

    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))


translate_text()



# get list of languages
#
# client = translate.TranslationServiceClient()
# project_id="august-victor-389603"
# location = "global"
# parent = f"projects/{project_id}/locations/{location}"
# display_language_code = "en"
# response = client.get_supported_languages(
#         parent=parent,
#         display_language_code=display_language_code,
#     )
# languages = response.languages
# for language in languages:
#     language_code = language.language_code
#     display_name = language.display_name
#     print(f"{language_code:10}{display_name}")
#





# from google.cloud import translate_v2 as translate
#
# translate_client = translate.Client()
# text = "The Adult cardiology treatments and services include Coronary angiogram and angioplasty (radial and femoral), Emergency Percutaneous Coronary Intervention (PCI), Complex coronary interventions (Left main, bifurcation, chronic total occlusion, rotaablation), Coronary lesion physiological assessment and imaging (FFR, IVUS, OCT),"
# target = "kn"
# if isinstance(text, bytes):
#     text = text.decode("utf-8")
#
# # Text can also be a sequence of strings, in which case this method
# # will return a sequence of results for each text.
# result = translate_client.translate(text, target_language=target)
#
# print("Text: {}".format(result["input"]))
# print("Translation: {}".format(result["translatedText"]))
# print("Detected source language: {}".format(result["detectedSourceLanguage"]))