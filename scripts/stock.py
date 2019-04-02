
def percentage():
    #price = [43,324,23112,23,23,231,3,231,23,2]
    price = day_and_price("/Users/rakeshkumar/private_data/parsed_data", "BEML")
    min_price = []
    min = float(price[0].get("price"))
    print(type(min))
    for i in range(1,len(price)):
        price_v = float(price[i].get("price"))
        if price_v < min:
            min = price_v
        min_price.append(min)

    for i in range(0,len(min_price)):
        percentage = (float(price[i].get("price")) - min_price[i])*100/min_price[i]
        print("Date = ", price[i].get("date"), "Profit/Loss = ", percentage, "Price closed = ", price[i].get("price"), end=", ")
        print()

def day_and_price(file, stock):
    f =  open(file,"r")
    date_price = []
    for l in f:
        if "csvContentDiv" not in l:
            data = l.split(",")
            cusip = data[0].replace(" ","")
            date = data[2].replace(" ","")
            price = data[8].replace(" ","")
            #print(cusip)
            if stock == cusip:
                date_price.append({"date": date, "price": float(price)})
                #print(data)
    return date_price

percentage()