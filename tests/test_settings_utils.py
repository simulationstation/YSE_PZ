import unittest
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from YSE_PZ.settings_utils import normalize_script_name, normalize_url_path, prefix_url_path


class SettingsUtilsTests(unittest.TestCase):
    def test_normalize_script_name(self):
        self.assertEqual(normalize_script_name(""), "")
        self.assertEqual(normalize_script_name("/"), "")
        self.assertEqual(normalize_script_name("YSE_PZ"), "/YSE_PZ")
        self.assertEqual(normalize_script_name("/YSE_PZ/"), "/YSE_PZ")

    def test_normalize_url_path(self):
        self.assertEqual(normalize_url_path("/"), "/")
        self.assertEqual(normalize_url_path("login"), "/login/")
        self.assertEqual(normalize_url_path("/login/"), "/login/")

    def test_prefix_url_path_without_prefix(self):
        self.assertEqual(prefix_url_path("", "/login/"), "/login/")
        self.assertEqual(prefix_url_path("", "/static/"), "/static/")

    def test_prefix_url_path_with_prefix(self):
        self.assertEqual(prefix_url_path("/YSE_PZ", "/login/"), "/YSE_PZ/login/")
        self.assertEqual(prefix_url_path("/YSE_PZ", "/static/"), "/YSE_PZ/static/")
        self.assertEqual(prefix_url_path("/YSE_PZ", "/"), "/YSE_PZ/")

    def test_prefix_url_path_does_not_double_prefix(self):
        self.assertEqual(prefix_url_path("/YSE_PZ", "/YSE_PZ/login/"), "/YSE_PZ/login/")
        self.assertEqual(prefix_url_path("/YSE_PZ", "/YSE_PZ/static/"), "/YSE_PZ/static/")


if __name__ == "__main__":
    unittest.main()
