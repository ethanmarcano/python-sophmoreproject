#importing Stocker

from stocker import Stocker

#preparing the test dictionary/lists
company = ['Microsoft', 'Google', 'AMD', 'Intel']
stock_dict = {'Microsoft':'MSFT', 'Google':'GOOG', 'AMD':'AMD', 'Intel':'INTC'}
#creating the function
#print("Hello, and welcome to the Stock Market Lookup Tool!")
#function input
#active = True
#while active:
#stock_input = input("What company's stock data do you want to see? Please input it here. ")
def stock(stock_input):
    """Assigning what stocks you want to know about"""
    if stock_input in stock_dict:
        success = print("Successfully recognized the stock.")
        return success
        stock_examples.get(stock_input)
        stock_analysis = Stocker(stock_input)
        return stock_analysis
    else:
        return ("Sorry, but we do not recognize this one. Try another.")
    stock_analysis = Stocker(stock_input)
    stock_analysis_history = stock_analysis.stock
    stock_analysis.plot_stock(plot_type='basic')
    model, model_data = stock_analysis.create_prophet_model()

#running the function  
active = True
while active:
    print("Hello, and welcome to the Stock Market Lookup Tool!\n")
    stock_input = input("What company's stock data do you want to see? Please input it here. ")
    stock(stock_input)
    repeat = input("Do you want to look at another company's records? ")
    if repeat == 'yes':
        print("Refreshing the tool...\n")
        continue
    else:
        print("\nThank you for using the Stock Market Lookup Tool!")
        active = False
        