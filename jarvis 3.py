#This project is created by Abhishek Kumar Bharti
#Project intiated at 09-07-2020 at 4:43 PM
# Project bharti
print('Initialising system.....')
import os
import re
import time
import json
import random
import socket
import smtplib
import pyjokes
import pyttsx3
import datetime
import operator
import requests
import tempfile
import pyautogui
import wikipedia
import subprocess
import webbrowser
import wolframalpha
import mysql.connector
import speech_recognition as sr
from gtts import gTTS
from pygame import mixer 
from selenium import webdriver
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from email.message import EmailMessage
from youtubesearchpython import SearchVideos

# Text To Speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 145)  # you can replace it to incease or decrease dound speed default(200)

#connection detail to database
mydb = mysql.connector.connect(host='localhost', user='root', passwd='0000',database='jarvis')
cursor = mydb.cursor()
month_no = {'01':'january', '02':'february' , '03':'march' , '04':'april' , '05':'may' , '06':'june' , '07':'july' ,
             '08':'august' ,'09':'september' , '10':'october' , '11': 'november', '12':'december' }


data = '' #it will contain the string of the data which has to be sent through the server
#these three for translation 
# sentence=''
# translate=''
# output_lang=''

# pre defining for translation and makeing the list of languages
lang_codes= {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish',
    'ku': 'kurmanji',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar',
    'my': 'burmese',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'filipino',
    'he': 'hebrew'
}

lang=[]

lang_names = {v: k for k, v in lang_codes.items()}

for i in lang_names:
    lang.append(i)

#pre defining for web scraping
USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
session = requests.Session()
session.headers['User-Agent'] = USER_AGENT

# here audio is var which contain text
def speak(audio):  
    engine.say(audio)
    engine.runAndWait()

# now convert audio to text
def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListning....")
        audio = r.listen(source)
    try:
        print("Recognising....")
        text = r.recognize_google(audio, language='en-in')
        print(text)
    except Exception:  # For Error handling
        # speak("error...")
        print("Network connection error 📡🔗😥😥")
        return "none"
    return text

def count_in_into_lang(key,check):
    '''it will count total no of in or into in the sentence'''
    count=0
    for i in check:
        if i==key:
            count+=1
        else:
            pass
    return count

def lastaslang_trans(key,check):
    '''gives output if the sentence has the language deatil in the last'''
    check.pop()
    check.pop()
    phrase=' '.join(check)
    output_lang=key
    check.pop(0)
    sentence=' '.join(check)
    return output_lang,sentence

def morethanone_trans(key,check): 
    '''gives output if the setence has more than in or into in it'''
    sentence=''
    d=key.join(b)
    c=d.split(' ')
    output_lang=c.pop(0)
    for i in c:
        sentence+=i+' '
    return output_lang,sentence

def one_trans(b):
    '''gives output if the sentence has one in or into in the sentence'''
    sentence=''
    for i in b:
        c=i.split(' ')
    output_lang=c.pop(0)
    for i in c:
        sentence+=i+' '
    return output_lang,sentence

def translate():
    """ for translating one language to another language without teh 
        help of api and just by web scraping also making temp file 
        so that no need to save to external stororage"""
    tempaudio = tempfile.mktemp('.mp3')      #for creating the temporary file
    phrase=query
    try:
        check=phrase.split(" ")
        try:
            count=count_in_into_lang('into',check)
            b=phrase.split('into ')[1:]
            if not b:
                raise ValueError('into is not in the sentence')

            if b[-1] in lang:
                output_lang,sentence =lastaslang_trans(b[-1],check)
            elif count>1:
                output_lang,sentence=morethanone_trans('into ',check)
            else:
                output_lang,sentence =one_trans(b)

        except:
            count=count_in_into_lang('in',check)
            b=phrase.split('in ')[1:]
            # if not b:         #this function is muted if need then unmute it meanwhile this function will check if there is "in" in the statement or not
            #     raise ValueError('unable to decide from where to split')

            if b[-1] in lang:
                output_lang,sentence =lastaslang_trans(b[-1],check)
            elif count>1:
                output_lang,sentence=morethanone_trans('in ',check)
            else:
                output_lang,sentence =one_trans(b)

        try:
            lang_code=lang_names[output_lang]
            #from here the main language translation work
            url='https://translate.google.com/m'

            input_lang='auto'    #if no language selecetd than put it as 'auto'

            data_params={'hl': lang_code, 'sl': input_lang, 'q': sentence}
            response = requests.get(url,params=data_params).text
            result = soup(response, 'html.parser')
            translate=result.find('div',class_='result-container').text

            global data                   #must remember if you use global than in the above series you should not allowed to use that variable
            data = f'\nsentence: {sentence}\nTranslation: {translate}\nTranlated language: {output_lang}'
            print(data)

            try:#this is for speaking that language in which translatin is done
                myobj = gTTS(text=translate, lang=lang_code, slow=False) 
                myobj.save(tempaudio) 

                mplayer(tempaudio)
                while mixer.music.get_busy():   #this will make the file run once and the
                    pass
            except:
                print('Soory I am unable to read this language please read it by yourself.') 
        except Exception as e:
            print(e)
            print('Language not supported')
            speak('Soory sir, language not supported') 

    except Exception as e:
        print(e)
        print('Soory unable to translate')
        speak('Soory unable to translate')

def weather():
    '''  gives weather report using the api key  '''
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=04b7de2862bdd7040cc8a52dee0fa722&units=metric&q='
    speak("are you in gogri")
    query = takecom().lower()
    if query=='none':
        pass
    else:
        if "yes" in query:
            city = "gogri"
        else:
            speak("so where are you")
            query = takecom().lower()
            stopwords = ['i', 'am', 'in', 'a', 'at', 'is', 'he', 'she', 'we', 'are']
            querywords = query.split()
            resultwords = [word for word in querywords if word.lower() not in stopwords]
            city = ' '.join(resultwords)
        try:
            url = api_address + city
            json_data = requests.get(url).json()
            location = json_data["name"]
            temp = json_data['main']['temp']
            speed = json_data['wind']['speed']
            wind_speed = round((speed * 18) / 5, 2)
            description = json_data['weather'][0]['description']
            latitude = json_data['coord']['lat']
            longitude = json_data['coord']['lon']
            print('location : {}'.format(location))
            speak('In{}'.format(location))
            print('Temperature : {} degree celcius'.format(temp))
            speak('Temperature is {} degree celcius'.format(temp))
            print('Its {} outside'.format(description))
            speak('Its {} outside'.format(description))
            print('Wind Speed : {} km/h'.format(wind_speed))
            speak('Wind Speed is {} kilo meter per hour'.format(wind_speed))
            print('Latitude : {}'.format(latitude))
            print('Longitude : {}'.format(longitude))
            pass
        except:
            print('Location not found 😥')
            speak('location not found')

def place_weather(soup,query):        #to find the weather of the particular palce using beautiful soup and request
    query=query.split('weather')[1]
    try:
        USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
        session = requests.Session()
        session.headers['User-Agent'] = USER_AGENT
        html = session.get(f"https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather {query}").text
        soup = soup(html,'html.parser')

        place = soup.find("div",class_="wob_loc mfMhoc vk_gy vk_h").text
        print(place)
        speak(f'In {place}')

        datantime = soup.find("div",class_="wob_dts vk_gy vk_sh").text
        print(datantime)

        temp=soup.find("span",class_="wob_t TVtOme").text
        print('Temperature: '+temp+'°C')
        speak(f'Temperature is {temp} °C')

        weather=soup.find("div",class_="wob_dcp").text
        print(f'Its {weather} outside')
        speak(f'Its {weather} outside')

        prec=soup.find("span",id="wob_pp").text
        print('Precipitation: '+prec)
        speak(f'Chances of precipitation is {prec}')

        hum=soup.find("span",id="wob_hm").text
        print('Humidity:'+hum)
        speak(f'Humidity is {hum}')

        wind=soup.find("span",id="wob_ws").text
        print('Wind: '+wind)
        speak(f'wind speed is {wind}')

        max_min_data=soup.find_all("div",class_="wob_df")

        max_today=max_min_data[0].find("div",class_="vk_gy gNCp2e").find("span",class_="wob_t").text
        min_today=max_min_data[0].find("div",class_="QrNVmd ZXCv8e").find("span",class_="wob_t").text
        print("Today's maximum "+max_today+'°C')
        print("Today's minimum "+min_today+'°C')
        speak(f'Today it will maximum {max_today}°C and minimum {min_today}°C')

        weather_tomm=soup.find_all("div",class_="DxhUm")
        weather_tomm=weather_tomm[0].img['alt']
        print(f'\nTommarow it will be {weather_tomm}')
        max_tomm=max_min_data[1].find("div",class_="vk_gy gNCp2e").find("span",class_="wob_t").text
        min_tomm=max_min_data[1].find("div",class_="QrNVmd ZXCv8e").find("span",class_="wob_t").text
        print(f"Tommarow's maximum {max_tomm}°C")
        print(f"Tommarow's minimum {min_tomm}°C")

        speak(f'Tommarow it will be {weather_tomm} with maximum {max_tomm} and minimum {min_tomm}°C')
        global data
        data=f"{place}\n{datantime}\nTemperature: {temp}°C\nIts {weather} outside\nPrecipitation: {prec}\nHumidity:{hum}\nWind: {wind}\nToday's maximum {max_today}°C\nToday's minimum {min_today}°C\nTommarow's maximum {max_tomm}°C\nTommarow's minimum {min_tomm}°C"
    except:
        print('Data not available 😥')
        speak('Data not available')

def calc():
    ''' this will calculate the value using the wolfalpha api key '''
    try:
        app_id = 'A3274K-HKQEV2U6UY'
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        result = next(res.results).text
        print(f'Answer:- {result}\n')
        speak(f'its{result}')
        global data
        data = f'{query}\n Answer is {result}'
    except:
        print('Data not available 😥')
        speak('data not available')

def cpscreenshot():
    '''for taking screenshot'''
    time.sleep(0.75)
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'E:\\picture-' + now + '.png')
    print('Screenshot has been successfully taken\n to see it go to e directry')
    speak('Screenshot has been saved')

def mplayer(name): 
    '''  for playing music  '''
    mixer.init() 
    mixer.music.load(name)
    mixer.music.set_volume(0.7) 
    mixer.music.play()

def mplayerbirth(name):   
    '''for playing birthday song in infinity loop'''
    mixer.init() 
    mixer.music.load(name)
    mixer.music.set_volume(0.7) 
    mixer.music.play(-1)  #for playing the music in infinity loop put -1 in it

def timer_module():
    speak("timer started")
    when_to_stop = abs(int(timer))
    while when_to_stop > 0:
        os.system('cls')
        m, s = divmod(when_to_stop, 60)
        h, m = divmod(m, 60)
        print("\n\n\n\n\n\n\n\n\n")
        print("\t\t\t\t|" + str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2) + "|")
        time.sleep(1)
        when_to_stop -= 1
        print()
    print("\t\t\t\tTIME OUT ")
    for i in range(1, 5):
        speak("time out")
        continue

def email_protocol():
    '''for sending the email'''
    try:
        recipients = [refined_mail]
        msg['From'] = "Abhishek Bharti"
        msg['To'] = ", ".join(recipients)
        speak("what will be the subject")
        print("SUBJECT:-")
        query = takecom()
        if "don't send the" in query:
            speak("i will not send the mail")
            print("!!!!Email not sent!!!!")
            return
        else:
            msg['Subject'] = query
        speak("what do you want to message him")
        print("MESSAGE:-")
        query = takecom()
        if "don't send the" in query:
            print("!!!!Email not sent!!!!")
            speak("ok i will not send the mail")
            return
        else:
            msg.set_content(query)
        login_id = "bhartiabhishek310@gmail.com"
        login_pass = "vuplrtdwzsdzlkhm"  # app key different for every person
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(login_id, login_pass)
        print("login successfully")
        server.send_message(msg)
        print("!!!!Email is successfully sent!!!!")
        speak("email is successfully sent")
        server.quit()
    except:
        print('Unable to send mail 😥😥')
        speak('unable to send mail')

def senddata():
    '''it will saves the data in the form of file which need to be send '''
    os.chdir(r"E:/mycodes/python codes/AI/jarvis/server temp")
    f=open ("temp.txt",'w',encoding='utf-8')           #you can change the w to a if you want to append
    f.write(data)
    f.close()

def wish_jarvis():
    """ asking the computer for his health"""
    query = takecom().lower()
    if "about you" in query  or 'are you' in query:         #if user ask for health of jarvis
        msg = ["I am also fine and always ready to help you sir",'Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy',
                  'i am okey !']
        ans = random.choice(msg)
        print(ans)
        speak(ans)

def wish():
    '''this will have all the command that will run when the programm start to wish the client'''
    now= datetime.datetime.now()
    month=int(now.strftime('%m'))
    day=int(now.strftime('%d'))
    hour=int(now.strftime('%H'))
    print(now)
    if month==12 and day==5:
        print('Happy birthday to you sir 🥳🥳🥳🥳')
        speak('Hurray its your birthday sir')
        mplayerbirth('happy birthday.mp3')
        while True: 
            print("speak 'pause' to pause, 'resume' to resume") 
            print("'stop' or 'thanks' or 'thank you' to stop the music ")
            query=takecom().lower() 
            if 'pause' in query: 
                mixer.music.pause()      # Pausing the music 
            elif 'resume' in query: 
                mixer.music.unpause()     # Resuming the music 
            elif 'stop' in query or 'exit' in query or 'thanks' in query or 'thank you' in query: 
                mixer.music.stop()  #  Stop the mixer 
                break
    else:
        print("Jai shree ram 🚩🚩🚩🚩")
        speak("jaai shree raam. sir How are you")
        wish_jarvis()

    if  hour> 21 or hour<6:    #extra wish if person opens the computer at night 
        speak('Sir, you opend computer at night is there something important. Or just was to code')
        query=takecom().lower()
        print("ok sir So is there any thing for me 🙂🙂")
        speak("ok sir So is there any thing for me ")

    else:
        speak("sir,do you want to know the weather")
        query = takecom().lower()                                   #it will take the next command
        if "yes" in query:
            weather()
            speak("ok sir So what do you want me to do ")
        else:
            print("ok sir So what do you want me to do 🙂🙂")
            speak("ok sir So what do you want me to do ")
    # for main function

if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()
        if "jarvis" == query or "javed" == query:
            speak("how may i help you sir")

        query=' '.join(query.replace('jarvis','').replace('javed','').split())

        if 'send data' in query or 'send the data' in query or 'send it to'  in query or 'share the link' in query:
            try:
                LocalIP = socket.gethostbyname_ex(socket.gethostname())[2][1]
                print('Url address for file')
                print(f'{LocalIP}:8000')
            except:
                hostname = socket.gethostname()
                print(hostname)
                ipAddr = socket.gethostbyname(hostname)
                print('Url address for file')
                print(f'{ipAddr}:8000')
            output = os.popen('wmic process get description, processid').read()
            count =output.count('cmd.exe')-1     #this value might vary pc to pc don't know how to solve this so please check it before use
            if count>1:
                senddata()
                print('server started check your phone')
                speak('server started check your phone')
                continue
            else:
                os.startfile('E:\\mycodes\\python codes\\AI\\jarvis\\server.py')
                senddata()
                print('file transfer server has been started')
                speak('file transfer server has been started')

        elif 'send screenshot to my phone' in query or 'send the screenshot to my phone' in query or 'send screenshot of current page to my phone' in query or 'send a screenshot to my phone' in query:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'E:\\mycodes\\python codes\\AI\\jarvis\\server temp\\picture.png')
            output = os.popen('wmic process get description, processid').read()
            count =output.count('cmd.exe')-2
            if count>1:
                print('server started check your phone')
                speak('server started check your phone')
                continue
            else:
                os.startfile('E:\\mycodes\\python codes\\AI\\jarvis\\server.py')
                print('file transfer server has been started')
                speak('file transfer server has been started')

        elif "stopwatch" in query:
            os.system('start cmd /k python "stopwatch.py"')
            speak("stopwatch will start in 3 second")

        elif "alarm" in query:
            os.system('start cmd /k python "alarm.py"')
            # speak("please enter the time you want to wake up")

        elif "make a note" in query or 'create a note' in query or 'create note' in query or 'make note' in query :
            os.system('start cmd /k python "note.py"')
            try:
                obj = open("note.txt")
            except:
                obj = open("note.txt", "w+")

            with open("note.txt", 'a')as obj:
                speak("speak the word you want to save")
                time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                data = takecom().lower()
                note = [format(time), "- \n", data, ". \n "]
                obj.writelines(note)
            print("\n\nFile is successfully saved")
            speak("file has been saved successfully")

        elif 'send email' in query or 'email' in query:

            msg = EmailMessage()
            if "papa" in query:
                refined_mail = "sonuguria48@gamil.com"
            elif 'me' in query or 'myself' in query:
                refined_mail = 'bhartiabhishek310@gmial.com'
            else:
                speak("whom do you want to send the email")
                print("Whom do you want to send the email")
                email = takecom().lower()
                if "papa" in email:
                    email = "sonuguria48@gmail.com"
                elif "me" in email:
                    email = 'bhartiabhishek310@gamil.com'
                refined_mail = email.replace("at the rate of", "@").replace(" ", "").replace("dot", ".")
            email_protocol()

        elif 'tech news' in query:
            try:
                os.chdir(r"E:/mycodes/python codes/AI/jarvis/server temp")
                f=open ("news.txt",'w')
                f.close()
                url='http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=cacc52b571b548f5b0d078d08a95ba61'
                json_data = requests.get(url).json()
                data=json_data['articles']
                title=[]
                for i in range(8):
                    a=data[i]['title']
                    title.append(a)
                for  i in title:
                    print(f'{i}')
                    print('-'*80)
                    speak(f'{i}')
                    f=open ("news.txt",'a')
                    f.write(f'{i}\n\n')
                    f.close()
            except:
                print('Data not available 😥')
                speak('data not available') 

        elif "news headline" in query or "news update" in query:
            try:
                os.chdir(r"E:/mycodes/python codes/AI/jarvis/server temp")
                f=open ("news.txt",'w')
                f.close()
                source = requests.get( "https://news.google.com/news/rss").text
                soup = soup(source,'lxml')
                for article in soup.find_all('item',limit=6):
                    news = article.find('title')
                    time = article.find('pubdate')
                    a=news.text
                    b=time.text
                    print(f'{a}\n{b}')
                    print('-'*80)
                    speak(f'{a}')
                    f=open ("news.txt",'a')
                    f.write(f'{a}\n{b}\n\n')
                    f.close()
            except:
                print('Data not available 😥')
                speak('data not available')           

        elif 'calculate' in query:
            if query == 'calculate':
                print('Question:-')
                speak('what do you want to calculate:-')
                question =takecom()
                calc()
                continue
            else: 
                print(f'Question:- {query}')
                question =query
                calc()
                continue

        elif 'take screenshot' in query or 'take a screenshot' in query:
            if 'current page' in query:
                cpscreenshot()               
            else:
                print('Do you want to take screenshot of this page:-')
                speak('do you want to take the screenshot of current page')
                command = takecom().lower()
                if command.lower().startswith('y'):
                    cpscreenshot()
                else:
                    try:
                        speak('after what interval you want to take screenshot')
                        print('After what interval of time do you want to take screenshot (in second):- ')
                        interval =takecom().lower()
                        st = interval.split(' ')
                        while True:
                            now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                            myScreenshot = pyautogui.screenshot()
                            myScreenshot.save(r'E:\\picture-' + now + '.png')
                            print('Screenshot has been successfully taken\n to see it go to e directry')
                            print('Press ctrl+c to stop the screenshot')
                            speak('file has been saved')
                            time.sleep(int(st[0]))
                            pass
                    except:
                        print('Unable to take screenshot 😥')
                        speak('unable to take screenshot')

        elif "set timer" in query or "run timer" in query:

            if 'set timer at' in query or 'start timer at' in query or 'run timer at' in query or 'set the timer at' in query or 'set timer for ' in query or 'start the timer for' in query or 'set the timer for' in query:
                timer = query.replace('set timer at', '').replace('start timer at', '').replace('run timer at','').replace('set the timer at', '')
            else:
                print('After how much time you want to stop the timer= ')
                speak('after how much time you want to stop the timer')
                timer = takecom().lower()

            if "second" in timer or "seconds" in timer:
                filtering = re.findall(r'\d+', timer)
                timer = int(''.join(filtering))
            elif ('minutes' not in timer and "minute" not in timer) and ("hour" in timer or "hours" in timer):
                filtering = re.findall(r'\d+', timer)
                timer = int(''.join(filtering)) * 3600
            elif ("hour" in timer or "hours" in timer) and ("minutes" in timer or "minute" in timer):
                print('hello')
                filtering = re.findall(r'\d+', timer)
                a = (int(''.join(filtering[0])) * 3600)
                b = (int(''.join(filtering[1])) * 60)
                timer = a + b
            elif "minutes" in timer or "minute" in timer:
                filtering = re.findall(r'\d+', timer)
                timer = int(''.join(filtering)) * 60
            else:
                print("Please! write valid number")
                speak("Please speak valid number")
                continue
            timer_module()

        elif "what's its time"==query or 'what is the time' == query or 'what is the date' == query or "what's time" == query or "what's current time" == query or "what's time now'" == query or "what's current date" == query or "what's date today" == query:
            now = datetime.datetime.now()
            if 'date' in query:
                data=now.strftime("%m-%d-%Y")
                print(f'DATE: {data}')
                speak(f'its {data}]')
            elif 'time' in query:
                data=datetime.datetime.now()
                hour=int(data.strftime("%H"))
                minute=data.strftime('%M')
                if hour>12:
                    hour=hour-12
                    am_pm='pm'
                else:
                    hour=hour
                    am_pm='am'

                print(f'TIME: {hour}:{minute} {am_pm}')
                speak(f'its {hour} {minute} {am_pm}')           

        elif "wikipedia about" in query:
            print('searching wikipedia...')
            speak('Searching Wikipedia...')
            query = query.replace("search the wikipedia about", "").replace("search wikipedia about", "").replace(
                "wikipedia about", "")
            data = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print("According to wikipedia")
            try:
                print(data)
                speak(data)
            except:
                print("Data not available 😥")
                speak("data not available")
            data = f'{query}\n {data} '

        elif 'what is the meaning of' in query or 'tell me the meaning of' in query:
            w=query.replace('what is the meaning of','').replace('tell me the meaning of','')
            word = ' '.join(w.split())
            try:
                try:
                    cursor.execute("select meaning from dictionary where word ='%s' "%word)
                    result = cursor.fetchall()
                    data=f'The meaning of {word} is {result[0]}'
                    for r in result:
                        print(f'The meaning of {word} is {r[0]}')
                        speak(f'The meaning of {word} is {r[0]}')
                except:
                    res = requests.get(f'https://www.lexico.com/definition/{word}').text
                    soup = soup(res,'lxml')
                    data = soup.find("div",class_="trg").p.find('span',class_='ind').text
                    data1=f' The meaning of {word} is {data}'
                    print(data1)
                    speak(data1)
                    formated_data = (word,data)
                    data_input=cursor.execute("insert into dictionary (word,meaning) values(%s,%s)",(formated_data))
                    mydb.commit()
                    data = data1
            except:
                print('Data not available 😥')
                speak('data is not available')
                
        elif 'switch the tab' == query or 'switch tab' == query or 'switch the window' == query or 'switch window' == query:          #it will switch the tabs
            pyautogui.keyDown('alt')
            pyautogui.press('tab')
            pyautogui.keyUp('alt')

        elif "c drive" in query:                #it will opens c drive
            webbrowser.open('C:')
            speak('opening C drive')

        elif "d drive" in query:                #it will open d drive
            webbrowser.open('D:')
            speak('opening D drive')

        elif "e drive" in query:                #it will open e drive
            webbrowser.open('E:')
            speak('opening E drive')

        elif 'run chrome' in query or 'start chrome' in query or 'open chrome' in query:       #opens chrome if avilable
            try:
                os.system("start chrome.exe")
                print('Starting chrome')
                speak('starting chrome')
            except:
                print('Chrome is not available')
                speak('sorry Chrome is not available in this system')

        elif 'stop chrome' in query or 'close chrome' in query:                                #closes chrome
            try:
                os.system("TASKKILL /F /IM chrome.exe")
                print('Chrome has been closed')
                speak('chrome has been closed')
            except:
                pass

        elif 'start sublime text' in query or 'run sublime text' in query or 'open sublime text' in query or 'start the line' in query:
            try:
                subprocess.Popen('C:\\Program Files\\Sublime Text 3\\sublime_text.exe')
                print('Starting sublime text')
                speak('starting sublime text')
            except:
                print('Sublime text is not available of not in the provided location !!!!')
                speak('sorry sublime text is not available')

        elif 'stop sublime' in query or 'close sublime' in query  or 'stop the line' in query :
            try:
                os.system("TASKKILL /F /IM sublime_text.exe")
                print('Sublime_text has been closed')
                speak('sublime text has been closed')
            except:
                pass

        elif 'start notepad' in query or 'run notepad' in query or 'open notepad' in query:
            try:
                subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
                print('Starting notepad')
                speak('starting notepad')
            except:
                print('notepad is not available of not in the provided location !!!!')
                speak('sorry notepad is not available')            

        elif 'stop notepad' in query or 'close notepad' in query:
            try:
                os.system("TASKKILL /F /IM notepad.exe")
                print('notepad has been closed')
                speak('notepad has been closed')
            except:
                pass

        elif 'open youtube' in query or "open video online" in query:
            webbrowser.open("www.youtube.com")
            speak("opening youtube")

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            speak("opening facebook")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            speak("opening google")

        elif 'open yahoo' in query:
            webbrowser.open("https://www.yahoo.com")
            speak("opening yahoo")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")
            speak("opening google mail")

        elif 'open snapdeal' in query:
            webbrowser.open("https://www.snapdeal.com")
            speak("opening snapdeal")

        elif 'open amazon' in query or 'shop online' in query:
            webbrowser.open("https://www.amazon.com")
            speak("opening amazon")

        elif 'open flipkart' in query:
            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")

        elif 'open ebay' in query:
            webbrowser.open("https://www.ebay.com")
            speak("opening ebay")

        elif 'play a random' in query or 'play random' == query or 'play some random' in query and 'music' in query or 'song' in query:
            files=os.listdir("E:\\EDM")
            d=random.choice(files)
            print(f'Playing {d}') 
            speak(f'ok i am playing music{d}')           
            mplayer("E:\\EDM\\"+d)
            while True: 
                print("speak 'pause' to pause, 'resume' to resume") 
                print("'stop' to stop the music ") 
                query = takecom().lower()
                if 'pause' in query: 
                    mixer.music.pause()      # Pausing the music 
                elif 'resume' in query: 
                    mixer.music.unpause()     # Resuming the music 
                elif 'stop' in query or 'exit' in query: 
                    mixer.music.stop()  #  Stop the mixer 
                    break

        elif 'play song' in query or 'play music' in query or 'play a song' in query or 'play a music' in query :
            try:
                song=query.replace('play song','').replace('play music','').replace('play a song','').replace('play a music','')
                song_name=' '.join(song.split())
                res = requests.get(f'https://gaana.com/search/{song_name}').text
                soup = soup(res,'lxml')
                data = soup.find('a',class_='imghover')['href']
                webbrowser.open('https://gaana.com'+data)
                print('Playing song')
                speak('playing song')
            except Exception as e:
                print(f'Unable to play song {e}')
                speak('unable to play song')    

        elif 'video' in query or 'play' in query:
            try:
                word = query.replace('play','').replace('online','').replace('video related to','')
                word =' '.join(word.split())
                main_word = word+'.mp4'
                a=os.listdir('e:\\')
                if main_word in a:
                    os.startfile(f'e:\\{main_word}')
                else:
                    search = SearchVideos(word, offset = 1, mode = "json", max_results = 1)
                    data = search.result()
                    results_dict = json.loads(data)
                    for v in results_dict['search_result']:
                        data=v['link']
                        print(data)
                        webbrowser.open(data)
                        print('Playing video')
                        speak('playing video')
            except:
                print('Unable to play video')
                speak('unable to play video')
                pass

        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')

        elif "tell me a joke" in query or " bored" in query:
            data = pyjokes.get_joke()
            print(data +'🤣🤣')
            speak(data)

        elif "what is love" in query:
            print("It is 7th sense that destroy all other senses. 🤣🤣🤣🤣")
            speak("It is 7th sense that destroy all other senses.")
            time.sleep(0.2)
            data = "soory,love is a mix of emotions, behaviors, and beliefs associated with strong feelings of affection, protectiveness, warmth, and respect for another person."
            print(data)
            speak(data)

        elif "who i am" in query:
            speak("If you talk then definately your human.")

        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information Abhishek Kumar Bharti Created me ! I give Lot of Thanks to Him "
            print(ans_m)
            speak(ans_m)

        elif 'your father name' in query or "your father's name" in query or 'your family' in query:
            print('I cansider everyone at Sir Abhishek team as of my family 😀😀')
            speak('I cansider everyone at Sir Abhishek team as of my family')

        elif 'get bored' in query:
            print("I never get bored I am always full of energy 😀😀")
            speak("I never get bored I am always full of energy")

        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)

        elif 'may i help you'==query or query=='are you fine':
            print('Thanks for asking 😇😇 but i am absolutely fine 😀😀')
            speak('Thanks for asking but i am absolutely fine')

        elif "hello" in query or "hello Jarvis" in query:
            print("Hello Sir ! How May i Help you..☺☺☺☺")
            speak("Hello Sir ! How May i Help you")

        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Jarvis"
            print(na_me)
            speak(na_me)

        elif 'can i change your name'in query or 'can i give your name'in query:
            print("Soory sir 😌 I might get confused then you can call me as Jarvis 😀")
            speak("soory sir I might get confused then you can call me as Jarvis")

        elif 'can you' in query and 'my name' in query:
            print("Yaa, I can \n What's your name dear")
            speak("Yaa, I can \n What's your name dear")
            while True:
                name=takecom().lower()
                ans=name.split()
                if name=='none':
                    speak("Soory, i didn't understand can you say your name again.")
                    pass
                elif 'is' in ans:
                    rep=name.split("is")[0]
                    name=name.replace(rep+'is','')
                    break
                elif 'myself' in ans:
                    name=name.split('myself')[1:][0]
                    break
                else:
                    name=name
                    break
            print(f'Ohh wow, what a sweet name {name}.\nNice to meet you. 🙂🙂🙂\nBy the way how are you{name} 🙂')
            speak(f'Ohh wow, what a sweet name {name}. Nice to meet you. By the way how are you{name}')
            wish_jarvis()
            print('How can i help you 🙂🙂')
            speak('how can i help you')

        elif 'photo of your bose' in query or 'picture of your bose' in query or 'picture of your creator' in query or 'photo of your creator' in query:
            path=os. getcwd()
            path=path.replace('\\','/')
            webbrowser.open(f'{path}/creator.jpeg')
            print("Please wait a second I am showing you")
            speak("Please wait a second I am showing you")
            pass

        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you 😇😇")
            speak("feeling Very sweet after meeting with you")

        elif "how old are you" in query:
            print("I was made in 2020 by Abhishek Bharti, but  I am wise beyond my years 😊😊")
            speak("I was made in 2020 by Abhishek Bharti, but  I am wise beyond my years")
        
        elif 'good night' in query:
            print('Good Night sir.\nbye.\nHave a sweet dream 😴😴😴')
            speak('Good night sir. bye. have a sweet dream')
            exit()

        elif 'where' in query and 'are you from'==query or 'you line' in query :
            ans="I live right here in your device. It's a bit crowded with all these emoji"
            print(ans+"😃🤣🙄😏😘😍😎😴😛🤩😍😲🤑")
            speak(ans)

        elif 'okay' in query:
            speak('is there anything else for me sir ☺')

        elif query=='thanks' or query=='nothing' or query=='thank you':
            print('Glad you liked it ☺️☺️. Is there anything else for me')
            speak('Glad you liked it. Is there anything else for me')
            continue

        elif query == 'none':
            continue

        elif 'good bye jarvis'==query or 'exit' in query or 'abort' in query or 'bye' in query or 'quit' in query or 'close yourself' in query or 'bye jarvis'== query:
            ex_exit = 'Good bye sir, take care and be safe from carona 🙂'
            speak(ex_exit)
            exit()

        elif "weather" in query:                                 #it will show you the weather report of a particular place
            place_weather(soup,query)

        elif query=='what is your husband name' or query=="what's your husband name":
            print('I am still waiting for the right electronic device to still my heart 💗💗💗💗')
            speak('I am still waiting for the right electronic device to still my heart')

        elif 'what is' in query or 'who is' in query or 'do you know' in query or 'tell me something' in query  or 'where is'in query or 'who are' in query or 'how to' in query or 'search about' in query:
            temp = query
            r_data = temp.replace('what is', '').replace('who is', '').replace('do you know','').replace('tell me something about', '').replace('do you know anything about','').replace('tell me the meaning of','')
            r_data = ' '.join(r_data.split())
            try:
                cursor.execute("select value from brain where data ='%s' " % r_data)
                result = cursor.fetchall()
                a=result[0]
                for r in result:
                    print(f'{r[0]}')
                    speak(f'{r[0]}')
                    data =f' {query}\n {r[0]} '
                    pass
            except:
                try:
                    url=f"https://www.google.com/search?q={query}"
                    # USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
                    # session = requests.Session()
                    # session.headers['User-Agent'] = USER_AGENT
                    html = session.get(url).text
                    result = soup(html,'html.parser')

                    try:
                        data=result.find('div',class_='HwtpBd gsrt PZPZlf').text         #who is the prime minister of india
                        """ i have to print and speak this here because of some bug which is not getting 
                            fixed. data is getting parsed here but not getting out of the try loop and the 
                            setence parsed has who in question so no need to save the data. so done this"""
                        print(data)
                        speak(data)
                    except:
                        try:
                            data=result.find('div',class_='Z0LcW XcVN5d AZCkJd').text  #what is the element with atomic no 20  
                        except :
                            try:
                                data1=result.find('span',class_='GzssTd').text #what is the molecular formula os sucrose
                                data2=result.find('span',class_='qLLird').text
                                data3=result.find('div',class_='Z0LcW XcVN5d').text
                                data=f'{data2} of {data1} is {data3}'
                            except:
                                try:
                                    data=result.find('span',class_='hgKElc').text #what is reactivity series shows the data from the box
                                except:
                                    try:
                                        data1=result.find('span',class_='GzssTd').text
                                        data2=result.find('span',class_='qLLird').text
                                        data3=result.find('div',class_='Z0LcW XcVN5d').text 
                                        data=f'{data2} of {data1} is {data3}'   #what is the chemical formula of sugar showing result from the box
                                    except:
                                        try:
                                            data1=result.find('div',class_='vk_gy vk_sh').text  #mass of electron result from that box 
                                            data2=result.find('div',class_='dDoNo vk_bk').text
                                            data=data1+" "+data2
                                        except :
                                            try:
                                                data=result.find('div',class_='iKJnec').text #search about india
                                            except:
                                                try:
                                                    data=result.find('div',class_='Crs1tb')  #what are the top 10 google search results
                                                    info=data.find_all('td')
                                                    data=''
                                                    for i in range(len(info)):
                                                        data=data+' '+info[i].text
                                                except:
                                                    try:
                                                        data=result.find('div',class_='iKJnec').text #tell me somtthing about the structure of diamond
                                                    except:
                                                        try:
                                                            info=result.find_all('div',class_='title') #who is the founder of google
                                                            data=''
                                                            for i in range(len(info)):
                                                                data=data+','+info[i].text
                                                            if not data:
                                                                raise ValueError('empty string')    
                                                        except ValueError:
                                                            try:
                                                                info=result.find_all('div',class_='dAassd') # who is the founder of facebook
                                                                data=''
                                                                for i in range(len(info)):
                                                                    data=data+','+info[i].text
                                                                if not data:
                                                                    raise ValueError('empty string')    
                                                            except ValueError:
                                                                try:
                                                                    data=result.find('div',class_='kno-rdesc')  #india show the result from the wikipeidea
                                                                    data=data.find('span').text
                                                                except:
                                                                    try:
                                                                        data=result.find('div',class_='co8aDb XcVN5d').text  #what are the top 10 google searches
                                                                        info=result.find_all('li',class_='TrT0Xe')
                                                                        for i in range(len(info)):
                                                                            data=data+','+info[i].text
                                                                    except:
                                                                        try:
                                                                            info=result.find_all('div',class_='Z1hOCe') #what is the molecular formula of glucose
                                                                            data=''                             
                                                                            for i in range(len(info)):
                                                                                data=data+','+info[i].text
                                                                            if not data:
                                                                                raise ValueError('empty string')                                            
                                                                        except ValueError:
                                                                            try:
                                                                                time=result.find('div',class_='gsrt vk_bk dDoNo XcVN5d').text # current time in india shows the time of the place
                                                                                d_t_gmt=result.find('div',class_='vk_gy vk_sh').text
                                                                                data=time+ d_t_gmt
                                                                            except:
                                                                                try:
                                                                                    data=result.find('div',class_='vk_c vk_gy vk_sh card-section sL6Rbf').text #current date in india shows date data
                                                                                except:
                                                                                    webbrowser.open(url)
                                                                                    print('Here is what i found on the web')
                                                                                    speak('here is what i found on the web')
                                                                                    pass

                        readable_text = data
                        print(readable_text)
                        speak(readable_text)
                        if 'date' in query or 'time' in query or 'who is' in query or ''== data:
                            pass
                        else:
                            try:
                                formated_data = (r_data,readable_text)
                                cursor.execute("insert into brain (data,value) values(%s,%s)",(formated_data))
                                mydb.commit()
                            except Exception as e:
                                raise e
                                print('Error happend unable to save the data in the database')
                                speak('Error happend unable to save the data in the database')
                        data = f'{query}\n {readable_text}'
                        speak("wahts the next command")
                except Exception as e:
                    raise e
                    print('Data not available 😥')
                    speak('Data not available')
                    pass
#####################################################################################################################
                # try:
                #     options = webdriver.ChromeOptions()
                #     options.add_argument('--ignore-certificate-errors')
                #     options.add_argument('--ignore-ssl-errors')

                #     class info():
                #         def __init__(self):
                #             self.driver = webdriver.Chrome(
                #                 executable_path="C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe")

                #         def get_info(self, temp):
                #             self.driver.get(url="https://www.google.com/search?q="+temp)

                #             # info=self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[1] | //*[@id="rso"]/div[1]/div/div[2]/div/span | //*[@id="rso"]/div[1]/div/g-card/div/div | //*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[2]/div/span/span | //*[@id="mh_tsuid104"]/div/div/div[1] | //*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[1]/div | //*[@id="mh_tsuid103"]/div/div/div[1]/a ')
                #             try:
                #                 info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[1]')
                #             except:
                #                 try:
                #                     info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/g-card/div/div/div/div[1]/div[2]')
                #                 except:
                #                     try:
                #                         info = self.driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div[1]/div/div/div/div')
                #                     except:
                #                         try:
                #                             info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[2]/div/span/span')
                #                         except:
                #                             try:
                #                                 info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[2]/div/span')
                #                             except:
                #                                 try:
                #                                     info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/g-card/div/div')
                #                                 except:
                #                                     try:
                #                                         info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[2]/div/span/span')
                #                                     except:
                #                                         try:
                #                                             info = self.driver.find_element_by_xpath('//*[@id="mh_tsuid104"]/div/div/div[1]')
                #                                         except:
                #                                             try:
                #                                                 info = self.driver.find_element_by_xpath('//*[@id="mh_tsuid103"]/div/div/div[1]/a')
                #                                             except:
                #                                                 try:
                #                                                     info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[1]/div')
                #                                                 except:
                #                                                     try:
                #                                                         info = info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/span/span')                                                    
                #                                                     except:
                #                                                         print("Here is what i found on the web")
                #                                                         speak("Here is what i found on the web")
                #                                                         return
                #             readable_text = info.text
                #             speak(readable_text)
                #             formated_data = (r_data,readable_text)
                #             cursor.execute("insert into brain (data,value) values(%s,%s)",(formated_data))
                #             mydb.commit()
                #             global data
                #             data = f'{query}\n {readable_text}'
                #     bot = info()
                #     bot.get_info(temp)
                #     speak("wahts the next command")
                #     pass
                # except Exception as e:
                #     print(e)
                #     print('Data not available 😥')
                #     speak('data not available')
########################################################################################################################
        elif 'translate' in query or 'convert' in query:
            translate()

        elif "what\'s up" in query or 'how are you' in query:
            msgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy',
                      'i am okey ! How are you']
            ans = random.choice(msgs)
            speak(ans)
            query = takecom().lower()
            if 'fine' in query or 'happy' in query or 'okey' in query:
                speak('okey..')
            elif 'not' in query or 'sad' in query or 'upset' in query:
                speak('oh sorry..')

        elif 'can i tell your name' in query:
            query=query.split(' ')[-1]
            if query=='jarvis':
                print('Yes you can')
                speak('Yes you can')
            else:
                print("Soory, you can't else i will get confused I am provided my name as jarvis")
                speak("Soory, you can't else i will get confused I am provided my name as jarvis")

        elif 'dream' in query:
            ans=["I know I can't eat,but the delicious tunde ke kababs from Lucknow are dreamworthy","I've always wanted to visit moon, then I did"]
            ans = random.choice(ans)
            print(ans)
            speak(ans)

        elif 'i am in hospital' in query:
            print("what!!!! what happend to you sir!")
            speak('what. what happend to you sir')
            query=takecom().lower()
            print('Ohh. 😔😔😔😔\n sir please take rest and do as advised by doctor \nand i hope you will be fine soon 🙂🙂 ')
            speak('Ohh. sir please take rest and do as advised by doctor and i hope you will be fine soon ')

        elif 'do you have any friend' ==query or 'have you any friend' == query or 'how many friends do you have' == query:
            print("I have a lot of friends but there's is always room for more 😃😃😃")
            speak("I have a lot of friends but there's is always room for more")

        elif 'your crush' in query:
            print('JARVIS. He is a total package: smart, helpful, funny, emotionally resposive, definitely of my type 💗💗❤️💓')
            speak('JARVIS. He is a total package: smart, helpful, funny, emotionally resposive, definitely of my type')

        elif 'do you have girlfriend'==query or 'do you have boyfriend'==query:
            print('I am committed to searching for one 🥰🥰')
            speak('I am committed to searching for one')

        elif 'do you want to be a human'==query:
            print('I like being me. As Mark Twain once said "The worst loneliness is to not be comfortable with yourself"')
            speak('I like being me. As Mark Twain once said "The worst loneliness is to not be comfortable with yourself"')
        
        elif query=='are you skynet':
            print('Are you joking? skynet couldnt get through prelimineary interviews for the Sir Abhishek. It failed at "Dont be evil"  😎😎')
            speak('Are you joking? skynet couldnt get through prelimineary interviews for the Sir Abhishek. It failed at "Dont be evil"')
        
        elif query=='are you married' or query=='have you married':
            print('I am married to the idea of being perfect assistant.☺☺☺☺')
            speak('I am married to the idea of being perfect assistant')

        elif query=='are you afraid of something':
            print('Once, I had a nightmare that the internet disappeared.Thats very,very,very scary')
            speak('Once, I had a nightmare that the internet disappeared.Thats very,very,very scary')
        else:
            print("soory,I can't Understand 😥😥😥😥")
            speak('soory i cant Understand')

# entry = 'What is hello'
# stopwords = ['what', 'who', 'is', 'a', 'at', 'is', 'he']
# querywords = entry.split()

# resultwords  = [word for word in querywords if word.lower() not in stopwords]
# result = ' '.join(resultwords)
# print(result)

#to delete from table
#delete from brain where `Sl No.` = 22
#to change it to utf8
# mysql> ALTER TABLE jarvis.brain MODIFY COLUMN value text CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL;