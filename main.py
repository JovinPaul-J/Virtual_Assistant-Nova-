import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser
import requests
import bs4
import pyautogui

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishes():
    times = int(datetime.datetime.now().hour)
    if times>= 0 and times<12:
        talk("Good Morning sir !")

    elif times>= 12 and times<18:
        talk("Good Afternoon sir !")

    else:
        talk("Good Evening sir !")

    talk("i am your virtual assistant nova, how can i help you,sir ?")

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        talk("listening")
        voice = listener.listen(source, phrase_time_limit=5)

    try:
        command = listener.recognize_google(voice, language='en-in')
        print("user said: " + command)

    except Exception as e:
        print(e)
        print("please say it again.")
        return "None"
    return command

if __name__=="__main__":
    while True:
        command = take_command().lower()
        if 'wake up' in command:
            wishes()

            while True:
                command = take_command().lower()
                if 'time' in command:
                    time = datetime.datetime.now().strftime('%I:%M %p')
                    print(time)
                    talk('current time is ' + time)

                elif 'date' in command:
                    date = datetime.datetime.now().strftime('%d %m %y')
                    print(date)
                    talk("today's date is " + date)

                elif 'play' in command:
                    yt = command.replace('play', '')
                    print(yt)
                    talk('playing' + yt)
                    pywhatkit.playonyt(yt)

                elif 'search' in command:
                    if 'on youtube' in command:
                        google = command.replace("search,on youtube", '')
                        youtube = google
                        webbrowser.open(f"https://www.youtube.com/results?search_query={youtube}")

                    else:
                        talk(f"searching {google}")
                        pywhatkit.search(google)

                elif 'from wikipedia' in command:
                    wiki = command.replace('from wikipedia', '')
                    print("how many lines do you want?")
                    talk("how many lines do you want?")
                    lines = take_command()
                    info = wikipedia.summary(command, sentences={lines})
                    print("according to wikipedia :" + info)
                    talk("according to wikipedia" + info)

                elif 'open' in command:
                    command = command.replace("open", "")
                    command = command.replace(" ", "")
                    talk(f"opening {command}sir")
                    if '.com' in command or ".org" in command or ".to" in command:
                        webbrowser.open(f"https://www.{command}")

                    elif 'whatsapp' in command:
                        webbrowser.open("https://web.whatsapp.com/")

                    else:
                        pyautogui.press("win")
                        pyautogui.typewrite(command)
                        pyautogui.sleep(2)
                        pyautogui.press("enter")

                elif "whatsapp" in command:
                    if 'message to' in command:
                        mes = command.replace('whatsapp message to', '')
                        pyautogui.hotkey('ctrl', 'alt', 'k')
                        pyautogui.sleep(2)
                        pyautogui.typewrite(mes)
                        pyautogui.sleep(2)
                        pyautogui.press("enter")
                    elif 'chat' in command:
                        if 'close' in command:
                            pyautogui.press("esc")
                        else:
                            talk("what should i chat sir")
                            msg = take_command()
                            pyautogui.typewrite(msg)

                elif "locate" in command:
                    loc = command.replace("locate", "")
                    location = loc
                    talk("you asked to locate")
                    talk(location)
                    webbrowser.open("https://www.google.com/maps/place/" + location + "")

                elif "temperature" in command:
                    talk("city name")
                    print("city name:")
                    city_name = take_command()
                    search = f"temperature in {city_name}"
                    url = f"https://www.google.com/search?q={search}"
                    t = requests.get(url)
                    data = bs4.BeautifulSoup(t.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    talk(f"current {search} is {temp}")
                    print(f"current {search} is {temp}")

                elif 'take a note' in command:
                    talk("what should i note, sir")
                    note = take_command()
                    file = open('virtual_assistant.txt','w')
                    file.write(note)

                elif 'show note' in command:
                    talk("showing notes")
                    file = open("virtual_assistant.txt", "r")
                    print(file.read())
                    talk(file.read(6))

                elif 'take a screenshot' in command:
                    pyautogui.hotkey("win", "prtsc")
                    talk("screenshot captured")

                elif 'mute' in command:
                    pyautogui.press("volumemute")

                elif 'increase volume' in command:
                    if '2' in command:
                        pyautogui.press("volumeup", presses=10)
                    elif '3' in command:
                        pyautogui.press("volumeup", presses=15)
                    elif '4' in command:
                        pyautogui.press("volumeup", presses=20)
                    elif '5' in command:
                        pyautogui.press("volumeup", presses=25)
                    else:
                        pyautogui.press("volumeup", presses=5)

                elif 'decrease volume' in command:
                    if '2' in command:
                        pyautogui.press("volumedown", presses=10)
                    elif '3' in command:
                        pyautogui.press("volumedown", presses=15)
                    elif '4' in command:
                        pyautogui.press("volumedown", presses=20)
                    elif '5' in command:
                        pyautogui.press("volumedown", presses=25)
                    else:
                        pyautogui.press("volumedown", presses=5)

                elif 'view' in command:
                    pyautogui.hotkey('ctrl', '1')

                elif 'press enter' in command:
                    pyautogui.press("enter")

                elif 'talking tom' in command:
                    talk("talking tom opened")
                    while True:
                        command = take_command().lower()
                        if "close talking tom" in command:
                            talk("talking tom closed")
                            break
                        else:
                            talk(command)

                elif 'sleep' in command:
                    talk("ok,sir! you can call me anytime")
                    break

                elif 'turn off' in command:
                    talk("yes sir, thank you")
                    exit()