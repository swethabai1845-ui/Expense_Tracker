import csv

while True:
    print("\nExpense Tractor")
    print("1. Add Expense")
    print("2.Exit")

    choice = input("Enter Choice:")

    if choice == "1":
        
        date = input("Enter Date:")

        category = input("Enter Category:")

        amount = input("Enter Amount:")

        with open("expenses.csv","a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date,category,amount])

            print("Expense Added Successfully!")
    elif choice == "2":
        break
    else:
        print("Invalid Choice")         
            
            
        
    
            
    
        
    

