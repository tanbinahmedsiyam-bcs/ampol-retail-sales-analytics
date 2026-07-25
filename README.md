# ampol-retail-sales-analytics
Data analytics &amp; predictive sales pipeline for Ampol retail fuel &amp; convenience store operations in Australia.
<div align="center">

# ⛽ Ampol Retail Sales & Convenience Analytics

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

*An end-to-end data processing and analytics pipeline evaluating fuel pricing, retail convenience store trends, and customer purchase patterns across Ampol Australia locations.*

</div>

---

## 📌 Business Overview

**Ampol Australia** operates one of the largest national networks of fuel stations and retail convenience hubs (Foodary). This project analyzes simulated and public retail operational data to extract actionable insights regarding:

* **Fuel vs. In-Store Spend:** Analyzing basket size correlation between fuel fill-ups and Foodary convenience store purchases.
* **Pricing & Volume Trends:** Assessing revenue sensitivity based on peak/off-peak fuel cycle price fluctuations across Australian states.
* **Peak Hour Footfall:** Identifying high-volume traffic hours to optimize store staffing and inventory replenishment.

---

## 📂 Project Structure

```text
ampol-retail-sales-analytics/
├── data/
│   ├── raw_ampol_sales.csv         # Raw transaction logs (simulated)
│   └── processed_sales.csv         # Cleaned & feature-engineered data
├── notebooks/
│   └── exploratory_analysis.ipynb  # EDA & statistical visualization
├── src/
│   ├── data_pipeline.py            # Data cleaning & aggregation scripts
│   └── sales_forecasting.py        # Trend analysis & predictive models
├── README.md                       # Project documentation
└── requirements.txt                # Python dependencies
