import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import argparse

parser = argparse.ArgumentParser()
args, beam_args = parser.parse_known_args()
pipeline_options = PipelineOptions(beam_args)

def main():
    with beam.Pipeline(options=pipeline_options) as p:
        steps = (p
                 | beam.io.ReadFromPubSub(subscription="projects/sandbox-boxsand/subscriptions/pycon2024-sub")
                 | beam.Map(print)
                 )


if __name__ == '__main__':
    main()