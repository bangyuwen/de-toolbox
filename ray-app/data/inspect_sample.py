import pandas as pd
import ray

"""init"""
ray.init()

print(
    """This cluster consists of
    {} nodes in total
    {} CPU resources in total
""".format(len(ray.nodes()), ray.cluster_resources()["CPU"])
)


"""pandas"""
df = pd.DataFrame({"food": ["spam", "ham", "eggs"], "price": [9.34, 5.37, 0.94]})
ds = ray.data.from_pandas(df)


print(ds.take(2))
print(ds.take_batch(2))
