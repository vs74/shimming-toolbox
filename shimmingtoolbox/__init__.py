# https://packaging.python.org/guides/single-sourcing-package-version/
try:
    from importlib import metadata
except ImportError:
    # Running on pre-3.8 Python; use importlib-metadata package
    import importlib_metadata as metadata
__version__ = metadata.version(__name__)
del metadata