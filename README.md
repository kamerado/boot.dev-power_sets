# Power Set Generator

This project is a Python implementation for generating the power set (all subsets) of a given set of elements. It uses binary representation to efficiently iterate through all possible subsets.

## Features
- Generate the power set of a given input set
- Utilize binary representation for subset generation
- Simple and efficient implementation

## How It Works

### 1. **Binary Representation of Subsets**
Each element in the input set is assigned a unique binary index. By iterating through all binary numbers of length equal to the input set's size, we determine which elements belong in each subset.

### 2. **Key Functions**
- `assign_bin(input_set)`: Assigns each element of the set a unique binary index.
- `bin_num_iter(input_set)`: Generates binary numbers from `0` to `2^n - 1`, representing subsets.
- `bin_array(bin_num)`: Converts a binary string into an array of integers.
- `power_set(input_set)`: Generates all possible subsets using binary representation.

### 3. **Example Usage**
```python
input_set = [1, 2, 3]
print(power_set(input_set))
```
**Output:**
```
[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
```

## Complexity Analysis
The overall complexity of this implementation is **O(n * 2^n)**. 
- `assign_bin(input_set)` runs in **O(n)**.
- `bin_num_iter(input_set)` generates **2^n** binary numbers.
- `power_set(input_set)` iterates through all **2^n** subsets and processes each in **O(n)**, resulting in **O(n * 2^n)**.

## Installation & Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/power-set-generator.git
   ```
2. Navigate to the directory:
   ```sh
   cd power-set-generator
   ```
3. Run the script:
   ```sh
   python script.py
   ```
