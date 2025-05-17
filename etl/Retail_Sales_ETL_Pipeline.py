import pandas as pd
from sqlalchemy import create_engine

# This code is an ETL pipeline that extracts data from an Excel file, cleans it, transforms it, and loads it into a SQL database.
def extract(filepath):
 
 try:
    df = pd.read_excel(filepath)
    print(f"[✔] Data extracted: {df.shape[0]} rows")
    return df
 except Exception as e:
   print(f"[❌] Extraction failed: {e}")
   return None


def clean_data(df):
  df = df[df["CustomerID"].notnull()]
  df = df[df["UnitPrice"] > 0]
  df = df[df["Quantity"] > 0]
  print(f"[✔] Cleaned data: {df.shape[0]} rows")
  return df


def transform(df):
   df['TotalPrice'] = df['UnitPrice'] * df['Quantity']
   df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
   df['Year'] = df['InvoiceDate'].dt.year
   df['Month'] = df['InvoiceDate'].dt.month
   print("[✔] Data transformed with TotalPrice, Year, and Month columns")
   return df


def load_to_sql(df, connection_string, table_name):
    try:
        engine = create_engine(connection_string)
        df.to_sql(table_name , con = engine, if_exists = 'replace' , index = False)
        print(f"[✔] Data loaded into SQL table: {table_name}")
    except Exception as e:
       print(f"[❌] Loading failed: {e}")

def run_etl(file_path, connection_string, table_name):
   df = extract(file_path)
   if df is not None :
      cleaned_data = clean_data(df)
      transformed_data = transform(cleaned_data)
      load_to_sql(transformed_data,connection_string,table_name)

if __name__ == "__main__":
    # Use raw string (r) prefix or double backslashes for Windows file paths
    run_etl(
        r"C:\your_Path_here\Online_Retail.xlsx",
        "mssql+pyodbc://username:password@ServerName/DatabaseName?driver=ODBC+Driver+17+for+SQL+Server"
    )

