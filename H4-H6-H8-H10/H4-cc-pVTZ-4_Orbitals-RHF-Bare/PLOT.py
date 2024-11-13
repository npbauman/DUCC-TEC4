import os
import re
import matplotlib.pyplot as plt
from ipywidgets import interact, Dropdown
import numpy as np

# Directory containing your ".out" files
directory = '.'

# Initialize dictionaries to hold data
one_electron_data = {}
two_electron_data = {}

# Function to parse files
def parse_files():
    for filename in os.listdir(directory):
        if filename.endswith(".out"):
            x_value = float(filename.replace(".out", ""))
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r') as file:
                content = file.readlines()

            # Parse one-electron integrals
            inside_one_electron = False
            inside_two_electron = False

            for line in content:
                line = line.strip()
                
                if line.startswith("begin_one_electron_integrals"):
                    inside_one_electron = True
                    continue
                elif line.startswith("end_one_electron_integrals"):
                    inside_one_electron = False
                    continue
                
                if line.startswith("begin_two_electron_integrals"):
                    inside_two_electron = True
                    continue
                elif line.startswith("end_two_electron_integrals"):
                    inside_two_electron = False
                    continue

                # Parse the values inside each integral block
                if inside_one_electron:
                    parts = line.split()
                    if len(parts) == 3:
                        label = (int(parts[0]), int(parts[1]))
                        value = float(parts[2])
                        if label not in one_electron_data:
                            one_electron_data[label] = []
                        one_electron_data[label].append((x_value, value))

                elif inside_two_electron:
                    parts = line.split()
                    if len(parts) == 5:
                        label = (int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3]))
                        value = float(parts[4])
                        if label not in two_electron_data:
                            two_electron_data[label] = []
                        two_electron_data[label].append((x_value, value))

# Run parsing function
parse_files()

# Function to plot selected data
def plot_data(label):
    if label in one_electron_data:
        x_vals, y_vals = zip(*sorted(one_electron_data[label]))
    elif label in two_electron_data:
        x_vals, y_vals = zip(*sorted(two_electron_data[label]))
    else:
        return
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, marker='o', linestyle='-')
    plt.xlabel('X Value')
    plt.ylabel('Integral Value')
    plt.title(f'Plot for Label {label}')
    plt.grid(True)
    plt.show()

# Create dropdown options from all labels
all_labels = list(one_electron_data.keys()) + list(two_electron_data.keys())
dropdown = Dropdown(options=all_labels, description="Select Label:")

# Create interactive plot
interact(plot_data, label=dropdown)
