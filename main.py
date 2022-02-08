hra = False
cheatoval = False
def main():
    global hra, cheatoval
    basic.clear_screen()
    basic.pause(randint(3000, 10000))
    if cheatoval == False:
        hra = True
        basic.show_leds("""\n. . # . .\n. . # . .\n# # # # #\n. . # . .\n. . # . .""")
        music.play_tone(Note.C, 1500)
control.in_background(main)

def on_forever():
    global cheatoval, hra
    p1 = pins.digital_read_pin(DigitalPin.P1)
    p2 = pins.digital_read_pin(DigitalPin.P2)
    if hra == True:
        if p1 == 0 and p2 == 1:
            hra = False
            basic.show_number(1)
            basic.pause(3000)
            control.reset()
        if p1 == 1 and p2 == 0:
            hra = False
            basic.show_number(2)
            basic.pause(3000)
            control.reset()
        if p1 == 0 and p2 == 0:
            hra = False
            basic.show_string("R")
            basic.pause(3000)
            control.reset()
    else:
        if p1 == 0 and p2 == 1:
            hra = False
            basic.show_string("B")
            cheatoval = True
            basic.pause(3000)
            control.reset()
        if p1 == 1 and p2 == 0:
            hra = False
            basic.show_string("A")
            cheatoval = True
            basic.pause(3000)
            control.reset()
        if p1 == 0 and p2 == 0:
            hra = False
            basic.show_string("C")
            cheatoval = True
            basic.pause(3000)
            control.reset()
basic.forever(on_forever)