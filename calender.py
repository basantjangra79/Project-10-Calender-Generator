
# Calender Generator

import calendar
from colorama import init, Fore, Style

init(autoreset=True)

while True:
    try:
        print(Fore.CYAN + "\n" + "=" * 40)
        print(Fore.YELLOW + "      ADVANCED CALENDAR GENERATOR")
        print(Fore.CYAN + "=" * 40)

        menu = [
            "View Month Calender",
            "View a Full Year Calender",
            "Check Leap Year",
            "Find Day of a Date",
            "Exit",
        ]

        for index, option in enumerate(menu, start=1):
            print(f"{index} - {option}")

        choice = input("Enter a Number (1-5): ")

        
        if choice == "1":
            try:
                year = int(input("Enter a Year: "))
                month = int(input("Enter a Month : "))

                print(Fore.GREEN)
                print(calendar.month(year, month))

            except:
                print(Fore.RED + "Invalid Input!")

        elif choice == "2":
            try:
                year = int(input("Enter a Year: "))

                print(Fore.GREEN)
                print(calendar.calendar(year))

            except:
                print(Fore.RED + "Invalid Input!")

        
        elif choice == "3":
            try:
                year = int(input("Enter a Year: "))

                if calendar.isleap(year):
                    print(Fore.GREEN + f"{year} is a Leap Year.")
                else:
                    print(Fore.RED + f"{year} is NOT a Leap Year.")

            except:
                print(Fore.RED + "Invalid Input!")

        
        elif choice == "4":
            try:
                year = int(input("Enter Year: "))
                month = int(input("Enter Month: "))
                day = int(input("Enter Day: "))

                day_number = calendar.weekday(year, month, day)

                days = [
                    "Monday",
                    "Tuesday",
                    "Wednesday",
                    "Thursday",
                    "Friday",
                    "Saturday",
                    "Sunday",
                ]

                print(Fore.GREEN + f"\n{day}/{month}/{year} was a {days[day_number]}")

            except:
                print(Fore.RED + "Invalid Date!")

        
        elif choice == "5":
            print(Fore.YELLOW + "\nThank you for using Calendar Generator!")
            break

        else:
            print(Fore.RED + "Invalid Choice!")

        
        print("\n" + Fore.CYAN + "=" * 40 + Fore.RESET)
        print(Fore.MAGENTA + "    📸 Follow on Instagram:" + Fore.RESET)
        print(Fore.MAGENTA + "     .---.  .---." + Fore.RESET)
        print(Fore.MAGENTA + "    |  _  \/  _  |" + Fore.RESET)
        print(
            Fore.MAGENTA
            + "    | | )    ( | |   "
            + Fore.YELLOW
            + Style.BRIGHT
            + "@Basantjangra79"
            + Style.RESET_ALL
        )
        print(Fore.MAGENTA + "    |  ~  /\  ~  |" + Fore.RESET)
        print(Fore.MAGENTA + "     '---'  '---'" + Fore.RESET)
        print(Fore.MAGENTA + "  📩 For Code: GitHub 🔗 in Bio  " + Fore.RESET)
        print(Fore.CYAN + "=" * 40 + "\n" + Fore.RESET)

        try:
            # Pause before restarting the loop
            input(Fore.BLUE + "Press Enter to Try again...[Ctrl + C] to Exit" + Fore.RESET)
            print("\n" * 2)

        except KeyboardInterrupt:
            print("\nThank you for using Calendar Generator!")
            break

    except KeyboardInterrupt:
            print("\nThank you for using Calendar Generator!")
            break
