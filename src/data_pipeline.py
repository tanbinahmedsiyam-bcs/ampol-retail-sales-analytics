import pandas as pd
import numpy as np

def load_and_clean_data(filepath):
    """Loads raw Ampol sales data and performs initial cleaning."""
    print(f"Loading retail data from {filepath}...")
    df = pd.read_csv(filepath)
    
    print("Cleaning data and engineering features...")
    # Drop rows with missing critical transaction IDs
    df = df.dropna(subset=['Transaction_ID'])
    
    # Calculate Total Spend
    df['Total_Spend'] = df['Fuel_Spend'] + df['In_Store_Spend']
    
    # Categorize the type of customer purchase
    conditions = [
        (df['Fuel_Spend'] > 0) & (df['In_Store_Spend'] > 0),
        (df['Fuel_Spend'] > 0) & (df['In_Store_Spend'] == 0),
        (df['Fuel_Spend'] == 0) & (df['In_Store_Spend'] > 0)
    ]
    choices = ['Hybrid (Fuel + Foodary)', 'Fuel Only', 'In-Store Only']
    df['Purchase_Category'] = np.select(conditions, choices, default='Unknown')
    
    print("Pipeline execution complete. Data preview:")
    print(df.head())
    
    return df

if __name__ == "__main__":
    # We will test this once our data file is uploaded!
    print("Ampol Retail Data Pipeline Initialized.")
