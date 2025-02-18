# ADPPM/services/ai/app/schema/xray_schema.py

from pydantic import BaseModel

class XrayInput(BaseModel):
    image_path: str  # Assuming base64 image string or path to the image
class XrayOutput(BaseModel):
    diagnosis: str
    confidence: float