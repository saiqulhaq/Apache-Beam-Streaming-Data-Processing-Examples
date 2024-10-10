batch-enabled-local:
	python stream_batch_pipeline.py \
	--runner=DirectRunner \
	--project=sandbox-boxsand \
	--job_name=dual-stream-batch \
	--region=asia-southeast2 \
	--temp_location="gs://sandbox-boxsand_pycon2024/beam-temp" \
	--allow_unsafe_triggers \
	--autoscaling_algorithm="THROUGHPUT_BASED"

stream-enabled-local:
	python stream_batch_pipeline.py \
	--runner=DirectRunner \
	--project=sandbox-boxsand \
	--job_name=dual-stream-batch \
	--region=asia-southeast2 \
	--temp_location="gs://sandbox-boxsand_pycon2024/beam-temp" \
	--allow_unsafe_triggers \
	--autoscaling_algorithm="THROUGHPUT_BASED" \
	--experiments=use_runner_v2 \
	--streaming


stream-simple-local:
	python simple_stream.py \
	--runner=DirectRunner \
	--project=sandbox-boxsand \
	--job_name=simple-stream \
	--region=asia-southeast2 \
	--temp_location="gs://sandbox-boxsand_pycon2024/beam-temp" \
	--allow_unsafe_triggers \
	--autoscaling_algorithm="THROUGHPUT_BASED" \
	--experiments=use_runner_v2 \
	--streaming

stream-windowing-local:
	python stream_windowing.py \
	--runner=DirectRunner \
	--project=sandbox-boxsand \
	--job_name=stream-windowing \
	--region=asia-southeast2 \
	--temp_location="gs://sandbox-boxsand_pycon2024/beam-temp" \
	--allow_unsafe_triggers \
	--autoscaling_algorithm="THROUGHPUT_BASED" \
	--experiments=use_runner_v2 \
	--streaming

stream-pubsub-join-local:
	python stream_pubsub_join.py \
	--runner=DirectRunner \
	--project=sandbox-boxsand \
	--job_name=stream-pubsub-join \
	--region=asia-southeast2 \
	--temp_location="gs://sandbox-boxsand_pycon2024/beam-temp" \
	--allow_unsafe_triggers \
	--autoscaling_algorithm="THROUGHPUT_BASED" \
	--experiments=use_runner_v2 \
	--streaming

chatbot-beam-local:
	python chatbot_beam.py \
	--runner=DirectRunner \
	--project=sandbox-boxsand \
	--job_name=chatbot-beam \
	--region=asia-southeast2 \
	--temp_location="gs://sandbox-boxsand_pycon2024/beam-temp" \
	--streaming

branching-beam-dataflow:
	python branching.py \
	--runner=DataflowRunner \
	--project=sandbox-boxsand \
	--job_name=branching \
	--region=asia-southeast2 \
	--temp_location="gs://sandbox-boxsand_pycon2024/beam-temp" \
	--machine_type="e2-small"