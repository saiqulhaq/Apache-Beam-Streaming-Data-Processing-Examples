# PyCon 2024 - Apache Beam Streaming Data Processing Examples

This repository contains streaming data processing examples using Apache Beam and Google Cloud Platform, presented at PyCon 2024. The examples demonstrate various streaming patterns including windowing, joins, branching, and real-time chat applications.

## Architecture Overview

The project showcases different Apache Beam patterns:
- **Simple Streaming**: Basic Pub/Sub message consumption
- **Windowed Aggregations**: Time-based data grouping and calculations  
- **Stream Joins**: Combining data from multiple sources
- **Branching Pipelines**: Conditional data routing
- **Interactive Chatbot**: Streamlit frontend with Pub/Sub backend

## Prerequisites

- Python 3.7+
- Google Cloud SDK
- Google Cloud Project with the following APIs enabled:
  - Cloud Pub/Sub API
  - Cloud Dataflow API
  - BigQuery API (for some examples)
- Apache Beam
- Streamlit (for chatbot examples)

## Setup

1. Install dependencies:
```bash
pip install apache-beam[gcp] streamlit google-cloud-pubsub
```

2. Set up Google Cloud authentication:
```bash
gcloud auth application-default login
```

3. Update the project ID in the scripts to match your GCP project.

## Examples

### 📁 Core Files

| File | Description |
|------|-------------|
| `simple_stream.py` | Basic streaming pipeline reading from Pub/Sub |
| `stream_windowing.py` | Demonstrates fixed windowing with aggregations |
| `stream_pubsub_join.py` | Shows stream-to-stream joins |
| `stream_pubsub_join_pardo.py` | Join implementation using ParDo |
| `stream_batch_pipeline.py` | Unified batch/streaming pipeline |
| `stream_watermark.py` | Watermark handling for late data |
| `branching.py` | Conditional pipeline branching |
| `chatbot.py` | Streamlit chatbot frontend |
| `chatbot_beam.py` | Beam backend for chatbot processing |

### 🗃️ Data Files

| File | Description |
|------|-------------|
| `students_data.csv` | Sample student data |
| `tables.sql` | BigQuery table definitions |

## Usage

The project includes a Makefile with predefined commands for different examples:

### Local Development (DirectRunner)

```bash
# Run simple streaming example
make stream-simple-local

# Run windowed aggregation example  
make stream-windowing-local

# Run stream join example
make stream-pubsub-join-local

# Run chatbot backend
make chatbot-beam-local

# Run batch-enabled pipeline
make batch-enabled-local

# Run streaming-enabled pipeline
make stream-enabled-local
```

### Production Deployment (DataflowRunner)

```bash
# Deploy branching pipeline to Dataflow
make branching-beam-dataflow
```

### Interactive Examples

```bash
# Run the chatbot frontend
streamlit run chatbot.py
```

## Pipeline Patterns Demonstrated

1. **Basic Streaming**: Reading from Pub/Sub and processing messages
2. **Windowing**: Grouping data into time windows for aggregation
3. **Joins**: Combining multiple data streams
4. **Branching**: Routing data based on conditions
5. **State Management**: Handling stateful operations
6. **Watermarks**: Managing late-arriving data
7. **Unified Batch/Stream**: Single pipeline for both modes

## Configuration

Key configuration parameters used across examples:
- **Project**: `sandbox-boxsand`
- **Region**: `asia-southeast2` 
- **Temp Location**: `gs://sandbox-boxsand_pycon2024/beam-temp`
- **Pub/Sub Topic**: `chatbot-pycon2024`
- **Subscription**: `projects/sandbox-boxsand/subscriptions/pycon2024-sub`

Update these values in the scripts to match your GCP setup.

## Troubleshooting

- Ensure your GCP project has the necessary APIs enabled
- Verify Pub/Sub topics and subscriptions exist
- Check that the temp GCS bucket exists and is accessible
- For Dataflow jobs, ensure proper IAM permissions are set

## License

This project is for educational purposes as part of PyCon 2024 presentation.
