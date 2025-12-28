import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

# Relative path use karein taake Windows aur Linux (GitHub) dono par chale
# Project root se path check karein
data_path = "data/USA_Housing.csv"

def train():
    # Check karein ke file maujood hai
    if not os.path.exists(data_path):
        print(f"Error: {data_path} not found!")
        return

    # Data load
    df = pd.read_csv(data_path)
    
    # Features aur Target (Apne columns ke mutabiq check karein)
    # Agar column names mein space hai toh 'area ' ya 'price ' ho sakta hai
    X = df[['area']] 
    y = df['price']

    # Model training
    model = LinearRegression()
    model.fit(X, y)

    # Models directory banana aur save karna
    os.makedirs('models', exist_ok=True)
    with open('models/model.pkl', 'wb') as f:
        pickle.dump(model, f)

    print("✅ Model trained and saved to models/model.pkl")

if __name__ == "__main__":
    train()