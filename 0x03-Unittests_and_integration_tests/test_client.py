#!/usr/bin/env python3
"""Test Suite
"""
from parameterized import parameterized
from unittest.mock import patch, Mock

import client
import unittest

expected = {'payload': True}


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient class."""
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('utils.requests.get')
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json, mock_get):
        """Test for GithubOrgClient.org property."""
        mock_response = Mock()
        mock_response.json.return_value = expected
        mock_get.return_value = mock_response        
        mock_get_json.return_value = expected
        c = client.GithubOrgClient(org_name)

        self.assertEqual(c.org, expected)
        self.assertEqual(c.org, expected)
        mock_get_json.assert_called_once_with(c.ORG_URL.format(org=c._org_name))

    def test_public_repos_url(self):
        """Test that the GithubOrgClient._public_repos_url property"""
        with patch('client.GithubOrgClient.org') as mock_org:
            mock_org.__getitem__.return_value = expected
            c = client.GithubOrgClient('abc')
            payload = c._public_repos_url
            self.assertEqual(payload, expected)
