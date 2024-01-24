import unittest
from unittest.mock import patch, MagicMock
from api_client import fetch_joke, save_to_database

class TestJokeApp(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_joke_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {'type': 'general', 'setup': 'Test setup', 'punchline': 'Test punchline'}
        mock_get.return_value = mock_response
        joke_data = fetch_joke()
        self.assertEqual(joke_data, {'type': 'general', 'setup': 'Test setup', 'punchline': 'Test punchline'})

    @patch('psycopg2.connect')
    def test_save_to_database_success(self, mock_connect):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value = mock_connection
        mock_connection.cursor.return_value.__enter__.return_value = mock_cursor

        joke_data = {'type': 'general', 'setup': 'Test setup', 'punchline': 'Test punchline'}
        save_to_database(joke_data)

        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO jokes (type, setup, punchline) VALUES (%s,%s,%s)",
            ('general', 'Test setup', 'Test punchline')
        )
        mock_connection.commit.assert_called_once()
if __name__ == '__main__':
    unittest.main()
