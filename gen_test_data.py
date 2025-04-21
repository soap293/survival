import os
import pandas as pd
import random
from datetime import datetime, timedelta

# ── CONFIG ────────────────────────────────────────────────────────────────
OUTPUT_DIR = "data/test_shoplst"
NUM_DAYS   = 20           # how many daily files to generate
BASE_DATE  = datetime.now().date()
random.seed(42)             # for reproducibility
# ─────────────────────────────────────────────────────────────────────────

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define a small pool of shops
shop_templates = [
    {"shopcode": "1001", "shopname": "A Cafe",   "address": "123 Main St",    "shoplst": "cozy",  "shoplng": 121.50, "catlst": "Coffee"},
    {"shopcode": "1002", "shopname": "B Bakery", "address": "456 Elm Rd",     "shoplst": "fresh", "shoplng": 121.51, "catlst": "Bakery"},
    {"shopcode": "1003", "shopname": "C Sushi",  "address": "789 Oak Ave",    "shoplst": "sushi", "shoplng": 121.52, "catlst": "Japanese"},
    {"shopcode": "1004", "shopname": "D Pizza",  "address": "321 Pine Blvd",  "shoplst": "slice", "shoplng": 121.53, "catlst": "Italian"},
    {"shopcode": "1005", "shopname": "E Tacos",  "address": "654 Maple Lane", "shoplst": "spicy", "shoplng": 121.54, "catlst": "Mexican", "test": True},
]

for i in range(NUM_DAYS):
    day = BASE_DATE - timedelta(days=NUM_DAYS - i)
    date_str = day.isoformat()
    
    # Randomly choose 3–5 shops to appear that day
    today_shops = random.sample(shop_templates, k=random.randint(3, 5))
    
    # Occasionally introduce a new shop on the last day
    if i == NUM_DAYS - 1:
        today_shops.append({
            "shopcode": "1006",
            "shopname": "F Burger",
            "address": "999 Sunset St",
            "shoplst": "grill",
            "shoplng": 121.55,
            "catlst": "Fast Food"
        })
    
    df = pd.DataFrame(today_shops)
    
    # Save to CSV named by the scrape date
    path = os.path.join(OUTPUT_DIR, f"{date_str}.csv")
    df.to_csv(path, index=False, encoding="utf-8-sig")
    print(f"Written {len(df)} rows to {path}")
