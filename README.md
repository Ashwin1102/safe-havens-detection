# Safe Havens Detection

 The Safe Haven Risk Detection system is a data analytics
 platform designed to assess community safety across U.S.
 counties and cities. Evaluate safety levels using socioeco
nomic indicators such as crime rates, poverty, and unemploy
ment. This system aids policymakers and organizations in
 making data-driven decisions to allocate resources effectively
 and enhance community well-being.
 
By Ashwin Khairnar and Rahul Reddy Mandadi
---

## How to Run the Project

Follow these steps to set up and run the project:

1. **Install Required Packages**  
   Install all the necessary Python packages by running:
   ```bash
   pip install -r requirements.txt

2. **Go to UI Folder**
   Run the following command:
   ```bash
   streamlit run view_table.py


## Project structure
1. **AnalyticsReport** - This has all images regarding the visualizations<br>
2. **Cleaned Data** - Data after the preprocessing<br>
3. **Data** - Raw data before preprocessing<br>
4. **Extract Data** - This has the files to extract the fipscode of the counties from geocoders api.<br>
5. **Machine Learning** - This contains the machine learning models.<br>
6. **Queries** - This has connection.py file which is used to establish the connection with DB. insert_data to insert the data from excel files (used in case the data in DB is deleted or changed).<br> query.py has all query functions which are used creating the visualizations.<br>
7. **UI**- Has the UI files (developed using strealit).<br>



 
