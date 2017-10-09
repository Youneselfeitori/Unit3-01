
# Created by: Younes Elfitori
# Created on: Oct 2017
# Created for: ICS3U
# This program makes a person guess a number and see if his guess is correct or incorrect

import ui

GUESSING_NUMBER = 5

def number_guess_touch_up_inside(sender):
    # check the number of students entered verses the constant above
    
    # input
    number_entered = int(view['your_guessing_number_textfield'].text)
    
    # process
    if number_entered == GUESSING_NUMBER:
        # output
        view['correct_label'].text = "right"
    #process
    if number_entered !=GUESSING_NUMBER:
       #output
       view['incorrect_label'].text = "wrong"
    
view = ui.load_view()
view.present('full_sheet')


