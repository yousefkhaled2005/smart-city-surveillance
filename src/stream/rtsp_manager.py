"""
RTSP Stream Ingestion Manager with zero-latency buffer management.
"""
from src.analytics.perimeter_breach import PerimeterBreachDetector
from src.analytics.crowd_density import CrowdDensityAnalyzer


def run_pipeline_demo():
    print("================ SMART CITY SURVEILLANCE PIPELINE ================")
    perimeter = PerimeterBreachDetector()
    crowd = CrowdDensityAnalyzer(threshold_count=5)

    restricted_zone = [(100, 100), (400, 100), (400, 400), (100, 400)]
    active_tracks = [
        {"track_id": 101, "class": "person", "x": 250, "y": 250},
        {"track_id": 102, "class": "person", "x": 50, "y": 50},
        {"track_id": 103, "class": "vehicle", "x": 300, "y": 300}
    ]

    breaches = perimeter.check_breaches(active_tracks, restricted_zone)
    crowd_stats = crowd.analyze(active_tracks)

    print(f"[*] Processed {len(active_tracks)} tracks.")
    print(f"[*] Perimeter Breaches Detected: {len(breaches)}")
    for b in breaches:
        print(f"    - Alert: Track #{b['track_id']} ({b['class']}) breached restricted zone at {b['position']}")
    print(f"[*] Crowd Status: {crowd_stats['status']} (Count: {crowd_stats['total_persons']})")
    print("==================================================================")


if __name__ == "__main__":
    run_pipeline_demo()
