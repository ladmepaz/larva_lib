import torch
import torchvision.transforms as transforms
from PIL import Image


class ModelInference:
    def __init__(self, model_path, device='cpu'):
        self.device = torch.device(device)
        self.model = torch.load(model_path, map_location=self.device)
        self.model.eval()

        self.transform = transforms.Compose([
            transforms.Resize((680, 420)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[
                                 0.229, 0.224, 0.225])
        ])

    def preprocess_image(self, image):
        image = self.transform(image)
        image = image.unsqueeze(0)  # (1, C, H, W)
        return image

    def predict(self, image):
        input_tensor = self.preprocess_image(image)
        input_tensor = input_tensor.to(self.device)
        with torch.no_grad():
            output = self.model(input_tensor)
        return output
