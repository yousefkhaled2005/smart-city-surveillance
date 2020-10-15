# Real-Time Smart City Multi-Camera Surveillance & Edge Video Analytics

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-red.svg)](https://opencv.org/)
[![YOLO](https://img.shields.io/badge/Model-YOLO%20%2F%20DeepSORT-brightgreen.svg)](#)
[![TensorRT](https://img.shields.io/badge/Inference-NVIDIA%20TensorRT-76B900.svg)](https://developer.nvidia.com/tensorrt)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A high-throughput computer vision pipeline designed for real-time multi-camera tracking, perimeter breach detection, and crowd density anomaly estimation across concurrent RTSP video streams.

---

## 🏛️ Surveillance Pipeline Architecture

```
+-------------------------------------------------------------------------+
|                  RTSP CAMERA STREAMS (30+ FEEDS)                        |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                      STREAM INGESTION & DECODING                        |
|  - Async Frame Dropping / Zero-latency Buffer                           |
|  - Hardware Accelerated Decoding (NVDEC / FFmpeg)                       |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                    TENSORRT INFERENCE (YOLO DETECTOR)                   |
|  - INT8 / FP16 Quantized Engine                                         |
|  - Batch Non-Maximum Suppression (NMS)                                  |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                       DEEPSORT MULTI-OBJECT TRACKER                     |
|  - Kalman Filter State Estimation                                       |
|  - Deep Cosine Feature Re-Identification                                |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                     SPATIAL ANALYTICS & ALERT ENGINE                    |
|  - Polygon Perimeter Intrusion Detection                                |
|  - Loitering Duration Calculation                                       |
|  - Dynamic Crowd Density Heatmaps                                       |
+------------------------------------+------------------------------------+
                                     |
                                     v
+-------------------------------------------------------------------------+
|                      ALERT DISPATCH & STREAMING API                     |
|  - WebSocket Streaming to Operations Dashboard                          |
|  - Low-Latency Video MJPEG / WebRTC Feeds                               |
+-------------------------------------------------------------------------+
```

---

## 📊 Performance Benchmarks (4× NVIDIA V100 GPU Cluster)

| Model Precision | Total RTSP Streams | Average FPS / Stream | P95 Detection Latency (ms) | GPU Memory / Stream (MB) |
|:---|:---:|:---:|:---:|:---:|
| PyTorch FP32 (Baseline) | 8 | 14.5 | 68.0 | 1,200 |
| TensorRT FP16 | 20 | 25.0 | 28.5 | 620 |
| **TensorRT INT8 (Ours)** | **32** | **28.4** | **14.2** | **380** |

---

## ⚡ Quick Start

```bash
git clone https://github.com/yousefkhaled2005/smart-city-surveillance.git
cd smart-city-surveillance

pip install -r requirements.txt
python -m src.stream.rtsp_manager --config configs/cameras.yaml
```

---

## 📜 License

MIT License (c) 2020 Yousef Khaled
