import argparse
import json

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.window import FixedWindows

parser = argparse.ArgumentParser()
args, beam_args = parser.parse_known_args()
pipeline_options = PipelineOptions(beam_args)


def main():
    with beam.Pipeline(options=pipeline_options) as p:
        steps = (p
                 | beam.io.ReadFromPubSub(subscription="projects/sandbox-boxsand/subscriptions/pycon2024-sub")
                 | "Decode message" >> beam.Map(lambda msg: json.loads(msg.decode('utf-8')))
                 | "Prepare key-value pairs" >> beam.Map(lambda s: (s.get("product"), s.get("price")))
                 | "2 Minutes window" >> beam.WindowInto(FixedWindows(120))
                 | "Sum all prices" >> beam.CombinePerKey(sum)
                 | "Show the output" >> beam.Map(print)
                 )


if __name__ == '__main__':
    main()
