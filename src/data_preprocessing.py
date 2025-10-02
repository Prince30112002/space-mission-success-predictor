import pandas as pd
import os

def clean_space_data(input_path, output_path):
    # Read the dataset
    df = pd.read_csv(input_path)

    # Show initial info
    print("✅ Data loaded successfully!")
    print("Columns:", df.columns.tolist())

    # Rename and convert date column
    df['Date'] = pd.to_datetime(df['Datum'], errors='coerce')
    df.drop(columns=['Datum'], inplace=True)

    # Strip extra spaces from column names
    df.columns = df.columns.str.strip()

    # Handle missing values
    df.dropna(subset=['Company Name', 'Location', 'Status Mission'], inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Clean column names
    df.columns = (
        df.columns.str.replace(' ', '_')
                  .str.replace('-', '_')
                  .str.lower()
    )

    # Ensure processed folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Save cleaned data
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to: {output_path}")
    print(f"🧹 Final shape: {df.shape}")

if __name__ == "__main__":
    clean_space_data(
        "data/raw/Space_Corrected.csv",
        "data/processed/cleaned_space_missions.csv"
    )
