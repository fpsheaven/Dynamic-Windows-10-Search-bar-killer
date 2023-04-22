import psutil,os, win32serviceutil,time,win32service,webbrowser
def kill():
    try:
        win32serviceutil.StopService("WSearch")
    except:
        pass
    print ("Minimize this app and ignore every output")
    time.sleep(2)
    while True:
        for i in range(2):
            os.system("taskkill /f /im SearchApp.exe")
            os.system("taskkill /f /im SearchIndexer.exe")

def start():
    print ("Starting Windows search service")
    try:
        win32serviceutil.StartService("WSearch")
    except:
        pass
    print ("Started the service.")
    print ("I love you.Goodbye")
    time.sleep(2)
    webbrowser.open('https://fpsheaven.com/services')
    quit()
def run():
    print ("FPSHEAVEN.com. Search app killer.")
    print("You will need to exit the app if you want to kill it. This version wont have switches for now.I will add them later.")
    user_input=input("Press 1 to load the default values or press 2 to kill the search app while you game.\n")
    if user_input=="1":
        start()
    elif user_input=="2":
        print ("This will keep killing the search bar forever until you manually exit the app. Ignore the error, just MINIMIZE the app")
        time.sleep(5)
        kill()
    else:
        print ("Watch what you press.Run the app again")
        quit()
run()

