def get_highly_recommended_games_query():
    return """
            MATCH (logged:User {username: $username})-[:FOLLOWED]->(f:User)
            MATCH (f)-[r:RATED]->(g:Game)
            WHERE r.rating >= 7 AND NOT (logged)-[:RATED]->(g)

            WITH g, count(r) AS following_count, avg(r.rating) AS avg_rating
            WHERE following_count >= 3

            RETURN g.title AS Game,
                   round(avg_rating, 2) AS rating,
                   following_count 
            ORDER BY rating DESC, following_count DESC;
            """

def get_games_recommended_by_similar_users_query():
    return """
            MATCH (logged:User {username: $username})-[r1:RATED]->(g:Game)
            MATCH (other:User)-[r2:RATED]->(g)
            WHERE r1.rating >= 7 AND r2.rating >= 7 AND logged <> other

            MATCH (other)-[r3:RATED]->(rec:Game)
            WHERE r3.rating >= 7 AND NOT (logged)-[:RATED]->(rec)

            RETURN rec.title AS Game,
                   avg(r3.rating) AS rating,
                   count(DISTINCT other) AS similar_users
            ORDER BY similar_users DESC, rating DESC
            """