import pandas as pd


def generate_csv(expenses):

    df = pd.DataFrame(expenses)

    df["Amount"] = pd.to_numeric(df["Amount"])

    df.to_csv(
        "output/expenses.csv",
        index=False
    )

    summary = (
        df.groupby("Category")["Amount"]
        .sum()
        .reset_index()
    )

    summary.to_csv(
        "output/summary.csv",
        index=False
    )

    return df, summary