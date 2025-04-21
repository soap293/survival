# README

## Overview

This notebook is designed to generate and update active/inactive shop lists for daily survival analysis. It processes shop data from a specified date range, identifies active and inactive shops based on their activity, and saves the results into CSV files.

---

## Features

1. **Create Active/Inactive Tables**:
   - Fetches shop data within a given date range.
   - Concatenates the data and generates active and inactive shop tables.

2. **Update to Target Date**:
   - Updates the active/inactive shop lists incrementally, day by day, until a specified target date.

---

## Functions

1. `deep_find_files(file_format: str, directory: str, *keywords: str) -> List[str]`
- Recursively searches for files with a specific format (e.g., `.csv`) in a directory and its subdirectories.
- Filters files based on optional keywords.

2. `concat_folder(folder_path: str, keywords: List[str], max_workers: int = 8) -> pd.DataFrame`
- Reads all CSV files in a folder (and subfolders) in parallel.
- Adds a `scrape_batch_date` column extracted from the folder name.
- Returns a concatenated DataFrame.

3. `update_survival_dfs(base_folder: str, start_date: str, end_date: str, keywords: List[str], max_workers: int = 8, active_file: str, inactive_file: str) -> Tuple[pd.DataFrame, pd.DataFrame]`
- Updates active/inactive shop lists:
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
    keywords=[],
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
    keywords=[],
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
  - `pathlib`

---

## Notes

- The `scrape_batch_date` column is used to determine the activity date of each shop.
- The `days_since_last` metric is calculated based on the most recent `last_seen` date in the dataset.
- Ensure the folder structure and file formats match the expected input for smooth execution.