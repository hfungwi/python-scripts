#import modules to be used for this program
import tkinter as tk

# Create the root window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("300x200")  # Set the initial size of the window

# Define quantities and their corresponding units
quantities = {
    "data_sizes": ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"],
    "height": ["meters", "centimeters", "feet", "inches"],
    "weight": ["kilograms", "grams", "pounds", "ounces"],
    "temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "distance": ["meters", "kilometers", "miles", "yards"],
}

# Initialize global variables
result_label = None

# Function to show the unit selection screen
def show_unit_selection():
    quantity = selected_quantity.get()
    units = quantities[quantity]

    # Clear the previous frame
    for widget in frame2.winfo_children():
        widget.destroy()

    # Add label and unit dropdowns to the frame
    unit_label = tk.Label(frame2, text=f"Select source and target units for {quantity}:")
    unit_label.pack()

    source_label = tk.Label(frame2, text="Source Unit:")
    source_label.pack()

    source_unit.set(units[0])  # Default value
    source_menu = tk.OptionMenu(frame2, source_unit, *units)
    source_menu.pack()

    target_label = tk.Label(frame2, text="Target Unit:")
    target_label.pack()

    target_unit.set(units[1])  # Default value
    target_menu = tk.OptionMenu(frame2, target_unit, *units)
    target_menu.pack()

    # Add the next button
    next_button = tk.Button(frame2, text="Next", command=show_input_screen)
    next_button.pack()

    # Add the back button
    back_button = tk.Button(frame2, text="Back", command=show_quantity_selection)
    back_button.pack()

    frame1.pack_forget()
    frame2.pack()

# Function to show the quantity selection screen
def show_quantity_selection():
    frame3.pack_forget()  # Hide frame3 if visible
    frame2.pack_forget()
    frame1.pack()

# Function to show the input value screen
def show_input_screen():
    for widget in frame3.winfo_children():
        widget.destroy()

    input_label = tk.Label(frame3, text="Enter the value to convert:")
    input_label.pack()

    input_entry = tk.Entry(frame3, textvariable=input_value)
    input_entry.pack()

    convert_button = tk.Button(frame3, text="Convert", command=perform_conversion)
    convert_button.pack()

    # Add the back button
    back_button = tk.Button(frame3, text="Back", command=show_unit_selection)
    back_button.pack()

    global result_label
    result_label = tk.Label(frame3, text="")
    result_label.pack()

    frame2.pack_forget()
    frame3.pack()

# Function to perform the conversion
def perform_conversion():
    try:
        value = float(input_value.get())
        source = source_unit.get()
        target = target_unit.get()
        quantity = selected_quantity.get()

        # Conversion formulas
        if quantity == "data_sizes":
            data_factors = {"bytes": 1, "kilobytes": 1024, "megabytes": 1024**2, "gigabytes": 1024**3, "terabytes":
1024**4}
            result = value * data_factors[source] / data_factors[target]
        elif quantity == "height":
            if source == "meters":
                if target == "centimeters":
                    result = value * 100
                elif target == "feet":
                    result = value * 3.28084
                elif target == "inches":
                    result = value * 39.3701
            elif source == "centimeters":
                if target == "meters":
                    result = value / 100
                elif target == "feet":
                    result = value * 0.0328084
                elif target == "inches":
                    result = value * 0.393701
            elif source == "feet":
                if target == "meters":
                    result = value / 3.28084
                elif target == "centimeters":
                    result = value * 30.48
                elif target == "inches":
                    result = value * 12
            elif source == "inches":
                if target == "meters":
                    result = value / 39.3701
                elif target == "centimeters":
                    result = value * 2.54
                elif target == "feet":
                    result = value / 12
        elif quantity == "weight":
            if source == "kilograms":
                if target == "grams":
                    result = value * 1000
                elif target == "pounds":
                    result = value * 2.20462
                elif target == "ounces":
                    result = value * 35.274
            elif source == "grams":
                if target == "kilograms":
                    result = value / 1000
                elif target == "pounds":
                    result = value * 0.00220462
                elif target == "ounces":
                    result = value * 0.035274
            elif source == "pounds":
                if target == "kilograms":
                    result = value / 2.20462
                elif target == "grams":
                    result = value * 453.592
                elif target == "ounces":
                    result = value * 16
            elif source == "ounces":
                if target == "kilograms":
                    result = value / 35.274
                elif target == "grams":
                    result = value * 28.3495
                elif target == "pounds":
                    result = value / 16
        elif quantity == "temperature":
            if source == "Celsius":
                if target == "Fahrenheit":
                    result = (value * 9/5) + 32
                elif target == "Kelvin":
                    result = value + 273.15
            elif source == "Fahrenheit":
                if target == "Celsius":
                    result = (value - 32) * 5/9
                elif target == "Kelvin":
                    result = (value - 32) * 5/9 + 273.15
            elif source == "Kelvin":
                if target == "Celsius":
                    result = value - 273.15
                elif target == "Fahrenheit":
                    result = (value - 273.15) * 9/5 + 32
        elif quantity == "distance":
            if source == "meters":
                if target == "kilometers":
                    result = value / 1000
                elif target == "miles":
                    result = value * 0.000621371
                elif target == "yards":
                    result = value * 1.09361
            elif source == "kilometers":
                if target == "meters":
                    result = value * 1000
                elif target == "miles":
                    result = value * 0.621371
                elif target == "yards":
                    result = value * 1093.61
            elif source == "miles":
                if target == "meters":
                    result = value / 0.000621371
                elif target == "kilometers":
                    result = value / 0.621371
                elif target == "yards":
                    result = value * 1760
            elif source == "yards":
                if target == "meters":
                    result = value / 1.09361
                elif target == "kilometers":
                    result = value / 1093.61
                elif target == "miles":
                    result = value / 1760

        result_label.config(text=f"Converting {value} {source} of {quantity} to {target}: {result} {target}")

    except ValueError:
        result_label.config(text="Please enter a valid number")

# Define frames
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)

# Frame 1: Quantity Selection
label = tk.Label(frame1, text="Select Quantity")
label.pack()

selected_quantity = tk.StringVar(root)
selected_quantity.set(list(quantities.keys())[0])  # Default value

quantity_menu = tk.OptionMenu(frame1, selected_quantity, *quantities.keys())
quantity_menu.pack()

next_button = tk.Button(frame1, text="Next", command=show_unit_selection)
next_button.pack()

frame1.pack()

# Frame 2: Unit Selection
source_unit = tk.StringVar(root)
target_unit = tk.StringVar(root)

# Frame 3: Input Value and Conversion
input_value = tk.StringVar()

root.mainloop()
