#!/usr/bin/env python3
"""Test Suite
"""
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest.mock import PropertyMock, patch, Mock

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
            "repos_url": "http://abc.com",
            "repos": [
                {"name": "abc_us"},
                {"name": "abc_uk"},
            ]
        }
        mock_get_json.return_value = test_payload.get('repos')
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as url:
            url.return_value = test_payload["repos_url"]
            c = client.GithubOrgClient('abc')
            self.assertEqual(c.public_repos(), ["abc_us", "abc_uk"])
            self.assertEqual(c.public_repos(), ["abc_us", "abc_uk"])
            url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, expected):
        """Test the static method GithubOrgClient.has_license"""
        self.assertEqual(
            client.GithubOrgClient.has_license(repo, license),
            expected
        )


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test suite for public_repos with and without license."""
    @classmethod
    def setUpClass(cls) -> None:
        """Arranges the Suite for testing."""
        default_url = "https://api.github.com/orgs/google"

        def side_effect(url):
            if url == default_url:
                return Mock(**{'json.return_value': cls.org_payload})
            elif url == default_url + "/repos":
                return Mock(**{'json.return_value': cls.repos_payload})

        cls.get_patcher = patch('requests.get', side_effect=side_effect)
        cls.get_patcher.start()

    def test_public_repos(self):
        """Tests the GithubOrgClient.public_repos method."""
        self.assertEqual(
            client.GithubOrgClient("google").public_repos(),
            self.expected_repos
        )

    def test_public_repos_with_license(self):
        """
           Tests the GithubOrgClient.public_repos method with
           a valid license key.
        """
        self.assertEqual(
            client.GithubOrgClient("google")
            .public_repos(license="apache-2.0"),
            self.apache2_repos
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Destroys setUp"""
        cls.get_patcher.stop()
