# stdlib
import unittest

# local
import imports_logger


# ==============================================================================


class TestHarness(unittest.TestCase):
    def test_basic(self):
        """
        as a minimum test, just ensure we can invoke this
        """
        imports_logger.setup_logger()
