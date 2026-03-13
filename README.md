# 💵 Sales Registration System 💵

## Description

This project is a simple sales registration program written in Python. It is designed to help a cashier or store employee record product sales quickly and accurately during a workday. The program is made up of two files that work together: one contains the tools (functions), and the other runs the actual program.

## How It Works

1. The program starts and welcomes the user with a banner on the screen.
2. The system asks the user if they want to register a sale.
3. If the user answers **yes**, the program asks for three pieces of information: the product name, the unit price, and the quantity sold.
4. The program automatically calculates the subtotal for that product (price × quantity) and saves it to a list.
5. After each entry, the system asks if the user wants to register another product.
6. Steps 3 through 5 repeat for every new product the user wants to add.
7. When the user answers **no**, the program prints a complete summary table showing all registered products, their prices, quantities, and subtotals.
8. Finally, the program displays the **grand total** of all sales collected and says goodbye to the user.

## Code Structure

The project is divided into two files to keep the code organized and easy to maintain.

**`Funciones_Reg_Cal_Tot.py`** — This file is the "toolbox" of the program. It contains three functions:
- `register_sale()` asks the user for product details and returns them as a neat package of data.
- `show_total()` receives all the recorded sales and returns the grand total as a formatted message.
- `show_summary()` prints the full sales report table with a timestamp.

**`main.py`** — This file is the "control room." It imports the tools from the toolbox, manages the list of sales, and controls the loop that keeps asking the user for new entries until they decide to stop.

## FLowchart

<img width="956" height="785" alt="Blank diagram" src="https://github.com/user-attachments/assets/01e32310-4b35-44d5-aaba-e99398b64dea" />




**Made by:** _Oscar Corzo_
## Repository's Link:
_https://github.com/corzooscar/Automated-sales-registration-system_
