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
    product, total_price = data
    text = f"Product: {product}\nTotal price: {total_price}"
    print(text)


def main():
    with beam.Pipeline(options=pipeline_options) as p:
        steps = (p
                 | beam.io.ReadFromPubSub(subscription="projects/sandbox-boxsand/subscriptions/pycon2024-sub")
                 | "Decode message" >> beam.Map(lambda msg: json.loads(msg.decode('utf-8')))
                 | "Prepare key-value pairs" >> beam.Map(lambda s: (s.get("product"), s.get("price")))
                 | "10 seconds window" >> beam.WindowInto(FixedWindows(10))
                 | "Sum all prices" >> beam.CombinePerKey(sum)
                 | "Show the output" >> beam.Map(show_data)
                 )


if __name__ == '__main__':
    main()
