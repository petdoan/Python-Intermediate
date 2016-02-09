import unittest
from mymock import Mock

class RmTestCase(unittest.TestCase):

    def setUp(self):
        self.rm = Mock()
        self.exists = Mock(True)

    def test_rm(self):
        if self.exists('tempfile'):
            self.rm('tempfile')
        self.assertTrue(self.rm.params[0][0] == 'tempfile')

    def test_rm_non_existent_file(self):
        self.exists.retval = False
        if self.exists('tempfile'):
            self.rm('tempfile')
        self.assertTrue(self.rm.called == False)

if __name__ == '__main__':
    unittest.main()

