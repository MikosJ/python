from datetime import datetime

with open("X:\zadanie22\daily_sales.txt") as file_read:
   daily_sales = file_read.read()

daily_sales_replaced = daily_sales.replace(";,;", "#")
daily_transactions = daily_sales_replaced.strip().split(",")
daily_transactions_split = []

for i in daily_transactions:
    i = i.replace("\n","").strip()
    daily_transactions_split.append(i.strip().split("#"))
    
transaction_clean = []

price, buyer, colors_list = [], [], []

for i in daily_transactions_split:
    if "&" in i[2]:
        a = i[2].split("&")
        for j in a:
            colors_list.append(j.strip())
    else:
        colors_list.append(i[2].strip())
    
    

for i in daily_transactions_split:
    price.append(i[1].strip())
    buyer.append(i[0].strip())

def sales(price_list):
    total = 0
    for i in price_list:
        i = i.replace("$","")
        total += float(i)
    return round(total,2)

def colors(color, lst):
    sum_colors = 0
    for i in lst:
        if i == color:
            sum_colors+=1 
    return sum_colors
            

colors_unique = set(colors_list)

def top_quantity(lst):
    max = 0
    for i in colors_unique:
        if colors(i, lst) > max:
            max = colors(i, lst)
            top_sold_color = i
    return top_sold_color

def single_color_quantity(lst):
    text = ""
    for i in colors_unique:
        text += f'Ubrań w kolorze {i} sprzedano: {colors(i, lst)}\n'
    return text

def sales_report():
    name = input("How would you like to name the report: ")
    ext = input("Provide file extension: ")
    now = datetime.now()
    date = now.strftime("%d/%m/%Y %H:%M:%S")
    with open(f"X:\\zadanie22\\{name}.{ext}", "x") as report:
        report.write(f"""
=======================================================
                    Podsumowanie dnia
=======================================================
Dziś sprzedano towar o łącznej kwocie: {sales(price)}$
=======================================================
{single_color_quantity(colors_list)}
=======================================================
Najlepiej sprzedały się ubrania w kolorze: {top_quantity(colors_list)}
=======================================================
                         
Raport sporządzono {date}
Przygotował Jakub Mikos""")

sales_report()
