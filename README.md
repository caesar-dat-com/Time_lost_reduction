<h1> ETL - lost_times proyect</h1>
---


![joanmz_an_image_of_a_water_company_with_this_format_54ab17a2-8d51-4f75-94f8-ef5e2ed97394](https://github.com/caesar-dat-com/Time_lost_reduction/assets/103477035/8047287e-11c3-48f0-bd51-aa8e9e8b8d79)

**Description**

<p>This project involves an Exploratory Data Analysis (EDA) process designed to handle data in various formats and perform tasks such as data loading, cleaning, and transformation. It is structured into three main modules: data loading, preliminary preprocessing, and transformation. Once these stages are completed, the data is loaded into an SQL database for further analysis.

The general objective of EDA is to examine and understand the input data, identify patterns, trends, or anomalies, and prepare the data for subsequent analysis. In this project, the aim is to recognize the structure and nature of the original data, and then process it to obtain four distinct datasets</p>


<h4 aling="center">
🐼 Requirements 🐼
<h4>




<p>For the requirements of the project, we need Python, SQL, and Power BI. Python libraries can be installed using </p>

<pre>pip install -r requirements.txt.</pre>



<p>First, we need to clean the data, which are located in 4 folders in the project: [dataset_actividades_no_programadas, dataset_actividades_programadas, dataset_inspecciones_no_programadas, dataset_inspecciones_programadas]. Since the data comes in an unmanageable state before we can even load them into a dataframe or a database, we need to process them. Therefore, before anything else, we need to execute the Python cleanin files located in the Aplication directory. This will generate c_data folders containing the first step of cleaning. Then, we will execute the merg.py file, which is the second process where we will concatenate all the data of the same nature. Finally, we will execute the postmerge.py file, which contains the last step to arrange the attributes of one of the CSVs. Once we finish the pre-cleaning process, we can use those data. Before loading the data,We need to create a .env file where we will place all the credentials of our database with the following structure:</p>

 
![Captura de pantalla 2024-03-08 234109](https://github.com/caesar-dat-com/Time_lost_reduction/assets/103477035/d0d55135-29a0-4d1a-afc5-3775c4ce2a7d)

<p>
After creating the database named etl_project, you can run the file Application/Pysqlconnect.py where our connection with the database will be configured. Then, you can run the Notebooks/load.py to add the data to our SQL database, in this case, PostgreSQL. Finally, you can use the EDA with the data from SQL.</p>

**this is the structure of the proyect**

- /
  - Aplication/                   <--- here clean the data and define connections to SQL
    - cleanin_actividades_no_programados.py
    - cleanin_actividades_programados.py
    - cleanin_inspecciones_no_programados.py
    - cleanin_inspecciones_programados.py
    - merg.py
    - post_merge.py
    - Pysql.connect.py
  - Dataset/                   <--- here we save the data
    - datasets limpios
  - Notebooks/                 <--- here we load the data and Explore the data
    - EDA.ipynb
    - load.ipynb
  - .env
  - requirements.txt
