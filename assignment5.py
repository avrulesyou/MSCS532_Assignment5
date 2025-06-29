import time
import random
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set a higher recursion limit to handle larger arrays without crashing.
# This is crucial for the worst-case scenario of deterministic Quicksort.
sys.setrecursionlimit(2000000)

# --- Core Quicksort Implementations ---

def partition(arr, low, high, randomize=False):
    """
    Partitions the array using the Lomuto partition scheme.
    If randomize is True, it chooses a random pivot. Otherwise, it uses
    the last element as a deterministic pivot.
    """
    if randomize:
        rand_pivot_index = random.randrange(low, high + 1)
        arr[rand_pivot_index], arr[high] = arr[high], arr[rand_pivot_index]
    
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_recursive(arr, low, high, randomize=False):
    """
    Recursive helper function for Quicksort.
    The 'randomize' flag determines the pivot strategy.
    """
    if low < high:
        pi = partition(arr, low, high, randomize=randomize)
        quicksort_recursive(arr, low, pi - 1, randomize=randomize)
        quicksort_recursive(arr, pi + 1, high, randomize=randomize)

def quicksort(arr, randomize=False):
    """
    Main Quicksort function. It creates a copy of the array to sort.
    :param arr: The list to be sorted.
    :param randomize: If True, uses randomized pivot selection. 
                      If False, uses deterministic pivot selection.
    :return: A new, sorted list.
    """
    arr_copy = list(arr)
    quicksort_recursive(arr_copy, 0, len(arr_copy) - 1, randomize=randomize)
    return arr_copy

# --- Data Generation ---

def generate_random_data(size):
    """Generates a list of 'size' random integers."""
    return [random.randint(0, size * 10) for _ in range(size)]

def generate_sorted_data(size):
    """Generates a sorted list of 'size' integers."""
    return list(range(size))

def generate_reverse_sorted_data(size):
    """Generates a reverse-sorted list of 'size' integers."""
    return list(range(size, 0, -1))

# --- Performance Analysis and Plotting ---

def plot_results(results_df):
    """
    Plots the performance results using matplotlib.
    This visually represents the best, average, and worst cases.
    """
    pivot_df = results_df.pivot_table(
        index='Input Size', 
        columns=['Algorithm', 'Data Type'], 
        values='Execution Time (s)'
    )
    
    # Define styles for plotting
    styles = {
        ('Deterministic', 'Random'): {'color': 'blue', 'marker': 'o', 'linestyle': '--'},
        ('Deterministic', 'Sorted'): {'color': 'red', 'marker': 'x', 'linestyle': '-'},
        ('Deterministic', 'Reverse-Sorted'): {'color': 'orange', 'marker': 'x', 'linestyle': '-'},
        ('Randomized', 'Random'): {'color': 'cyan', 'marker': 'o', 'linestyle': '--'},
        ('Randomized', 'Sorted'): {'color': 'green', 'marker': 's', 'linestyle': '-.'},
        ('Randomized', 'Reverse-Sorted'): {'color': 'purple', 'marker': 's', 'linestyle': '-.'},
    }
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(14, 8))
    
    for column in pivot_df.columns:
        label = f"{column[0]} - {column[1]}"
        style = styles.get(column, {'color': 'gray', 'marker': '.'}) # Default style
        pivot_df[column].plot(ax=ax, label=label, **style)

    # Labeling and final touches
    ax.set_title('Quicksort Performance: Deterministic vs. Randomized', fontsize=16)
    ax.set_xlabel('Input Size (n)', fontsize=12)
    ax.set_ylabel('Execution Time (s) - Logarithmic Scale', fontsize=12)
    ax.set_yscale('log')
    ax.grid(True, which="both", linestyle='--', linewidth=0.5)
    ax.legend(title="Legend (Algorithm - Data Type)", bbox_to_anchor=(1.05, 1), loc='upper left')
    
    # Adding annotations for clarity
    plt.text(0.5, 0.6, 'Worst Case ($O(n^2)$)\n(Deterministic on sorted data)', 
             transform=ax.transAxes, color='red', fontsize=10, verticalalignment='top')
    plt.text(0.5, 0.4, r'Average/Best Case ($O(n \log n)$)' + '\n(Randomized on sorted data and\nboth on random data)', 
             transform=ax.transAxes, color='green', fontsize=10, verticalalignment='top')
    
    plt.tight_layout(rect=[0, 0, 0.85, 1]) # Adjust layout to make space for legend
    plt.show()

# --- Main Execution Block ---

if __name__ == "__main__":
    # Define dataset sizes to test.
    # Note: Using smaller sizes for sorted data with deterministic quicksort
    # to avoid excessively long run times that demonstrate the O(n^2) behavior.
    sizes_for_random = [1000, 5000, 10000, 20000, 50000]
    sizes_for_sorted = [1000, 2000, 4000, 6000] # Smaller to manage O(n^2) time

    results = []

    # A helper function to run and store results
    def run_test_case(alg_func, data, alg_name, data_name, randomize_flag):
        size = len(data)
        print(f"Testing {alg_name} on {data_name} data (size {size})...")
        
        start_time = time.perf_counter()
        alg_func(data, randomize=randomize_flag)
        end_time = time.perf_counter()
        
        execution_time = end_time - start_time
        print(f"Finished in {execution_time:.6f} seconds.\n")
        
        results.append({
            'Algorithm': alg_name,
            'Data Type': data_name,
            'Input Size': size,
            'Execution Time (s)': execution_time
        })

    # --- Run tests on Random Data (Average Case for both) ---
    for size in sizes_for_random:
        print(f"--- Running tests for RANDOM data, size: {size} ---\n")
        random_arr = generate_random_data(size)
        run_test_case(quicksort, list(random_arr), "Deterministic", "Random", randomize_flag=False)
        run_test_case(quicksort, list(random_arr), "Randomized", "Random", randomize_flag=True)

    # --- Run tests on Sorted/Reverse-Sorted Data (Worst Case for Deterministic) ---
    for size in sizes_for_sorted:
        print(f"--- Running tests for ORDERED data, size: {size} ---\n")
        sorted_arr = generate_sorted_data(size)
        reverse_arr = generate_reverse_sorted_data(size)
        
        # Test Deterministic (Worst Case)
        run_test_case(quicksort, list(sorted_arr), "Deterministic", "Sorted", randomize_flag=False)
        run_test_case(quicksort, list(reverse_arr), "Deterministic", "Reverse-Sorted", randomize_flag=False)

        # Test Randomized (Should remain efficient)
        run_test_case(quicksort, list(sorted_arr), "Randomized", "Sorted", randomize_flag=True)
        run_test_case(quicksort, list(reverse_arr), "Randomized", "Reverse-Sorted", randomize_flag=True)

    # --- Convert results to a pandas DataFrame and plot ---
    if results:
        results_df = pd.DataFrame(results)
        print("\n--- Empirical Analysis Results Summary ---")
        print(results_df)
        print("\nGenerating performance comparison plot...")
        plot_results(results_df)
    else:
        print("No results to plot.")
