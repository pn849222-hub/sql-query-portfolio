# SQL Query Portfolio - Superstore Business Questions
# Author: [BenDTA]
# 10 queries from basic to advanced

import sqlite3
import pandas as pd

conn = sqlite3.connect("superstore.db")

def run_query(title, sql):
    print(f"\n{'='*55}")
    print(f" {title}")
    print('='*55)
    df = pd.read_sql_query(sql, conn)
    print(df.to_string(index=False))

# ── BASIC ────────────────────────────────────────────────

# Q1: Total revenue and profit
run_query("Q1: Overall Business Performance", """
    SELECT 
        COUNT(*)           AS total_orders,
        ROUND(SUM(Sales),2)  AS total_revenue,
        ROUND(SUM(Profit),2) AS total_profit,
        ROUND(AVG(Sales),2)  AS avg_order_value
    FROM orders
""")

# Q2: Revenue by category
run_query("Q2: Revenue & Profit by Category", """
    SELECT 
        Category,
        ROUND(SUM(Sales),2)                            AS total_sales,
        ROUND(SUM(Profit),2)                           AS total_profit,
        ROUND(SUM(Profit)*100.0/SUM(Sales),1)          AS profit_margin_pct
    FROM orders
    GROUP BY Category
    ORDER BY total_sales DESC
""")

# Q3: Top 5 states by revenue
run_query("Q3: Top 5 States by Revenue", """
    SELECT 
        State,
        ROUND(SUM(Sales),2) AS total_sales,
        COUNT(*)            AS num_orders
    FROM orders
    GROUP BY State
    ORDER BY total_sales DESC
    LIMIT 5
""")

# ── INTERMEDIATE ─────────────────────────────────────────

# Q4: Monthly sales trend
run_query("Q4: Yearly Sales Growth", """
    SELECT 
        SUBSTR(Order_Date, 7, 4)   AS year,
        ROUND(SUM(Sales),2)        AS total_sales,
        COUNT(*)                   AS num_orders
    FROM orders
    GROUP BY year
    ORDER BY year
""")

# Q5: Best sub-categories by profit
run_query("Q5: Top 5 Most Profitable Sub-Categories", """
    SELECT 
        "Sub-Category",
        Category,
        ROUND(SUM(Profit),2) AS total_profit,
        COUNT(*)             AS num_orders
    FROM orders
    GROUP BY "Sub-Category"
    ORDER BY total_profit DESC
    LIMIT 5
""")

# Q6: Worst sub-categories (losing money)
run_query("Q6: Sub-Categories Losing Money", """
    SELECT 
        "Sub-Category",
        Category,
        ROUND(SUM(Profit),2) AS total_profit,
        COUNT(*)             AS num_orders
    FROM orders
    GROUP BY "Sub-Category"
    HAVING total_profit < 0
    ORDER BY total_profit ASC
""")

# ── ADVANCED ─────────────────────────────────────────────

# Q7: Discount impact on profit
run_query("Q7: How Discount Levels Affect Profit", """
    SELECT 
        CASE 
            WHEN Discount = 0         THEN '0%'
            WHEN Discount <= 0.10     THEN '1-10%'
            WHEN Discount <= 0.20     THEN '11-20%'
            WHEN Discount <= 0.30     THEN '21-30%'
            ELSE 'Over 30%'
        END                          AS discount_range,
        COUNT(*)                     AS num_orders,
        ROUND(AVG(Profit),2)         AS avg_profit,
        ROUND(SUM(Profit),2)         AS total_profit
    FROM orders
    GROUP BY discount_range
    ORDER BY avg_profit DESC
""")

# Q8: Top 10 customers by revenue
run_query("Q8: Top 10 Customers by Revenue", """
    SELECT 
        Customer_Name,
        Segment,
        ROUND(SUM(Sales),2)  AS total_spent,
        COUNT(*)             AS num_orders,
        ROUND(AVG(Sales),2)  AS avg_order_value
    FROM orders
    GROUP BY Customer_Name
    ORDER BY total_spent DESC
    LIMIT 10
""")

# Q9: Ship mode performance
run_query("Q9: Shipping Mode Analysis", """
    SELECT 
        Ship_Mode,
        COUNT(*)                AS num_orders,
        ROUND(AVG(
            CAST(SUBSTR(Ship_Date,7,4) AS INT)*365 +
            CAST(SUBSTR(Ship_Date,1,2) AS INT)*30 +
            CAST(SUBSTR(Ship_Date,4,2) AS INT)
            -
            CAST(SUBSTR(Order_Date,7,4) AS INT)*365 -
            CAST(SUBSTR(Order_Date,1,2) AS INT)*30 -
            CAST(SUBSTR(Order_Date,4,2) AS INT)
        ),1)                    AS avg_ship_days,
        ROUND(SUM(Sales),2)     AS total_sales
    FROM orders
    GROUP BY Ship_Mode
    ORDER BY num_orders DESC
""")

# Q10: Region + Category performance matrix
run_query("Q10: Region x Category Performance Matrix", """
    SELECT 
        Region,
        Category,
        ROUND(SUM(Sales),2)   AS total_sales,
        ROUND(SUM(Profit),2)  AS total_profit,
        ROUND(SUM(Profit)*100.0/SUM(Sales),1) AS margin_pct
    FROM orders
    GROUP BY Region, Category
    ORDER BY Region, total_sales DESC
""")

conn.close()
print("\n✓ All queries completed!")