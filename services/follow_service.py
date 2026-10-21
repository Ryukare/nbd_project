from database.neo4j_driver import driver
from database.queries.follow_queries import get_not_followed_accounts_query, get_followed_accounts_query, \
    get_followers_accounts_query, create_follow_query, delete_follow_query


def get_not_followed_accounts(user):
    with driver.session() as session:
        result = session.run(get_not_followed_accounts_query(), username=user)
        return [record.data() for record in result]

def get_followed_accounts(user):
    with driver.session() as session:
        result = session.run(get_followed_accounts_query(), username = user)
        return [record.data() for record in result]

def get_followers_accounts(user):
    with driver.session() as session:
        result = session.run(get_followers_accounts_query(), username = user)
        return [record.data() for record in result]

def create_follow(user_1, user_2):
    with driver.session() as session:
        session.run(create_follow_query(), user_1=user_1, user_2=user_2)

def delete_follow(user_1, user_2):
    with driver.session() as session:
        session.run(delete_follow_query(), user_1=user_1, user_2=user_2)