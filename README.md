# 🗄️ SQL Query Portfolio

A collection of 10 SQL business queries on the Superstore retail dataset,
demonstrating skills from basic aggregations to advanced analysis using SQLite.

---

## 📊 Queries Overview

| # | Query | Skill Level |
|---|-------|-------------|
| Q1 | Overall Business Performance | Basic |
| Q2 | Revenue & Profit by Category | Basic |
| Q3 | Top 5 States by Revenue | Basic |
| Q4 | Yearly Sales Growth | Intermediate |
| Q5 | Top 5 Most Profitable Sub-Categories | Intermediate |
| Q6 | Sub-Categories Losing Money | Intermediate |
| Q7 | How Discount Levels Affect Profit | Advanced |
| Q8 | Top 10 Customers by Revenue | Advanced |
| Q9 | Shipping Mode Analysis | Advanced |
| Q10 | Region × Category Performance Matrix | Advanced |

---

## 💡 Key Findings

- **Total revenue:** $2,297,200 across 9,994 orders
- **Technology** has the highest profit margin (17.4%)
- **Furniture** barely profitable at only 2.5% margin
- **California** is the #1 state ($457,687 revenue)
- Orders with **>30% discount** average a loss per order
- **Standard Class** is the most used shipping method

---

## 🛠️ Tech Stack

- **Python 3.x**
- **SQLite3** — lightweight database engine
- **pandas** — query execution and display

---

## ⚙️ How to Run
```bash
# 1. Clone the repo
git clone https://github.com/pn849222-hub/sql-query-portfolio.git
cd sql-query-portfolio

# 2. Install dependencies
pip install pandas

# 3. Setup database
python setup_database.py

# 4. Run all queries
python queries.py
```

---

## 📂 Dataset

- **Source:** [Kaggle — Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Records:** 9,994 orders | **Period:** 2014–2017

---

*Part of a Data Analytics portfolio for OJT applications.*
