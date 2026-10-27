import pandas as pd
import re


def validate(df):

    errors = []

    # Required field validation
    for column in df.columns:

        for index, value in enumerate(df[column]):

            if pd.isna(value) or str(value).strip() == "":

                errors.append({
                    "Row": index + 2,
                    "Column": column,
                    "Value": value,
                    "Error": "Required field missing"
                })

    # Duplicate Order ID

    if "Order ID" in df.columns:

        duplicates = df[df["Order ID"].duplicated()]

        for index in duplicates.index:

            errors.append({
                "Row": index + 2,
                "Column": "Order ID",
                "Value": df.loc[index, "Order ID"],
                "Error": "Duplicate Order ID"
            })

    # Email Validation

    if "Email" in df.columns:

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        for index, value in enumerate(df["Email"]):

            if pd.notna(value):

                if not re.match(email_pattern, str(value)):

                    errors.append({
                        "Row": index + 2,
                        "Column": "Email",
                        "Value": value,
                        "Error": "Invalid Email"
                    })

    return pd.DataFrame(errors)