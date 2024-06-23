import ray
from typing import Dict
import numpy as np
import os

"""init"""
ray.init()

print(
    """This cluster consists of
    {} nodes in total
    {} CPU resources in total
""".format(len(ray.nodes()), ray.cluster_resources()["CPU"])
)

"""read"""
ds = ray.data.read_csv("s3://anonymous@air-example-data/iris.csv")
print(ds.schema())
ds.show(limit=1)


"""transform"""
def transform_batch(batch: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
    vec_a = batch["petal length (cm)"]
    vec_b = batch["petal width (cm)"]
    batch["petal area (cm^2)"] = vec_a * vec_b
    return batch


transformed_ds = ds.map_batches(transform_batch)
print(transformed_ds.materialize())

print(transformed_ds.take_batch(batch_size=3))

"""write"""

transformed_ds.write_parquet(".data/iris_transformed")

print(os.listdir(".data/iris_transformed"))
