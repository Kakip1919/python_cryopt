import tkinter.ttk as ttk
from tkinter import messagebox as msg_box
import tkinter as tk
import sys
import csv
from binance.client import Client


class BinanceAPI:

    def __init__(self):
        api_key = 'mZdbP1239L6TjscUB0brUNoUM4WMfTTWQ36Q6YNFh2drAs22J0MnJo4LzW3QOEO6'
        api_secret = 'lVPLwgGFUivV9BWY510Roy4rSO91XnaP8zYs9N3FJfJPSkoXIeTwaIzKUgV0DTgw'

        self.client = Client(api_key, api_secret)

    def get_ticker(self, pair):
        try:
            value = self.client.get_ticker(symbol=pair)
            return value
        except Exception as e:
            print('Exception Messege : {}'.format(e))
            return None





def get_pair(event):
    current_pair = []
    index = event.widget.curselection()
    for i in event.widget.get(index):
        current_pair.append(i)
        sv.set(current_pair)
        pv.set(price_label)
        replace_current = str(current_pair).replace("/", "")
        special = replace_current.replace("[", "").replace("]", "").replace("'", "")
        return special

def main():
    binance_set = BinanceAPI()
    ticker = binance_set.get_ticker
    return ticker['lastPrice']


days = []
root = tk.Tk()
root.title(u"Software Title")
root.geometry("1400x850")
root.resizable(width=0, height=0)
frame = ttk.Frame(root)
frame.pack(anchor=tk.E)
with open('crypto_writer_row.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        days.append(row)

lists = tk.StringVar(value=days)

Listbox = tk.Listbox(frame, listvariable=lists, height=53, width=20, font=("Courier", 15))

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=Listbox.yview)

Listbox["yscrollcommand"] = scrollbar.set

sv = tk.StringVar()
pv = tk.StringVar()
sv.set("")
pv.set("")
bind_current = Listbox.bind("<<ListboxSelect>>", get_pair)

price_label = main()
Selected_currencies = tk.Label(textvariable=pv, font=("MSゴシック", "15", "bold"))
Selected_prices = tk.Label(textvariable=sv, font=("MSゴシック", "20", "bold"))
Selected_currencies.place(x=420, y=100)
Selected_prices.place(x=420, y=400)
Listbox.grid(row=0, column=0)

scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

root.mainloop()
