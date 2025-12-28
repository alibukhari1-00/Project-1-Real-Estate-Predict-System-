import os
import pickle
import pandas as pd

def test_data_path():
    """Check if dataset is in the correct place"""
    assert os.path.exists("data/USA_Housing.csv")

def test_training_output():
    """Verify that models directory and file are created"""
    # Note: Ye tabhi pass hoga agar CI mein pehle train.py chal chuka ho
    assert os.path.exists("models/model.pkl")

def test_model_logic():
    """Check if model can actually predict"""
    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)
    
    # Test prediction with a dummy value
    prediction = model.predict([[2000]])
    assert prediction[0] > 0