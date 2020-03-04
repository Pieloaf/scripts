# Scripts
This repo just contains some of my random scripts.
It will be updated with any scripts I find useful or fun.
Feel free to use and modify them :)

---

## 1. Img2Ascii ##
This script can be used to convert an image to ASCII art. It is still being worked for QoL improvments (Error Handling, Brightness&Contrast Adjustments and Dealing with Transparent Backgrounds Better) but for the most part is done.

```  ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! 
! { { { { { { { { { { { { { { { { { { { { { { { { { { { { { { { { 
! { { { { { { { { { { { ( c C w d q Q z | { { { { { { { { { { { { 
! { { { { { { { { { c h % % % % % % % % % * U 1 { { { { { { { { { 
! { { { { { { { r # % % % % % % % % % % % % % W c { { { { { { { { 
! { { { { { { L % % % % % % % % % % % % % % % % % q 1 { { { { { { 
! { { { { { w % % % % % % % % % % % % % % % % % % % h 1 { { { { { 
! { { { { O % % % % % % % % % % % % % % % % % % % % % k { { { { { 
! { { { v % % % % 0 a % % % % % % % % % % % # O W % % % L { { { { 
! { { ( 8 % % % h { { f h W k O Q O b M # n { { Z % % % % t { { { 
! { { 0 % % % % m { { { { { { { { { { { { { { { Y % % % % b { { { 
! { 1 8 % % % % d { { { { { { { { { { { { { { { Q % % % % % / { { 
! { v % % % % % h { { { { { { { { { { { { { { { Z % % % % % L { { 
! { w % % % % % | { { { { { { { { { { { { { { { { W % % % % o { { 
! { * % % % % p { { { { { { { { { { { { { { { { { L % % % % % { { 
! { % % % % % U { { { { { { { { { { { { { { { { { x % % % % % ( { 
! { % % % % % U { { { { { { { { { { { { { { { { { x % % % % % t { 
! { % % % % % C { { { { { { { { { { { { { { { { { n % % % % % t { 
! { % % % % % p { { { { { { { { { { { { { { { { { L % % % % % ( { 
! { o % % % % 8 1 { { { { { { { { { { { { { { { { * % % % % % { { 
! { Z % % % % % L { { { { { { { { { { { { { { { v % % % % % h { { 
! { u % % % % % % c { { { { { { { { { { { { { r 8 % % % % % C { { 
! { { & % % b 8 % % d x { { { { { { { { { f w % % % % % % % | { { 
! { { C % % q J M % % % % k { { { { { w % % % % % % % % % q { { { 
! { { 1 W % % w Z 8 % % % u { { { { { / % % % % % % % % 8 | { { { 
! { { { x % % % / 0 * # k { { { { { { { % % % % % % % % U { { { { 
! { { { { L % % o ( t z j { { { { { { { % % % % % % % p { { { { { 
! { { { { { 0 % % 8 b m k { { { { { { { % % % % % % d { { { { { { 
! { { { { { { X 8 % % % % { { { { { { { % % % % % Q { { { { { { { 
! { { { { { { { / k % % % { { { { { { { % % % * r { { { { { { { { 
! { { { { { { { { { j q a { { { { { { { d b u { { { { { { { { { { 
! { { { { { { { { { { { { { { { { { { { { { { { { { { { { { { { { 
```


## 2. C++ Class Generator ##
This script was written to automatically generate base cpp class files with optional accessors and mutators when given the class name, data members and inheritance. There is no error handling, but the functionality is there complete.

## 3. Menu Class ##
Menu Class for python scripts to create simple CLI Menu Systems:
#### Syntax: ####
``` 
mainMenu = Menu(["New File", "Options", "Quit"],[func1, func2, func3])
```
Each option is mapped to the function in the same position in the function array. The menu can contain as many options as desired. The option is selected by entering the coressponding number

#### Output: ####
```
1. New File
2. Options
3. Quit
```
