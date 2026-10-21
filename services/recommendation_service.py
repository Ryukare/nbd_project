from database.neo4j_driver import driver
from database.queries.recommendation_queries import get_highly_recommended_games_query, \
    get_games_recommended_by_similar_users_query

def get_highly_recommended_games(user):
    with driver.session() as session:
        result = session.run(get_highly_recommended_games_query(), username=user)
        return [record.data() for record in result]

def get_games_recommended_by_similar_users(user):
    with driver.session() as session:
        result = session.run(get_games_recommended_by_similar_users_query(), username=user)
        return [record.data() for record in result]