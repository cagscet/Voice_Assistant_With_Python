from playsound import playsound  #ses dosyalarını çalmaya yarar
from gtts import gTTS            #Belirli bir metni ses dosyasına dönüştürmek için Google'ın metin okuma API'sini kullanır.
import speech_recognition as sr  #Mikrofon veya ses dosyalarından alınan ses verilerini metne dönüştürmek için
import pyaudio                   #Mikrofon gibi giriş cihazlarından ses almak ve hoparlörler gibi çıkış cihazlarına ses göndermek için kullanılır
import os                        #Dosya ve dizin işlemleri, ortam değişkenlerine erişim gibi işlemler için kullanılır.
import webbrowser
import math
import random
import datetime
import tkinter as tk  # Tkinter modülü
from tkinter import messagebox

at = "Asistan : "
r = sr.Recognizer() # Recognizer nesnesi oluştur

def record(ask = False):
    with sr.Microphone() as source: # cihazda hangi mikrofon varsan onun kullanıcak
        if ask:
            print(ask)
        r.adjust_for_ambient_noise(source)  # Ortam gürültüsüne göre mikrofondan ses almayı ayarla
        audio = r.listen(source)
        voice = ""
        try:
            voice= r.recognize_google(audio,language="tr-TR")
        except sr.UnknownValueError: # bilinmeyen ses de öksürük gibi
            print(at+"Anlayamadım")
        except sr.RequestError:      # internet giderse felan
            print(at+"Sistemde sorun var")
        return voice

def response(voice):  # cevap fonksiyonu

    while True:
        if "selam" in voice or "merhaba" in voice or "meraba" in voice:
            speak("Selam")

        elif "nasılsın" in voice or "naber" in voice or "ne haber" in voice:
            speak("İyiyim, siz nasılsınız?")


        elif "adın ne" in voice or "ismin ne" in voice:
            speak("Benim bir adım yok ben bir yapay zekayım, peki senin adın ne")
            # user_voice = record()  # Kullanıcının yanıtını almak için tekrar dinle
            if record():
                speak(f"memnun oldum ,{record()} sana nasıl yardımcı olabilirim")
            else:
                speak("Adını anlayamadım")


        elif "bende iyiyim" in voice or "ben de iyiyim" in voice or "iyiyim" in voice or "iyi" in voice:
            speak("Güzel, size nasıl yardımcı olabilirim?")

        elif "benim için bir şaka yapar mısın" in voice or "şaka yap" in voice or "bir şaka yap" in voice:
            selection = ["Yılan neden iş bulamadı   Çünkü çok kıvrak ",
                         "Neden bilgisayar denize girmedi  Çünkü deniz dalgaları vardı ",
                         "Kedi neden bilgisayarı sevmedi  Çünkü fareyle oynadı"]
            selection = random.choice(selection)
            speak(selection)

        elif "google'da ara" in voice or "internette ara" in voice or "gogılda ara" in voice:
            selection = ["sizin için ne arayabilirim", "ne aramamı istersiniz", "ne aratmamı istersiniz"]
            selection = random.choice(selection)
            speak(selection)
            print(selection)
            search = record()  # search değişkeni oluşturup recorda bağladım

            if search.strip():  # Boş olup olmadığını kontrol edelim
                url = f"https://www.google.com/search?q={search}"
                webbrowser.get().open(url)
                speak(f"{search} için Google'da arama yapıyorum.")
                print("Arama sorgusu:", search)
            else:
                speak("Anlayamadım, tekrar söyleyebilir misiniz?")

        elif "hava durumu" in voice:
            speak("Hangi şehrin hava durmunu öğrenmek istersiniz ")
            search = record()
            if search.strip():
                url = f"https://www.google.com/search?q={search, "hava durumu"}"
                webbrowser.get().open(url)
                speak(f"{search, " için hava durumu"} için Google'da arama yapıyorum.")
            else:
                speak("Anlayamadım, tekrar söyleyebilir misiniz?")
                continue


        elif "youtube'da ara" in voice or "yutupta'da ara" in voice or "yutupda ara" in voice or "yotube ara" in voice:
            selection = ["sizin için ne arayabilirim", "ne aramamı istersiniz", "ne aratmamı istersiniz"]
            selection = random.choice(selection)
            speak(selection)
            print(selection)
            search = record()  # search değişkeni oluşturup recorda bağladım

            # https://www.youtube.com/results?search_query=

            if search.strip():
                url = f"https://www.youtube.com/results?search_query={search}"
                webbrowser.get().open(url)
                speak(f"{search} için Youtube'da arama yapıyorum.")
                print("Arama sorgusu:", search)
            else:
                speak("Anlayamadım, tekrar söyleyebilir misiniz?")
                continue

        elif "şarkı aç" in voice:
            selection = ["ne dinlemek istersiniz", "hangi şarkıyı açmamı istersiniz", "ne aratmamı istersiniz"]
            selection = random.choice(selection)
            speak(selection)
            print(selection)
            search = record()

            if search.strip():
                url = f"https://www.youtube.com/results?search_query={search}"
                webbrowser.open(url)
                speak(f"{search} için müzik aranıyor.")
            else:
                print("Şarkıyı bulamadım")
                continue

        elif "saat kaç" in voice:
            now = datetime.datetime.now()
            time_str = now.strftime("%H:%M:%S")
            speak(f"Saat şu anda {time_str}" or "saat kaçtı")

        elif "tarih ne" in voice:
            today = datetime.date.today()
            date_str = today.strftime("%d %B %Y")
            speak(f"Bugünün tarihi {date_str}")

        elif "en büyük kim" in voice or "en iyi takım hangisi" in voice:
            speak("beşiktaş")

        elif "hangi takımlısın" in voice:
            speak("beşiktaş")

        elif "not al" in voice or "notal" in voice or "not yaz" in voice:
            with open("konusma.txt", "a",
                      encoding="utf-8") as f:  # encoding="utf-8" kullanarak Türkçe karakterlerin doğru şekilde yazılmasını sağlarız. open fonksiyonuyla dosyayı açarız ve a (append) modunu kullanırız.
                f.write(f"{datetime.datetime.now()}: {voice}\n")
            speak("Notunuzu aldım.")

        elif "kapat" in voice:
            speak("Yapay zeka kapanıyor")
            exit()

        else:
            speak("Anlayamadım, başka bir şey söyleyebilir misin?")
            continue


def voice_recognition():
    while True:
        voice = record()
        if voice.strip():  # Boşluk ya da hatalı sesleri kontrol et
            print("Kayıt edilen ses:", voice)
            voice = voice.lower()  # Kayıt edilen kelimeleri küçük harfe dönüştür
            response(voice)
        else:
            print(at + "Anlayamadım, tekrar deneyin.")


def speak(string):
    tts = gTTS(text=string,lang="tr",slow=False) # kütüphaneyi kullan tek string yavaş okuması false dil türkçe
    file = "cevap.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)


if __name__ == "__main__":
    speak("Yapay zeka başladı, size nasıl yardımcı olabilirim?")
    voice_recognition()


