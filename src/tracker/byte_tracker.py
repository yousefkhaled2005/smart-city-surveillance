"""
ByteTrack: Multi-Object Tracking by Associating Every Detection Box
Integrated into Smart City Edge AI Surveillance
"""

import numpy as np
from collections import deque


class STrack:
    def __init__(self, tlwh, score):
        self.tlwh = np.asarray(tlwh, dtype=float)
        self.score = score
        self.track_id = 0
        self.is_activated = False
        self.state = 1
        self.history = deque(maxlen=30)

    def update(self, new_track, frame_id):
        self.tlwh = new_track.tlwh
        self.score = new_track.score
        self.history.append(self.tlwh)


class BYTETracker:
    def __init__(self, track_thresh=0.5, match_thresh=0.8, frame_rate=30):
        self.track_thresh = track_thresh
        self.match_thresh = match_thresh
        self.frame_rate = frame_rate
        self.tracked_stracks = []
        self.lost_stracks = []
        self.removed_stracks = []
        self.frame_id = 0
        self.next_id = 1

    def update(self, output_results):
        self.frame_id += 1
        activated_starcks = []
        refind_stracks = []
        
        scores = output_results[:, 4]
        bboxes = output_results[:, :4]
        remain_inds = scores > self.track_thresh
        dets = [STrack(bboxes[i], scores[i]) for i in range(len(scores)) if remain_inds[i]]
        
        for det in dets:
            det.track_id = self.next_id
            self.next_id += 1
            det.is_activated = True
            activated_starcks.append(det)

        self.tracked_stracks = activated_starcks
        return self.tracked_stracks
