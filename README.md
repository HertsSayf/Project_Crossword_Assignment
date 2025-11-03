# Project Crossword Assignment
This is the repo for our crossword project it is made from a team of four. Rayyan, Fayaaz, Sayfullah, and Kalid.
## Project overview
Our group has chosen to create a web-based crossword game designed for children aged 10-14 (although we're planning to make a separate version for adults). The aim is to make an educational and fun tool that helps the users improve their vocabulary, spelling and problem solving skills through the interactive gameplay.

## Project specification
The overall aim of this project is to design an engaging, educational web-based crossword that’s aimed at children aged 10 – 14 years of age. Our system will allow players to input their answers into a designated bar along with having numbered squares which would correspond to clues on the side. These clues would be revealed and answered by clicking on the appropriate number. Users will be able to type answers into a small bar and if correct will be added to the grid. If the input is incorrect the system will let the user know that what they typed was wrong and that answer wont be added to the grid. This application will be developed using HTML, CSS and python. The finished product will be deployed via GitHub Pages.

## Target audience
 - Age group: 10 - 14 years old
 - Purpose: To help kids strengthen their fundamentals like vocabulary and spelling skills through an interactive experience

## Project Design and objectives
The game is going to feature a simple and visually clear interface with:
  - A grid layout
  - Readable text
  - Easy colour-coded navigation between clues
Feedback will be helpful, guiding players through the crossword.
Once we get the game up and running, we plan to add 2 extra difficulties:
  - Easy: shorter simpler words (tailored for students)
  - Hard: Longer more challenging words (better for teachers)


## User profiles:
<img width="374" height="543" alt="image" src="https://github.com/user-attachments/assets/4086df15-c5d0-4309-822a-a725b45cf385" />


<img width="380" height="543" alt="image" src="https://github.com/user-attachments/assets/24c46e00-629f-4a11-9e7a-5ab7c812970a" />


## Functional and nonfuncional requirments 

 ### Functional 
  - The crossword will be in a grid layout where players can see the length of the word by counting the number of cells
  - Players can enter their answer into an input bar below the grid
  - when a player inputs an answer, either a completion message  if correct or an error message if incorrect will appear 
  - Once all words are guessed correctly, a final completion message will pop up to confirm the puzzle is complete
  - Users will have the option to restart the game at any time by pressing the reset button
  - a difficulty selection including easy, medium and hard which would vary the grid sizes and complexity of the words

## Nonfunctional 
  - The interface will be simple, clear and easy to navigate so users can quickly understand how to play
  - Designed to be used by 10-14 year olds however by adding a difficulty system, older more intelligent people can play
  - A simple and school appropriate design will keep the game engaging without being distracting
  - the system will be reliable and robust


## System requirments 

### Hardware
 - Dual core CPU
 - Minimum 4GB RAM
 - Minimum resolution of 1280×720
 - Keyboard and Mouse

### Software
 - Windows 10 or newer
 - MacOS 10.15 or newer
 - Google chrome
 - Microsoft edge
 - Safari
 - HTML
 - CSS
 - Python Flask 
 - Microsoft Visual Studio Code
  

## Mock-ups :
-	<img width="936" height="742" alt="image" src="https://github.com/user-attachments/assets/f5393e46-f750-4a3c-ae62-8876424ce237" />
## Easy Mode Grid Format Mock-up:
- <img width="902" height="775" alt="image" src="https://github.com/user-attachments/assets/6d3e86ad-d663-4927-8a36-ddd9a281d497" />
## Medium Mode Grid Format Mock-up
- <img width="304" height="229" alt="image" src="https://github.com/user-attachments/assets/02cc6bcb-8b07-4c44-b6d5-2151f1f2384a" />

## Hard Mode Grid Format Mock-up:
<img width="413" height="358" alt="image" src="https://github.com/user-attachments/assets/27187cd1-97cc-4c6d-a62c-72cf1edb88bf" />





### Basic storyboard:
-	<img width="1131" height="611" alt="image" src="https://github.com/user-attachments/assets/d52438ce-62c4-4bbd-bd01-dd383fe9ac9b" />



	## Potential risks to the project’s success: (not including time management)

  1. Technical Knowledge, we all have limited knowledge and experience in python and coding in general. This could cause delays and issues in development as we would spend time trying to figure   out how to implement the code and our ideas. This is the main issue for our project due to lack of knowledge and experience we may not have it to a great quality.
   
  2. Trying to add optional features and things to make the game better will be hard for us due to the lack of time given to complete the project. If we spend too many resources on one feature,   then we won't be able to focus on important parts and developing the functionality of the game
    
  3. Testing issues may occur due to various devices not being compatible with our game. Also, we will not be able to receive real user feedback from our target audience which leads to less       usability improvements.
   
  4. Our reliance on external libraries might cause compatibility issues or even if we use external images or other things there could be an issue due to licensing. Also, another issue we will   face is conflicting changes on GitHub when we all commit changes at the same time.


## Software development strategy

Our software development strategy is the spiral methodology, which contains elements of other methods such as waterfall with its clearly defined phases, combined with an iterative development process. It is great for projects that contain a risk element to it, largely used for complicated, expensive projects. The main advantage of the spiral model is the “coil with many loops”. When the spiral model is visually presented, you can see these loops. This is to show the iterative process that you can go back to prior stages even after moving on and correct any mistakes and improve further. This means we can gradually release stages of the new system and make refinements, too, as time passes.


- **Overall test plan Submitted in the format of a table in a seperate file**

## Flowchart 
<img width="464" height="202" alt="image" src="https://github.com/user-attachments/assets/3d128cad-94f4-4cc9-8c1d-483eb2894bac" />


## Game State Management 
Our crossword game follows a simple system to track the players these sates are :
### Start  - The game begins by loading up the easiest version of the crosswords along with clues by the side. All words are hidden until guessed corectly.
### Win - Win will be achieved when the user manages to complete and solve all the words in the grid correctly. We have implemented a timer that goes up so users can time how quickly they complete the crossword.
### lose - Since the crossword does not have a lives system or a time limit to complete the crossword in, it does not have a lose state. However, the game does display an incorrect message when the user inputs an incorrect word.
### Draw - this state does not apply to our crossword however it could be added if we include a multiplayer feature in the future however that would require more time and resources.

## Contribution to Project
### Rayyan:
- Delegated tasks to other members and gave them deadlines for completion
- Basic Storyboard
- User and System Requirements
- User Profiles
- Refined the html code and added new features
- Refined the Pyhton code and added new features
- Added comments onto the html
- Added comments onto the Python 
- Done game state management
- Added a timer feature to the game
- Added numbers to the grid to coorelate to the word
- Done the whole test plan, regularly updating it 
- medium and hard crossword grid mock-ups
- Tested different versions of the code
- Included screenshots of results of tests
- created meduim clues
- created hard clues
- Wrote functional requirments
- Wrote non functional requirments
- Wrote software requirments
- Wrote Hardware requirments
- Wrote the overall project specification 

### Sayfullah:
- Created Git Hub repository
- Created the Flask link to python file
- Connected the backend with the HTML template using Flask’s render_template() for live updates in the web app.
- Developed Main Game, Including the Easy, Medium and Hard Modes:
- Created all the functions and backend logic for the crossword application using Python and Flask
- Developed the build_grid() function to dynamically generate crossword grids and the home() route to manage gameplay, user input, and difficulty levels.
- Wrote and organised all clue dictionaries and word lists for the easy, medium, and hard crosswords.
- Developed Main Game and Game modes HTML Code for the website
- Created working crossword.py and index.html uptill the modes features
- Designed the game state system to handle guessed words and difficulty switching.
- Tested out to see core functionality of the game
- Implemented word validation, clue checking, and grid updating so that correct guesses reveal automatically.
- Created mock ups
- Visual representation of the User Profiles
- Created Crossword grids on excel to find coords
- Easy clues crossword grid mock-ups
- Addeded in depth Python comments
  
### Fayaaz:
- Identifying and ranking potential risks to projects success
- Software development strategy
- Original basic version of game on main py file
- Clues for the game
- Presentaion for the crossword game

### Kalid:
- Flowchart
- Some code for main py file

## Problems fixed with code 
<img width="2044" height="1093" alt="Screenshot 2025-11-03 012625" src="https://github.com/user-attachments/assets/914d926a-3177-46c1-941d-197121c0e88f" />
### The code had 22 probolems and now is fixed
<img width="2557" height="1388" alt="Screenshot 2025-11-03 012851" src="https://github.com/user-attachments/assets/3e8becdf-776f-482c-ad21-c041fe1b8557" />
