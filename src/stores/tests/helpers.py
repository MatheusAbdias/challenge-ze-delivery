from model_bakery import baker


def sample_store(**kwargs):
    """Create and return a store"""
    return baker.make("stores.Store", **kwargs)
