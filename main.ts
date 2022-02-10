pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
let hra = false
let cheatoval1 = false
let cheatoval2 = false
function main() {
    
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
}

control.inBackground(main)
basic.forever(function on_forever() {
    
    //     p1 = pins.digital_read_pin(DigitalPin.P1)
    //     p2 = pins.digital_read_pin(DigitalPin.P2)
    let p1 = input.pinIsPressed(TouchPin.P1)
    let p2 = input.pinIsPressed(TouchPin.P2)
    if (hra == true) {
        if (p1 == true && p2 == false) {
            hra = false
            basic.showNumber(1)
            basic.pause(3000)
            main()
        }
        
        if (p1 == false && p2 == true) {
            hra = false
            basic.showNumber(2)
            basic.pause(3000)
            main()
        }
        
        if (p1 == true && p2 == true) {
            hra = false
            basic.showString("R")
            basic.pause(3000)
            main()
        }
        
        if (cheatoval1 == true && cheatoval2 == true) {
            hra = false
            basic.showString("C")
            basic.pause(3000)
            main()
        }
        
        if (cheatoval1 == true && cheatoval2 == false) {
            hra = false
            basic.showString("A")
            basic.pause(3000)
            main()
        }
        
        if (cheatoval1 == false && cheatoval2 == true) {
            hra = false
            basic.showString("B")
            basic.pause(3000)
            main()
        }
        
    } else {
        if (p1 == true && p2 == false) {
            cheatoval1 = true
        }
        
        if (p2 == true && p1 == false) {
            cheatoval2 = true
        }
        
    }
    
})
