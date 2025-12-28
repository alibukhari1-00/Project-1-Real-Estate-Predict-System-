import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import os

def process_housing_data(input_path, output_dir):
    # 1. Data Load karein
    if not os.path.exists(input_path):
        print(f"Error: {input_path} nahi mili!")
        return

    df = pd.read_csv(input_path)
    
    # 2. Unnecessary columns drop karein (Address string hai, model mein nahi jayega)
    # USA Housing dataset mein 'Address' column hota hai
    if 'Address' in df.columns:
        df = df.drop('Address', axis=1)

    # 3. Missing values handle karein
    df = df.dropna()

    # 4. Features (X) aur Target (y) alag karein
    # 'Price' hamara target variable hai
    X = df.drop('Price', axis=1)
    y = df['Price']

    # 5. Train-Test Split (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 6. Scaling (Zaroori hai kyunki units different hain)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # 7. Processed data ko save karein (CSV format mein)
    os.makedirs(output_dir, exist_ok=True)
    
    pd.DataFrame(X_train_scaled, columns=X.columns).to_csv(f"{output_dir}/X_train.csv", index=False)
    pd.DataFrame(X_test_scaled, columns=X.columns).to_csv(f"{output_dir}/X_test.csv", index=False)
    y_train.to_csv(f"{output_dir}/y_train.csv", index=False)
    y_test.to_csv(f"{output_dir}/y_test.csv", index=False)

    print(f"✅ Data processing mukammal! Files '{output_dir}' mein save ho gayi hain.")

if __name__ == "__main__":
    # Assignment ke mutabiq paths
    INPUT_FILE = "data/USA_Housing.csv" 
    OUTPUT_FOLDER = "data/processed"
    process_housing_data(INPUT_FILE, OUTPUT_FOLDER)