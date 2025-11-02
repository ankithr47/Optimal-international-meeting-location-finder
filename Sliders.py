import tkinter as tk

def get_weights():
    weights = {}

    def confirm_weights():
        weights['t'] = float(time_scale.get())
        weights['c'] = float(co2_scale.get())
        weights['f'] = float(fair_scale.get())
        root.destroy()

    root = tk.Tk()
    root.title("Select Weights")

    time_scale = tk.Scale(root, from_=0, to=1, orient="horizontal", resolution=0.01,
        label="Time Weight", length=500)
    co2_scale = tk.Scale(root, from_=0, to=1, orient="horizontal", resolution=0.01,
        label="CO₂ Weight", length=500)
    fair_scale = tk.Scale(root, from_=0, to=1, orient="horizontal", resolution=0.01,
        label="Fairness Weight", length=500)
    confirm_button = tk.Button(root, text="Confirm", command=confirm_weights)

    time_scale.set(0.6)
    co2_scale.set(0.4)
    fair_scale.set(0.0)

    time_scale.pack(fill='x')
    co2_scale.pack(fill='x')
    fair_scale.pack(fill='x')
    confirm_button.pack(pady=10)

    root.mainloop()
    return weights['t'], weights['c'], weights['f']

# Example of use:
if __name__ == "__main__":
    t, c, f = get_weights()
    print("Selected weights:", t, c, f)