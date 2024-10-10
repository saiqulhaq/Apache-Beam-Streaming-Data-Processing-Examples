import argparse

import apache_beam as beam
from apache_beam.io.gcp.internal.clients import bigquery
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions

parser = argparse.ArgumentParser()
args, beam_args = parser.parse_known_args()
options = PipelineOptions(beam_args)
standard_options = options.view_as(StandardOptions)


def main():
    with beam.Pipeline(options=options) as p:
        if standard_options.streaming:
            source = (p
                      | beam.io.ReadFromPubSub(subscription="projects/sandbox-boxsand/subscriptions/pycon2024-sub")
                      )
        else:
            table_spec = bigquery.TableReference(projectId="sandbox-boxsand",
                                                 datasetId="pycon2024",
                                                 tableId="students")
            source = (p | beam.io.ReadFromBigQuery(table=table_spec))

        # Implement ETL logic
        transform = (source | "Show output" >> beam.Map(print))


if __name__ == '__main__':
    main()
