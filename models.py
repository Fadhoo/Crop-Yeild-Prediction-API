from pydantic import BaseModel


class YeildPrediction(BaseModel):
    state: str
    local_gov: str
    crop: str
    area: str

