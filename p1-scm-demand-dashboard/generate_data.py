import pandas as pd
import numpy as np
import random
import os

# Reproducibility
np.random.seed(42)
random.seed(42)

# ── Create output folder next to this script ────────────────────────────────
base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

# ── dim_product ──────────────────────────────────────────────────────────────
rows = []
pid = 1

categories = {
    "Electronics": [
        "Laptop", "Monitor", "Keyboard", "Mouse",
        "Headset", "Webcam", "Tablet", "Charger"
    ],
    "Pharma": [
        "Paracetamol", "Ibuprofen", "Vitamin C", "Antiseptic",
        "Bandages", "Syringes", "Masks", "Gloves"
    ],
    "Retail": [
        "T-Shirt", "Jeans", "Sneakers", "Jacket",
        "Cap", "Socks", "Belt", "Backpack"
    ],
    "Supply Chain": [
        "Pallet", "Shrink Wrap", "Forklift Part", "Conveyor Belt",
        "Label Printer", "Barcode Scanner", "Shelving Unit", "Hand Truck"
    ]
}

for category, products in categories.items():
    for product in products:
        rows.append({
            "product_id": f"PRD{pid:03d}",
            "product_name": product,
            "category": category,
            "unit_price": round(random.uniform(5, 1200), 2),
            "lead_time_days": random.randint(2, 21),
            "reorder_point": random.randint(50, 300),
            "safety_stock": random.randint(20, 100)
        })
        pid += 1

dim_product = pd.DataFrame(rows)

# ── dim_supplier ─────────────────────────────────────────────────────────────
supplier_names = [
    "GlobalTech Supplies", "FastTrack Logistics", "PrimeParts Co",
    "NexGen Materials", "SwiftSource Ltd", "AsiaPac Traders",
    "EuroBridge Goods", "IndiaFirst Exports", "CoastLine Vendors",
    "ApexSupply Chain"
]

supplier_countries = ["India", "China", "Germany", "USA", "Vietnam", "Singapore", "UK", "Japan"]

supplier_rows = []
for i, name in enumerate(supplier_names, start=1):
    supplier_rows.append({
        "supplier_id": f"SUP{i:03d}",
        "supplier_name": name,
        "country": random.choice(supplier_countries),
        "reliability_score": round(random.uniform(0.60, 0.99), 2),
        "avg_lead_time_days": random.randint(3, 20),
        "contract_value_usd": round(random.uniform(50000, 2000000), 2)
    })

dim_supplier = pd.DataFrame(supplier_rows)

# ── dim_warehouse ────────────────────────────────────────────────────────────
warehouse_rows = [
    {"warehouse_id": "WH001", "warehouse_name": "Mumbai Hub",     "city": "Mumbai",    "country": "India",     "capacity_sqft": 50000},
    {"warehouse_id": "WH002", "warehouse_name": "Delhi North",    "city": "Delhi",     "country": "India",     "capacity_sqft": 35000},
    {"warehouse_id": "WH003", "warehouse_name": "Bangalore Tech", "city": "Bangalore", "country": "India",     "capacity_sqft": 28000},
    {"warehouse_id": "WH004", "warehouse_name": "Chennai Port",   "city": "Chennai",   "country": "India",     "capacity_sqft": 42000},
    {"warehouse_id": "WH005", "warehouse_name": "Singapore DC",   "city": "Singapore", "country": "Singapore", "capacity_sqft": 60000},
    {"warehouse_id": "WH006", "warehouse_name": "Frankfurt Euro", "city": "Frankfurt", "country": "Germany",   "capacity_sqft": 55000}
]

dim_warehouse = pd.DataFrame(warehouse_rows)

# ── dim_date ─────────────────────────────────────────────────────────────────
date_range = pd.date_range(start="2023-01-01", end="2025-12-31", freq="D")

dim_date = pd.DataFrame({
    "date_id": date_range.strftime("%Y%m%d").astype(int),
    "date": date_range,
    "year": date_range.year,
    "quarter": date_range.quarter,
    "month": date_range.month,
    "month_name": date_range.strftime("%B"),
    "week": date_range.isocalendar().week.astype(int),
    "day_of_week": date_range.strftime("%A"),
    "is_weekend": (date_range.dayofweek >= 5).astype(int)
})

# ── fact_orders ──────────────────────────────────────────────────────────────
n = 10500

selected_dates = np.random.choice(date_range, n)
selected_products = np.random.choice(dim_product["product_id"], n)
selected_suppliers = np.random.choice(dim_supplier["supplier_id"], n)
selected_warehouses = np.random.choice(dim_warehouse["warehouse_id"], n)
selected_regions = np.random.choice(["North", "South", "East", "West", "International"], n)

order_qty = np.random.randint(10, 500, n)
forecasted_qty = (order_qty * np.random.uniform(0.85, 1.15, n)).round().astype(int)

actual_lead_days = np.random.randint(1, 25, n)
promised_lead_days = np.random.randint(3, 20, n)

unit_cost_lookup = dim_product.set_index("product_id")["unit_price"].to_dict()
unit_cost = [unit_cost_lookup[p] for p in selected_products]
total_order_value = np.round(np.array(order_qty) * np.array(unit_cost), 2)

forecast_accuracy_pct = (
    1 - (np.abs(order_qty - forecasted_qty) / np.maximum(forecasted_qty, 1))
) * 100
forecast_accuracy_pct = np.clip(forecast_accuracy_pct, 0, 100)

on_time_delivery = (actual_lead_days <= promised_lead_days).astype(int)
stockout_flag = np.random.choice([0, 1], n, p=[0.88, 0.12])
return_flag = np.random.choice([0, 1], n, p=[0.95, 0.05])

fact_orders = pd.DataFrame({
    "order_id": [f"ORD{i:05d}" for i in range(1, n + 1)],
    "date_id": pd.to_datetime(selected_dates).strftime("%Y%m%d").astype(int),
    "product_id": selected_products,
    "supplier_id": selected_suppliers,
    "warehouse_id": selected_warehouses,
    "region": selected_regions,
    "order_qty": order_qty,
    "forecasted_qty": forecasted_qty,
    "unit_cost": np.round(unit_cost, 2),
    "total_order_value": total_order_value,
    "actual_lead_days": actual_lead_days,
    "promised_lead_days": promised_lead_days,
    "on_time_delivery": on_time_delivery,
    "forecast_accuracy_pct": np.round(forecast_accuracy_pct, 2),
    "stockout_flag": stockout_flag,
    "return_flag": return_flag
})

# ── Save CSV files ───────────────────────────────────────────────────────────
dim_product.to_csv(os.path.join(data_dir, "dim_product.csv"), index=False)
dim_supplier.to_csv(os.path.join(data_dir, "dim_supplier.csv"), index=False)
dim_warehouse.to_csv(os.path.join(data_dir, "dim_warehouse.csv"), index=False)
dim_date.to_csv(os.path.join(data_dir, "dim_date.csv"), index=False)
fact_orders.to_csv(os.path.join(data_dir, "fact_orders.csv"), index=False)

# ── Print summary ────────────────────────────────────────────────────────────
print("✅ Done!")
print("CSV folder:", data_dir)
print(f"fact_orders    : {len(fact_orders):,} rows x {len(fact_orders.columns)} cols")
print(f"dim_product    : {len(dim_product):,} rows")
print(f"dim_supplier   : {len(dim_supplier):,} rows")
print(f"dim_warehouse  : {len(dim_warehouse):,} rows")
print(f"dim_date       : {len(dim_date):,} rows")
print(f"Total value    : ${fact_orders['total_order_value'].sum():,.0f}")
print(f"OTD rate       : {fact_orders['on_time_delivery'].mean() * 100:.1f}%")
print(f"Forecast acc   : {fact_orders['forecast_accuracy_pct'].mean():.1f}%")
print(f"Stockout rate  : {fact_orders['stockout_flag'].mean() * 100:.1f}%")