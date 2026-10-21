def get_all_games_query():
    return """
            MATCH (g:Game)
            OPTIONAL MATCH (g)<-[r1:RATED]-(:User)
            OPTIONAL MATCH (g)<-[r2:RATED]-(u:User {username: $username})
            RETURN
                g.title AS title,
                g.genre AS genre,
                g.description AS description,
                g.releaseDate AS releaseDate,
                g.developer AS developer,
                g.publisher AS publisher,
                g.price AS price,
                g.platforms AS platforms,
                round(avg(r1.rating), 2) AS rating,
                r2.rating AS your_rating
            """

def create_game_query():
    return """
            CREATE (:Game {
                title: $title,
                genre: $genre,
                developer: $developer,
                publisher: $publisher,
                releaseDate: date($releaseDate),
                price: $price,
                description: $description,
                platforms: $platforms
            })
                """

def update_game_query():
    return """
            MATCH (g:Game {title: $old_title})
            SET
                g.title =
                CASE
                    WHEN g.title <> $title THEN $title
                    ELSE g.title
                END,
                g.genre = $genre,
                g.developer = $developer,
                g.publisher = $publisher,
                g.releaseDate = date($releaseDate),
                g.price = $price,
                g.platforms = $platforms,
                g.description = $description
            """

def delete_game_query():
    return """
            MATCH (g:Game {title: $title})
            DETACH DELETE g
            """