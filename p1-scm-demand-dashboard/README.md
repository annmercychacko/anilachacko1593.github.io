SCM Demand Dashboard project files
# Global Manufacturing Supply Chain Control Tower

This project is a Power BI dashboard built to simulate a manufacturing supply chain control tower using synthetic but business-realistic data. It focuses on core operational metrics such as order volume, order value, on-time delivery, forecast accuracy, stockout rate, supplier performance, and warehouse-level visibility. [Data generated locally using Python.]

## Overview

The goal of this project is to showcase an end-to-end business intelligence workflow for supply chain analytics:
- Generate structured synthetic data with Python
- Model a star schema in Power BI
- Create DAX measures for logistics and operations KPIs
- Build an executive-style dashboard for monitoring supply chain performance

This project is designed as a portfolio-ready analytics case study relevant to manufacturing, logistics, and supply chain visibility roles.

## Files in this Repository

```text
p1-scm-demand-dashboard/
├── data/
│   ├── dim_date.csv
│   ├── dim_product.csv
│   ├── dim_supplier.csv
│   ├── dim_warehouse.csv
│   └── fact_orders.csv
├── screenshots/
├── generate_data.py
├── scm_control_tower.pbix
└── README.md
```

## Dataset

The dataset used in this project was generated using Python and exported as CSV files. It includes:

- `fact_orders` — transactional order-level data
- `dim_date` — calendar table for time analysis
- `dim_product` — product master data
- `dim_supplier` — supplier details and reliability context
- `dim_warehouse` — warehouse and location details

### Fact table fields
The fact table includes metrics such as:
- order quantity
- forecasted quantity
- total order value
- actual lead time
- promised lead time
- on-time delivery flag
- forecast accuracy percentage
- stockout flag
- return flag

## Data Model

The Power BI model follows a star schema design:
- `fact_orders` at the center
- linked to `dim_date`
- linked to `dim_product`
- linked to `dim_supplier`
- linked to `dim_warehouse`

This structure supports scalable reporting, cleaner DAX calculations, and easier slicing by time, product, supplier, and warehouse.

## Dashboard KPIs

The dashboard includes the following key performance indicators:

- Total Orders
- Total Order Quantity
- Total Forecast Quantity
- Total Order Value
- On-Time Delivery %
- Avg Forecast Accuracy %
- Stockout Rate %
- Return Rate %
- Avg Actual Lead Time
- Avg Promised Lead Time
- Lead Time Variance

## Dashboard Views

The dashboard was built as an executive supply chain monitoring view with:
- KPI cards for top-level performance tracking
- trend analysis over time
- supplier performance comparisons
- warehouse-level performance monitoring
- tables for operational drilldown
- slicers for date, category, supplier, warehouse, and country/region

## Key Insights

A few typical insights this dashboard can help surface:
- Forecast accuracy may remain strong even when operational execution is weaker.
- On-time delivery performance can vary significantly across suppliers and warehouses.
- Stockout rate can remain meaningful despite relatively high forecast accuracy.
- Warehouse and supplier segmentation helps isolate operational bottlenecks.
- Lead time gaps between promised and actual delivery help identify fulfillment issues.

## Tools Used

- Python
- Pandas
- NumPy
- Power BI Desktop
- DAX
- CSV

## How to Use

1. Open the `.pbix` file in Power BI Desktop.
2. If needed, refresh file paths for the CSVs inside the `data/` folder.
3. Review the data model and DAX measures.
4. Explore the dashboard using slicers and filters.

## Why this Project

This project was built to demonstrate:
- data generation with Python
- dimensional modeling
- DAX-based KPI creation
- dashboard design for supply chain operations
- business storytelling through Power BI

It is intended as a portfolio project for analytics, business intelligence, and supply chain data roles.
