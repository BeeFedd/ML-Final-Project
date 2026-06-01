import os
import pandas as pd
from catboost import CatBoostClassifier
from fastapi import HTTPException

MODEL_PATH = os.path.join(os.path.dirname(__file__), '../../model/catboost_model.cbm')

model = CatBoostClassifier()
model.load_model(MODEL_PATH)

mapping = {
    'buying': {'low': 1, 'med': 2, 'high': 3, 'vhigh': 4},
    'maint': {'low': 1, 'med': 2, 'high': 3, 'vhigh': 4},
    'doors': {'2': 2, '3': 3, '4': 4, '5more': 5},
    'persons': {'2': 2, '4': 4, 'more': 5},
    'lug_boot': {'small': 1, 'med': 2, 'big': 3},
    'safety': {'low': 1, 'med': 2, 'high': 3}
}

class_mapping_inv = {0: 'unacc', 1: 'acc', 2: 'good', 3: 'vgood'}

def get_prediction(buying: str, maint: str, doors: str, persons: str, lug_boot: str, safety: str) -> str:
    try:
        data = {
            'buying': [mapping['buying'][buying]],
            'maint': [mapping['maint'][maint]],
            'doors': [mapping['doors'][doors]],
            'persons': [mapping['persons'][persons]],
            'lug_boot': [mapping['lug_boot'][lug_boot]],
            'safety': [mapping['safety'][safety]]
        }
    except KeyError as e:
        raise HTTPException(
            status_code=400, 
            detail=f"Некорректное значение признака: {e.args[0]}. Проверьте допустимые значения."
        )
        
    df = pd.DataFrame(data)
    
    pred = model.predict(df)
    
    try:
        pred_int = int(pred[0][0])
    except Exception:
        try:
            pred_int = int(pred[0])
        except Exception:
            pred_int = int(pred)
            
    return class_mapping_inv.get(pred_int, "unknown")
