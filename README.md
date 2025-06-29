# Quicksort Performance Analysis: Deterministic vs Randomized

This project implements and compares the performance of deterministic and randomized Quicksort algorithms across different data types (random, sorted, and reverse-sorted). The analysis demonstrates the theoretical time complexity differences between these approaches and provides empirical evidence through benchmarking and visualization.

## 🎯 Project Overview

The project showcases:

- **Deterministic Quicksort**: Uses the last element as pivot (Lomuto partition scheme)
- **Randomized Quicksort**: Uses random pivot selection
- **Performance Analysis**: Tests on random, sorted, and reverse-sorted data
- **Visualization**: Generates performance comparison plots using matplotlib

### Key Findings

- **Deterministic Quicksort**: O(n²) worst-case on sorted/reverse-sorted data, O(n log n) average case on random data
- **Randomized Quicksort**: O(n log n) average case across all data types
- **Empirical Evidence**: Clear performance degradation of deterministic approach on ordered data

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation & Setup

#### For macOS/Linux:

```bash
# Clone the repository
git clone <your-repo-url>
cd Assignment-5

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### For Windows:

```bash
# Clone the repository
git clone <your-repo-url>
cd Assignment-5

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 📊 Running the Analysis

### Basic Execution

```bash
# Make sure your virtual environment is activated
python assignment5.py
```

### What the Program Does

1. **Generates test data** of varying sizes:
   - Random data: 1,000 to 50,000 elements
   - Sorted/Reverse-sorted data: 1,000 to 6,000 elements
2. **Runs performance tests** on both algorithms
3. **Displays results** in a formatted table
4. **Generates visualization** showing performance comparison

## 📈 Example Output

### Console Output

```
--- Running tests for RANDOM data, size: 1000 ---

Testing Deterministic on Random data (size 1000)...
Finished in 0.000585 seconds.

Testing Randomized on Random data (size 1000)...
Finished in 0.000758 seconds.

--- Running tests for ORDERED data, size: 1000 ---

Testing Deterministic on Sorted data (size 1000)...
Finished in 0.022443 seconds.

Testing Deterministic on Reverse-Sorted data (size 1000)...
Finished in 0.016710 seconds.

Testing Randomized on Sorted data (size 1000)...
Finished in 0.000772 seconds.

Testing Randomized on Reverse-Sorted data (size 1000)...
Finished in 0.000772 seconds.

--- Empirical Analysis Results Summary ---
        Algorithm       Data Type  Input Size  Execution Time (s)
0   Deterministic          Random        1000            0.000585
1      Randomized          Random        1000            0.000758
2   Deterministic          Sorted        1000            0.022443
3   Deterministic  Reverse-Sorted        1000            0.016710
4     Randomized          Sorted        1000            0.000772
5     Randomized  Reverse-Sorted        1000            0.000772
...
```

### Performance Visualization

The program generates an interactive matplotlib plot showing:

- **Blue dashed line**: Deterministic on random data (average case)
- **Red solid line**: Deterministic on sorted data (worst case - O(n²))
- **Orange solid line**: Deterministic on reverse-sorted data (worst case - O(n²))
- **Cyan dashed line**: Randomized on random data (average case)
- **Green dash-dot line**: Randomized on sorted data (average case)
- **Purple dash-dot line**: Randomized on reverse-sorted data (average case)

## 🔧 Code Structure

### Core Functions

- `quicksort(arr, randomize=False)`: Main sorting function
- `partition(arr, low, high, randomize=False)`: Lomuto partition scheme
- `generate_random_data(size)`: Creates random test data
- `generate_sorted_data(size)`: Creates sorted test data
- `generate_reverse_sorted_data(size)`: Creates reverse-sorted test data
- `plot_results(results_df)`: Generates performance visualization

### Key Features

- **In-place sorting**: Modifies arrays directly for efficiency
- **Recursion limit**: Set to 2,000,000 to handle large datasets
- **Logarithmic scale**: Y-axis uses log scale for better visualization
- **Comprehensive testing**: Multiple data sizes and types

## 📊 Performance Analysis

### Time Complexity Comparison

| Algorithm     | Best Case  | Average Case | Worst Case |
| ------------- | ---------- | ------------ | ---------- |
| Deterministic | O(n log n) | O(n log n)   | O(n²)      |
| Randomized    | O(n log n) | O(n log n)   | O(n log n) |

### Empirical Results Summary

- **Random Data**: Both algorithms perform similarly (O(n log n))
- **Sorted Data**: Deterministic shows O(n²) behavior, Randomized maintains O(n log n)
- **Reverse-Sorted Data**: Same pattern as sorted data

## 🛠️ Customization

### Modifying Test Sizes

Edit the `sizes_for_random` and `sizes_for_sorted` lists in the main execution block:

```python
sizes_for_random = [1000, 5000, 10000, 20000, 50000]  # For random data
sizes_for_sorted = [1000, 2000, 4000, 6000]          # For sorted data
```

### Adding New Data Types

Create new data generation functions and add them to the testing loop:

```python
def generate_custom_data(size):
    # Your custom data generation logic
    return your_data

# Add to testing loop
custom_arr = generate_custom_data(size)
run_test_case(quicksort, list(custom_arr), "Deterministic", "Custom", randomize_flag=False)
```

## 🐛 Troubleshooting

### Common Issues

**Import Errors:**

```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

**Recursion Limit Errors:**

- The code sets `sys.setrecursionlimit(2000000)` to handle large datasets
- If you still get recursion errors, reduce the test sizes

**Memory Issues:**

- Reduce the maximum test sizes in the configuration
- Close other applications to free up memory

### Performance Tips

- Use smaller test sizes for quick testing
- The deterministic algorithm on sorted data can be very slow for large sizes
- Consider running on a machine with sufficient RAM for large datasets

## 📝 Dependencies

- **matplotlib**: For performance visualization
- **pandas**: For data manipulation and results display
- **numpy**: For numerical operations (auto-installed with matplotlib/pandas)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Abhishek Vishwakarma**


---

**Note**: This project is designed for educational purposes to demonstrate the performance characteristics of different Quicksort implementations. The results clearly show why randomized pivot selection is preferred in practice.
