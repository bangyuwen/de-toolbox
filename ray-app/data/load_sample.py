import ray
import pandas as pd

"""GCS"""
# import gcsfs

# filesystem = gcsfs.GCSFileSystem(project="my-google-project")
# ds = ray.data.read_parquet(
#     "gcs://anonymous@ray-example-data/iris.parquet",
#     filesystem=filesystem
# )

# print(ds.schema())

"""GZIP"""
ds = ray.data.read_csv(
    "s3://anonymous@ray-example-data/iris.csv.gz",
    arrow_open_stream_args={"compression": "gzip"},
)


"""Dict"""
ds = ray.data.from_items(
    [
        {"food": "spam", "price": 9.34},
        {"food": "ham", "price": 5.37},
        {"food": "eggs", "price": 0.94},
    ]
)

print(ds)

"""pandas"""
df = pd.DataFrame({"food": ["spam", "ham", "eggs"], "price": [9.34, 5.37, 0.94]})
ds = ray.data.from_pandas(df)

print(ds)
