from database.neo4j_driver import driver
from neo4j.exceptions import ConstraintError
from database.queries.game_queries import get_all_games_query, create_game_query, update_game_query, delete_game_query

def get_all_games(user):
    with driver.session() as session:
        result = session.run(get_all_games_query(), username=user)
        return [record.data() for record in result]

def create_game(game):
    with driver.session() as session:
        try:
            session.run(create_game_query(), parameters=game)
        except ConstraintError:
            raise ValueError(f"A game with the title '{game['title']}' already exists.")

def update_game(old_title, game):
    with driver.session() as session:
        try:
            session.run(update_game_query(), old_title=old_title, parameters=game)
        except ConstraintError:
            raise ValueError(f"A game with the title '{game['title']}' already exists.")

def delete_game(game):
    with driver.session() as session:
        session.run(delete_game_query(), parameters=game)