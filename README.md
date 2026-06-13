# 📅 Advanced Calendar Generator

A Python-based Calendar Generator that allows users to view monthly calendars, full-year calendars, check leap years, and find the day of any date.

This project demonstrates practical usage of Python's built-in `calendar` module while providing a colorful and interactive command-line experience.

---

# 🚀 Features

## 📆 Calendar Generation

* View a specific month's calendar
* View an entire year's calendar
* Clean formatted output

## 🗓️ Date Utilities

* Check whether a year is a leap year
* Find the day of the week for any date
* Supports historical and future dates

## 🎨 User Experience

* Colored terminal output using Colorama
* Menu-driven interface
* Interactive navigation
* Easy-to-use command-line application

## 🛡️ Error Handling

* Invalid menu selection handling
* Invalid date detection
* Keyboard Interrupt support (`Ctrl + C`)
* Graceful program termination

---

# 📸 Menu Preview

```text
========================================
      ADVANCED CALENDAR GENERATOR
========================================

1 - View Month Calendar
2 - View a Full Year Calendar
3 - Check Leap Year
4 - Find Day of a Date
5 - Exit
```

---

# 📦 Modules Used

```python
import calendar
from colorama import init, Fore, Style
```

| Module   | Purpose                      |
| -------- | ---------------------------- |
| calendar | Calendar and date operations |
| colorama | Colored terminal output      |

---

# 🧠 Concepts Used

This project helped practice:

* Python Modules
* Menu-Driven Applications
* Loops
* Conditional Statements
* Exception Handling
* Lists
* Date Processing
* User Input Validation

---

# 📂 Project Structure

```text
Project-10-Calender-Generator/
│
├── calender.py
└── README.md
```

---

# ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/basantjangra79/Project-10-Calender-Generator.git
```

### Open Project Folder

```bash
cd Project-10-Calender-Generator
```

### Install Dependency

```bash
pip install colorama
```

### Run Program

```bash
python calender.py
```

---

# 📆 Feature 1 — View Monthly Calendar

### Example

```text
Enter a Year: 2026
Enter a Month: 6
```

### Output

```text
     June 2026
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
...
```

---

# 📅 Feature 2 — View Full Year Calendar

### Example

```text
Enter a Year: 2026
```

### Output

Displays all 12 months of the selected year in a formatted layout.

---

# 🌍 Feature 3 — Leap Year Checker

### Example

```text
Enter a Year: 2024
```

### Output

```text
2024 is a Leap Year.
```

### Example

```text
Enter a Year: 2025
```

### Output

```text
2025 is NOT a Leap Year.
```

---

# 📍 Feature 4 — Find Day of a Date

### Example

```text
Enter Year: 2007
Enter Month: 5
Enter Day: 15
```

### Output

```text
15/5/2007 was a Tuesday
```

---

# 🎯 Learning Outcomes

Through this project, I practiced:

* Using Python's built-in Calendar Module
* Working with dates and years
* Leap year calculations
* Date-to-weekday conversion
* Building menu-driven programs
* Creating user-friendly CLI applications
* Handling invalid user inputs

---

# ⚠️ Error Handling

### Invalid Menu Choice

```text
Invalid Choice!
```

### Invalid Date

```text
Invalid Date!
```

### Invalid Input

```text
Invalid Input!
```

### User Exit

```text
Thank you for using Calendar Generator!
```

---

# 🔮 Future Improvements

Possible upgrades for future versions:

* Event Scheduler
* Holiday Calendar
* Birthday Reminder System
* Monthly Planner
* Export Calendar to PDF
* Export Calendar to Text File
* Time Zone Support
* Date Difference Calculator
* GUI Version using Tkinter
* Web Version using Flask

---

# 👨‍💻 Author

**Basant Jangra**

Python Learning Journey — Project #10

### Completed Projects

* Project 1 — Advance Mini Calculator
* Project 2 — Number Guessing Game
* Project 3 — Password Generator
* Project 4 — To-Do List Maker
* Project 5 — Age Calculator
* Project 6 — OTP Generator
* Project 7 — Calendar Generator
* Project 8 — QR Code Generator
* Project 9 — Password Cracking Simulator
* Project 10 — Advanced Calendar Generator

GitHub:
https://github.com/basantjangra79

Instagram:
@Basantjangra79

---

## ⭐ If you found this project useful, consider starring the repository and following my Python learning journey.
