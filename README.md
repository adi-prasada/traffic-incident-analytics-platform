# Traffic Incident Analytics Platform

An analytical engine designed for municipal and highway road safety authorities. Ingests, normalizes, and analyzes multi-agency traffic crash records to identify hazardous road corridors (Blackspots) and temporal accident patterns.

## Features
- **Multi-Source Ingestion**: Harmonizes disparate schemas (Police / Insurance / Transport Ministry).
- **Blackspot Scoring Index**: Computes corridor hazard risk weights based on fatality, severe injury, and property damage indices.
- **Temporal Peaks**: Identifies crash clustering by day-of-week and hourly intervals.

## Usage
```bash
pip install -r requirements.txt
python main.py
pytest tests/
```
