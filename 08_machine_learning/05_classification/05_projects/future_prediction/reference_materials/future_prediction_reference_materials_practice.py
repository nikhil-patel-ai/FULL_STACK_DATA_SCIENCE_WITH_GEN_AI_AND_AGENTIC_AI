"""\nFuture Prediction Reference Materials\n\nLearning goal: Review project-specific supporting documents and images.\nRun with: python "Future_Prediction_Reference_Materials_practice.py"\n"""\n\nfrom pathlib import Path
for path in sorted(Path.cwd().iterdir()):
    print(path.name)\n