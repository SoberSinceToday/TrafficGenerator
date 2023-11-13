<h1 align="center">:octocat:This traffic generator<h1>
<h3 align="center">can be used as a tool for testing sites for stress resistance, as a tool for hiding real outgoing traffic and etc.</h3>

<h2>Quick start guide in the root folder:</h2>

:neckbeard:
main - console version of the program, has full functionality👍

:trollface:
QT - version of the program with a graphical interface written in PyQt5 has limited and not the most useful functionality👎

🔗
Links - contains the Links class describing interaction with links

🪵
browserDriver - file that creates ChromeDriver

📂 
projLogging - is responsible for logging of the execution process, and is output to the console upon completion

utils contains the file links.txt in which the basic links are recorded, chromedriver is chromedriver ofc

<h2>User manual:</h2>

1) Open project and run pip install PyQt5 if u need this, install a ChromeDriver compatible with your version of Chrome, the repository has a driver for version 119.0.6045.106

2) Customize links as u want using class Links from links.py
  
3) Using class TrafficGenerator run process


Deeper customization requires studying the project code. Currently only ChromeDriver is organized, you can adapt the project to your needs  
