#!/usr/bin/env python3
import csv
from datetime import datetime
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

#keep trac
LOG_FILE = 'income_log.csv'
HEADERS = ['type', 'amount', 'date', 'notes']

def init_file():
	"""Start the CSV file if it doesnt exist"""
	try:
	#create file
		with open(LOG_FILE, 'x', newline='') as file:
			writer = csv.writer(file)
			writer.writerow(HEADERS)
	except FileExistsError:

		pass

def add_income():
	"""add a new income entry"""
	income_type = input("Cash or Deposit (c/d):  ").strip().lower()
	amount = float(input("Amount of money?  "))
	#open file and append the stuff
	with open(LOG_FILE, 'a', newline ='') as file:
		writer = csv.writer(file)
		writer.writerow([income_type, amount, datetime.now().fromisoformat()])

def display_total():
	"""display totals"""
	total_cash = 0
	total_deposit = 0

	try:
		#open file and add up totals
		with open(LOG_FILE, 'r') as file:
			reader = csv.DictReader(file)
			for row in reader:
			#sum amounts
				if row ['type'] == 'c':
					total_cash += float(row['amount'])
				elif row['type'] == 'd':
					total_deposit += float(row['amount'])
	except FileNotFoundError:
		print("No data found, Start Making Money Bro")
		return

	print(Style.BRIGHT + Fore.BLUE + f"Total Cash ${total_cash:.2f}")
	print(Style.BRIGHT + Fore.YELLOW + f"Total Direct Deposit: ${total_deposit:.2f}")
	print(Style.BRIGHT + Fore.GREEN + f"Subtotal: ${total_cash + total_deposit:.2f}")


def display_all_logs():
    """Display all income logs."""
    try:
        with open(LOG_FILE, 'r') as file:
            reader = csv.DictReader(file)
            print(Style.BRIGHT + "All income entries:")
            for row in reader:
                # Parse date from ISO format and format it
                date_obj = datetime.fromisoformat(row['date'])
                formatted_date = date_obj.strftime('%Y-%m-%d')
                print(Style.BRIGHT + f"Type: {row['type']} - Amount: ${float(row['amount']):.2f} - Date: {formatted_date} - Notes: {row['notes']}")
    except FileNotFoundError:
        print(Style.BRIGHT + "No data found. Please start logging some income.")

def main():
	"""does the thing that it does"""
#initialize log file with headers
#cli will hopefully be simple enough

	init_file()
	print(Fore.GREEN + Style.BRIGHT + "Welcome to Your Personal Income Tracker")
	while True:
		print("\nOptions:")
		print(Style.BRIGHT + Fore.RED + "1. Add income")
		print(Style.BRIGHT + Fore.RED + "2. Show total income")
		print(Style.BRIGHT + Fore.RED + "3. Display previous logs")
		print(Style.BRIGHT + Fore.RED + "4. Exit")
		choice = input(Style.BRIGHT + Fore.YELLOW + "Pick 1-4: ")
		if choice == '1':
			add_income()
		elif choice == '2':
			display_total()
		elif choice == '3':
			display_all_logs()
		elif choice == '4':
			print(Style.BRIGHT + Fore.GREEN + "Exiting.")
			break
		else:
			print(Fore.BLUE + "Invalid")

if __name__ == '__main__':
	main()
