#CS175
#Conor Jacob
#restaurant
      
run = True
while run == True:

    inp = True
    while inp:
        veg = input("Is anyone in your party vegetarian?(Yes/No) ").lower()
        if veg == "yes" or veg == "no":
            inp = False
        else:
            print("Incorrect input. Enter Yes/No")
            
    inp = True
    while inp:
        vegan = input("Is anyone in your party vegan?(Yes/No) ").lower()
        if vegan == "yes" or vegan == "no":
            inp = False
        else:
            print("Incorrect input. Enter Yes/No")
            
    inp = True
    while inp:
        gluten = input("Is anyone in your party gluten-free?(Yes/No) ").lower()
        if gluten == "yes" or gluten == "no":
            inp = False
        else:
            print("Incorrect input. Enter Yes/No")

    if veg == "no" and vegan == "no" and gluten == "no":
        print("Here are your restaurant choices."
                "\nJoe's Gourmet Burgers" 
                "\nMama's Fine Italian" 
                "\nMain Street Pizza Company"
                "\nCorner Cafe"
                "\nThe Chef's Kitchen")
        
    elif veg == "yes" and vegan == "no" and gluten == "no":
        print("Here are your restaurant choices." 
              "\nMama's Fine Italian" 
              "\nMain Street Pizza Company"
              "\nCorner Cafe"
              "\nThe Chef's Kitchen")
            
    elif veg == "no" and vegan == "no" and gluten == "yes":
        print("Here are your restaurant choices."
              "\nMain Street Pizza Company"
              "\nCorner Cafe"
              "\nThe Chef's Kitchen")
            
    elif veg == "yes" and vegan == "no" and gluten == "yes":
        print("Here are your restaurant choices." 
              "\nMain Street Pizza Company"
              "\nCorner Cafe"
              "\nThe Chef's Kitchen")
              
    else:
        print("Here are your restaurant choices."
              "\nCorner Cafe"
              "\nThe Chef's Kitchen")
    inp = True
    while inp== True:
        again = input("Would you like to run again?(Yes to run again/No to exit program) ").lower()
        if again == "yes":
            inp = False
        elif again == "no":
            print("Exiting program")
            inp = False
            run = False
        else:
            print("Incorrect input. Enter Yes/No")

    
    

        
    
