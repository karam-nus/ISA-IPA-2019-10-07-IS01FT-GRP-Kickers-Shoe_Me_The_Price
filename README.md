# SECTION 1: PROJECT TITLE
Shoe Me The Price (SMTP) -- 

AN IPA AGENT FOR GETTING THE BEST ONLINE SHOE PRICES

![alt text](https://github.com/karamjotsinghmalik/ISA-IPA-2019-10-07-IS01FT-GRP-Kickers-Shoe_Me_The_Price/blob/master/templates/Poster.png)


# SECTION 2: EXECUTIVE SUMMARY
Over the last few decades shopping has transitioned from the traditional brick and mortar stores around the block to internationally shipped online stores that don’t have a single physical store. With the above  as the basis for our product we have concentrated on the vital process of comparing the product from the above definition ‘one or more retailers’.  
Specifically we’ve decided to place our product for a niche market of the population that thinks twice before spending money on a product that can be considered an essential and a luxury. And given that asian market is considered to be one of the most convservative markets, in terms of spending, we’ll plan to cater this market for now. 
In respect to spending, we’ve built upon this idea and came up with a solution to compare shoe prices online and receive price updates of user selected shoes over time based on per user subscription. In addition to comparing price we also predict if the price of a user selected shoe will either slump in the times to come or will remain the same. All this by just letting us know the name of the shoe the user is interested in and the users email address.

SYSTEM DESIGN AND WORKING
- The user can send a request via email or from the website.
- The request for the particular shoes gets processed at the backend. 
- The bots scrape the details of the shoes from various websites in real-time to ensure that the latest prices are always pushed to the user.
- Along with the prices, a recommendation about the trend of the price is also calculated.
- Once all the bots are finished with their processes, a custom response is developed for each user with the shoes they requested, the price of the shoes from various websites along with a recommendation stating whether the prices are likely to go up or down or remain the same.
- The developed response is shared with the user via the email id they provided and user can click on each shoe to visit the respective website for further details.

# SECTION 3: CREDITS/PROJECT CONTRIBUTION

| Official Full Name|Student ID| Work Scope  |Email|
|:---------:|:-------------:|:-----:|:----:|
|Karamjot Singh|A0198470U		| Application design; Market research; Creation of RPA robots; Code for - mail-bot, sending & receiving mail responses, Env & DB creation scripts, DB update modules, Gmail API integration; Parallel processing of multi-channel scripts; Report; Video Editing	|	singh@u.nus.edu|
|Kartik Chopra|A0198483L		|Initial survey for algorithm design, Algorithm Design, Question based knowledge system, Backend code for time calculation 	|kartik@u.nus.edu|
|Tarun Rajkumar|A0198483L		|Initial survey for algorithm design, Algorithm Design, Question based knowledge system, Backend code for time calculation 	|kartik@u.nus.edu|


# SECTION 4: VIDEO INTRODUCTION
<a href="https://youtu.be/xhr5-ozRhjk" target="_blank"><img src="https://img.youtube.com/vi/xhr5-ozRhjk/0.jpg" 
alt="ITLMS" width="640" height="360" border="10" /></a>


# SECTION 5: USER GUIDE
To see this system in action, please follow the below steps. Once all one-time activities are handled correctly, the whole application can be run by just a simple command on command line interface.

System Requirements - 
A PC running macOS/Windows or Linux operating system with :
- Python3 (this system will be used as a server for execution of bots).
- A python env on above machine based on  file: requirements.txt
- PostgreSQL - https://www.postgresql.org/download/
- PostgreSQL server application -
    Recommended for macOS : PostgresApp(Free) - https://postgresapp.com
    Recommended for Windows/Linux : 
        DataGrip(Free) - https://www.jetbrains.com/datagrip/
        pgAdmin(Free) - https://www.pgadmin.org/download/
- Google Chrome - https://www.google.com/chrome/

Environment Setup (one-time process) - 
- Download and unzip the project to a path on disk without any spaces, like ‘~/development/ISA-IPA-2019-10-07-IS01FT-GRP-Kickers-Shoe_Me_The_Price’.
- Setup the PostgreSQL server and note the username and password. If using remote server, please note host, port as well.
- Add this information to file: configurations.ini located in the home folder, under the [DATABASE] tag.
- Create a new python virtual env OR using an existing, install dependencies from the requirements.txt file - pip3 install -r requirements.txt

Application execution - 
- Activate python env (if using a virtual env for this application)
- Activate postgres server from the server application
- Open terminal/command-line interface
- Goto home folder of the app - ISA-IPA-2019-10-07-IS01FT-GRP-Kickers-Shoe_Me_The_Price/
- Execute - “python3 initiate.py”

Example flows - 
Once the application is running, choose any of the two channels for shoe price utility - 
1. Web-interface
2. Mail service

1 Web-interface - 
- Go to http://127.0.0.1:5000/. This acts as a front-end where the user can request a query to the application. A form will be presented (figure A).
![alt text](https://github.com/karamjotsinghmalik/ISA-IPA-2019-10-07-IS01FT-GRP-Kickers-Shoe_Me_The_Price/blob/master/templates/UI.png)
Figure A : Web interface of the application

- Complete and submit the form. One can enter more than one shoe names. Press Enter after key-ing in every shoe-name- to make shoe-name chips. On completion, confirmation screen (Figure B) will be shown.
![alt text](https://github.com/karamjotsinghmalik/ISA-IPA-2019-10-07-IS01FT-GRP-Kickers-Shoe_Me_The_Price/blob/master/templates/Submit.png)
Figure B: Successful submission of request

- Once the request is successful and correct, the bots will execute on the hosting machine  and will mail the request user with appropriate details in response.

2. Mail service - 
- Compose & send a mail with the following details - 
    To - shoemetheprice@gmail.com
    Subject - [Gender] Shoe_Name_1, Shoe_Name2...
        E.g. 1 [M] Nike Air Max 1
        E.g. 2 [F] Nike Joyride, Nike Vapourmax
        E.g. 3 [M] Nike Free
- Once the request is successful and correct, the bots will execute on the hosting machine  and will mail the request user with appropriate details.

 Notes  - 
- It is advisable to let the machine execute the flows unaltered, meaning not to perform actions on the system which is being used as the server for this application. Also, advisable to not alter the  chrome browser execution window.
- Running the application from home folder is mandatory. Firstly, please reach the project’s home folder & only then run the application.

# SECTION 6: PROJECT REPORT
[https://github.com/karamjotsinghmalik/ISA-IPA-2019-10-07-IS01FT-GRP-Kickers-Shoe_Me_The_Price/blob/master/data/Project_Report_STMP_TheKickers.pdf]
