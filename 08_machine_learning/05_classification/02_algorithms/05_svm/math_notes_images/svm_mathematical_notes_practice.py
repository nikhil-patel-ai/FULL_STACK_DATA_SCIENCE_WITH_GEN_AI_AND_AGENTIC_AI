"""\nSVM Mathematical Notes\n\nLearning goal: Review the diagrams as visual support for margins, hyperplanes, and support vectors.\nRun with: python "SVM_Mathematical_Notes_practice.py"\n"""\n\nfrom pathlib import Path
images = [p for p in Path.cwd().iterdir() if p.suffix.lower() in {".png", ".jpg", ".jpeg"}]
print("Math note images:", len(images))
for image in sorted(images):
    print(image.name)\n