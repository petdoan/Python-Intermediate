from rm import rm
from unittest import mock
import unittest

class RmTestCase(unittest.TestCase):
    
    @mock.patch('rm.os.path')
    @mock.patch('rm.os')
    def test_rm(self, mock_os, mock_path):
        mock_path.isfile.return_value = False
        
        rm('any path')
        
        self.assertFalse(mock_os.remove.called, ''' 
                Tried to remove when file not present.''')
        # make the file 'exist'
        mock_path.isfile.return_value = True
        
        rm('any path')
        mock_os.remove.assert_called_with('any path')

unittest.main()
