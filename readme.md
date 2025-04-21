# README

## Overview

This notebook is designed to manage and update active/inactive shop lists for a daily survival analysis. It processes shop data from a specified date range, identifies active and inactive shops based on their activity, and saves the results into CSV files.

---

## Features

1. **Active/Inactive Table Generation**:
   - Fetches shop data within a given date range.
   - Concatenates the data and calculates active and inactive shop lists based on the last activity date.

2. **Incremental Updates**:
   - Updates the active/inactive shop lists day by day until a target date.
   - Merges new data with existing records and recalculates the shop statuses.

3. **Parallel Processing**:
   - Uses multithreading to process multiple files and folders in parallel for faster execution.

---

## Functions

### 1. `deep_find_files(file_format, directory, *keywords)`
- Recursively searches for files with a specific format (e.g., `.csv`) in a directory and its subdirectories.
- Filters files based on optional keywords.

### 2. `concat_folder(folder_path, max_workers=4)`
- Reads all CSV files in a folder (and subfolders) in parallel.
- Returns a concatenated DataFrame of all the data.

### 3. `update_survival_dfs(base_folder, start_date, end_date, max_workers=8, active_file, inactive_file)`
- Updates the active and inactive shop lists:
  - Reads existing active/inactive CSV files if available.
  - Processes new shop data from the specified date range.
  - Merges new data with existing records.
  - Identifies active shops (last seen within 60 days) and inactive shops (last seen 60+ days ago).
  - Saves the updated active and inactive shop lists to CSV files.

---

## Usage

### Generate New Records
To process shop data for a specific date range and generate active/inactive shop lists:
```python
active, inactive = update_survival_dfs(
    base_folder="data/survive_test_data",
    start_date="2024-01-01",
    end_date="2024-12-31",
    max_workers=8,
    active_file="active_shops.csv",
    inactive_file="inactive_shops.csv"
)
```

### Update Existing Records
To update the active/inactive shop lists incrementally:
```python
active, inactive = update_survival_dfs(
    base_folder="data/survive_test_data",
    start_date="2025-01-01",
    end_date="2025-01-01",
    max_workers=8,
    active_file="active_shops.csv",
    inactive_file="inactive_shops.csv"
)
```

---

## Output

1. **Active Shops**:
   - Saved to active_shops.csv.
   - Contains shops that were last seen within the last 60 days.

2. **Inactive Shops**:
   - Saved to inactive_shops.csv.
   - Contains shops that were last seen 60 or more days ago.

---

## Dependencies

- Python 3.11+
- Libraries:
  - `pandas`
  - `numpy`
  - `os`
  - `traceback`
  - `concurrent.futures`
  - `tqdm`

---

## Notes

- The `scrape_batch_date` column is used to determine the activity date of each shop.
- The `days_since_last` metric is calculated based on the most recent `last_seen` date in the dataset.
- Ensure the folder structure and file formats match the expected input for smooth execution.