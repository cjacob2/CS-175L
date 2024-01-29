#CS175L
#Conor Jacob
#stocks

while True:

    try:
        
#Gathers info from user   
        comPurch = float(input("Enter commission rate percentage (ex 0.03) on stock purchase: "))
        comSale = float(input("Enter commission rate percentage (ex 0.03) on stock sale: "))
        sharesBought = float(input("Enter number of shares purchased: "))
        sharesSold = float(input("Enter number of shares sold: "))
        purchPrice = float(input("Enter purchase price per share: "))
        sellPrice = float(input("Enter sell price per share: "))

#calculates outputs
        amountPaidForStock = round((sharesBought * purchPrice),2)
        purchCom = round((comPurch * amountPaidForStock),2)
        totPaid = amountPaidForStock + purchCom
        stockSoldFor = round((sharesSold * sellPrice),2)
        sellCom = round((comSale * stockSoldFor),2)
        totReceived = stockSoldFor - sellCom
        profOrLoss = totReceived - totPaid

#prints outputs
        print(f"Amount paid for the stock: ${amountPaidForStock:,.2f}" +
        f"\nCommision paid on the purchase: ${purchCom:,.2f}" +
        f"\nAmount the stock sold for: ${stockSoldFor:,.2f}" +
        f"\nCommision paid on the sale: ${sellCom:,.2f}" +
        f"\nProfit (or loss if negative): ${profOrLoss:,.2f}")
        
        break
    
    except ValueError:
        print("Input entered incorrectly. Please try again.")
