
from rm import rm
import os.path
import tempfile
import unittest

class RmTestCase(unittest.TestCase):

    def setUp(self):
        self.tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")
        with open(self.tmpfilepath, "w") as f:
            f.write("Delete me!")
        print("Just created tempfile: ", self.tmpfilepath)
        
    def test_rm(self):
        # remove the file
        rm(self.tmpfilepath)
        # test that it was actually removed
        self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")

if __name__ == '__main__':
    unittest.main()

