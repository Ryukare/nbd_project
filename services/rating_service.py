from database.neo4j_driver import driver
from database.queries.rating_queries import get_rated_games_query, check_if_game_is_rated_query, create_rating_query, \
    update_rating_query, delete_rating_query

def get_rated_games(user):
    with driver.session() as session:
        result = session.run(get_rated_games_query(), username=user)
        return [record.data() for record in result]

def check_if_game_is_rated(user, game):
    with driver.session() as session:
        result = session.run(check_if_game_is_rated_query(), username=user, title=game)
        record = result.single()
        if record:
            return record
        else:
            return None

def create_rating(user, game, rating):
    with driver.session() as session:
        session.run(create_rating_query(), username=user, title=game, rating=rating)

def update_rating(user, game, rating):
    with driver.session() as session:
        session.run(update_rating_query(), username=user, title=game, rating=rating)

def delete_rating(user, game):
    with driver.session() as session:
        session.run(delete_rating_query(), username=user, title=game)