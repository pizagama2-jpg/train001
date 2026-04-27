def on_forever():
    basic.show_number(pins.analog_read_pin(AnalogPin.P0))
    pins.analog_write_pin(AnalogPin.P15, 300)
    basic.pause(1000)
    pins.analog_write_pin(AnalogPin.P15, 0)
    basic.pause(1000)
basic.forever(on_forever)
