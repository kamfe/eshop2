def only_objects_decorator(func):
    def only_objects_wrapper(objects, only=(), *args, **kwargs):
        return func(objects, *args, **kwargs).only(*only)
    return only_objects_wrapper


@only_objects_decorator
def all_objects(objects, **kwargs):
    return objects.all()


def filter_objects(objects, **kwargs):
    return objects.filter(**kwargs)


def available_products(product_objects):
    return filter_objects(product_objects, on_sale=True, units_in_stock__gt=0)
