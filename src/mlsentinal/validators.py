"""
Validation functions for MLSentinal SDK
"""

from .error_codes import ErrorCodes

from .exceptions import (
    ProjectValidationError,
    ModelValidationError,
    MetricValidationError,
)

SUPPORTED_METRICS = {
    "accuracy",
    "precision",
    "recall",
    "f1_score",
    "roc_auc",
    "val_loss"
}

def validate_project(project: str):

    if not isinstance(project, str):
        raise ProjectValidationError(
            ErrorCodes.PROJECT_NAME_INVALID,
            "Project name must be a string."
        )
    
    if not project.strip():
        raise ProjectValidationError(
            ErrorCodes.PROJECT_NAME_REQUIRED,
            "Project name connot be empty."
        )
    

def validate_model(model: str):

    if not isinstance(model, str):
        raise ModelValidationError(
            ErrorCodes.MODEL_NAME_INVALID,
            "Model name must be a string."
        )
    
    if not model.strip():
        raise ModelValidationError(
            ErrorCodes.MODEL_NAME_REQUIRED,
            "Model name cannot be empty."
        )
    
def validate_metrics(metrics: dict):

    if not isinstance(metrics, dict):
        raise MetricValidationError(
            ErrorCodes.METRICS_MUST_DICT,
            "Metrics should be a dictionary."
        )
    
    if len(metrics) == 0:
        raise MetricValidationError(
            ErrorCodes.METRICS_REQUIRED,
            "Metrics dictionary cannot be empty."
        )
    
    for metric_name, value in metrics.items():

        if metric_name not in SUPPORTED_METRICS:
            raise MetricValidationError (
                ErrorCodes.METRIC_UNSUPPORTED,
                f"Unsupported Metric '{metric_name}'. "
                f"Supported metrics are {', '.join(sorted(SUPPORTED_METRICS))}."
            )

        if not isinstance(value, (int, float)):
            raise MetricValidationError(
                ErrorCodes.METRIC_VALUE_BE_NUMERIC,
                f"{metric_name} must be numeric."
            )
        
        if metric_name != "val_loss":

            if value < 0 or value > 1:
                raise MetricValidationError(
                    ErrorCodes.METRIC_OUT_RANGE,
                    f"{metric_name} must be between 0 and 1."
                )
            
        else:
            
            if value < 0:
                raise MetricValidationError(
                    ErrorCodes.METRIC_OUT_RANGE,
                    "Validation loss cannot be negative."
                )