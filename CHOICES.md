# CHOICES.md

## Engineering Decisions and Trade-offs

### Objective

The goal of this project was not to build the most complex computer vision system possible, but to build a practical and working Store Intelligence System that can process CCTV footage, generate business-relevant events, expose analytics through APIs, and provide actionable insights through a dashboard.

Throughout the project, I focused on making engineering decisions that balanced implementation complexity, system reliability, performance, and explainability.

---

## Why I Chose YOLOv8

For person detection, I selected YOLOv8 because it provides a strong balance between speed and accuracy while requiring minimal setup.

Alternative approaches such as Faster R-CNN could potentially provide higher accuracy but would significantly increase inference time and system complexity.

Since the challenge focuses on building an end-to-end system rather than achieving state-of-the-art detection performance, YOLOv8 was the most practical choice.

Benefits:

* Fast inference
* Easy integration
* Reliable person detection
* Production-friendly deployment

---

## Why I Process Every 5th Frame

During testing, I observed that running inference on every frame was computationally expensive and unnecessary for the business metrics being calculated.

The primary objective is footfall estimation, dwell time calculation, and zone analytics rather than frame-level precision.

To improve performance, I processed every 5th frame.

Trade-off:

* Slight reduction in temporal granularity
* Significant improvement in processing speed

This decision allows the system to scale better while still preserving the quality of business metrics.

---

## Why I Started With a Simple Tracking Approach

Initially, I implemented a simple tracking mechanism to validate the complete pipeline from video processing to event generation.

My objective was to ensure that all downstream components such as APIs, metrics, and dashboards were functional before optimizing the tracking layer.

This iterative approach allowed faster development and easier debugging.

After validating the pipeline, I moved toward persistent tracking using YOLO tracking capabilities.

---

## Why I Used Event-Driven Processing

Instead of directly generating metrics from raw video frames, I converted detections into structured events.

Example events:

* entry
* exit
* zone_entered

This design separates computer vision logic from business logic.

Advantages:

* Easier debugging
* Easier analytics generation
* Better scalability
* Cleaner architecture

The same event stream can later support additional features without changing the detection pipeline.

---

## Why JSONL Was Chosen for Event Storage

The challenge resources included sample events in JSONL format.

I adopted the same structure to maintain consistency with the provided examples and simplify event processing.

Advantages:

* Human readable
* Easy to append
* Easy to debug
* Compatible with streaming architectures

In a production deployment, this layer could be replaced with Kafka or a database-backed event store.

---

## Why I Built APIs First

The evaluation framework specifically highlights API correctness and business logic.

For this reason, I prioritized:

* /metrics
* /funnel
* /anomalies

before implementing additional features.

This ensured that the system remained testable throughout development and aligned with the evaluation criteria.

---

## Why Zone Analytics Were Added

The CCTV footage and store layout indicated multiple product zones and shelf areas.

Instead of only counting people, I wanted to extract richer business insights.

Zone analytics enable questions such as:

* Which shelf receives the highest traffic?
* Which zones attract longer dwell times?
* How customers move through the store

These metrics are more valuable for retail decision-making than simple footfall counts.

---

## Why FastAPI Was Chosen

FastAPI provides a lightweight and modern framework for serving analytics endpoints.

Advantages:

* Fast development
* Automatic Swagger documentation
* Simple deployment
* Strong Python ecosystem support

This made it ideal for rapidly building and testing business intelligence APIs.

---

## Why Streamlit Was Chosen

The objective of the dashboard is to communicate insights clearly rather than build a highly customized frontend.

Streamlit allowed rapid development of:

* KPI cards
* Funnel metrics
* Anomaly monitoring
* Zone analytics

while keeping the project focused on engineering functionality.

---

## Assumptions

Several assumptions were made during development:

* Each tracked individual represents a unique customer.
* Zone boundaries are manually defined based on camera views.
* Event timestamps are generated during processing.
* CCTV footage quality is sufficient for person detection.
* Business metrics prioritize consistency over perfect accuracy.

These assumptions were chosen to keep the system practical and aligned with the challenge timeline.

---

## Future Improvements

Given additional time, I would extend the system with:

* ByteTrack integration for stronger tracking accuracy
* Multi-camera identity association
* Real-time streaming event pipeline using Kafka
* Heatmap generation
* Queue length estimation
* Customer journey analytics
* Advanced anomaly detection models

These improvements would increase scalability and analytical depth while preserving the current architecture.

---

## Final Reflection

Throughout this project, my focus was to build a working, maintainable, and explainable Store Intelligence System rather than optimize a single component in isolation.

Every major decision was made by balancing implementation effort, system performance, maintainability, and alignment with the business goals of retail analytics.
