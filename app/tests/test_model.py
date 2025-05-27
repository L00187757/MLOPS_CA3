import pytest
import numpy as np
from app.models.train import model, category_map

def test_model_prediction():
    # Test normal weight
    test_bmi = np.array([[22]]).reshape(-1, 1)
    prediction = model.predict(test_bmi)[0]
    assert prediction in category_map.keys()
    assert isinstance(category_map[prediction], str)

    # Test obese
    test_bmi = np.array([[32]]).reshape(-1, 1)
    prediction = model.predict(test_bmi)[0]
    assert prediction >= 4  # Should be obese or extremely obese

def test_category_mapping():
    assert len(category_map) == 6
    assert category_map[0] == "Extremely Underweight"
    assert category_map[2] == "Normal"
