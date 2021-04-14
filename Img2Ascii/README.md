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