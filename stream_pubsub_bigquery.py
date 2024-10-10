import apache_beam as beam
import argparse
from apache_beam.options.pipeline_options import PipelineOptions

parser = argparse.ArgumentParser()
args, beam_args = parser.parse_known_args()
pipeline_options = PipelineOptions(beam_args)

def main():
    pass


if __name__ == '__main__':
    main()