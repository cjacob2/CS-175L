#CS175L
#Conor Jacob
#TemperatureConversions

def main():
    controlLoop()

def convertToKelvin(fahrenheit):
    #Take in the fahrenheit temp as an argument
    #Convert Fahrenheit to Kelvin
    #return Kelvin
    f_kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return f_kelvin
    

def convertToCentigrade(fahrenheit):
    #Take in the fahrenheit temp as an argument
    #Convert Fahrenheit to Centigrade
    #return Centigrade
    f_celsius = (fahrenheit - 32) / 1.8
    return f_celsius
    

def doConversion():
    #getFahrenheit(), get back Fahrenheit
    #convertToKelvin(), send Fahrenheit get back Kelvin
    #ConvertToCentigrade, sends Fahrenheit gets back Centigrade
    #prints for example: 'Fahrenheit: xx Kelvin xx Centigrade: xx'
    fahrenheit = getFahrenheit()
    f_kelvin = convertToKelvin(fahrenheit)
    f_celsius = convertToCentigrade(fahrenheit)
    print(f"Fahrenheit: {fahrenheit} Kelvin: {f_kelvin:.2f} Centigrade: {f_celsius:.2f}")

def repeat():
    #Inputs How many conversions would you like to do this time?
    #for x in range how many
        #doConversion()
    while True:
        try:
            how_many = int(input("How many conversions would you like to do this time? "))
            for i in range(how_many):
                doConversion()
            break
        except ValueError:
            print("Incorrect input. Enter a number.")
            
def controlLoop():
    #Inputs 'Do you want to do some conversions(Yes or No)?'
    #if 'yes' repeat()
            while True:
                control_int= input('Do you want to do some conversions(Yes or No)? ').lower()
                if control_int == "yes":
                    repeat()
                elif control_int == "no":
                    print("Conversions Complete!")
                    break
                else:
                    print("Incorrect inpout try again")
            
def getFahrenheit():
    #Inputs 'Enter Fahrenheit temperature (must be -50 to 130):
    #(validation loop)'Please re-enter'
    #return Fahrenheit
    while True:
        fahrenheit = int(input('Enter Fahrenheit temperature (must be -50 to 130): '))
        if -50<=fahrenheit<=130 :
            return fahrenheit
        else:
            print("Please re-enter")
        
    

# This code will call the 'main' function if the entire program was run.
if __name__ == '__main__':
    main()
