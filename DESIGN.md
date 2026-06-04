# Store Intelligence System – Design Document

## 1. Problem Overview

The objective of this project is to transform raw CCTV footage from a retail store into actionable business intelligence. Instead of treating the problem purely as a computer vision task, the solution focuses on building an end-to-end system that converts customer movement into structured events, metrics, analytics, and operational insights.

The system processes CCTV footage, detects customers, tracks their movement, generates events, calculates business metrics, and exposes the results through APIs and an analytics dashboard.

---

## 2. Design Goals

The primary goals of the solution were:

* Build a working end-to-end pipeline rather than focusing solely on model accuracy.
* Generate structured events from CCTV footage.
* Create business-relevant metrics such as footfall, dwell time, funnel progression, and zone visits.
* Expose analytics through APIs.
* Provide a dashboard for visualization.
* Keep the solution simple, maintainable, and production-friendly.

---

## 3. System Architecture

```text
CCTV Video
    │
    ▼
YOLOv8 Person Detection
    │
    ▼
Tracking Layer
    │
    ▼
Event Generator
    │
    ▼
Event Store (JSONL)
    │
    ├── Metrics Engine
    ├── Anomaly Detection
    ├── Funnel Analytics
    └── Zone Analytics
            │
            ▼
FastAPI Backend
            │
            ▼
Streamlit Dashboard
```

---

## 4. Detection Pipeline

The system uses YOLOv8 to detect people from CCTV footage.

Only person detections are considered because customer movement is the primary business signal required for store intelligence.

To improve processing speed, inference is performed on every fifth frame rather than every frame. This significantly reduces computational cost while preserving enough information for customer movement analysis.

---

## 5. Event Generation

The system converts detections into structured events.

Example events include:

* entry
* exit
* zone_entered

Each event contains:

* customer identifier
* camera identifier
* timestamp
* event type

This event-driven architecture separates video processing from analytics and allows business metrics to be calculated independently from the detection layer.

---

## 6. Zone Analytics

The store layout was used to define logical retail zones.

Examples include product display areas and customer interaction sections.

When a tracked customer enters a zone, a zone event is generated.

This enables:

* zone popularity analysis
* customer movement tracking
* shelf engagement measurement

---

## 7. Metrics Engine

The metrics layer consumes generated events and computes:

### Operational Metrics

* Footfall
* Average Dwell Time
* Zone Visits

### Funnel Metrics

* Entered Store
* Visited Product Zones
* Exited Store

### Business Metrics

* Revenue
* Orders
* Conversion-related insights

Transaction data provided in the POS dataset is used to enrich store-level business analytics.

---

## 8. API Layer

FastAPI was selected as the backend framework.

Endpoints include:

* /metrics
* /funnel
* /anomalies
* /zones

The API layer acts as the single source of truth for dashboard consumption and external integrations.

---

## 9. Dashboard

A Streamlit dashboard was implemented to visualize:

* Footfall
* Dwell Time
* Funnel Analytics
* Anomalies
* Zone Insights

The dashboard provides a simple interface for understanding store activity without directly inspecting raw events.

---

## 10. Anomaly Detection

The system includes a lightweight anomaly detection module.

Current anomalies include:

* Crowd spikes
* Unusual traffic patterns

The objective is not advanced anomaly modeling but practical operational monitoring.

---

## 11. Future Improvements

Possible future enhancements include:

* Multi-camera customer re-identification
* Staff/customer separation
* Queue detection
* Heatmap generation
* Real-time event streaming using Kafka
* Database-backed event storage
* Advanced conversion analytics

---

## 12. Conclusion

This project focuses on transforming CCTV footage into business intelligence through a practical engineering approach. The design prioritizes modularity, maintainability, explainability, and real-world usability while remaining computationally efficient and easy to deploy.
