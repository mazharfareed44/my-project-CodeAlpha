#We are to creat stock  potfolio tracker  which calculate the totol investment using basic arithmatic operators
import csv
print("Welcome to Pakistan Stock Exchange")
#Here is created hardcoded dictionary  containg stocks with prices
Stocks_dict1={"UBL":400,"MCB":300,"lUCK":270,"ENGRO":100,"NESTLE":100,"PTCL":1000}
#To store grand total variable is created as while loop will work may be more on total
grand_total=0
#while is used which will continue untill user will enter done
while True:
    Stock_symbol=input("Enter your desire stock or enter 'DONE' to finish").upper()
    if Stock_symbol== "DONE":
            break  # if done will be entered loop will break
    print("Ok! Thanks")
    Stock_quantity=int(input("Enter your stock quantity"))
    if Stock_symbol in Stocks_dict1:
        total=Stocks_dict1[Stock_symbol]*Stock_quantity #basic arithmatic operator will do calculaion
        print(f"Your total portfolio investment in {Stock_symbol}is {total}")
        grand_total+=total #assignment operatore is used which will total to grand total of totals are more then 1
    else:
        print("Sorry! Stock is not found,try from given")
print(f"Your final and total inivestment is {grand_total}")
with open("portfolio.text","w") as file:
        file.write(f"Stock: {Stock_symbol},Quantity:{Stock_quantity},Total investment:{grand_total}\n")