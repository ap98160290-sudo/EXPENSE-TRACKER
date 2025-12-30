from storage import load_data, save_data
from tracker import create_transaction

def show_menu():
    print("\n====Expense Tracker====")
    print("1. ADD INCOME")
    print("2. ADD EXPENSE")
    print("3. VIEW ALL TRANSACTIONS")
    print("4. EXIT")

def add_transaction(transaction_type,transactions):
    try:

        amount=float(input("ENTER AMOUNT"))
        category=input("ENTER CATEGORY").strip()
        date=input("ENTER DATE IN VALID FORMAT").strip()
        note=input("ENTER NOTE FOR REFERENCE").strip()

        transaction=create_transaction(amount=amount,
                                       transaction_type=transaction_type,
                                       category=category,
                                       date=date,
                                       note=note
                                       )
    
        transactions.append(transaction)
        save_data(transactions)
        print("TRANSACTION ADDED SUCCESSFULLY")
    except ValueError as e:
        print(f"ERROR:{e}")


def view_transactions(transactions):
    if not (transactions):
        print("NO TRANSACTIONS FOUND")
        return
    
    print("\n------TRANSACTIONS------")
    for i, txn in enumerate(transactions,start=1):
        print(txn)
        print(f"{i}.{txn['date']} | {txn['amount']} | {txn['type']} | {txn['category']} | {txn['note']}")



def main():
    transactions=load_data()

    while True:
        show_menu()

        choice=input("CHOOSE OPTION")


        if choice=="1":
            add_transaction("income",transactions)

        elif choice=="2":
            add_transaction("expense",transactions)

        elif choice=="3":
            transactions=load_data()
            view_transactions(transactions)

        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break


        else:
            print("Invalid choice. Please select 1–4.")

if __name__ == "__main__":
    main()

