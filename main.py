pins.touch_set_mode(TouchTarget.P1, TouchTargetMode.CAPACITIVE)
pins.touch_set_mode(TouchTarget.P2, TouchTargetMode.CAPACITIVE)
def on_forever():
    console.log_value("P1", input.pin_is_pressed(TouchPin.P1))
    console.log_value("P2", input.pin_is_pressed(TouchPin.P2))
    čekání = randint(3000, 10000)
    def run_parallel():
        basic.pause(čekání)
        basic.show_leds("""
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            """)
        music.play_tone(Note.C, music.beat())
    control.in_background(run_parallel)
    
    if input.pin_is_pressed(TouchPin.P1) == True and input.pin_is_pressed(TouchPin.P2) == False:
        basic.show_number(1)
    if input.pin_is_pressed(TouchPin.P2) == True and input.pin_is_pressed(TouchPin.P1) == False:
        basic.show_number(2)
    if input.pin_is_pressed(TouchPin.P1) == True and input.pin_is_pressed(TouchPin.P2) == True:
        basic.show_string("R")
basic.forever(on_forever)