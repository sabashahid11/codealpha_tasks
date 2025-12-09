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
    
    portfolio = {}
    
    while True:
        print("\n" + "="*60)
        print("STOCK PORTFOLIO TRACKER MAIN MENU")
        print("="*60)
        print("1. Add or Manage Stocks")
        print("2. View Portfolio")
        print("3. View Available Stocks")
        print("4. Save Portfolio to File")
        print("5. Clear Portfolio")
        print("6. Exit")
        print("-"*60)
        
        try:
            choice = input("\nEnter choice (1 6): ").strip()
            
            if choice == "1":
                while True:
                    print("\n" + "-"*50)
                    print("ADD OR MANAGE STOCKS")
                    print("-"*50)
                    
                    if portfolio:
                        total = 0
                        print("\nCurrent Portfolio:")
                        for stock, qty in portfolio.items():
                            value = stock_prices[stock] * qty
                            total += value
                            print(f"  {stock}: {qty} shares = ${value:.2f}")
                        print(f"  Current Total: ${total:.2f}")
                    
                    print(f"\nAvailable stocks: {list(stock_prices.keys())}")
                    
                    stock = input("\nEnter stock symbol (or 'back' to return): ").upper().strip()
                    
                    if stock == "BACK":
                        break
                    
                    if stock not in stock_prices:
                        print(f"'{stock}' not found! Available: {list(stock_prices.keys())}")
                        continue
                    
                    try:
                        qty = int(input(f"Quantity for {stock}: "))
                        if qty <= 0:
                            print("Quantity must be positive!")
                            continue
                    except ValueError:
                        print("Enter a valid number!")
                        continue
                    
                    portfolio[stock] = portfolio.get(stock, 0) + qty
                    value = stock_prices[stock] * qty
                    print(f"Added {qty} shares of {stock} = ${value:.2f}")
            
            elif choice == "2":
                print("\n" + "="*50)
                print("YOUR PORTFOLIO")
                print("="*50)
                
                if not portfolio:
                    print("Portfolio is empty!")
                    input("\nPress Enter to continue...")
                    continue
                
                total = 0
                print("\nStock Holdings:")
                print("-"*45)
                print(f"{'Stock':<8} {'Qty':<8} {'Price':<12} {'Value':<15}")
                print("-"*45)
                
                for stock, qty in portfolio.items():
                    price = stock_prices[stock]
                    value = price * qty
                    total += value
                    print(f"{stock:<8} {qty:<8} ${price:<11.2f} ${value:<14.2f}")
                
                print("-"*45)
                print(f"\nTOTAL INVESTMENT: ${total:.2f}")
                
                print("\nOptions:")
                print("1. Return to Main Menu")
                print("2. Remove a stock")
                print("3. Clear Portfolio")
                
                sub_choice = input("\nEnter choice (1 3): ").strip()
                
                if sub_choice == "2":
                    stock = input("Enter stock symbol to remove: ").upper().strip()
                    if stock in portfolio:
                        del portfolio[stock]
                        print(f"Removed {stock} from portfolio")
                    else:
                        print(f"{stock} not in portfolio")
                
                elif sub_choice == "3":
                    if input("Clear entire portfolio? (yes or no): ").lower() == "yes":
                        portfolio.clear()
                        print("Portfolio cleared!")
            
            elif choice == "3":
                print("\n" + "="*50)
                print("AVAILABLE STOCKS AND PRICES")
                print("="*50)
                
                print(f"\n{'Stock':<8} {'Price':<12}")
                print("-"*25)
                for stock, price in stock_prices.items():
                    print(f"{stock:<8} ${price:<11.2f}")
                
                input("\nPress Enter to continue...")
            
            elif choice == "4":
                if not portfolio:
                    print("Portfolio is empty! Add stocks first.")
                    continue
                
                print("\n" + "-"*50)
                print("SAVE PORTFOLIO")
                print("-"*50)
                print("\n1. Save as Text File (.txt)")
                print("2. Save as CSV File (.csv)")
                print("3. Back to Main Menu")
                
                save_choice = input("\nEnter choice (1 3): ").strip()
                
                if save_choice == "1":
                    filename = input("Enter filename (or press Enter for 'portfolio.txt'): ").strip()
                    if not filename:
                        filename = "portfolio.txt"
                    elif not filename.endswith('.txt'):
                        filename += '.txt'
                    
                    total = sum(stock_prices[stock] * qty for stock, qty in portfolio.items())
                    
                    with open(filename, 'w') as f:
                        f.write("STOCK PORTFOLIO\n")
                        f.write("="*50 + "\n\n")
                        for stock, qty in portfolio.items():
                            value = stock_prices[stock] * qty
                            f.write(f"{stock}: {qty} shares at ${stock_prices[stock]:.2f} = ${value:.2f}\n")
                        f.write("\n" + "="*50 + "\n")
                        f.write(f"TOTAL INVESTMENT: ${total:.2f}\n")
                    
                    print(f"Portfolio saved to {filename}")
                
                elif save_choice == "2":
                    filename = input("Enter filename (or press Enter for 'portfolio.csv'): ").strip()
                    if not filename:
                        filename = "portfolio.csv"
                    elif not filename.endswith('.csv'):
                        filename += '.csv'
                    
                    total = sum(stock_prices[stock] * qty for stock, qty in portfolio.items())
                    
                    with open(filename, 'w', newline='') as f:
                        f.write("Stock,Quantity,Price per Share,Total Value\n")
                        for stock, qty in portfolio.items():
                            value = stock_prices[stock] * qty
                            f.write(f"{stock},{qty},{stock_prices[stock]:.2f},{value:.2f}\n")
                        f.write(f"TOTAL,,,{total:.2f}\n")
                    
                    print(f"Portfolio saved to {filename}")
            
            elif choice == "5":
                if portfolio:
                    confirm = input("Clear entire portfolio? (yes or no): ").lower().strip()
                    if confirm == "yes":
                        portfolio.clear()
                        print("Portfolio cleared!")
                else:
                    print("Portfolio is already empty!")
            
            elif choice == "6":
                print("\n" + "="*50)
                print("Thank you for using Stock Portfolio Tracker!")
                print("Goodbye!")
                print("="*50)
                break
            
            else:
                print("Invalid choice! Enter 1 6.")
        
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"Error: {e}")
            continue


def quick_example():
    print("\n" + "="*50)
    print("QUICK EXAMPLE")
    print("="*50)
    
    example_portfolio = {
        "AAPL": 10,
        "TSLA": 5,
        "GOOGL": 8
    }
    
    example_prices = {
        "AAPL": 180.25,
        "TSLA": 250.75,
        "GOOGL": 135.50
    }
    
    total = 0
    print("\nExample Portfolio:")
    print("-"*45)
    print(f"{'Stock':<8} {'Qty':<8} {'Price':<12} {'Value':<15}")
    print("-"*45)
    
    for stock, qty in example_portfolio.items():
        value = example_prices[stock] * qty
        total += value
        print(f"{stock:<8} {qty:<8} ${example_prices[stock]:<11.2f} ${value:<14.2f}")
    
    print("-"*45)
    print(f"\nTOTAL: ${total:.2f}")
    
    input("\nPress Enter to continue...")


def main():
    print("\n" + "="*60)
    print("WELCOME TO STOCK PORTFOLIO TRACKER")
    print("="*60)
    
    while True:
        print("\nMAIN MENU:")
        print("1. Start Stock Portfolio Tracker")
        print("2. See Quick Example")
        print("3. Exit Program")
        print("-"*40)
        
        try:
            choice = input("\nEnter choice (1 3): ").strip()
            
            if choice == "1":
                stock_portfolio_tracker()
                continue
            
            elif choice == "2":
                quick_example()
            
            elif choice == "3":
                print("\nGoodbye! Thank you for using our program.")
                break
            
            else:
                print("Invalid choice! Enter 1 3.")
        
        except KeyboardInterrupt:
            print("\nProgram stopped by user.")
            break
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
