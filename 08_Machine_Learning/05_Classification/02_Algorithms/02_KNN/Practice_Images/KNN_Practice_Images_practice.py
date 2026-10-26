"""\nKNN Practice Images\n\nLearning goal: Review the practice images and solve each exercise before checking the corresponding notes.\nRun with: python "KNN_Practice_Images_practice.py"\n"""\n\nfrom pathlib import Path
images = [p for p in Path.cwd().iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg"}]
print("Practice image count:", len(images))
for image in sorted(images):
    print(image.name)\n