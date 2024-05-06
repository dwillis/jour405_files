import os
import pandas as pd

# Load the dataset to inspect its structure
file_path = 'MDOT_MVA_Electric_and_Plug-in_Hybrid_Vehicle_Registrations_by_County_as_of_each_month_end_from_July_2020_to_April_2024_20240506.csv'
data = pd.read_csv(file_path)

data['Fuel_Category'] = data['Fuel_Category'].str.upper()

# List of Maryland's 24 jurisdictions
counties = [
    "ALLEGANY", "ANNE ARUNDEL", "BALTIMORE", "BALTIMORE CITY", "CALVERT", 
    "CAROLINE", "CARROLL", "CECIL", "CHARLES", "DORCHESTER", "FREDERICK", 
    "GARRETT", "HARFORD", "HOWARD", "KENT", "MONTGOMERY", "PRINCE GEORGES", 
    "QUEEN ANNES", "SAINT MARYS", "SOMERSET", "TALBOT", "WASHINGTON", 
    "WICOMICO", "WORCESTER"
]

# Create and save a CSV for each county
for county in counties:
    # Filter data for the county
    filtered_data = data[data['County'].str.strip().str.upper() == county]
    
    # Pivot the table to make 'Fuel_Category' into columns
    pivoted_data = filtered_data.pivot_table(
        index=['Year_Month', 'County'],  # Keep County as part of the index
        columns='Fuel_Category', 
        values='Count', 
        aggfunc='sum', 
        fill_value=0
    ).reset_index()
    
    # Build the output path
    output_path = f"{county.lower()}.csv"
    
    # Save to CSV, index=False to avoid adding an unnamed index column
    pivoted_data.to_csv(output_path, index=False)
