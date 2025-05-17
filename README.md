# Data Engineering
# 🛍️ Online Retail ETL & Sales Dashboard Project

An end-to-end **ETL pipeline and interactive Power BI dashboard** built using Python, SQL Server, and Power BI — based on real-world e-commerce data.

![Dashboard Screenshot](powerbi/Screenshot.png)

---

## 📦 Dataset

- Source: [UCI Machine Learning Repository – Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)
- Transactions from a UK-based online retailer (2010–2011)
- Includes: invoices, products, customers, quantity, country, etc.

---

## 🧰 Tech Stack

- **Python** (ETL with `pandas`, `sqlalchemy`)
- **SQL Server** (Data warehousing)
- **Power BI** (Interactive dashboard)
- **GitHub** (Version control & portfolio)
- **Optional:** Docker, Cron for scheduling

---

---

## 🔁 ETL Pipeline

The entire ETL process is handled in one script:

📄 [`retail_etl_pipeline.py`](etl/Retail_Sales_ETL_Pipeline.py)

### Steps Included:

1. **Extract**: Load Excel file into pandas
2. **Transform**:
   - Remove null `CustomerID`
   - Remove negative quantities
   - Create new fields: `TotalPrice`, `Year`, `Month`
3. **Load**: Write clean data to SQL Server using SQLAlchemy

✅ Output Table: `OnlineRetail` in your SQL Server database

---

## ▶️ Run the ETL Script

```bash
python etl/retail_etl_pipeline.py


---

## 📊 Power BI Dashboard Design

**Key Features:**
- 💰 Total Revenue & Orders KPIs
- 📈 Revenue trend by month & year
- 🌍 Sales by Country (TreeMap)
- 🏆 Top Selling Products
- 🔎 Interactive filters: Country, Product, Year

📷 Screenshot:
![Sales Dashboard](powerbi/dashboard_screenshot.png)

---

## 🧠 Business Insights

- Seasonal sales trends are highest in November and December.
- Majority of sales are from the United Kingdom.

---

## 🛠️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/Online-Retail-ETL-Dashboard.git
cd Online-Retail-ETL-Dashboard

##2. Install Requirements

pip install -r requirements.txt

##3. Configure DB Connection
Edit the load.py connection string with your SQL Server credentials.
connection_string = "mssql+pyodbc://username:password@ServerName/DatabaseName?driver=ODBC+Driver+17+for+SQL+Server"

##4. Run ETL Pipeline

python etl_pipeline/run_etl.py

##5. Open Power BI
Load data from SQL Server table OnlineRetail

Import the .pbix file or recreate the dashboard using provided visuals

🙋‍♂️ Author
Yahya Elshazly
🔗 www.linkedin.com/in/yahya-elshazly-24ab97113
📬 yahyaelshazly96@gmail.com.com
