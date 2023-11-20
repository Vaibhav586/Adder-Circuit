import tkinter as tk

def select_adder(choice):
    if choice == "Half Adder":
        half_adder()
    elif choice == "Full Adder":
        full_adder()
    elif choice == "Ripple Carry Adder":
        ripple_carry_adder()
    elif choice == "Carry Look-Ahead Adder":
        carry_lookahead_adder()

def half_adder():
    result_label.config(text="Half Adder Circuit")
    a = int(a_entry.get())
    b = int(b_entry.get())

    if a in {0, 1} and b in {0, 1}:
        sum_ab = a ^ b
        carry_ab = a & b
        result_label.config(text=f"Sum (A⊕B): {sum_ab}\nCarry (A.B): {carry_ab}")
    else:
        result_label.config(text="Wrong Input")

def full_adder():
    result_label.config(text="Full Adder Circuit")
    a = int(a_entry.get())
    b = int(b_entry.get())

    if a in {0, 1} and b in {0, 1}:
        sum_ab = a ^ b
        carry_ab = a & b
        result_label.config(text=f"Sum (A⊕B): {sum_ab}\nCarry (A.B): {carry_ab}")
    else:
        result_label.config(text="Wrong Input")

def ripple_carry_adder():
    result_label.config(text="Ripple Carry Adder")
    a = a_entry.get()
    b = b_entry.get()

    if set(a + b) <= {'0', '1'} and len(a) == len(b) == 4:
        a = a.zfill(4)
        b = b.zfill(4)

        n = len(a)
        carry = 0
        result = []

        for i in range(n - 1, -1, -1):
            bit_a = int(a[i])
            bit_b = int(b[i])
            sum_ab = bit_a ^ bit_b ^ carry
            carry = (bit_a & bit_b) | (carry & (bit_a ^ bit_b))
            result.insert(0, str(sum_ab))

        result_label.config(text=f"Sum: {''.join(result)}\nCarry: {carry}")
    else:
        result_label.config(text="Invalid input. Please enter valid 4-bit binary numbers.")

def carry_lookahead_adder():
    result_label.config(text="Carry Look-Ahead Adder")
    a = a_entry.get()
    b = b_entry.get()

    if set(a + b) <= {'0', '1'} and len(a) == len(b) == 4:
        a = a.zfill(4)
        b = b.zfill(4)

        n = len(a)
        carry_in = 0
        carry_out = [0] * (n + 1)
        result = []

        for i in range(n - 1, -1, -1):
            bit_a = int(a[i])
            bit_b = int(b[i])
            G = bit_a & bit_b
            P = bit_a | bit_b

            carry_out[i] = G | (P & carry_in)
            sum_bit = bit_a ^ bit_b ^ carry_in
            result.insert(0, str(sum_bit))

            carry_in = carry_out[i]

        result_label.config(text=f"Sum: {''.join(result)}\nCarry: {''.join(map(str, carry_out[:-1]))}")
    else:
        result_label.config(text="Invalid input. Please enter valid 4-bit binary numbers.")


app = tk.Tk()
app.title("Adder GUI")
app.geometry("800x450")

frame = tk.Frame(app)
frame.pack()

instruction_label = tk.Label(frame, text="Select the type of adder:")
instruction_label.pack()

choices = ["Half Adder", "Full Adder", "Ripple Carry Adder", "Carry Look-Ahead Adder"]
selected_choice = tk.StringVar(value=choices[0])

for choice in choices:
    choice_radio = tk.Radiobutton(frame, text=choice, variable=selected_choice, value=choice)
    choice_radio.pack()

a_label = tk.Label(frame, text="A:")
a_label.pack()

a_entry = tk.Entry(frame)
a_entry.pack()

b_label = tk.Label(frame, text="B:")
b_label.pack()

b_entry = tk.Entry(frame)
b_entry.pack()

result_label = tk.Label(frame, text="")  # Define result_label here
result_label.pack()

select_button = tk.Button(frame, text="Select", command=lambda: select_adder(selected_choice.get()))
select_button.pack()

app.mainloop()
