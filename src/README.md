# ISM2411 Data Cleaning with Copilot

This project is a small, GitHub ready data cleaning pipeline built for the ISM2411 Data Cleaning + Copilot Assignment.  
The goal is to load a messy sales dataset, clean it using Python, and generate a polished CSV file suitable for analysis.  
The project also demonstrates use of GitHub Copilot for generating and refining code.

What the Script Does:

The main script (`data_cleaning.py`) performs the following cleaning steps:

Load the raw CSV file, Standardize column names(lowercase, remove spaces, convert to underscores), Strip whitespace from text columns such as product and category, Handle missing values(remove rows missing price or quantity), Remove invalid rows(drop rows with negative prices or quantities), Export the cleaned dataset to `data/processed/sales_data_clean.csv`, All steps are explained in comments within the script.

How to Run

From the project root folder:

If everything is set up correctly, you will see:
No errors  
A new file at `data/processed/sales_data_clean.csv`  
A preview of the first few cleaned rows printed in the terminal

Copilot Usage

This project includes several functions that were initially generated using GitHub Copilot, then modified to fit the assignment goals.  
Details about what Copilot generated and what was changed are included in reflection.md.