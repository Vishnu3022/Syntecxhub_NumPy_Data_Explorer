# NumPy Data Explorer

## Overview
NumPy Data Explorer is a hands-on Python project that demonstrates NumPy’s power for fast numerical computing. It walks through array creation, manipulation, reshaping, broadcasting, file storage, and performance benefits compared to native Python lists.

## What You’ll Learn
- Creating and inspecting NumPy arrays
- Indexing, slicing, and data selection
- Element-wise math and statistical analysis
- Axis-based operations and aggregation
- Reshaping arrays and using `-1` for automatic dimensions
- Broadcasting rules for combining arrays
- Saving/loading `.npy`, `.npz`, and text data
- Measuring performance gains from vectorized NumPy operations

## Installation

1. Install Python 3.8 or newer.
2. Install NumPy:

```bash
python -m pip install numpy
```

If you use a virtual environment, activate it before installing.

## Quick Start

Run the main demonstration script:

```bash
cd numpy_data_explorer
python main.py
```

This executes examples from the following modules:
- `main.py` — overall walkthrough and sample output
- `operations.py` — math, axis, and statistical operations
- `reshape_broadcast.py` — reshaping and broadcasting examples
- `file_io.py` — save/load `.npy`, `.npz`, and text files
- `performance_compare.py` — NumPy versus Python list timing

## Project Structure

- `main.py` — orchestrates demos for array creation, indexing, operations, reshaping, file I/O, and performance
- `operations.py` — dataset generation plus math/statistics helper functions
- `reshape_broadcast.py` — reshaping techniques and broadcasting examples
- `file_io.py` — array persistence with NumPy binary and text formats
- `performance_compare.py` — runtime comparison between Python lists and NumPy arrays
- `array_data.npy` — sample binary NumPy file created by the demo
- `multiple_arrays.npz` — sample compressed archive created by the demo
- `array.txt` — sample text export created by the demo

## Usage Examples

### Array creation and inspection
```python
python main.py
```

### Use modules directly
```python
python -c "from numpy_data_explorer.operations import create_dataset; import numpy as np; print(create_dataset())"
```

### Re-run file I/O examples
```bash
cd numpy_data_explorer
python file_io.py
```

### Re-run performance comparison
```bash
cd numpy_data_explorer
python performance_compare.py
```

## Notes
- The demo generates and saves files in the working directory.
- `np.save` creates `array_data.npy`.
- `np.savez` creates `multiple_arrays.npz`.
- `np.savetxt` creates `array.txt`.

## Recommended Improvements
- Add a `requirements.txt` for reproducible installs.
- Add unit tests for each helper module.
- Add more examples for masking, filtering, and advanced indexing.

## License
This project is open for learning and experimentation.
