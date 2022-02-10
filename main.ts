pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
let hra = false
let cheatoval1 = false
let cheatoval2 = false
let cheatoval = false
let pismeno = ""
control.inBackground(function main() {
    
    hra = false
    cheatoval1 = false
    cheatoval2 = false
    basic.clearScreen()
    basic.pause(randint(3000, 10000))
    hra = true
    basic.showLeds(`
. . # . .
. . # . .
# # # # #
. . # . .
. . # . .`)
    music.playTone(Note.C, 1500)
})
basic.forever(function on_forever() {
    let pismeno: string;
    
    //     p1 = pins.digital_read_pin(DigitalPin.P1)
    //     p2 = pins.digital_read_pin(DigitalPin.P2)
    let p1 = input.pinIsPressed(TouchPin.P1)
    let p2 = input.pinIsPressed(TouchPin.P2)
    if (cheatoval1 || cheatoval2) {
        cheatoval = true
    }
    
    if (cheatoval1) {
        pismeno = "A"
    }
    
    if (cheatoval1 && cheatoval2) {
        pismeno = "C"
    }
    
    if (cheatoval2) {
        pismeno = "B"
    }
    
    if (!hra) {
        if (p1) {
            cheatoval1 = true
        }
        
        if (p2) {
            cheatoval2 = true
        }
        
    }
    
    if (hra) {
        if (p1 && p2) {
            hra = false
            basic.showString("R")
            basic.pause(3000)
            control.reset()
        } else if (p1) {
            hra = false
            basic.showNumber(1)
            basic.pause(3000)
            control.reset()
        } else if (p2) {
            hra = false
            basic.showNumber(2)
            basic.pause(3000)
            control.reset()
        }
        
        if (cheatoval) {
            hra = false
            basic.showString(pismeno)
            basic.pause(3000)
            control.reset()
        }
        
    }
    
})
