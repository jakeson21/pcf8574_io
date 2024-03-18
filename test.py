import pcf8574_io

# You can use up to 8 PCF8574 boards
# the board will start in input mode
# the pins are HIGH in input mode
p1 = pcf8574_io.PCF(0x20)

# You can use multiple boards with different addresses
#p2 = pcf8574_io.PCF(0x21)

# p0 to p7 are the pins name
# INPUT or OUTPUT is the mode
p1.pin_mode("p0", "INPUT")
print(p1.read("p0"))

# You can write and read the output pins
# use HIGH or LOW to set the pin, HIGH is +3.3v LOW is 0v
p1.pin_mode("p7", "OUTPUT")
p1.write("p7", "LOW")
p1.write(7, 1)
print(p1.read("p7"))
print(p1.read(7))

# Additional you can do the following
p1.set_i2cBus(1) # Set i2c bus number to use (default=1)
p1.get_i2cBus() # Return the current i2c bus
print(p1.get_pin_mode("p7")) # returns string OUTPUT, INPUT
print(p1.is_pin_output("p7")) # returns boolean True, False
print(p1.get_all_mode()) # returns list of all pins ["OUTPUT","INPUT",...etc]
print(p1.read_all()) # returns all pin states as a byte


