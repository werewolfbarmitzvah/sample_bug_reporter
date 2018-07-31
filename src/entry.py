import argparse

from src.jira_client import create_jira_issue


def is_jira(destination):
    """
    Check if the report is needed to be sent to jira
    More work could be done to support testrail, slack, confluence, etc.
    """
    if destination == 'jira':
        create_jira_issue(args.project, args.file)


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--destination',
                    action='store',
                    help="Where to create issue, e.g. jira, testrail, etc")
parser.add_argument('-f', '--file',
                    action='store',
                    help='Path to xml file for failing tests')
parser.add_argument('-p', '--project',
                    action='store',
                    help='Project type, e.g. Android, back-end, etc.')
args = parser.parse_args()
is_jira(args.destination)
