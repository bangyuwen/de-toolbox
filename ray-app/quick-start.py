from typing import Dict
import numpy as np
import ray

ds = ray.data.read_csv("s3://anonymous@ray-example-data/iris.csv")

def compute_area(batch: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
    length = batch["petal length (cm)"]
    width = batch["petal width (cm)"]
    batch["petal area (cm^2)"] = length * width
    return batch

transformed_ds = ds.map_batches(compute_area)
for batch in transformed_ds.iter_batches(batch_size=4):
    print(batch)

transformed_ds.write_parquet("local://.ray-app")
