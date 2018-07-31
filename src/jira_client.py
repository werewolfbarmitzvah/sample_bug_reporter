from jira import JIRA

import xmltodict
import json

import logging

log = logging.getLogger(__name__)


def jira_auth():
    """
    This would return your Jira object.
    I would store the credentials in
    an .env file and load them in rather than hardcode.
    """
    return JIRA(basic_auth=('jira_username', 'jira_password'))


def create_jira_issue(project_type, xml_report):
    """
    Creates a jira issue or issues
    """
    report_dict = create_issue_dict(project_type, xml_report)
    return jira_auth().create_issue(fields=report_dict)


def create_issue_dict(project, xml_report):
    """
    Takes in an xml file, turns it into json and then parses for failures
    to send to jira.
    Creating a list of issues and the strucutre for that is based
    solely on this documentation
    https://jira.readthedocs.io/en/master/examples.html#issues
    """
    # Assuming this is just id from jira project
    # project_search = jira_auth().project(project)
    # project_name = project_search.id
    project_name = project
    issues_list = []
    with open(xml_report) as file:
        report = json.loads(json.dumps(xmltodict.parse(file.read())))
        for item in report['testsuite']['testcase']:
            if 'failure' in item:
                issue_dict = {}
                project_dict = {}
                project_dict['id'] = project_name
                issue_type_dict = {}
                issue_type_dict['name'] = 'Bug'
                issue_dict['project'] = project_dict['id']
                issue_dict['summary'] = item['@name']
                issue_dict['description'] = item['failure']
                issue_dict['issuetype'] = issue_type_dict['name']
                issues_list.append(issue_dict)
            continue
    file.close()
    return issues_list
