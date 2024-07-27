import tkinter as tk

def miles_to_kilometers():
    miles = float(input_miles_entry.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


window = tk.Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

input_miles_entry = tk.Entry(width=7)
input_miles_entry.grid(column=1,row=0)

mile_label = tk.Label(text="Miles")
mile_label.grid(row=0, column=2)

is_equal_label = tk.Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

km_result_label = tk.Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = tk.Label(text="KM")
km_label.grid(column=2, row=1)

calculate_button = tk.Button(text="Calculate", command=miles_to_kilometers)
calculate_button.grid(column=1, row=2)

window.mainloop()