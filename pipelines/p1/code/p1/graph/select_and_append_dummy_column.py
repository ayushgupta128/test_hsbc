from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from p1.config.ConfigStore import *
from p1.functions import *

def select_and_append_dummy_column(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(col("col1"), col("col2"), col("col3"), lit("dummy").alias("col4"))
