1. Aplikacja My Game List korzysta z:
- python
- streamlit
- neo4j

2. Uruchomienie Aplikacji:
- zmienne środowiskowe
  - NEO4J_URI - uri do bazy
  - NEO4J_USER - nazwa użytkownika bazy
  - NEO4J_PASSWORD - hasło do bazy
- requirements
  - streamlit
  - streamlit_option_menu
  - neo4j
  - pandas
  - python-dotenv
- Aplikację uruchamia się w konsoli za pomocą komendy: streamlit run app.py

3. Struktura bazy danych:
- obiekty występujące w bazie:
  - User - wszyscy użytkownicy w bazie
      - email - unikalny
      - username - unikalny
      - password
  - Game - wszystkie gry w bazie
    - title - unikalny
    - description
    - developer
    - publisher
    - genre
    - price
    - platforms
    - release date
- relacje w bazie:
  - FOLLOWED - jeden user może obserwować drugiego
  - RATED - user może ocenić jedną z gier występujących w bazie za pomocą atrybutu rating
- zapytania do bazy:
  - Możliwość odczytu wszystkich danych z bazy
  - każdą grę i każdego użytkownika można dodać/edytować/usunąć
  - można dodać/usunąć relację FOLLOWED
  - można dodać/edytować/usunąć relację RATED
  - zapytanie zwracające rekomendacje na podstawie:
    - wysokich not wystawianych przez min. 3 obserwowanych użytkowników
    - użytkowników mających podobne rekomendacje do naszych

4. Architektura aplikacji:
- aplikacja składa się z modułu frontend. Korzysta ona z biblioteki streamlit
- moduł database łączy się z bazą neo4j za pomocą neo4j.driver oraz przechowuje zapytania do bazy
- moduł config pobiera wszystkie zmienne środowiskowe
- moduł services korzysta z neo4j.driver i wykonuje zapytania do bazy danych
- app.py służy do uruchomienia aplikacji, a także wyświetla sidebar oraz obsługuje przełączanie się pomiędzy stronami aplikacji

5. Przykładowe dane znajdują się w:
- database/data