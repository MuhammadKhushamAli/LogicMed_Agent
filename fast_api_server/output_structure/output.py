from dataclasses import dataclass


@dataclass
class Output:
    status: int
    response: str
    prev_history_id: str | None = None