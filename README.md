# Project information
Name: Measurement Converter
Student Name: Alexander Wilson

# Program Discription
This program is a simple measurement converter with a graphical user interface.
It allows the user to enter a number and convert it between inches and meters. The
user selects theype of conbersion using buttons, then clicks the "Convert" button to see the result displayed on the screen.

The app also includes a "Clear" button to reset everything and an "Exit" button to close the programe. There is basic error handling to make sure the user enters a valid positive number. If something is wrong ( like empty input or text instead of a number ), an error message pops up.

There's also an imaage included in the interface. If the image can;t be found, the program will show a message instead.

# How to Run the Programe
Run the convert.py file, from there put in a number you wish to convert then click on the the button to convert your inches to meters or meters to inches. Then click the convert button to see the converted number, from there you can clear what you put to do anouther conversion or click the Exit button to close the program.

# Attributions
I used the PySide6 and Python to build this assignment.

# Issues Encountered
One issue I ran into was getting the image to load correctly because of the file path. It took a bit of trial and error to fix that.