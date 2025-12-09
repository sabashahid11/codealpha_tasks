def stock_portfolio_tracker():
    stock_prices = {
        "AAPL": 180.25,
        "TSLA": 250.75,
        "GOOGL": 135.50,
        "MSFT": 330.40,
        "AMZN": 145.60,
        "NVDA": 420.80,
        "META": 320.90,
        "NFLX": 510.25
    }
    
    print("=" * 50)
    print("STOCK PORTFOLIO TRACKER")
    print("=" * 50)
    
    print("\nAvailable stocks and their current prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price:.2f}")
    
    print("\n" + "-" * 50)
    
    portfolio = {}
    total_investment = 0
    
    while True:
        stock_name = input("\nEnter stock symbol (or type 'done' to finish): ").upper()
        
        if stock_name == 'DONE':
            break
            
        if stock_name not in stock_prices:
            print(f"Error: {stock_name} is not in our database. Please enter a valid stock symbol.")
            continue
            
        try:
            quantity = int(input(f"Enter quantity for {stock_name}: "))
            if quantity <= 0:
                print("Quantity must be a positive number. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number for quantity.")
            continue
        
        stock_value = stock_prices[stock_name] * quantity
        portfolio[stock_name] = {
            'quantity': quantity,
            'price_per_share': stock_prices[stock_name],
            'total_value': stock_value
        }
        
        total_investment += stock_value
        
        print(f"Added {quantity} shares of {stock_name} at ${stock_prices[stock_name]:.2f} each")
        print(f"Current total investment: ${total_investment:.2f}")
    
    print("\n" + "=" * 50)
    print("PORTFOLIO SUMMARY")
    print("=" * 50)
    
    if not portfolio:
        print("No stocks in portfolio.")
        return
    
    print("\nStock Holdings:")
    print("-" * 40)
    print(f"{'Stock':<10} {'Qty':<10} {'Price/Share':<15} {'Total Value':<15}")
    print("-" * 40)
    
    for stock, details in portfolio.items():
        print(f"{stock:<10} {details['quantity']:<10} ${details['price_per_share']:<14.2f} ${details['total_value']:<14.2f}")
    
    print("-" * 40)
    print(f"\nTOTAL INVESTMENT: ${total_investment:.2f}")
    
    save_option = input("\nDo you want to save the portfolio to a file? (yes/no): ").lower()
    
    if save_option in ['yes', 'y']:
        print("\nChoose file format:")
        print("1. Text file (.txt)")
        print("2. CSV file (.csv)")
        
        try:
            choice = int(input("Enter your choice (1 or 2): "))
            
            if choice == 1:
                save_to_txt(portfolio, total_investment)
            elif choice == 2:
                save_to_csv(portfolio, total_investment)
            else:
                print("Invalid choice. Portfolio not saved.")
        except ValueError:
            print("Invalid input. Portfolio not saved.")
    
    print("\nThank you for using Stock Portfolio Tracker!")


def save_to_txt(portfolio, total_investment):
    filename = "portfolio_summary.txt"
    
    with open(filename, 'w') as file:
        file.write("=" * 50 + "\n")
        file.write("PORTFOLIO SUMMARY\n")
        file.write("=" * 50 + "\n\n")
        
        file.write("Stock Holdings:\n")
        file.write("-" * 40 + "\n")
        file.write(f"{'Stock':<10} {'Qty':<10} {'Price/Share':<15} {'Total Value':<15}\n")
        file.write("-" * 40 + "\n")
        
        for stock, details in portfolio.items():
            file.write(f"{stock:<10} {details['quantity']:<10} ${details['price_per_share']:<14.2f} ${details['total_value']:<14.2f}\n")
        
        file.write("-" * 40 + "\n\n")
        file.write(f"TOTAL INVESTMENT: ${total_investment:.2f}\n")
    
    print(f"\nPortfolio saved to {filename}")


def save_to_csv(portfolio, total_investment):
    import csv
    
    filename = "portfolio_summary.csv"
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow(["Stock", "Quantity", "Price per Share", "Total Value"])
        
        for stock, details in portfolio.items():
            writer.writerow([
                stock,
                details['quantity'],
                f"${details['price_per_share']:.2f}",
                f"${details['total_value']:.2f}"
            ])
        
        writer.writerow([])
        writer.writerow(["TOTAL INVESTMENT", "", "", f"${total_investment:.2f}"])
    
    print(f"\nPortfolio saved to {filename}")


def quick_example():
    print("=" * 50)
    print("QUICK EXAMPLE PORTFOLIO")
    print("=" * 50)
    
    stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 135.50}
    
    example_portfolio = {
        "AAPL": {"quantity": 10, "price_per_share": stock_prices["AAPL"]},
        "TSLA": {"quantity": 5, "price_per_share": stock_prices["TSLA"]},
        "GOOGL": {"quantity": 8, "price_per_share": stock_prices["GOOGL"]}
    }
    
    total = 0
    
    print("\nStock Holdings:")
    print("-" * 40)
    print(f"{'Stock':<10} {'Qty':<10} {'Price/Share':<15} {'Total Value':<15}")
    print("-" * 40)
    
    for stock, details in example_portfolio.items():
        stock_value = details['quantity'] * details['price_per_share']
        total += stock_value
        print(f"{stock:<10} {details['quantity']:<10} ${details['price_per_share']:<14.2f} ${stock_value:<14.2f}")
    
    print("-" * 40)
    print(f"\nTOTAL INVESTMENT: ${total:.2f}")


def main():
    print("Welcome to Stock Portfolio Tracker!")
    print("\nChoose an option:")
    print("1. Build your own portfolio")
    print("2. See a quick example")
    print("3. Exit")
    
    try:
        choice = int(input("\nEnter your choice (1-3): "))
        
        if choice == 1:
            stock_portfolio_tracker()
        elif choice == 2:
            quick_example()
        elif choice == 3:
            print("Goodbye!")
        else:
            print("Invalid choice. Please run the program again.")
    except ValueError:
        print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()

