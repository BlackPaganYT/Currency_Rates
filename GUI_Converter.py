import tkinter as tk
from tkinter import messagebox
import Currency_rates

class Currency_сonverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвертер валют")
        self.root.geometry("500x400")
        self.root.configure(bg="#f0f8ff")

        title_label = tk.Label(
            root,
            text="$ КОНВЕРТЕР ВАЛЮТ $",
            font=("Comic Sans MS", 16, "bold"),
            bg="#ffebcd",
            fg="#8b4513"
        )
        title_label.pack(pady=10)


        update_btn = tk.Button(
            root,
            text="ОБНОВИТЬ КУРСЫ",
            command=self.update_rates,
            bg="#98fb98",
            font=("Arial", 12, "bold")
        )
        update_btn.pack(pady=5)


        tk.Label(
            root,
            text="Введите сумму в рублях:",
            font=("Arial", 10),
            bg="#f0f8ff"
        ).pack(pady=5)
        self.rubles_entry = tk.Entry(
            root,
            width=20,
            font=("Arial", 12)
        )
        self.rubles_entry.pack(pady=5)


        convert_btn = tk.Button(
            root,
            text="КОНВЕРТИРОВАТЬ",
            command=self.convert_currency,
            bg="#ffa07a",
            font=("Arial", 12, "bold")
        )
        convert_btn.pack(pady=10)


        self.result_text = tk.Text(
            root,
            height=12,
            width=50,
            font = ("Courier New", 9),
            wrap=tk.WORD
        )
        self.result_text.pack(pady=10, padx=20)
        scrollbar = tk.Scrollbar(root, command=self.result_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_text.config(yscrollcommand=scrollbar.set)


        self.rates = {}
        self.date_str = ""
        self.update_rates()

    def update_rates(self):
        try:
            self.rates, self.date_str = Сurrency_rates.get_currency_rates()
            if self.rates:
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, f"Курсы валют на {self.date_str}:\n\n")
                order = ['USD', 'EUR', 'CNY', 'GBP']
                for currency_code in order:
                    if currency_code in self.rates:
                        data = self.rates[currency_code]
                        self.result_text.insert(
                            tk.END,
                            f"{data['name']} ({currency_code}): {data['rate']} руб.\n"
                        )
            else:
                messagebox.showerror("Ошибка", "Не удалось получить курсы валют!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Проблема с получением данных: {e}")

    def convert_currency(self):
        try:
            rubles = float(self.rubles_entry.get())
            if rubles < 0:
                messagebox.showwarning("Внимание", "Введите положительное число!")
                return
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"\nКонвертация {rubles} руб.:\n\n")
            order = ['USD', 'EUR', 'CNY', 'GBP']
            for currency_code in order:
                if currency_code in self.rates:
                    rate = self.rates[currency_code]['rate']
                    if currency_code == 'CNY':
                        converted = (rubles / rate) / 10
                    else:
                        converted = rubles / rate
                    self.result_text.insert(
                        tk.END,
                        f"{rubles:,} руб. = {converted:,.2f} {self.rates[currency_code]['name']} ({currency_code})\n"
                    )
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка конвертации: {e}")

def main():
    root = tk.Tk()
    app = Currency_сonverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()
