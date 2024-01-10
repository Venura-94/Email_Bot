from datetime import date 
import pandas as pd 
from send_email import send_email #local python module

#public googlesheet url - not secure
#SHEET_ID = "<1OmQPYrEuLT38EtxNHHor7fjnTDo1cWz5lgyyPcIlho4>"
#SHEET_NAME = "<Sheet1>"
#URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

URL = f"https://docs.google.com/spreadsheets/d/1OmQPYrEuLT38EtxNHHor7fjnTDo1cWz5lgyyPcIlho4/edit#gid=0"

def load_df(url):
    parse_dates = ["due date","reminder date"]
    df =pd.read_csv(url, parse_dates=parse_dates)
    return df

print(load_df(URL))

def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present >= row["reminder_date"].date()) and (row["has_paid"] == "no"):
            send_email(
                subject=f'[Dozen Invoice: {row["invoice_no"]}]',
                receiver_email=row["email"],
                name=row["name"],
                due_date=row["due_date"].strftime("%d,%b %Y"),  # Date example
                invoice_no=row["invoice_no"],
                amount=row["amount"],
            )
            email_counter += 1
    return f"total Emails Sent: {email_counter}"

df = load_df(URL)
result = query_data_and_send_emails(df)
print(result)
