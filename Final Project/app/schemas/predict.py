from pydantic import BaseModel, Field
from enum import Enum

class BuyingEnum(str, Enum):
    vhigh = "vhigh"
    high = "high"
    med = "med"
    low = "low"

class MaintEnum(str, Enum):
    vhigh = "vhigh"
    high = "high"
    med = "med"
    low = "low"

class DoorsEnum(str, Enum):
    two = "2"
    three = "3"
    four = "4"
    five_more = "5more"

class PersonsEnum(str, Enum):
    two = "2"
    four = "4"
    more = "more"

class LugBootEnum(str, Enum):
    small = "small"
    med = "med"
    big = "big"

class SafetyEnum(str, Enum):
    low = "low"
    med = "med"
    high = "high"

class PredictionRequest(BaseModel):
    buying: BuyingEnum = Field(..., description="Покупательская цена")
    maint: MaintEnum = Field(..., description="Цена обслуживания")
    doors: DoorsEnum = Field(..., description="Количество дверей")
    persons: PersonsEnum = Field(..., description="Вместимость")
    lug_boot: LugBootEnum = Field(..., description="Размер багажника")
    safety: SafetyEnum = Field(..., description="Оценка безопасности")

class PredictionResponse(BaseModel):
    prediction: str = Field(..., description="Оценка качества автомобиля: unacc, acc, good, vgood")
