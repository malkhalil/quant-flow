"""
Test basic project setup and imports.
"""


def test_quantflow_version():
    """Test that quantflow module can be imported and has a version."""
    import quantflow

    assert hasattr(quantflow, "__version__")
    assert quantflow.__version__ == "0.1.0"


def test_all_modules_importable():
    """Test that all main modules can be imported."""
    from quantflow import data_ingestion
    from quantflow import processing
    from quantflow import storage
    from quantflow import strategy
    from quantflow import api

    # All imports should succeed without errors
    assert data_ingestion is not None
    assert processing is not None
    assert storage is not None
    assert strategy is not None
    assert api is not None


def test_module_docstrings():
    """Test that modules have proper docstrings."""
    from quantflow import data_ingestion, processing, storage, strategy, api

    assert data_ingestion.__doc__ is not None
    assert processing.__doc__ is not None
    assert storage.__doc__ is not None
    assert strategy.__doc__ is not None
    assert api.__doc__ is not None
