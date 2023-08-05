def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    display_report(incomes, number_of_months)
    print("\nIncome Report\n-------------")

def display_report(incomes, number_of_months):
    """Get income and number of months to display monthly income report."""
    total = 0
    for number_of_months in range(1, number_of_months + 1):
        income = incomes[number_of_months - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(number_of_months, income, total))
main()