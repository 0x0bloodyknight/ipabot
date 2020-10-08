import requests
from bs4 import BeautifulSoup

cookies = {
    "output_dialect": "am",
}

headers = {
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Origin": "https://tophonetics.com",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
    "Sec-Fetch-Dest": "document",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Referer": "https://tophonetics.com/",
    "Accept-Language": "en-US,en;q=0.9",
}

data = {
    "text_to_transcribe": "text_to_transcribe",
    "submit": "Show transcription",
    "output_dialect": "am",
    "output_style": "only_tr",
    "preBracket": "",
    "postBracket": "",
    "speech_support": "1",
}


def get_transcription(text_to_transcribe):
    try:
        data["text_to_transcribe"] = text_to_transcribe

        response = requests.post(
            "https://tophonetics.com/", headers=headers, cookies=cookies, data=data
        )

        soup = BeautifulSoup(response.text)

        text = []

        for element in soup.find_all("span", class_="transcribed_word"):
            try:
                text += element.find("a")
            except:
                text += element.contents

        transcription = " ".join(text)

        return transcription

    except Exception as e:
        print(e)