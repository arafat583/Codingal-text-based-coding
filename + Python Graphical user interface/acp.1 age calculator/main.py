import tkinter as tk

root = tk.Tk()
root.title("Interest Calculator")

tk.Label(root, text="Principal:").pack()
entry_principal = tk.Entry(root)
entry_principal.pack()

tk.Label(root, text="Rate (%):").pack()
entry_rate = tk.Entry(root)
entry_rate.pack()

tk.Label(root, text="Time (years):").pack()
entry_time = tk.Entry(root)
entry_time.pack()

def calculate():
    principal = float(entry_principal.get())
    rate = float(entry_rate.get())
    time = float(entry_time.get())
    

    simple_interest = (principal * rate * time) / 100
    

    compound_interest = principal * ((1 + rate / 100) ** time) - principal
    

    result_label.config(text=f"Simple Interest: {simple_interest:.2f}\nCompound Interest: {compound_interest:.2f}")


tk.Button(root, text="Calculate", command=calculate).pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()



