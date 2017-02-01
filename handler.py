import urlparse
import json


message_choices = {
    "1": {"audio": "https://www.dropbox.com/s/6u1pgu3yt0b1gyk/english.mp3?dl=1"},
    "2": {"audio": "https://www.dropbox.com/s/pgo1nsfgflu5gtp/arabic.mp3?dl=1"},
    "3": {"audio": "https://www.dropbox.com/s/3rkn1ri99frluy5/farsi.mp3?dl=1",},
    "4": {"audio": "https://www.dropbox.com/s/pviynwf6f8idwcv/somali.mp3?dl=1"},
}

intro_alerts = "https://www.dropbox.com/s/b1getcw9shw2y0d/intro.mp3?dl=1"
options_menu = "https://www.dropbox.com/s/oca252w786zin40/options.mp3?dl=1"


def response(xml):
    return {"statusCode": 200,
            "body": xml,
            "headers": {"content-type": "text/xml"}}


def greeting(event, context):
    body_xml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Play>{intro_alerts}</Play>
    <Gather numDigits="1" action="play_selected" method="POST">
        <Play>{options_menu}</Play>
        <Pause length="3"></Pause>
        <Play>{options_menu}</Play>
    </Gather>
</Response>""".format(
        intro_alerts=intro_alerts,
        options_menu=options_menu,
    )

    return response(body_xml)



def play_selected(event, context):
    post_params = dict(urlparse.parse_qsl(event["body"]))
    choice = post_params["Digits"]
    if choice not in message_choices:
        return {
            "statusCode": "302",
            "headers": {"location": "greeting"}
        }

    recording_url = message_choices[choice]["audio"]
    body_xml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Play>{url}</Play>
</Response>""".format(url=recording_url)

    return response(body_xml)


def respond_to_sms(event, context):
    body_xml = """<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Sms>http://www.masslegalhelp.org/immigration/boston-logan-tro.pdf</Sms>
</Response>"""

    return response(body_xml)
