def add_expense(expenses,amount,category):
    expenses.append({'amount':amount,'category':category})

def show_expenses(expenses): 
    for expense in expenses:
        print(f'Amount: {expense["amount"]},Category: {expense["category"]}')

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'],expenses))

def filter_by_expense_category(expenses,category):
    return filter(lambda expense:expense['category'] == category,expenses)

def main():
    expenses=[]

    while True:
        print('WELCOME TO MY EXPENSE TRACKER\n''\nSelect from the following choices:\n')
        print('1. Add expense')
        print('2. Show expenses')
        print('3. Total expenses')
        print('4. Filter by expense category')
        print('5. Exit program')

        choice=input('\nEnter your choice: ')

        if choice =='1':
            amount=float(input('Enter amount: '))
            category=input('Enter category: ')
            add_expense(expenses,amount,category)

        elif choice == '2':
            print('Expences:')
            show_expenses(expenses)

        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
        elif choice == '4':
            category=input('Enter your category: ')
            print(f'Expenses for {category}:')
            filter_category=filter_by_expense_category(expenses,category)
            show_expenses(filter_category)
        elif choice == '5':
            print('THANK YOU FOR PARTICIPATING')
            break 

main()