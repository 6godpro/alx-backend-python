#!/usr/bin/env python3
"""Test Suite
"""
from parameterized import parameterized
from unittest.mock import patch, Mock

import client
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient class."""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test for GithubOrgClient.org property."""
        expected = {'payload': True}
        mock_get_json.return_value = expected
        c = client.GithubOrgClient(org_name)

        self.assertEqual(c.org, expected)
        self.assertEqual(c.org, expected)
        mock_get_json.assert_called_once_with(
            c.ORG_URL.format(org=c._org_name)
        )

    def test_public_repos_url(self):
        """Test the GithubOrgClient._public_repos_url property"""
        with patch('client.GithubOrgClient.org') as mock_org:
            mock_org.__getitem__.return_value = "http://abc.com"
            c = client.GithubOrgClient('abc')
            payload = c._public_repos_url
            self.assertEqual(payload, "http://abc.com")

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the GithubOrgClient.public_repos method."""
        test_payload = {
            "repos": [
                {"name": "abc_us"},
                {"name": "abc_uk"},
            ]
        }
        mock_get_json.return_value = test_payload.get('repos')
        with patch('client.GithubOrgClient._public_repos_url') as url:
            url.return_value = 'http://abc.com'
            c = client.GithubOrgClient('abc')
            self.assertEqual(c.public_repos(), ["abc_us", "abc_uk"])
