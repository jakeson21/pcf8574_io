### **Python driver for PCF8574 8bit IO Expander board**
Developed for the Raspberry Pi, requires python-smbus2 package to access the I2C bus.

Tested on raspberry pi 3b plus with two PCF8574 boards.


First install smbus2 using:
`pip3 install smbus2` 

then install the actual package using:
`pip3 install pcf8574-io`


Usage Example:
```python
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

p1.pin_mode_all("OUTPUT")
for v in range(257):
    p1.write_all(v)

```

The board been used:
![alt text](https://image.made-in-china.com/2f0j00CbvRKwBGGecA/Pcf8574-Io-Expansion-Board-I-O-Expander-I2c-Bus-Evaluation-Development-Module.jpg)

**Link**
[pcf8574-io](https://pypi.org/project/pcf8574-io/)


