"""\nSVM Notes Images\n\nLearning goal: Use the image sequence as supplementary notes for SVM concepts.\nRun with: python "SVM_Notes_Images_practice.py"\n"""\n\nfrom pathlib import Path
images = [p for p in Path.cwd().iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg"}]
print("Note images:", len(images))
for image in sorted(images):
    print(image.name)\n