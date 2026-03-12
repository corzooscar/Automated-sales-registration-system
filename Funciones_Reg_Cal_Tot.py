# ─────────────────────────────────────────────────────────
# Sales Functions
# Contains functions to register, total, and summarize sales
# ─────────────────────────────────────────────────────────
 
# Tracks how many products have been registered in this session
import time
product_count = 0
 
 
def register_sale():
    """
    Asks the user for product details and returns them as a dictionary.
    Also increments the product counter to label each entry.
    """
    global product_count
    product_count += 1
 
    print(f"\n======================= Product #{product_count} =========================")
    product_name = input("~ Product name: ")
    unit_price   = float(input("~ Unit price: $"))
    quantity     = int(input("~ Quantity sold: "))
    subtotal     = unit_price * quantity
 
    return {
        "Product":  product_name,
        "Price":    unit_price,
        "Quantity": quantity,
        "Total":    subtotal
    }
 
 
def show_total(sales_list):
    """
    Receives the list of sales dictionaries and returns a formatted
    string showing the grand total collected across all products.
    """
    grand_total = sum(sale['Total'] for sale in sales_list)
    return f"— Grand Total Collected: ${grand_total:.2f}"
 
 
def show_summary(sales_list):
    """
    Prints a formatted summary table of all registered sales.
    Iterates over each sale dictionary and displays its fields.
    """
    print(f"""{"="*60}
{"DAILY SALES SUMMARY".center(60)}
{"-"*60}
{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()).center(60)}
{"="*60}""")
 
    for sale in sales_list:
        print(f"""— Product:  {sale["Product"]}
  Unit price: ${sale["Price"]:.2f}
  Quantity:   {sale["Quantity"]}
  Subtotal:   ${sale["Total"]:.2f}
  {"─"*31}""")
