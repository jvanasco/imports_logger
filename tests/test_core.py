# stdlib
import unittest

# local
import imports_logger


# ==============================================================================


def test_basic():
    """
    as a minimum test, just ensure we can invoke this
    """
    imports_logger.setup_logger()
