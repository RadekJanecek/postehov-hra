pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)
hra = False
cheatoval1 = False
cheatoval2 = False
cheatoval = False
pismeno = ""
def main():
    global hra, cheatoval1, cheatoval2
    hra = False
    cheatoval1 = False
    cheatoval2 = False
    basic.clear_screen()
    basic.pause(randint(3000, 10000))
    hra = True
    basic.show_leds("""\n. . # . .\n. . # . .\n# # # # #\n. . # . .\n. . # . .""")
    music.play_tone(Note.C, 1500)
control.in_background(main)

def on_forever():
    global cheatoval1, hra, cheatoval2, cheatoval
#    p1 = pins.digital_read_pin(DigitalPin.P1)
#    p2 = pins.digital_read_pin(DigitalPin.P2)
    p1 = input.pin_is_pressed(TouchPin.P1)
    p2 = input.pin_is_pressed(TouchPin.P2)
    if cheatoval1 or cheatoval2:
        cheatoval = True
    if cheatoval1:
        pismeno = "A"
    if cheatoval1 and cheatoval2:
        pismeno = "C"
    if cheatoval2:
        pismeno = "B"
    if not hra:
        if p1:
            cheatoval1 = True
        if p2:
            cheatoval2 = True
    if hra:
        if p1 and p2:
            hra = False
            basic.show_string("R")
            basic.pause(3000)
            control.reset()
        elif p1:
            hra = False
            basic.show_number(1)
            basic.pause(3000)
            control.reset()
        elif p2:
            hra = False
            basic.show_number(2)
            basic.pause(3000)
            control.reset()
        if cheatoval:
            hra = False
            basic.show_string(pismeno)
            basic.pause(3000)
            control.reset()
basic.forever(on_forever)