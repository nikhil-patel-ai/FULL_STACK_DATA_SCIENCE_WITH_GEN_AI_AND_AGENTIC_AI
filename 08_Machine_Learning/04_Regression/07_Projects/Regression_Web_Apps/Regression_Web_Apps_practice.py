"""\nRegression Web Apps\n\nLearning goal: Review the source code, input validation, model-loading logic, and requirements before launching a regression app.\nRun with: python "Regression_Web_Apps_practice.py"\n"""\n\nfrom pathlib import Path
for name in ["app.py", "app1.py", "flask practise.py", "index.html", "requirements.txt"]:
    path = Path(name)
    print(f"{name}: {'present' if path.exists() else 'not present'}")
print("Check requirements.txt and the model feature order before running the app.")\n