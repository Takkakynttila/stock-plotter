#import yahoo finance module
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn

#loop for the text ui
while True:
	print('Welcome to SSS (Super Shitty Stocker)')
	print('Available commands:\n>stop\n>stock\n')
	command = input('Input command: ')

	if command == 'stop':
		break
	elif command == 'stock':
		stock = input('Input ID of stock (has to be from Yahoo finance): ') #for yfinance
		range = input ('Input data range for chart and avg: ') #range for ticker
		stock.upper()

		ticker = yf.Ticker(stock) #pulls a data ticker object
		hstr = ticker.history("{r}d".format(r=range)) #pulls historical stock data
		sum = 0
		for i in hstr['Close']: #this loop is used to calculate average stock price
			sum += int(i)
		print('\nAverage closing price within given timeframe:\n' + str(sum/len(hstr)))

		#if the user chooses to display chart, they'll get a chart showing the historical closing prices for the time-frame they choose
		#and historical rolling averages for the same timeframe
		chart = input('Display chart? [y/n]')
		if chart == 'y':
			rolling_sum = 0
			list_of_averages = []
			for i in hstr['Close']:
				rolling_sum += int(i)
				if len(list_of_averages) == 0: #if length of the list is 0, the item to be added is the first and no average can be calculated
					list_of_averages.append(rolling_sum)
				else:
					to_be_added = rolling_sum / (len(list_of_averages) + 1) #if the item is not the first, an average is calculated for the list items and added to list
					list_of_averages.append(to_be_added)

			list_of_historical_closing_prices = []
			for i in hstr['Close']: #this loop is used to convert pandas data frame to a list of closing prices
				list_of_historical_closing_prices.append(i)
			#if yes, this is were the charts are plotted
			#hstr['Close'].plot(figsize=(16,9))
			history, = plt.plot(list_of_historical_closing_prices)
			history.set_label('Historical closing prices')
			averages, = plt.plot(list_of_averages)
			averages.set_label('Rolling average')
			plt.legend()
			plt.grid(color='black', linestyle="-.")
			plt.show()
