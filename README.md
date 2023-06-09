# Animal Hangman Game in Python
  
 ![Screenshot of the main screen in the terminal](https://cdn.discordapp.com/attachments/1049024982694498367/1114303161172234290/image.png) 
  
 Welcome to my animal themed hangman game.
 View the live project [here](https://hangman-kai.herokuapp.com/)
  
  
 ## Table of Contents
 * [User Experience (UX)](#user-experience-ux)
 * [Features](#features)
 * [Design](#design)
 * [Technologies Used](#technologies-used)
 * [Testing](#testing)
 * [Deployment](#deployment)
 * [Credits](#credits)
 
 
 ## User Experience (UX) 
  
 -   ### User stories 
  
     -   #### First Time User Goals 
         1. As a First Time User, I want to easily understand the main purpose of the site.  
         2. As a First Time User, I want to be able to easily interact with the site.
         3. As a First Time User, I want to be able to easily play another game or quit. 
  
     -   #### Returning User Goals 
  
         1. As a Returning User, I want to be able to access and view the game quickly and easily. 
         2. As a Returning User, I want to be able to guess new animals.

     -   #### Frequent User Goals 
  
         1. As a Frequent User, I want to be able to find different categories and/or difficulties to keep the game interesting. 
         2. As a Frequent User, I want to be able to save my score and compete against others in the leader board.
  
  
 ## Features 
  
 #### Existing Features 
  
 - _F01 Main Screen_ 
  
     - At the start of the game you will be directed to the main menu. 
     - From here you have three options to choose from.
  
 ![Screenshot of the main menu](https://cdn.discordapp.com/attachments/1049024982694498367/1114303426923335780/image.png) 
  
 - _F02 Menu_ 
  
     - The user must choose an option from the menu to continue. 
     - The user will see an error if they do not enter a valid option. 
  
 ![Screenshot of the options with a faulty input resulting in an error](https://cdn.discordapp.com/attachments/1049024982694498367/1114304344028872714/image.png) 
  
 - _F03 Ingame screen_ 
  
     - The user can see how many letters the randomly chosen animal contains.
     - The user can see which letters they have already used.
     - The user can see which letters have been guessed correctly
     - The user can see a hangman graphic indicating the current lives left. 
  
 ![Screenshots of the ingame screen after the input of all vowels](https://cdn.discordapp.com/attachments/1049024982694498367/1114304741082665070/image.png) 
  
 - _F04 End game screen_ 
  
     - The game ends on a victory or loss screen.
     - Underneith the current hangman picture the user can see the animal they were guessing.
     - From here the user can choose to play again or go back to the main menu.
 
 ![Screenshot of the victory screen](https://media.discordapp.net/attachments/1049024982694498367/1114305109602607144/image.png)
  
 - _F05 Submitting users score_ 

     - After playing a full game the user has the chance to submit their score.
     - The score will be saved to an external [google spread sheet](https://docs.google.com/spreadsheets/d/1JcjePGRrhzi-rMYGhRxBmu7SjgNCYYw3jtnmtMeGE4k/edit?usp=sharing).
     - After a short delay of 3 seconds the user gets send back to the main menu.

 ![Screenshot of user submitting their score](https://cdn.discordapp.com/attachments/1049024982694498367/1114306289766514698/image.png)

  - _F06 The leader board_

     - From the main manu the user can open the Highscores with the input "2"
     - Only the top ten players will be shown in the Highscores.

 ![Screenshot of the current Highscores](https://cdn.discordapp.com/attachments/1049024982694498367/1114307345477021696/image.png)   

 #### Future Features 
  
 - Categories and levels can be added for future development to ensure return users are getting value and finding new things to keep them interested. 
  
 ## Design 
  
 -   ### Imagery 
     -   The hangman images and screen layouts are all done by myself with the help of ChatGPT. The layout needed adjustments later on.
 ![Screenshot of the chat with ChatGPT](https://cdn.discordapp.com/attachments/1049024982694498367/1114149291041226792/image.png)
  
 -   ### Color 
     -   To choose a color directly from python I asked ChatGPT to give me all possible colors.
     -   I chose red for error messages and the Game Over in the end screen. Red is, because of its long wavelength, one of the most visible colors in the spectrum and therefore often used for warnings.
     -   I chose yellow to reveal the animal in the end screen because next to red it stands out the most.
     -   I chose green for the Congratulations message in the end screen since the color usually represents good things.
 ![Screenshot of the chat with ChatGPT](https://cdn.discordapp.com/attachments/1049024982694498367/1114314885594091621/image.png)
  
 -   ### Flow chart 
  
     ![Screenshot of the Flowchart](https://cdn.discordapp.com/attachments/978011606271262820/1114313489524215858/image.png) 
  
  
 ## Technologies Used 
  
 ### Languages Used 
  
 -   [Python](https://www.python.org/) 
  
 ### Python Modules 
  
 * [random](https://docs.python.org/3/library/random.html?highlight=random#module-random) - to select random words  
  
 * sleep from [time](https://docs.python.org/3/library/time.html?highlight=time#module-time) - to add a short timer into the clear function so the screen pauses for 2 seconds before clearing the terminal. 

 * [os](https://docs.python.org/3/library/os.html?highlight=os#module-os) - to add a clear function to refresh the terminal output.

 * [gspread](https://docs.gspread.org/en/latest/) - to add an external spread sheet in which the user scores are saved.

 * Credentials from [google.oauth2.service_account](https://google-auth.readthedocs.io/en/stable/reference/google.oauth2.credentials.html) - to be able to edit the external sheet.

  
 ### Frameworks, Libraries & Programs Used 
  
 This project used: 
  
 * [Git](https://git-scm.com/) for version control. 
  
 * [GitHub](https://github.com/) to store the project files. 
  
 * [Codeanywhere](https://app.codeanywhere.com/) as the IDE for development. 
  
 * [Heroku](https://www.heroku.com/home/) to deploy the website. 
  
 * [Lucidchart](https://www.lucidchart.com/) to create the flow chart. 
  
 * [ChatGPT](https://chat.openai.com/) to create layout and colors for the display. 
  
 ## Testing 
  
 ### Automated Validator Testing 
  
  - Code Institutes [Python Validator](https://pep8ci.herokuapp.com) 
  
     - latest test ~23.20 02.06.2023 
  
     ![Screenshot of the latest test results](https://cdn.discordapp.com/attachments/1049024982694498367/1114302621407268864/image.png) 
 
 ### Additional Testing Comments
 
 - Special letters like an umlaut (ä,ö,ü,å etc.) are valid letters from the alphabet and don't raise any error. This could be seen as validation error.
 
 
 ## Deployment 
 
 ### How this site was deployed 
 
 - Login to Heroku. 
 - On the Dashboards page click 'New' and select 'Create New App'. 
 - Enter a unique app name and select your region. Then click 'Create App' . 
 - On the next page displayed, click on the Settings tab. 
 - Click 'Reveal Config Vars' and enter PORT as key and 8000 as the value. Click 'Add'. 
 - In the Buildpack section, select Python from 'Add Buildpack' and Save. 
 - In the same Buildpack section, select Node.js from 'Add Buildpack' and Save.
 - Node.js needs to be below Python! If it isn't, drag it on the icon to the left.
 - Go to the Deploy tab and choose Gibhub as the deployment method. 
 - Find the repository name and connect. 
 - At the bottom of the page select to deploy manually or automatically. 
 - A link to the deployed page can be seen once deployment is complete. 
  
   The live link can be found here - [Hangman](https://hangman-kai.herokuapp.com/)  
  
 ### How to clone the repository
  
 - Go to the [hangman](https://github.com/KaiLangen96/hangman) repository on GitHub
 - Click the "Fork" button in the top right corner
  
 ### How to clone the repository
  
 - Go to the [hangman](https://github.com/KaiLangen96/hangman) repository on GitHub
 - Click the "Code" button to the right of the screen, click HTTPs and copy the link there
 - Open a GitBash terminal and navigate to the directory where you want to locate the clone
 - On the command line, type "git clone" then paste in the copied url and press the Enter key to begin the clone process
  
 ## Credits
  
 ### Code research
  
 - Initial inspiration to build hangman game came from my mentor, [Antonio Rodríguez](https://www.linkedin.com/in/antonio-rodr%C3%ADguez-bb9b99b7/).
 - Research ways to code hangman game Youtube:
 - [NeuralNine](https://www.youtube.com/watch?v=5x6iAKdJB6U)
 - [CBT Nuggest](https://www.youtube.com/watch?v=JNXmCOumNw0)
 - [Yujian Tang](https://www.youtube.com/watch?v=6G4n3oY5Svo)
 - [NPStation](https://www.youtube.com/watch?v=MtYw0RaZ4B0)
 - [Jenny's Lectures CS IT](https://www.youtube.com/watch?v=tMJbCWHAWQ4)
 - Clear terminal screen researched on [Stack Overflow](https://stackoverflow.com/questions/2084508/clear-terminal-in-python)
  
 ### Special Thanks
  
[Code Institude](https://codeinstitute.net/), for teaching me the language needed to create this page.

[w3schools](https://www.w3schools.com/), for so many helpful pages and tools to support learning python.

[Lucidchart](https://www.lucidchart.com/), helping me to create the flow chart.

[Antonio Rodríguez](https://www.linkedin.com/in/antonio-rodr%C3%ADguez-bb9b99b7/), as my mentor. He is an absolute legend and an immense help in creating my projects.
