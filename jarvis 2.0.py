# Project bharti
print('Initialising system.....')
import datetime
import operator
import os
import random
import re
import smtplib
import time
import webbrowser
from email.message import EmailMessage
from urllib.request import urlopen
import pyautogui
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
import subprocess
import wolframalpha
import mysql.connector
from pygame import mixer 
from bs4 import BeautifulSoup as soup
from selenium import webdriver

# Text To Speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)  # you can replace it to incease or decrease dound speed default(200)

#connection detail to database
mydb = mysql.connector.connect(host='localhost', user='root', passwd='0000')
cursor = mydb.cursor()
cursor.execute('use jarvis')
month_no = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8,
            'september': 9, 'october': 10, 'november': 11, 'december': 12}

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
        print("Network connection error")
        return "none"
    return text

def weather():
    api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=04b7de2862bdd7040cc8a52dee0fa722&units=metric&q='
    speak("are you in gogri")
    query = takecom().lower()
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
        print('Location not found')
        speak('location not found')

def calc():
    app_id = 'A3274K-HKQEV2U6UY'
    client = wolframalpha.Client(app_id)
    res = client.query(question)
    result = next(res.results).text
    print(f'Answer:- {result}\n')
    speak(f'its{result}')
    global data
    data = f'{query}\n Answer is {result}'

def cpscreenshot():
    time.sleep(0.75)
    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(r'E:\\picture-' + now + '.png')
    print('Screenshot has been successfully taken\n to see it go to e directry')
    speak('Screenshot has been saved')

def mplayer(name):
    mixer.init() 
    mixer.music.load("E:\\EDM\\"+name)
    mixer.music.set_volume(0.7) 
    mixer.music.play()

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
    print("\t\t\t\tTIME OUT")
    for i in range(1, 5):
        speak("time out")
        continue


def email_protocol():
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
        login_pass = "vmodlnnqpcnbdtdl"  # app key different for every person
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(login_id, login_pass)
        print("login successfully")
        server.send_message(msg)
        print("!!!!Email is successfully sent!!!!")
        speak("email is successfully sent")
        server.quit()
    except:
        print('Unable to send mail')
        speak('unable to send mail')
def senddata():
    os.chdir(r"E:/mycodes/python codes/AI/jarvis/server temp")
    f=open ("temp.txt",'w')           #you can change the w to a if you want to append
    f.write(data)
    f.close()

def wish():
    speak("jaai shree raam. sir.How are you")
    print("jai shree ram")
    query = takecom().lower()
    if "about you" in query:
        print("I am also fine and always ready to help you sir")
        speak("i am also fine and always ready to help you sir")
    speak("sir,do you want to know the weather")
    query = takecom().lower()
    if "yes" in query:
        weather()
        speak("ok sir.So what do you want me to do ")
    else:
        speak("ok sir.So what do you want me to do ")
        print("ok sir.So what do you want me to do ")
    # for main function

data = ''
if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()
        if "jarvis" in query or "javed" in query:
            speak("how may i help you sir")

        elif 'send data' in query or 'send the data' in query or 'send it to'  in query:
            output = os.popen('wmic process get description, processid').read()
            count =output.count('cmd.exe')-2
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

        elif "news headline" in query or "news update" in query:
            try:
                news_url = "https://news.google.com/news/rss"
                Client = urlopen(news_url)
                xml_page = Client.read()
                Client.close()

                soup_page = soup(xml_page, "xml")
                news_list = soup_page.findAll("item", limit=6)
                for news in news_list:
                    print(news.title.text)
                    speak(news.title.text)
                    # print(news.link.text)
                    print(news.pubDate.text)
                    print("-" * 60)
            except:
                print('Data not available')
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
                        print('Unable to take screenshot')
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

        elif 'what is the time' in query or 'what is the date' in query or 'whats time' in query:
            now = datetime.datetime.now()
            print("Current date and time : ")
            data=now.strftime("%d-%m-%Y %H:%M")
            print()
            speak()

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
                print("data not available")
                speak("data not available")
            data = f'{query}\n {data} '

        elif 'mean' in query or 'what' in query or 'tell' in query and 'of' in query:
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
                print('Data not available')
                speak('data is not available')

        elif "c drive" in query:
            webbrowser.open('C:')

        elif "d drive" in query:
            webbrowser.open('D:')

        elif "e drive" in query:
            webbrowser.open('E:')

        elif 'run chrome' in query or 'start chrome ' in query or 'open chrome' in query:
            os.system("start chrome.exe")
            print('Starting chrome')
            speak('starting chrome')

        elif 'stop chrome ' in query or 'close chrome' in query:
            os.system("TASKKILL /F /IM chrome.exe")
            print('Chrome has been closed')
            speak('chrome has been closed')

        elif 'start sublime text' in query or 'run sublime text' in query or 'open sublime text' in query or 'start the line' in query:
            subprocess.Popen('C:\\Program Files\\Sublime Text 3\\sublime_text.exe')
            print('Starting sublime text')
            speak('starting sublime text')

        elif 'stop sublime ' in query or 'close sublime' in query  or 'stop the line' in query :
            os.system("TASKKILL /F /IM sublime_text.exe")
            print('Sublime_text has been closed')
            speak('sublime text has been closed')

        elif 'start notepad' in query or 'run notepad' in query or 'open notepad' in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            print('Starting notepad')
            speak('starting notepad')

        elif 'stop notepad' in query or 'close notepad' in query:
            os.system("TASKKILL /F /IM notepad.exe")
            print('notepad has been closed')
            speak('notepad has been closed')

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

        elif 'music from pc' in query or "music" in query or  'play music' in query or 'play a song' in query or 'play song' in query:
            files=os.listdir("E:\\EDM")
            d=random.choice(files)
            print(f'Playing {d}') 
            speak(f'ok i am playing music{d}')           
            mplayer(d)
            while True: 
                print("speak 'pause' to pause, 'resume' to resume") 
                print("'stop' to stop the music ") 
                query = takecom().lower()
                if 'pause' in query: 
                    mixer.music.pause()      # Pausing the music 
                elif 'resume' in query: 
                    mixer.music.unpause()     # Resuming the music 
                elif 'stop' in query or 'exit' in query: 
                    mixer.music.stop()  # Stop the mixer 
                    break      

        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = './video'
            videos = os.listdir(music_dir)
            os.startfile(os.path.join(video_dir, videos[0]))

        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy',
                      'i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)
            ans_take_from_user_how_are_you = takecom().lower()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')

        elif "tell me a joke" in query or " bored" in query:
            data = pyjokes.get_joke()
            print(data)
            speak(data)

        elif "what is love" in query:
            speak("It is 7th sense that destroy all other senses.")
            time.sleep(0.2)
            data = "soory,love is a mix of emotions, behaviors, and beliefs associated with strong feelings of affection, protectiveness, warmth, and respect for another person. Love can also be used to apply to non-human animals, to principles, and to religious beliefs"
            print(data)
            speak(data)

        elif "who i am" in query:
            speak("If you talk then definately your human.")

        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information Abhishek Kumar Bharti Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)

        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am Jarvis an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)

        elif "hello" in query or "hello Jarvis" in query:
            data = "Hello Sir ! How May i Help you.."
            print(data)
            speak(data)

        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Jarvis"
            print(na_me)
            speak(na_me)

        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")

        elif "how old are you" in query:
            print("I was made in 2020 by Abhishek Bharti, but  I am wise beyond my years")
            speak("I was made in 2020 by Abhishek Bharti, but  I am wise beyond my years")

        elif query == 'none':
            continue

        elif 'exit' in query or 'abort' in query or 'bye' in query or 'quit' in query or 'close yourself' in query :
            ex_exit = 'Good bye sir, take care and besafe from carona'
            speak(ex_exit)
            exit()

        elif "weather" in query:
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')


            class info():
                def __init__(self):
                    self.driver = webdriver.Chrome(
                        executable_path="C:\\Users\\Abhishek\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\chromedriver.exe")

                def get_info(self, query):
                    self.query = query
                    self.driver.get(url="https://www.google.com/")
                    search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
                    search.click()
                    search.send_keys(query)

                    remove_wrong_click = self.driver.find_element_by_xpath('//*[@id="lga"]')
                    remove_wrong_click.click()

                    enter = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
                    enter.click()

                    place = self.driver.find_element_by_xpath('//*[@id="wob_loc"]')
                    place_text = place.text
                    speak("i am showing the weather of " + place_text)

                    dateandtime = self.driver.find_element_by_xpath('//*[@id="wob_dts"]')
                    dateandtime_text = dateandtime.text
                    speak("its" + dateandtime_text)

                    description = self.driver.find_element_by_xpath('//*[@id="wob_dc"]')
                    description_text = description.text
                    if "Mostly cloudy" in description_text or "Cloudy" in description_text or "Raining" in description_text or "Sunny" in description_text:
                        speak("and its" + description_text + "so bring umbrbella with yourself")
                    else:
                        speak("data not available")

                    temp = self.driver.find_element_by_xpath('//*[@id="wob_tm"]')
                    temperature = temp.text
                    speak("temperature is" + temperature + "degree celcius")

                    prec = self.driver.find_element_by_xpath('//*[@id="wob_d"]/div/div[2]/div[1]')
                    precipitation = prec.text
                    speak(precipitation)

                    wind = self.driver.find_element_by_xpath('//*[@id="wob_d"]/div/div[2]/div[3]')
                    wind_speed = wind.text
                    speak("and" + wind_speed)
                    global data
                    data=f'{query}\n temperature is {temperature} \n chance of precipitation is {precipitation}\n speed of wind is {wind_speed} '

                    speak("do you want to know the temperature of tommarow")
                    query = takecom()
                    if "yes" in query:
                        tomm = self.driver.find_element_by_xpath('//*[@id="wob_dp"]/div[2]/div[3]')
                        tommarow = tomm.text
                        speak("it will be" + tommarow + "maximum and minimum temperature respectivily tommarow")
                    else:
                        speak("data not available")

            bot = info()
            bot.get_info(query)

        else:
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
                    options = webdriver.ChromeOptions()
                    options.add_argument('--ignore-certificate-errors')
                    options.add_argument('--ignore-ssl-errors')


                    class info():
                        def __init__(self):
                            self.driver = webdriver.Chrome(
                                executable_path="C:\\Users\\Abhishek\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\chromedriver.exe")

                        def get_info(self, query):
                            self.query = query
                            self.driver.get(url="https://www.google.com/")
                            search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
                            search.click()
                            search.send_keys(query)

                            remove_wrong_click = self.driver.find_element_by_xpath('//*[@id="lga"]')
                            remove_wrong_click.click()

                            enter = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
                            enter.click()

                            # info=self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[1] | //*[@id="rso"]/div[1]/div/div[2]/div/span | //*[@id="rso"]/div[1]/div/g-card/div/div | //*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[2]/div/span/span | //*[@id="mh_tsuid104"]/div/div/div[1] | //*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[1]/div | //*[@id="mh_tsuid103"]/div/div/div[1]/a ')
                            try:
                                info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[1]')
                            except:
                                try:
                                    info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/g-card/div/div/div/div[1]/div[2]')
                                except:
                                    try:
                                        info = self.driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div[1]/div/div/div/div')
                                    except:
                                        try:
                                            info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[2]/div/span')
                                        except:
                                            try:
                                                info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/g-card/div/div')
                                            except:
                                                try:
                                                    info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[2]/div/span/span')
                                                except:
                                                    try:
                                                        info = self.driver.find_element_by_xpath('//*[@id="mh_tsuid104"]/div/div/div[1]')
                                                    except:
                                                        try:
                                                            info = self.driver.find_element_by_xpath('//*[@id="mh_tsuid103"]/div/div/div[1]/a')
                                                        except:
                                                            try:
                                                                info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[1]/div')
                                                            except:
                                                                try:
                                                                    info = info = self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[1]/div[2]/span/span')                                                    
                                                                except:
                                                                    print("Here is what i found on the web")
                                                                    speak("Here is what i found on the web")
                                                                    return
                            readable_text = info.text
                            speak(readable_text)
                            formated_data = (r_data,readable_text)
                            cursor.execute("insert into brain (data,value) values(%s,%s)",(formated_data))
                            mydb.commit()
                            global data
                            data = f'{query}\n {readable_text}'
                    bot = info()
                    bot.get_info(temp)
                    speak("wahts the next command")
                    pass
                except:
                    print('Data not available')
                    speak('data not available')
# entry = 'What is hello'
# stopwords = ['what', 'who', 'is', 'a', 'at', 'is', 'he']
# querywords = entry.split()

# resultwords  = [word for word in querywords if word.lower() not in stopwords]
# result = ' '.join(resultwords)
# print(result)
