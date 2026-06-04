import pandas as pd

def load_sales_data(path):

    return pd.read_csv(path)

def get_sales_metrics(df):

    total_orders = len(df)

    total_revenue = df["total_amount"].sum()

    avg_order_value = round(
        total_revenue / total_orders,
        2
    ) if total_orders else 0

    return {
        "total_orders": int(total_orders),
        "total_revenue": float(total_revenue),
        "avg_order_value": float(avg_order_value)
    }

def conversion_rate(
    footfall,
    total_orders
):

    if footfall == 0:
        return 0

    return round(
        (total_orders / footfall) * 100,
        2
    )