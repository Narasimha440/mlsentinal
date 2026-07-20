import mlsentinal
print(mlsentinal.__file__)

from mlsentinal import MLDoc

doctor = MLDoc("narasimha_9963111874")

response = doctor.doc_report(
    project="Spam detector",
    model="Random forest",
    metrics={
        "accuracy": 0.95,
        "precision": 0.94,
        "recall": 0.93,
        "f1_score": 0.935,
        "val_loss": 0.18
    }
)
print(response)

print("SDK version:", doctor.version())