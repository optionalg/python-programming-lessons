'''
Berit Homework -
write 2 programs, one that converts Celsius degrees to Fahrenheit, and another one that does the opposite conversion. Each program must do the following:
- Ask the user to enter a temperature in Celsius or Fahrenheit degrees
- Calculate the result and print it in a sentence
- add a comment at the beginning of each file with your name and a description of what your program does
- You can find the conversion formula on Google (research is part of a programmer's job!)
- please don't google for a programming solution directly, that won't help you train your new skill :slightly_smiling_face:
- please send me 2 python files on Slack when you're done
'''

temperature_celsius = int(input("Please enter the temperature in Celsius: "))
temperature_fahrenheit = (temperature_celsius * 9 / 5) + 32
                        
                            
print ("Your temperature converts to " + str(temperature_fahrenheit) + " Fahrenheit")
