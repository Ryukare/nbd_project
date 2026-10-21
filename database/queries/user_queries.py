def get_all_users_query():
    return """
            MATCH (user:User)
            RETURN user.username AS username
            """

def create_user_query():
    return """
            CREATE (u:User {
                email: $email,
                username: $username,
                password: $password
            })
            RETURN 
                u.username AS username,
                u.email AS email,
                u.password AS password
            """

def update_user_query():
    return """
            MATCH (u:User {username: $old_username})
            SET
                u.username =
                CASE
                    WHEN u.username <> $username THEN $username
                    ELSE u.username
                END,
                u.email =
                CASE
                    WHEN u.email <> $email THEN $email
                    ELSE u.email
                END,
                u.password = $password
            RETURN
                u.username AS username,
                u.email AS email,
                u.password AS password
    """

def delete_user_query():
    return """
            MATCH (u:User {username: $username})
            DETACH DELETE u
            """

def validate_user_query():
    return """
            MATCH (u:User)
            WHERE (u.username = $login OR u.email = $login)
              AND u.password = $password
            RETURN 
                u.username AS username,
                u.email AS email,
                u.password AS password
            """