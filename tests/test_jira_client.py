from mock import patch

from src import jira_client


@patch.object(jira_client, 'create_jira_issue')
def test_create_jira_issue_called(mock):
    jira_client.create_jira_issue("Android", "./path/to/file.xml")
    mock.assert_called_with("Android", "./path/to/file.xml")


@patch.object(jira_client, 'create_issue_dict')
def test_create_jira_dict_called(mock):
    jira_client.create_issue_dict("Android", "./path/to/file.xml")
    mock.assert_called_with("Android", "./path/to/file.xml")
