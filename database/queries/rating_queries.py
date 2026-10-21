def get_rated_games_query():
    return """
            MATCH (:User {username: $username})-[r:RATED]->(g)
            OPTIONAL MATCH (g)<-[r1:RATED]-(:User) 
            RETURN g.title AS title,
                g.genre AS genre,
                g.description AS description,
                g.releaseDate AS releaseDate,
                g.developer AS developer,
                g.publisher AS publisher,
                g.price AS price,
                g.platforms AS platforms, 
                round(avg(r1.rating), 2) AS rating,
                r.rating AS your_rating;
            """

def check_if_game_is_rated_query():
    return """
            MATCH (:User {username: $username})-[r:RATED]->(:Game {title: $title})
            RETURN r
            """

def create_rating_query():
    return """
            MATCH (u:User {username: $username})
            MATCH (g:Game {title: $title})
            CREATE (u)-[:RATED {rating: $rating}]->(g);
            """

def update_rating_query():
    return """
            MATCH (:User {username: $username})-[r:RATED]-(:Game {title: $title})
            SET r.rating = $rating
            """

def delete_rating_query():
    return """
            MATCH (:User {username: $username})-[r:RATED]-(:Game {title: $title})
            DELETE r
            """