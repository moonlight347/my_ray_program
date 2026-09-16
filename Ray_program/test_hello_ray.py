import ray
ray.init()
@ray.remote
def hello_ray():
    return "hello ray"

print(ray.get(hello_ray.remote()))