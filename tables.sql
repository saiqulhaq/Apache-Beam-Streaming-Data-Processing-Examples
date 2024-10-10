CREATE
OR REPLACE TABLE `sandbox-boxsand.pycon2024.students`
PARTITION BY RANGE_BUCKET(student_id, GENERATE_ARRAY(0, 100, 10))
AS
SELECT d.*
FROM UNNEST([
  STRUCT(1 AS student_id, "Bimantara Hanumpraja" AS name, "Engineering Physics" AS major, "Engineering" AS faculty),
             STRUCT(2, "Ivan Ega Pratama", "Engineering Physics", "Engineering"),
             STRUCT(3, "Firli Ilhami", "Mathematics", "Applied Science"),
             STRUCT(4, "Illona Acyntiajovita", "Psychology", "Psychology")
                 ]) AS d;

CREATE
OR REPLACE TABLE `sandbox-boxsand.pycon2024.gpa`
PARTITION BY RANGE_BUCKET(student_id, GENERATE_ARRAY(0, 100, 10))
AS
SELECT d.*
FROM UNNEST([
  STRUCT(1 AS student_id, 120 AS credits, 3.34 AS gpa), STRUCT(2, 144, 3.78),
                                                        STRUCT(3, 144, 3.80),
                                                        STRUCT(4, 140, 3.98)
                                                                        ]) AS d;