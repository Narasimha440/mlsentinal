"""
Handles communication with the MLSentinal Backend
"""
print(">>> NEW TRANSPORT.PY IS LOADED <<<")
import requests


from .config import (
    BASE_URL,
    REQUEST_TIMEOUT,
    DEFAULT_HEADERS
)

class Transport:
    """
    Handles HTTP communication with the MLSentinal API.
    """

    def __init__(self, api_key: str):
        self.api_key = api_key

    def send_report(self, report):
        """
        Send a report to the MLSentinal Backend
        """

        headers = DEFAULT_HEADERS.copy()

        headers["X-API-Key"] = self.api_key

        payload = {
            "project": report.project,
            "model": report.model,
            "metrics": report.metrics
        }

        response = requests.post(
            f"{BASE_URL}/api/report",
            headers=headers,
            json=payload,
            timeout=REQUEST_TIMEOUT
        )

        response.raise_for_status()

        return response.json()