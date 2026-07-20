![LOGO](https://raw.githubusercontent.com/Narasimha440/mlsentinal/refs/heads/main/logo.png)

# MLSentinel

[![PyPI version](https://img.shields.io/pypi/v/mlsentinel.svg)](https://pypi.org/project/mlsentinel/)
[![Python](https://img.shields.io/pypi/pyversions/mlsentinel.svg)](https://pypi.org/project/mlsentinel/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

MLSentinel is a Python SDK that enables Machine Learning developers to validate and submit model evaluation reports to the MLSentinel platform. The SDK performs local validation before securely sending reports to the backend using API key authentication.

> 🚧 **Developer Preview**
>
> MLSentinel is currently under active development. This release provides the SDK foundation, including input validation, backend communication, API key authentication, and custom exceptions. AI-powered model analysis and dashboard features will be introduced in future releases.

---

# 🎉 What's New in v0.1.3.dev2

- ✅ Added HTTP transport layer
- ✅ Connected SDK with MLSentinel backend
- ✅ Added API Key authentication (`X-API-Key`)
- ✅ Added request timeout handling
- ✅ Added custom SDK exceptions
- ✅ Improved input validation
- ✅ Improved SDK architecture
- ✅ Various bug fixes and code improvements

---

# Features

- 🚀 Simple `MLDoc` client
- 📊 Submit machine learning model reports
- ✅ Automatic validation of projects, models, and metrics
- 🔐 Secure API Key authentication
- 🌐 HTTP transport layer
- ⚡ Lightweight with minimal dependencies
- 🛡️ Custom SDK exceptions
- 📦 Typed report models
- 🔄 SDK version tracking

---

# Installation

```bash
pip install mlsentinal
```

---

# Quick Start

```python
from mlsentinal import MLDoc

client = MLDoc("YOUR_API_KEY")

response = client.doc_report(
    project="Spam Detector",
    model="Random Forest",
    metrics={
        "accuracy": 0.95,
        "precision": 0.94,
        "recall": 0.93,
        "f1_score": 0.935,
        "val_loss": 0.18
    }
)

print(response)
print("SDK Version:", client.version())
```

---

# Validation Rules

Before submitting a report, MLSentinel validates all inputs locally.

| Field | Validation |
|--------|------------|
| Project Name | Required |
| Model Name | Required |
| Accuracy | Between 0.0 and 1.0 |
| Precision | Between 0.0 and 1.0 |
| Recall | Between 0.0 and 1.0 |
| F1 Score | Between 0.0 and 1.0 |
| Validation Loss | Greater than or equal to 0 |

If validation fails, an exception is raised before any request is sent to the backend.

---

# SDK Architecture

```
Developer
      │
      ▼
  MLDoc Client
      │
      ▼
 Validation Engine
      │
      ▼
  Report Model
      │
      ▼
 HTTP Transport
      │
      ▼
 API Authentication
      │
      ▼
 MLSentinel Backend
```

---

# Project Structure

```
src/
└── mlsentinal/
    ├── __init__.py
    ├── client.py
    ├── config.py
    ├── exceptions.py
    ├── models.py
    ├── transport.py
    ├── validators.py
    └── version.py
```

---

# Requirements

- Python 3.9+
- requests

---

# Roadmap

## ✅ Version 0.1.x (Current)

- SDK Foundation
- MLDoc Client
- Report Models
- Input Validation
- HTTP Transport Layer
- API Key Authentication
- Backend Integration
- Custom SDK Exceptions

---

## 🚧 Version 0.1.3

- Standardized SDK Error Codes
- Cleaner Developer Error Messages
- Enhanced Exception Handling
- Better Response Formatting
- Improved Documentation

---

## 🚧 Version 0.2.0

- AI Analysis Engine
- Model Health Reports
- Performance Recommendations
- Intelligent Diagnostics
- Report Analysis API

---

## 🚀 Future Releases

- Web Dashboard
- Team Workspaces
- Project Management
- Model Monitoring
- Drift Detection
- Report History
- Model Comparison
- REST API Expansion
- CI/CD Integrations

---

# Contributing

Contributions are welcome!

If you'd like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

# Vision

Machine Learning developers often know **what** their evaluation metrics are, but not **why** model performance changed or what should be improved.

MLSentinel aims to bridge that gap by providing intelligent analysis, actionable recommendations, and model health insights, helping developers build more reliable machine learning systems.

The current SDK is the foundation for that vision, focusing on secure report submission and validation.

---

# Author

**Adari Narasimha Dhoni**

GitHub: https://github.com/Narasimha440

---

# License

This project is licensed under the MIT License.