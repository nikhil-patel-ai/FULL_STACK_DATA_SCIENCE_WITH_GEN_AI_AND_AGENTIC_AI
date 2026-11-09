"""\nKNN Notes Images\n\nLearning goal: Use these images as visual notes while studying KNN distance calculations and classification.\nRun with: python "KNN_Notes_Images_practice.py"\n"""\n\nfrom pathlib import Path
images = [p for p in Path.cwd().iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg"}]
print("Image count:", len(images))
for image in sorted(images):
    print(image.name)\n