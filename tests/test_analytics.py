from src.analytics.perimeter_breach import PerimeterBreachDetector
from src.analytics.crowd_density import CrowdDensityAnalyzer


def test_perimeter_breach():
    detector = PerimeterBreachDetector()
    poly = [(0, 0), (10, 0), (10, 10), (0, 10)]
    tracks = [
        {"track_id": 1, "x": 5, "y": 5, "class": "person"},
        {"track_id": 2, "x": 15, "y": 15, "class": "person"}
    ]
    breaches = detector.check_breaches(tracks, poly)
    assert len(breaches) == 1
    assert breaches[0]["track_id"] == 1


def test_crowd_density():
    analyzer = CrowdDensityAnalyzer(threshold_count=2)
    detections = [{"class": "person"}, {"class": "person"}, {"class": "person"}]
    res = analyzer.analyze(detections)
    assert res["anomaly"] is True
