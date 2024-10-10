import argparse
import json

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.window import FixedWindows

parser = argparse.ArgumentParser()
args, beam_args = parser.parse_known_args()
pipeline_options = PipelineOptions(beam_args)

class AverageGPA(beam.DoFn):
    def process(self, element):
        student_id, agg_data = element
        name = agg_data.get("source1").get("name")
        gpa = agg_data.get("source2").get("gpa")
        info = {"data": {"name": name, "gpa": gpa}}
        return [info]

def main():
    with beam.Pipeline(options=pipeline_options) as p:
        source1 = (p
                   | "Read from PubSub1" >> beam.io.ReadFromPubSub(
                    subscription="projects/sandbox-boxsand/subscriptions/pycon2024-sub")
                   | "Decode message" >> beam.Map(lambda msg: json.loads(msg.decode('utf-8')))
                   | "Prepare key-value pair" >> beam.Map(lambda kv: (kv.get("student_id"), kv.get("name")))
                   | "Window 1" >> beam.WindowInto(FixedWindows(120))
                   )

        source2 = (p
                   | "Read from Pubsub2" >> beam.io.ReadFromPubSub(
                    subscription="projects/sandbox-boxsand/subscriptions/pycon2024-2-sub")
                   | "Decode message 2" >> beam.Map(lambda msg: json.loads(msg.decode('utf-8')))
                   | "Prepare key-value pair 2" >> beam.Map(lambda kv: (kv.get("student_id"), kv.get("gpa")))
                   | "Window 2" >> beam.WindowInto(FixedWindows(120))
                   )

        join = ({"source1": source1, "source2": source2}
                | beam.CoGroupByKey()
                | beam.ParDo(AverageGPA())
                | beam.Map(print)
                )


if __name__ == '__main__':
    main()
