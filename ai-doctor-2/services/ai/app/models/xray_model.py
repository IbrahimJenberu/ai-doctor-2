import torch
import torchvision.transforms as transforms
from PIL import Image

# Load the pre-trained DEBNSNet model (Assuming model is saved as 'debnsnet.pth')
MODEL_PATH = "models/debnsnet.pth"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model
model = torch.load(MODEL_PATH, map_location=device)
model.eval()

# Define image transformations
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

def analyze_xray(image_path: str):
    """Analyzes a Chest X-ray image and returns disease prediction scores."""
    try:
        # Load image
        image = Image.open(image_path).convert("RGB")
        image = transform(image).unsqueeze(0).to(device)
        
        # Make prediction
        with torch.no_grad():
            output = model(image)
        
        # Convert to probability scores (assuming softmax output)
        probabilities = torch.nn.functional.softmax(output, dim=1).cpu().numpy().tolist()
        
        return {"probabilities": probabilities}
    except Exception as e:
        return {"error": str(e)}

