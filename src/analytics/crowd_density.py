from typing import List, Dict


class CrowdDensityAnalyzer:
    """Calculates spatial density and generates high-occupancy alerts."""

    def __init__(self, threshold_count: int = 30):
        self.threshold = threshold_count

    def analyze(self, detections: List[Dict]) -> Dict:
        person_count = sum(1 for d in detections if d.get("class") == "person")
        is_overcrowded = person_count > self.threshold

        return {
            "total_persons": person_count,
            "threshold": self.threshold,
            "status": "CRITICAL_CROWD_DENSITY" if is_overcrowded else "NORMAL",
            "anomaly": is_overcrowded
        }
