import pandas as pd
import sqlite3
conn = sqlite3.connect("data.sqlite")

# # ----------------- Select all products -----------------
# products = pd.read_sql("""
# SELECT *
#     FROM products
# """, conn)

# print(products)

# # ----------------- Order by product name ASC -----------------
# order_by_productName = pd.read_sql("""
# SELECT *
#     FROM products
#     ORDER BY productName ASC
# """, conn)

# print(order_by_productName)

# # ----------------- Order by product name DESC -----------------
# order_by_productName = pd.read_sql("""
# SELECT *
#     FROM products
#     ORDER BY productName DESC
# """, conn)

# print(order_by_productName)

# # ----------------- Sort based on string length -----------------
# sort_by_string_length = pd.read_sql("""
# SELECT productName, length(productDescription) AS description_length
#     FROM products
#     ORDER BY description_length
# """, conn)

# print(sort_by_string_length)

# # ----------------- Sort by something without selecting it -----------------
# sort_without_selecting = pd.read_sql("""
# SELECT productName
#     FROM products
#     ORDER BY length(productDescription)
# """, conn)

# print(sort_without_selecting)


# # ----------------- Sort by multiple columns  -----------------
# sort_by_multiple_columns = pd.read_sql("""
# SELECT productVendor, productName, MSRP
#     FROM products
#     ORDER BY productVendor, productName
# """, conn)

# print(sort_by_multiple_columns)


# # ----------------- Find how many unique values are in a column -----------------
# num_unique_values = pd.read_sql("""
# SELECT COUNT(DISTINCT productVendor) AS num_product_vendors,
#        COUNT(DISTINCT productName) AS num_product_names
#     FROM products
# """, conn)

# print(num_unique_values)

# # ----------------- Typecasting string values to sort correctly -----------------
# typecasting_values = pd.read_sql("""
# SELECT productName, quantityInStock
#     FROM products
#     ORDER BY CAST(quantityInStock AS INTEGER)
# """, conn)

# print(typecasting_values)


# # ----------------- Using LIMIT to specify only certain number of results -----------------
# limiting_results = pd.read_sql("""
# SELECT *
#     FROM orders
#     LIMIT 5
# """, conn)

# print(limiting_results)


# # ----------------- Using LIMIT with ORDER BY -----------------
# limit_and_order_by_results = pd.read_sql("""
# SELECT *
#     FROM orders
#     ORDER BY length(comments) DESC
#     LIMIT 10
# """, conn)

# print(limit_and_order_by_results)


# # ----------------- Using LIMIT with WHERE and ORDER BY -----------------
# limit_where_order_by_results = pd.read_sql("""
# SELECT *
#     FROM orders
#     WHERE status = "Cancelled"
#     ORDER BY length(comments) DESC
#     LIMIT 10
# """, conn)

# print(limit_where_order_by_results)


# # ----------------- Using LIMIT with WHERE IN and ORDER BY -----------------
# limit_where_in_order_by_results = pd.read_sql("""
# SELECT *
#     FROM orders
#     WHERE status IN ("Cancelled", "Resolved")
#     ORDER BY length(comments) DESC
#     LIMIT 10
# """, conn)

# print(limit_where_in_order_by_results)


# # ----------------- Using LIMIT with Date/Time Data -----------------
# limit_with_date_time = pd.read_sql("""
# SELECT DISTINCT customerNumber, orderDate
#     FROM orders
#     ORDER BY orderDate
#     LIMIT 5
# """, conn)

# print(limit_with_date_time)


# # ----------------- Select orders not shipped and not cancelled -----------------
# orders_not_shipped_or_cancelled = pd.read_sql("""
# SELECT *
#     FROM orders
#     WHERE shippedDate = "" AND status != "Cancelled"
#     ORDER BY orderDate DESC
#     LIMIT 10
# """, conn)

# print(orders_not_shipped_or_cancelled)


# ----------------- Order that took the longest to fill -----------------
order_longest_to_fill = pd.read_sql("""
SELECT *, julianday(shippedDate) - julianday(orderDate) AS days_to_fulfill
    FROM orders
    WHERE shippedDate != ""
    ORDER BY days_to_fulfill DESC
    LIMIT 1
""", conn)

print(order_longest_to_fill)



conn.close()