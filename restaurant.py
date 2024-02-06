#CS175
#Conor Jacob
#restaurant
def run_again():
    again = input("Would you like to run again?(Yes/No) ").lower()
    if again == "yes":
        run = True
    else:
        exit()
run = True
while run:
    veg = input("Is anyone in your party vegetarian?(Yes/No) ").lower()
    vegan = input("Is anyone in your party vegan?(Yes/No) ").lower()
    gluten = input("Is anyone in your party gluten-free?(Yes/No) ").lower()
    if veg == "no" and vegan == "no" and gluten == "no":
        print("Here are your restaurant choices." +
              "\nJoe's Gourmet Burgers" +
              "\nMama's Fine Italian" +
              "\nMain Street Pizza Company"+
              "\nCorner Cafe"+
              "\nThe Chef's Kitchen")
        run_again()
    elif veg == "yes" and vegan == "no" and gluten == "no":
        print("Here are your restaurant choices." +
              "\nMama's Fine Italian" +
              "\nMain Street Pizza Company"+
              "\nCorner Cafe"+
              "\nThe Chef's Kitchen")
        run_again()
    elif veg == "no" and vegan == "no" and gluten == "yes":
        print("Here are your restaurant choices." +
              "\nMain Street Pizza Company"+
              "\nCorner Cafe"+
              "\nThe Chef's Kitchen")
        run_again()
    elif veg == "yes" and vegan == "no" and gluten == "yes":
        print("Here are your restaurant choices." +
              "\nMain Street Pizza Company"+
              "\nCorner Cafe"+
              "\nThe Chef's Kitchen")
        run_again()
    else:
        print("Here are your restaurant choices." +
              "\nCorner Cafe"+
              "\nThe Chef's Kitchen")
        run_again()
        
    

        
    
