#Project bharti
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
from bs4 import BeautifulSoup as soup
from selenium import webdriver
#Text To Speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate', 145) #you can replace it to incease or decrease dound speed default(200)
def speak(audio):  #here audio is var which contain text
    engine.say(audio)
    engine.runAndWait()
#now convert audio to text
def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        audio = r.listen(source)
    try:
        print("Recognising....") 
        text = r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:                #For Error handling
        # speak("error...")
        print("Network connection error") 
        return "none"
    return text

def weather():
    api_address='http://api.openweathermap.org/data/2.5/weather?appid=04b7de2862bdd7040cc8a52dee0fa722&units=metric&q='
    speak("are you in gogri")
    query=takecom().lower()
    if "yes" in query:
        city ="gogri"
    else:
        speak("so where are you")
        query=takecom().lower()
        stopwords = ['i', 'am', 'in', 'a', 'at', 'is', 'he','she','we','are']
        querywords = query.split()
        resultwords  = [word for word in querywords if word.lower() not in stopwords]
        city = ' '.join(resultwords)
        url = api_address + city
        json_data = requests.get(url).json()
        location = json_data["name"]
        temp = json_data['main'] ['temp']
        speed =json_data['wind']['speed']
        wind_speed=round((speed*18)/5 , 2)
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

def wish():  
    speak("jaai shree raam. sir.How are you")
    print("jai shree ram")
    query=takecom().lower()
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
#for main function                               
if __name__ == "__main__":
    wish()
    while True:
        query = takecom().lower()
        if "jarvis" in query or "javed" in query:
            speak("how may i help you sir")

        elif "c drive" in query:
        	webbrowser.open('C:')

        elif "d drive" in query:
        	webbrowser.open('D:')

        elif "e drive" in query:
        	webbrowser.open('E:')


        elif "stopwatch" in query:
            os.system('start cmd /k python "stopwatch.py"') 
            speak("stopwatch will start in 3 second")

        elif "alarm" in query:
            os.system('start cmd /k python "alarm.py"')
            # speak("please enter the time you want to wake up") 
        elif "note" in query:
            os.system('start cmd /k python "note.py"')
            try:
                obj = open("note.txt")
            except :
                obj= open("note.txt","w+")
            obj =open("note.txt",)
            for line in obj:
                print(line,end='')
                
            with open("note.txt",'a')as obj:
                speak("speak the word you want to save")
                time=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                note =[format(time),"- \n",takecom().lower(),". \n "]
                obj.writelines(note)
            print("\n\nFile is successfully saved")
            speak("file has been saved successfully")

        elif "send email" in query or "email" in query:
            msg = EmailMessage()
            speak("whom do you want to send the email")
            print("Whom do you want to send the email")
            email=takecom().lower()
            if "papa" in email:
                email="sonuguria48@gmail.com"
            elif "me" in email :
                email ="bhartiabhishek310@gamil.com"
            refined_mail=email.replace("at the rate of","@").replace(" ","").replace("dot",".")
            recipients=[refined_mail]
            msg['From'] = "Abhishek Bharti"
            msg['To'] =  ", ".join(recipients)
            speak("what will be the subject")
            print("what will be the subject")
            msg['Subject'] = takecom()
            speak("what do you want to message him")
            print("what do you want to message him")
            msg.set_content(takecom())
            # Send the message via our own SMTP server.
            login_id ="bhartiabhishek310@gmail.com"
            login_pass ="vmodlnnqpcnbdtdl"                  #app key different for every person
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(login_id,login_pass)
            print("login successfully")
            server.send_message(msg)
            print("Email is successfully sent")
            speak("email is successfully sent")
            server.quit()                                  

        elif "news headline" in query or "news update" in query:
            news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()

            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item" , limit=6)
            for news in news_list:
              print(news.title.text )
              speak(news.title.text )
              # print(news.link.text)
              print(news.pubDate.text)
              print("-"*60)

        elif 'calculate' in query:
            print("Your speech_recognition version is: "+sr.__version__)
            r = sr.Recognizer()
            my_mic_device = sr.Microphone(device_index=1)
            with my_mic_device as source:
                print("Say what you want to calculate, example: 3 plus 3")
                print("what do you want to calculate just speak \n listening....")
                speak("what do you want to calculate")
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return {
                    '+' : operator.add,
                    '-' : operator.sub,
                    'x' : operator.mul,
                    'divided' :operator.__truediv__,
                    'Mod' : operator.mod,
                    'mod' : operator.mod,
                    '^' : operator.xor,
                    }[op]
            def eval_binary_expr(op1, oper, op2):
                op1,op2 = int(op1), int(op2)
                return get_operator_fn(oper)(op1, op2)
            print(eval_binary_expr(*(my_string.split())))
            speak(eval_binary_expr(*(my_string.split())))

        elif "take screenshot" in query or "take a screenshot" in query:
            print("Do you want to take screenshot of this page \n If yes type 'y' otherwise 'n' :-  ")
            speak("do you want to take the screenshot of current page")
            command =takecom().lower()
            try :
                if command.lower().startswith("y"):
                    time.sleep(1)
                    now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                    myScreenshot = pyautogui.screenshot()
                    myScreenshot.save(r"E:\\picture-"+now+".png")
                    print("Screenshot has been successfully taken\n to see it go to e directry")
                    speak("file has been saved to e directry")
                else:
                    speak("after what interval you want to take screenshot")
                    print("After what interval of time do you want to take screenshot (in second) :-")
                    st=int(takecom().lower())
                    while True:
                        now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                        myScreenshot = pyautogui.screenshot()
                        myScreenshot.save(r"E:\\picture-"+now+".png")
                        print("Screenshot has been successfully taken\n to see it go to e directry")
                        print("Press ctrl+c to stop the screenshot")
                        speak("file has been saved")
                        time.sleep(st)           
            except :
                print("error")  

        elif "set timer" in query or "run timer" in query:
            speak("enter the time when to stop the timer")
            print("Enter the time when to stop the timer = ")
            os.system('start cmd /k python "timer.py"') 
            try:
                timer = takecom().lower()
                if "second" in timer or "seconds"in timer:
                    filtering = re.findall(r'\d+', timer)
                    timer = int(''.join(filtering))
                elif ('minutes' not in timer and "minute" not in timer) and ("hour" in timer or "hours" in timer):
                    filtering = re.findall(r'\d+', timer)
                    timer = int(''.join(filtering))*3600
                elif ("hour" in timer or "hours" in timer) and ("minutes" in timer or "minute" in timer):
                    print('hello')
                    filtering = re.findall(r'\d+', timer)
                    a=(int(''.join(filtering[0]))*3600)
                    b=(int(''.join(filtering[1]))*60)
                    timer =a+b
                elif "minutes" in timer or "minute" in timer:
                    filtering = re.findall(r'\d+', timer)
                    timer = int(''.join(filtering))*60
                else:
                    print("Please! write valid number")
                    speak("Please speak valid number")
                    continue

                when_to_stop =abs(int(timer))
                while when_to_stop >0:
                    speak("timer started")
                    os.system('cls')
                    m,s = divmod(when_to_stop,60)
                    h,m = divmod(m,60)
                    print("\n\n\n\n\n\n\n\n\n")
                    print("\t\t\t\t|"+str(h).zfill(2)+":" + str(m).zfill(2)+":"+str(s).zfill(2)+"|")
                    time.sleep(1)
                    when_to_stop -=1
                    print()
                print("\t\t\t\tTIME OUT")
                for i in range(1, 5):
                   speak("time out")
            except KeyboardInterrupt :
                speak("please enter the right value")
                continue         
             
        elif 'what is the time' in query or 'what is the date' in query or 'whats time' in query:
            now = datetime.datetime.now()
            print ("Current date and time : ")
            print (now.strftime("%d-%m-%Y %H:%M:%S"))
            speak(now.strftime("%d-%m-%Y %H:%M"))

        elif "search wikipedia about" in query or "search the wikipedia about" in query :
            print('searching wikipedia...')
            speak('Searching Wikipedia...') 
            query = query.replace("search the wikipedia about", "").replace("search wikipedia about","") 
            results = wikipedia.summary(query, sentences = 3) 
            speak("According to Wikipedia")
            print("According to wikipedia")
            try: 
                print(results) 
                speak(results)
            except:
                print("data not available")
                speak("data not available")         

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

        elif 'music from pc' in query or "music" in query:
            speak("ok i am playing music")
            music_dir = './music'
            musics = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,musics[0]))

        elif 'video from pc' in query or "video" in query:
            speak("ok i am playing videos")
            video_dir = './video'
            videos = os.listdir(music_dir)
            os.startfile(os.path.join(video_dir,videos[0]))  

        elif 'good bye' in query or 'close yourself' in query:
            speak("good bye")
            exit()

        elif "shutdown" in query:
            speak("shutting down")
            os.system('shutdown -s') 

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takecomm()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')

        elif "tell me a joke" in query or " bored" in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())

        elif "what is love" in query:
            speak("It is 7th sense that destroy all other senses.")
            time.sleep(0.2)
            speak("soory,A mix of emotions, behaviors, and beliefs associated with strong feelings of affection, protectiveness, warmth, and respect for another person. Love can also be used to apply to non-human animals, to principles, and to religious beliefs") 

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
            hel = "Hello Sir ! How May i Help you.."
            print(hel)
            speak(hel)

        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! Jarvis"  
            print(na_me)
            speak(na_me)

        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")

        elif "how old are you" in query:
        	print("I was made in 2020, but  I am wise beyond my years")
        	speak("I was made in 2020, but  I am wise beyond my years")

        elif query == 'none':
            continue 

        elif 'exit' in query or 'abort' in query or 'stop' in query or 'bye' in query or 'quit' in query :
            ex_exit = 'Good bye sir, take care and besafe from carona'
            speak(ex_exit)
            exit()
            
        elif "weather" in query:
	        options = webdriver.ChromeOptions()
	        options.add_argument('--ignore-certificate-errors')
	        options.add_argument('--ignore-ssl-errors')
	        class info():
	            def  __init__(self):
	                self.driver = webdriver.Chrome(executable_path="C:\\Users\\Abhishek\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\chromedriver.exe")

	            def get_info(self,query):
	                self.query =query
	                self.driver.get(url="https://www.google.com/")
	                search= self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
	                search.click()
	                search.send_keys(query)

	                remove_wrong_click =self.driver.find_element_by_xpath('//*[@id="lga"]')
	                remove_wrong_click.click()

	                enter =self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
	                enter.click()

	                place=self.driver.find_element_by_xpath('//*[@id="wob_loc"]')
	                place_text = place.text
	                speak("i am showing the weather of "+place_text)

	                dateandtime=self.driver.find_element_by_xpath('//*[@id="wob_dts"]')
	                dateandtime_text = dateandtime.text
	                speak("its"+dateandtime_text)

	                description=self.driver.find_element_by_xpath('//*[@id="wob_dc"]')
	                description_text = description.text
	                if "Mostly cloudy" in description_text or "Cloudy" in description_text or "Raining" in description_text or "Sunny" in description_text  :
	                    speak("and its"+ description_text+"so bring umbrbella with yourself")
	                else:
	                    speak("data not available")

	                temp=self.driver.find_element_by_xpath('//*[@id="wob_tm"]')
	                temperature=temp.text
	                speak("temperature is"+temperature+"degree celcius")

	                prec=self.driver.find_element_by_xpath('//*[@id="wob_d"]/div/div[2]/div[1]')
	                precipitation=prec.text
	                speak(precipitation)

	                wind=self.driver.find_element_by_xpath('//*[@id="wob_d"]/div/div[2]/div[3]')
	                wind_speed=wind.text
	                speak("and"+wind_speed)                

	                speak("do you want to know the temperature of tommarow")
	                query=takecom()
	                if "yes" in query:
	                    tomm=self.driver.find_element_by_xpath('//*[@id="wob_dp"]/div[2]/div[3]')
	                    tommarow=tomm.text
	                    speak("it will be"+tommarow+"maximum and minimum temperature respectivily tommarow")
	                else:
	                    speak("data not available")                    

	        bot=info()
	        bot.get_info(query)

        else:
            temp = query
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--ignore-ssl-errors')
            class info():
                def  __init__(self):
                    self.driver = webdriver.Chrome(executable_path="C:\\Users\\Abhishek\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\chromedriver.exe")

                def get_info(self,query):
                    self.query =query
                    self.driver.get(url="https://www.google.com/")
                    search= self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
                    search.click()
                    search.send_keys(query)

                    remove_wrong_click =self.driver.find_element_by_xpath('//*[@id="lga"]')
                    remove_wrong_click.click()

                    enter =self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
                    enter.click()

                    # info=self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[1] | //*[@id="rso"]/div[1]/div/div[2]/div/span | //*[@id="rso"]/div[1]/div/g-card/div/div | //*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[2]/div/span/span | //*[@id="mh_tsuid104"]/div/div/div[1] | //*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[1]/div | //*[@id="mh_tsuid103"]/div/div/div[1]/a ')
                    try:
                        info=self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div[1]')
                    except:
                        try:
                            info=self.driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div[1]/div/div/div/div')
                        except:
                            try:
                                info=self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[2]/div/span')
                            except:
                                try:
                                    info=self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/g-card/div/div')
                                except:
                                    try:
                                        info=self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[2]/div/span/span')
                                    except:
                                        try:
                                            info=self.driver.find_element_by_xpath('//*[@id="mh_tsuid104"]/div/div/div[1]')
                                        except:
                                            try:
                                                info=self.driver.find_element_by_xpath('//*[@id="mh_tsuid103"]/div/div/div[1]/a')
                                            except:
                                                try:
                                                    info=info=self.driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div[1]/div/div[1]/div/div[1]/div')
                                                except:
                                                    print("data not available")
                                                    speak("data not available")
                    readable_text = info.text
                    speak(readable_text)
            bot=info()
            bot.get_info(temp)     
            speak("wahts the next command")                              #xpath link
# entry = 'What is hello'
# stopwords = ['what', 'who', 'is', 'a', 'at', 'is', 'he']
# querywords = entry.split()

# resultwords  = [word for word in querywords if word.lower() not in stopwords]
# result = ' '.join(resultwords)
# print(result)
