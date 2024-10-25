import argparse
import json
from typing import Tuple

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.window import FixedWindows

parser = argparse.ArgumentParser()
args, beam_args = parser.parse_known_args()
pipeline_options = PipelineOptions(beam_args)


def show_data(data: Tuple):
    _, result = data
    text = f"Student name: {result.get('source1')[0]}\nStudent GPA: {result.get('source2')[0]}"
    print(text)


def main():
    with beam.Pipeline(options=pipeline_options) as p:
        source1 = (p
                   | "Read from PubSub1" >> beam.io.ReadFromPubSub(
                    subscription="projects/sandbox-boxsand/subscriptions/pycon2024-sub")
                   | "Decode message" >> beam.Map(lambda msg: json.loads(msg.decode('utf-8')))
                   | "Prepare key-value pair" >> beam.Map(lambda kv: (kv.get("student_id"), kv.get("name")))
                   | "Window 1" >> beam.WindowInto(FixedWindows(20))
                   )

        source2 = (p
                   | "Read from Pubsub2" >> beam.io.ReadFromPubSub(
                    subscription="projects/sandbox-boxsand/subscriptions/pycon2024-2-sub")
                   | "Decode message 2" >> beam.Map(lambda msg: json.loads(msg.decode('utf-8')))
                   | "Prepare key-value pair 2" >> beam.Map(lambda kv: (kv.get("student_id"), kv.get("gpa")))
                   | "Window 2" >> beam.WindowInto(FixedWindows(20))
                   )

        join = ({"source1": source1, "source2": source2}
                | beam.CoGroupByKey()
                | beam.Map(show_data)
                )


if __name__ == '__main__':
    main()
