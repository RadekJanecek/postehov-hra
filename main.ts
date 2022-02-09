let hra = false
let cheatoval = false
function main() {
    
    hra = false
    cheatoval = false
    basic.clearScreen()
    basic.pause(randint(3000, 10000))
    if (cheatoval == false) {
        hra = true
        basic.showLeds(`
. . # . .
. . # . .
# # # # #
. . # . .
. . # . .`)
        music.playTone(Note.C, 1500)
    }
    
}

control.inBackground(main)
basic.forever(function on_forever() {
    
    let p1 = pins.digitalReadPin(DigitalPin.P1)
    let p2 = pins.digitalReadPin(DigitalPin.P2)
    if (hra == true) {
        if (p1 == 0 && p2 == 1) {
            hra = false
            basic.showNumber(1)
            basic.pause(3000)
            main()
        }
        
        if (p1 == 1 && p2 == 0) {
            hra = false
            basic.showNumber(2)
            basic.pause(3000)
            main()
        }
        
        if (p1 == 0 && p2 == 0) {
            hra = false
            basic.showString("R")
            basic.pause(3000)
            main()
        }
        
    } else {
        if (p1 == 0 && p2 == 1) {
            hra = false
            basic.showString("B")
            cheatoval = true
            basic.pause(3000)
            main()
        }
        
        if (p1 == 1 && p2 == 0) {
            hra = false
            basic.showString("A")
            cheatoval = true
            basic.pause(3000)
            main()
        }
        
        if (p1 == 0 && p2 == 0) {
            hra = false
            basic.showString("C")
            cheatoval = true
            basic.pause(3000)
            main()
        }
        
    }
    
})
