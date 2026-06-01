from fastapi import APIRouter, Depends
from app.schemas.predict import PredictionRequest, PredictionResponse
from app.services.inference import get_prediction

router = APIRouter()

@router.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest = Depends()):
    pred_str = get_prediction(
        buying=request.buying.value,
        maint=request.maint.value,
        doors=request.doors.value,
        persons=request.persons.value,
        lug_boot=request.lug_boot.value,
        safety=request.safety.value
    )
    return PredictionResponse(prediction=pred_str)
