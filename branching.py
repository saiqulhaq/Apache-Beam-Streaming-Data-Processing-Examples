import argparse

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

parser = argparse.ArgumentParser()
args, beam_args = parser.parse_known_args()
options = PipelineOptions(beam_args)


def main():
    # Sample pipeline with branching
    with beam.Pipeline(options=options) as p:
        data = p | 'Create Data' >> beam.Create([10, 20, 30, 40, 50, 60])

        # Branch 1: Filter for values less than 30
        less_than_30 = data | 'Filter < 30' >> beam.Filter(lambda x: x < 30)

        # Branch 2: Filter for values greater than or equal to 30
        greater_or_equal_30 = data | 'Filter >= 30' >> beam.Filter(lambda x: x >= 30)

        # Output results
        less_than_30 | 'Output Less Than 30' >> beam.Map(print)
        greater_or_equal_30 | 'Output Greater or Equal 30' >> beam.Map(print)


if __name__ == '__main__':
    main()
