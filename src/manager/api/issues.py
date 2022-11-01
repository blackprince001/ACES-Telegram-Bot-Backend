from sqlalchemy import select, update
from sqlalchemy.orm import Session
from manager.database.schemas.issues import IssueCreate as IssueSchema
from src.manager.database.models import Issues as issuesModel

# TODO write issuess to database
def create_issues():
    pass


def get_issues(db: Session, issues_id: int) -> issuesModel | None:
    return db.get(issuesModel, issues_id)


# TODO update Issue is_resolved column
def issue_resolved():
    pass


# TODO update existing issue statement
def update_issues_statement():
    pass
