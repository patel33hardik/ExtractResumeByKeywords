import unittest
import resumeExtractor


class TestResumeExtractor(unittest.TestCase):
    text = "This is the test case for python script, js, flask"

    def test_find_resume_with_no_match(self):
        keywords = ["html, css"]
        expected_output = []
        result = resumeExtractor.search_keywords(self.text, keywords)
        self.assertEqual(result, expected_output)

    def test_search_keywords(self):
        keywords = ['python', 'js', 'flask']
        result = resumeExtractor.search_keywords(self.text, keywords)
        self.assertEqual(result, keywords)

if __name__ == '__main__':
    unittest.main()
