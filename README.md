# PygameUI
UI widgets for pygame

Currently have [button](#--button), [textbox](#--textbox) and [checkbox](#--checkbox) and [other](--other) functions

# - Button

## Create a button with `UI.Button(x,y,[optional parameters])`

## All paramters are optional except x and y location


### Arguments for `Button(x,y,w= 0,h=0,text="", calculateSize = False,background = (255,255,255),font = "Calibri", font_size = 30, text_colour = (0,0,0), outline = None,action = None, action_arg = None, surface = None, image = None, enlarge = False, enlarge_amount = 1.1)`


- x - x location of the button
- y - y location of the button
- w = 0 - width of the button, if 0, width will be calculated off length of text(text argument must be supplied)
- h=0 - height of the button, if 0, height will be calculated off height of text(text argument must be supplied)
- text="" - the text of the button, if button is image, no text will be put on screen
- calculateSize = False - when set to True, it will calculate the width and height, the width and height supplied as parameters will be added to calculated.
- background = (255,255,255) - background color of the button, does not affect image
- hover_background_color = None - this is the colour of the background when the mouse is over the button, by default it is the background supplied
- font = "Calibri" - the font of the text
- font_size = 30  - the font size of the text
- font_colour = (0,0,0) - the color of the text
- outline = None - Outline for the object, needs to be an `UI.Outline()` object
- action = None - function that gets called when button clicked
- action_arg = None - argument for action function
- surface = None - surface the button gets blit to, if left as None, it will use the window surface
- image = None - surface will be the button, using this means there can be no text, or outline
- enlarge = False - When enlarge is set to True, it will enlarge the image when the mouse is over the button, only when image is supplied
- enlarge_amount = 1.1 - the amount to enlarge by 
- dont_generate = False - when set to True, it will not create the images, this is handy when you cant supply the text and want to calculate the width and height. 

## Methods for Button

### To update the button, you can use `button.update()` => bool
This method draws the button and calculates if the mouse has clicked the button

return True if the user clicked on the button, If the mouse is held down on the button, only return True first frame

### To change the text of the button, use `button.Update_text(text)`
This method changes the text of the button and creates the surfaces for the button, if `calculateSize = True`, it will recalculate the width and height

### You can get the rect of the Button with `button.get_rect()` => pygame.Rect
This method returns a `pygame.Rect` object with the x, y, width and height of the button 

# - TextBox
  
## Create a Inputbox with `UI.TextBox(x, y, w, [optional parameters])`


### arguments for `TextBox(self,x, y, w, h = 0,lines = 1, text = "", background = None, font_size = 30, font = "Calibri", text_colour = (0,0,0), surface = None, margin = 2, cursor = True,Enter_action = None, calculateSize = False)`

all optional except x,y, width and height, it syas height it optional but if you want background, you need to supply height

- x - x position of the textBox
- y - y position of the textBox
- w - width of the textbox
- h = 0 - height of the textbox, when left as 0, it will use the font height, when calculateSize is True, this will be added to font height
- lines = 1 - amount of lines the textbox has/can type in
- text = "" - starting text for textbox
- background = False - background color
- font_size = 30 - font size of the text
- font = "Calibri" - font of the text
- text_colour = (0,0,0) - text color
- surface = None - the surface to blit to, if None is supplied, it will blit to window
- margin = 2 - the distance from when the letters start from the side of the textbox
- cursor = True - show a cursor
- Enter_action = None - a function that gets called when enter is pressed, no matter if there is more lines to write on
- calculateSize = False - when calculateSize is True, the height will be calculated and the height supplied will be added on top

## methods for textbox

### - `textbox.key_down(event)`
event is a pygame.event()
best way to do this is 
`for event in pygame.event.get()`

`    if e.type == pygame.KEYDOWN:`

`        textbox.key_down(event)`

### - `textbox.draw()`
draws the textbox

### - `textbox.get_rect()` => pygame.Rect
This method returns a `pygame.Rect` object with the x, y, width and height of the textbox

### - `textbox.get_lines(lines = -1, return_as_string = False)` => string or list
This method returns the text on a specific line or lines, by defualt, it returns all lines
The parameter `lines`, it the line or lines you want, this can be an integer of the line or a tuple of 2 integers that are the start and end lines 
e.g. 
    `get_lines()`, gets all lines  
    
     get_lines(lines = 2) gets 2nd line
    
     get_lines(lines = (0,2)) gets the 1st and 2nd line

The parameter `return_as_string` will return multiple lines as one string with `"\n"` representing a new line instead of a list

# - CheckBox

## Create a CheckBox with `CheckBox(x, y, w, [optional parameters])`

### arguments for `CheckBox(x,y,w,checked=False,background=(255,255,255),outline=None,surface=None,check_width = 2)`
- x - the x position of the checkbox
- y - the y position of the checkbox
- w - the width and height of the checkbox
- checked = False - this is if the checkbox is checked or not, False by default
- background = (0,0,0) - this is the background colour of the checkbox, white by default
- outline = None - this outlines the object, needs to be a `UI.Outline()` object
- surface = None - this is the surface to draw the checkbox on, if left as None, uses Window surface
- check_width = 2 - the thickness of the x when the checkbox is checked

## methods for CheckBox

### CheckBox.update()
this updates the checkbox and draws it on the screen

## To check whether the Checkbox is checked or not

you can check if the CheckBox is checked or not by using `Checkbox.checked` or by checking if it is True

e.g. `print(Checkbox.checked)

     if CheckBox:
     
         print("The checkbox is checked")
`

# Other Functions

## - Window(w,h) => pygame.Surface
this is a shorter way of typing `screen = pygame.display.set_mode((w,h))`

you can input a width and height, or in a tuple. If no width and height is supplied, it creates 500x500

e.g. 
` screen = Window(500,500) 
  screen = Window((500,500))
  screen = Window()
  `

## - update_all()
updates all widgets, easier than calling `widget.update()` on every widget 

## - curved_square(width, height, curve, color) => pygame.Surface
this creates a rectangle with curved corners.

width and height is the width and height of the rectangle

curve is the curve amount, 0 is 0 curve and 1 is full curve, giving a value above 1 or below 0 will result in a ValueError

color is the colour to draw it

returns the shape on a pygame.Surface.

