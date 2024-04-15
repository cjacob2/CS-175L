#CS175L
#Conor Jacob
#expensePieChart
import matplotlib.pyplot as plt

def read_expenses(filename):
    amounts = []
    categories = []
    try:
        with open(filename, "r") as file:
            for line in file:
                category, amount = line.strip().split("\t")
                try:
                    amounts.append(float(amount))
                    categories.append(category)
                except (IOError, ValueError) as e:
                    print("Error reading file:", e)
                    continue
    except IOError:
        print("Error")
    return amounts, categories

def plot_pie_chart(amounts, categories):
    labels = categories
    sizes = amounts
    plt.figure(figsize=(10, 6))
    plt.pie(sizes, labels=labels)
    plt.title("Monthly Expenses")
    plt.show()

def main():
    filename = "expenses.txt"
    amounts, categories = read_expenses(filename)
    plot_pie_chart(amounts, categories)

if __name__ == "__main__":
    main()


