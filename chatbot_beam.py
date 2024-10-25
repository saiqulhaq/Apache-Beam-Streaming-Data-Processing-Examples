import argparse
import json
from typing import Tuple

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.transforms.window import Sessions, FixedWindows

parser = argparse.ArgumentParser()
args, beam_args = parser.parse_known_args()
options = PipelineOptions(beam_args)

def show_output(data: Tuple):
    _, number = data
    print(f"Total number you input: {number}")

def main():
    with beam.Pipeline(options=options) as p:
        source = (p
                  | beam.io.ReadFromPubSub(subscription="projects/sandbox-boxsand/subscriptions/chatbot-pycon2024-sub")
                  | beam.Map(lambda line: json.loads(line))
                  | beam.Map(lambda s: ("number", s.get("number")))
                  | beam.WindowInto(Sessions(10))
                  | beam.CombinePerKey(sum)
                  | beam.Map(show_output)
                  )


if __name__ == '__main__':
    main()
