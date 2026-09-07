"""Editable metadata defaults shared by the settings panel and first boot."""

from copy import deepcopy


DEFAULT_QUESTION_TYPES = [
    {"value": "single_choice", "label": "单选题"},
    {"value": "multi_choice", "label": "多选题"},
    {"value": "fill_in_blank", "label": "填空题"},
    {"value": "detailed_answer", "label": "解答题"},
]

DEFAULT_DIFFICULTIES = [
    {
        "value": "easy_error",
        "label": "易错题",
        "color": "text-green-600 bg-green-50 border-green-200",
    },
    {
        "value": "normal",
        "label": "常规题",
        "color": "text-blue-600 bg-blue-50 border-blue-200",
    },
    {
        "value": "challenge",
        "label": "挑战题",
        "color": "text-red-600 bg-red-50 border-red-200",
    },
    {
        "value": "qiangji",
        "label": "强基题",
        "color": "text-purple-600 bg-purple-50 border-purple-200",
    },
]

METADATA_FIELDS = ("question_types", "difficulties")


def normalize_metadata(payload: dict) -> dict:
    """Keep only the editable metadata dimensions this build understands."""

    return {
        "question_types": deepcopy(payload.get("question_types") or []),
        "difficulties": deepcopy(payload.get("difficulties") or []),
    }


def build_default_metadata() -> dict:
    """Build the editable metadata payload used by settings and first boot."""

    return normalize_metadata(
        {
            "question_types": DEFAULT_QUESTION_TYPES,
            "difficulties": DEFAULT_DIFFICULTIES,
        }
    )
