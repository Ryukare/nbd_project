def get_not_followed_accounts_query():
    return """
            MATCH (logged:User {username: $username})
            MATCH (user:User)
            WHERE NOT (logged)-[:FOLLOWED]->(user) AND logged <> user
            RETURN user.username AS username
            """

def get_followed_accounts_query():
    return """
            MATCH (:User {username: $username})-[:FOLLOWED]->(following:User) 
            RETURN following.username AS username;
            """

def get_followers_accounts_query():
    return """
            MATCH (follower:User)-[:FOLLOWED]->(:User {username: $username}) 
            RETURN follower.username AS username;
            """

def create_follow_query():
    return """
            MATCH (u1:User {username: $user_1})
            MATCH (u2:User {username: $user_2})
            CREATE (u1)-[:FOLLOWED]->(u2)
            """

def delete_follow_query():
    return """
            MATCH (u1:User {username: $user_1})-[follow:FOLLOWED]->(u2:User {username: $user_2})
            DELETE follow
            """