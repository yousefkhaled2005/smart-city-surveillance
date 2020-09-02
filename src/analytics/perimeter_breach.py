from typing import List, Tuple, Dict


class PerimeterBreachDetector:
    """Ray-casting algorithm to detect object intrusions into restricted polygon zones."""

    @staticmethod
    def point_in_polygon(point: Tuple[float, float], polygon: List[Tuple[float, float]]) -> bool:
        x, y = point
        inside = False
        n = len(polygon)
        p1x, p1y = polygon[0]
        for i in range(n + 1):
            p2x, p2y = polygon[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y
        return inside

    def check_breaches(self, tracks: List[Dict], zone_polygon: List[Tuple[float, float]]) -> List[Dict]:
        breaches = []
        for track in tracks:
            # track coordinates: [x_center, y_center]
            pos = (track["x"], track["y"])
            if self.point_in_polygon(pos, zone_polygon):
                breaches.append({
                    "track_id": track["track_id"],
                    "class": track.get("class", "person"),
                    "position": pos,
                    "alert": "PERIMETER_BREACH_DETECTED"
                })
        return breaches
