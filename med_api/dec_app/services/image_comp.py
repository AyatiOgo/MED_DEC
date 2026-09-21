import torch
import open_clip
from PIL import Image


# Load the model once when Django starts
model, _, preprocess = open_clip.create_model_and_transforms(
    "ViT-B-32",
    pretrained="laion2b_s34b_b79k"
)

model.eval()


def get_image_embedding(image_path):

    image = Image.open(image_path).convert("RGB")

    image_tensor = preprocess(image).unsqueeze(0)

    with torch.no_grad():
        embedding = model.encode_image(image_tensor)

    # Normalize embedding
    embedding = embedding / embedding.norm(
        dim=-1,
        keepdim=True
    )

    return embedding


def compare_images(
    reference_image_path,
    uploaded_image_path
):

    reference_embedding = get_image_embedding(
        reference_image_path
    )

    uploaded_embedding = get_image_embedding(
        uploaded_image_path
    )

    similarity = torch.nn.functional.cosine_similarity(
        reference_embedding,
        uploaded_embedding
    )

    return similarity.item()