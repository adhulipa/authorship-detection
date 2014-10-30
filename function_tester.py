import find_author
import unittest
import os.path

class TestFindAuthorFunctions(unittest.TestCase):
    
    def setUp(self):
        self.prompt = 'Enter filename: '
    
    def test_average_word_length(self):
        return

    def test_read_directory_name(self):
        # TODO:
        ## Need to learn how totest input/output calls
        ## within user-defined functions
        return
    
    def test_get_valid_filename(self):
        # TODO: make sure empty filename argument requests for new filename
        # TODO: make sure valid filename returns the "filename"
        # TODO: make sure invalid filename prompts that file does not exit and requests new filename
        return

if __name__ == "__main__":
    unittest.main()
