# ─────────────────────────────────────────────────────────
# MAIN.py
# Entry point for the Sales Registration System
# ─────────────────────────────────────────────────────────

from Funciones_Reg_Cal_Tot import register_sale, show_total, show_summary
 
# Central list that stores every registered sale as a dictionary
sales_list = []
 
# Welcome banner
print(f"""╔═══════════════════════════════════════════════════════════╗
                🏦  SALES REGISTRATION SYSTEM  🏦
╚═══════════════════════════════════════════════════════════╝""")
 
answer = input("~ Would you like to register a sale? y/n: ").lower()
 
while answer == "y":
    # Call the function and store the returned dictionary
    sale = register_sale()
    sales_list.append(sale)
 
    # Show a quick confirmation after each entry
    print(f"""{"-"*60}
  ~ Subtotal: ${sales_list[-1]["Total"]} | Product: {sales_list[-1]["Product"]}
{"="*60}
""")
    answer = input("~ Would you like to register another sale? y/n: ").lower()
 
# ── End of loop: display full report ──
show_summary(sales_list)          # prints internally, no need for print()
print(show_total(sales_list))     # returns a string, so print() is needed
print("="*60)
print("~ Thank you for using the Sales Registration System ʕ•́ᴥ•̀ʔっ")
