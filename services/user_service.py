from database.neo4j_driver import driver
from neo4j.exceptions import ConstraintError

from database.queries.user_queries import get_all_users_query, create_user_query, validate_user_query, \
    update_user_query, delete_user_query


def get_all_users():
    with driver.session() as session:
        result = session.run(get_all_users_query())
        return [record.data() for record in result]

def create_user(email, username, password):
    with driver.session() as session:
        try:
            result = session.run(create_user_query(), email=email, username=username, password=password)
            record = result.single()
            if record:
                return record.data()
            else:
                return None
        except ConstraintError as e:
            raise ValueError(str(e))

def update_user(old_username, email, username, password):
    with driver.session() as session:
        try:
            result = session.run(update_user_query(), old_username=old_username, email=email, username=username,
                        password=password)
            record = result.single()
            if record:
                return record.data()
            else:
                return None
        except ConstraintError as e:
            raise ValueError(str(e))

def delete_user(username):
    with driver.session() as session:
        session.run(delete_user_query(), username=username)

def validate_user(login, password):
    with driver.session() as session:
        result = session.run(validate_user_query(), login=login, password=password)
        record = result.single()
        if record:
            return record.data()
        else:
            return None