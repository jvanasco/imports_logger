# stdlib
import unittest

# local
import import_logger


# ==============================================================================


def test_basic():
    """
    as a minimum test, just ensure we can invoke this
    """
    import_logger.setup_logger()
