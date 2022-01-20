pins.touchSetMode(TouchTarget.P1, TouchTargetMode.Capacitive)
pins.touchSetMode(TouchTarget.P2, TouchTargetMode.Capacitive)
basic.forever(function on_forever() {
    console.logValue("P1", input.pinIsPressed(TouchPin.P1))
    console.logValue("P2", input.pinIsPressed(TouchPin.P2))
    let čekání = randint(3000, 10000)
    control.inBackground(function run_parallel() {
        basic.pause(čekání)
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            `)
        music.playTone(Note.C, music.beat())
    })
    if (input.pinIsPressed(TouchPin.P1)) {
        basic.showNumber(1)
    }
    
    if (input.pinIsPressed(TouchPin.P2)) {
        basic.showNumber(2)
    }
    
})
