pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
hra = False
cheatoval1 = False
cheatoval2 = False
def main():
    global hra, cheatoval1, cheatoval2
    hra = False
    cheatoval = False
    basic.clear_screen()
    basic.pause(randint(3000, 10000))
    if cheatoval == False:
        hra = True
        basic.show_leds("""\n. . # . .\n. . # . .\n# # # # #\n. . # . .\n. . # . .""")
        music.play_tone(Note.C, 1500)
    if cheatoval1 == True and cheatoval2 == True:
        hra = False
        basic.show_string("C")
        basic.pause(3000)
        main()
    if cheatoval1 == True and cheatoval2 == False:
        hra = False
        basic.show_string("A")            
        basic.pause(3000)
        main()
    if cheatoval1 == False and cheatoval2 == True:
        hra = False
        basic.show_string("B")
        basic.pause(3000)
        main()
control.in_background(main)

def on_forever():
    global cheatoval1, hra, cheatoval2
#    p1 = pins.digital_read_pin(DigitalPin.P1)
#    p2 = pins.digital_read_pin(DigitalPin.P2)
    p1 = input.pin_is_pressed(TouchPin.P1)
    p2 = input.pin_is_pressed(TouchPin.P2)
    if hra == True:
        if p1 == True and p2 == False:
            hra = False
            basic.show_number(1)
            basic.pause(3000)
            main()
        if p1 == False and p2 == True:
            hra = False
            basic.show_number(2)
            basic.pause(3000)
            main()
        if p1 == True and p2 == True:
            hra = False
            basic.show_string("R")
            basic.pause(3000)
            main()
    else:
        if p1 == True and p2 == False:
            cheatoval2 = True
        if p1 == False and p2 == True:
            cheatoval1 = True
        if p1 == True and p2 == True:
            cheatoval1 = True
            cheatoval2 = True
basic.forever(on_forever)