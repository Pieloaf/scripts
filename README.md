# Scripts
This repo just contains some of my random scripts.
It will be updated with any scripts I find useful or fun.
Feel free to use and modify them :)

---

## 1. Img2Ascii ##
This script can be used to convert an image to ASCII art. It is still being worked for QoL improvments (Error Handling, Brightness&Contrast Adjustments and Dealing with Transparent Backgrounds Better) but for the most part is done.

``` 
  ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ 
  ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ▒ ▒ ▒ ▓ ▒ ▒ ▒ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ 
  ░ ░ ░ ░ ░ ░ ░ ░ ░ ▒ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ 
  ░ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ ░ ░ ░ ░ ░ 
  ░ ░ ░ ░ ░ ░ ▒ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ ░ ░ ░ ░ 
  ░ ░ ░ ░ ░ ▒ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ░ ░ ░ ░ ░ ░ 
  ░ ░ ░ ░ ▒ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ░ ░ ░ ░ ░ 
  ░ ░ ░ ░ ▓ ▓ ▓ ▓ ▒ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▒ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ ░ 
  ░ ░ ░ ▓ ▓ ▓ ▓ ▓ ░ ░ ░ ▓ ▓ ▓ ▒ ▒ ▒ ▓ ▓ ▓ ░ ░ ░ ▒ ▓ ▓ ▓ ▓ ░ ░ ░ ░ 
  ░ ░ ▒ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ▒ ▓ ▓ ▓ ▓ ▓ ░ ░ ░ 
  ░ ░ ▓ ▓ ▓ ▓ ▓ ▓ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ▒ ▓ ▓ ▓ ▓ ▓ ░ ░ ░ 
  ░ ░ ▓ ▓ ▓ ▓ ▓ ▓ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ▒ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ 
  ░ ▒ ▓ ▓ ▓ ▓ ▓ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ▓ ▓ ▓ ▓ ░ ░ 
  ░ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ▒ ▓ ▓ ▓ ▓ ▓ ░ ░ 
  ░ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ▓ ▓ ▓ ░ ░ 
  ░ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ▓ ▓ ▓ ░ ░ 
  ░ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ▓ ▓ ▓ ░ ░ 
  ░ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ▒ ▓ ▓ ▓ ▓ ▓ ░ ░ 
  ░ ▓ ▓ ▓ ▓ ▓ ▓ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ▓ ▓ ▓ ▓ ░ ░ 
  ░ ▒ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ▓ ▓ ▓ ▓ ░ ░ 
  ░ ░ ▓ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ 
  ░ ░ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ▒ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ░ ░ ░ 
  ░ ░ ▒ ▓ ▓ ▒ ▒ ▓ ▓ ▓ ▓ ▓ ▓ ░ ░ ░ ░ ░ ▒ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ 
  ░ ░ ░ ▓ ▓ ▓ ▒ ▒ ▓ ▓ ▓ ▓ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ░ ░ ░ ░ 
  ░ ░ ░ ░ ▓ ▓ ▓ ░ ▒ ▓ ▓ ▓ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ ░ 
  ░ ░ ░ ░ ▒ ▓ ▓ ▓ ░ ░ ▒ ░ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ ░ ░ 
  ░ ░ ░ ░ ░ ▒ ▓ ▓ ▓ ▓ ▒ ▓ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ▓ ▓ ▓ ▓ ▓ ░ ░ ░ ░ ░ ░ 
  ░ ░ ░ ░ ░ ░ ▒ ▓ ▓ ▓ ▓ ▓ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ▓ ▓ ▓ ▒ ░ ░ ░ ░ ░ ░ ░ 
  ░ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ▓ ▓ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ▓ ▓ ░ ░ ░ ░ ░ ░ ░ ░ ░ 
  ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ▒ ▓ ░ ░ ░ ░ ░ ░ ░ ▓ ▓ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ 
  ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ ░ 

```


## 2. C++ Class Generator ##
This script was written to automatically generate base cpp class files with optional accessors and mutators when given the class name, data members and inheritance. There is no error handling, but the functionality is there complete.

## 3. Menu Class ##
Menu Class for python scripts to create simple CLI Menu Systems:
#### Syntax: ####
``` 
#Menu Object Declaration:
mainMenu = Menu(["New File", "Options", "Quit"],[func1, func2, func3])

#Displaying Menu and Getting User Input:
main.choice(input(main))
```
Each option is mapped to the function in the same position in the function array. The menu can contain as many options as desired. The option is selected by entering the coressponding number

#### Output: ####
```
1. New File
2. Options
3. Quit
```
## 4. Stream Count Down and Loading Bar ##
Python script that takes an input number of mins and counts down until done. A progress bar also fills up until timer is done. Finally the text "Starting Soon..." has the dots increment to 3 and reset, one dot every second. Each of these are written to a text file and updated once a second that OBS can then read from and display on screen:
![](images/countdown.gif)

## 5. Directory Divider ## 
*Still WIP* I had music I wanted to burn to a disc it was 1GB but the CD only held 700MB rather than having one full disc and one nearly blank disc, I wrote the script to divide the folder in half, into a disc one and disc two folder. I could burn each folder to two seperate discs and have each disc approx. the same length. Once I finish my exams I hope to make it more usable in other situations.
