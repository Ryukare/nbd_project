CREATE
(:User {username: "admin", password: "admin", email: "admin@system.local"}),
(:User {username: "rkowalski", password: "pass123", email: "rkowalski@mail.com"}),
(:User {username: "annak", password: "pass123", email: "annak@mail.com"}),
(:User {username: "janek77", password: "pass123", email: "janek77@mail.com"}),
(:User {username: "kasia.dev", password: "pass123", email: "kasia@mail.com"}),
(:User {username: "michal_g", password: "pass123", email: "michal@mail.com"}),
(:User {username: "ola_play", password: "pass123", email: "ola@mail.com"}),
(:User {username: "piotr89", password: "pass123", email: "piotr@mail.com"}),
(:User {username: "tomek_fps", password: "pass123", email: "tomek@mail.com"}),
(:User {username: "zuza_rpg", password: "pass123", email: "zuza@mail.com"}),
(:User {username: "marek_it", password: "pass123", email: "marek.it@mail.com"}),
(:User {username: "ania_stream", password: "pass123", email: "ania.stream@mail.com"}),
(:User {username: "pawel_k", password: "pass123", email: "pawel.k@mail.com"}),
(:User {username: "lukasz_rpg", password: "pass123", email: "lukasz.rpg@mail.com"}),
(:User {username: "monika_gamer", password: "pass123", email: "monika.gamer@mail.com"});

CREATE
(:Game {title:"The Witcher 3", genre:"RPG", description:"Become Geralt of Rivia, a monster hunter in a vast fantasy world filled with political intrigue, moral choices, and epic adventures.", releaseDate:date("2015-05-19"), developer:"CD Projekt Red", publisher:"CD Projekt", price:40, platforms:["PC","PS4","Xbox One"]}),
(:Game {title:"Cyberpunk 2077", genre:"RPG", description:"Experience a futuristic adventure in Night City, full of corporate intrigue, cybernetic enhancements, and dynamic missions, where every decision has consequences.", releaseDate:date("2020-12-10"), developer:"CD Projekt Red", publisher:"CD Projekt", price:60, platforms:["PC","PS5","Xbox Series X"]}),
(:Game {title:"Elden Ring", genre:"Action RPG", description:"Explore a vast open world created in collaboration with George R. R. Martin, filled with secrets, powerful bosses, and brutal challenges for every soulslike fan.", releaseDate:date("2022-02-25"), developer:"FromSoftware", publisher:"Bandai Namco", price:70, platforms:["PC","PS5","Xbox Series X"]}),
(:Game {title:"Dark Souls III", genre:"Action RPG", description:"Play as the chosen one struggling through a dark world full of undead, treacherous enemies, and challenging bosses. Combat requires patience and strategy.", releaseDate:date("2016-04-12"), developer:"FromSoftware", publisher:"Bandai Namco", price:50, platforms:["PC","PS4","Xbox One"]}),
(:Game {title:"Red Dead Redemption 2", genre:"Action", description:"Live an epic story in the American Wild West as a member of the Van der Linde gang, where loyalty, honor, and survival are tested.", releaseDate:date("2018-10-26"), developer:"Rockstar", publisher:"Rockstar", price:60, platforms:["PC","PS4","Xbox One"]}),
(:Game {title:"GTA V", genre:"Action", description:"Explore the open world of Los Santos, complete criminal missions, or just enjoy a sandbox full of chaos and humor.", releaseDate:date("2013-09-17"), developer:"Rockstar", publisher:"Rockstar", price:30, platforms:["PC","PS4","Xbox One"]}),
(:Game {title:"Hades", genre:"Roguelike", description:"Experience the adventure as Hades' son trying to escape the Underworld, using various weapons and powers in a beautifully designed mythological world.", releaseDate:date("2020-09-17"), developer:"Supergiant", publisher:"Supergiant", price:25, platforms:["PC","Switch","PS5"]}),
(:Game {title:"Hollow Knight", genre:"Metroidvania", description:"Dive into the dark and beautiful world of Hallownest, uncover secrets, fight challenging enemies, and develop your skills in platform exploration.", releaseDate:date("2017-02-24"), developer:"Team Cherry", publisher:"Team Cherry", price:15, platforms:["PC","Switch","PS4"]}),
(:Game {title:"Stardew Valley", genre:"Simulation", description:"Develop your farm, build relationships and romances in a charming village, take care of animals, grow crops, and explore the surrounding secrets.", releaseDate:date("2016-02-26"), developer:"ConcernedApe", publisher:"ConcernedApe", price:15, platforms:["PC","Switch","PS4"]}),
(:Game {title:"Baldur's Gate 3", genre:"RPG", description:"Take the role of a hero in the Forgotten Realms world, shaping their destiny through story decisions, tactical turn-based combat, and interactions in a rich fantasy setting.", releaseDate:date("2023-08-03"), developer:"Larian", publisher:"Larian", price:70, platforms:["PC","PS5"]}),
(:Game {title:"God of War", genre:"Action", description:"Follow Kratos on a journey through Norse mythology, fighting powerful enemies and solving puzzles in a beautifully crafted world.", releaseDate:date("2018-04-20"), developer:"Santa Monica Studio", publisher:"Sony", price:50, platforms:["PC","PS4"]}),
(:Game {title:"God of War Ragnarök", genre:"Action", description:"Continue the adventures of Kratos and Atreus in the world of Norse gods, full of epic battles, emotional storytelling, and breathtaking landscapes.", releaseDate:date("2022-11-09"), developer:"Santa Monica Studio", publisher:"Sony", price:70, platforms:["PS5"]}),
(:Game {title:"The Last of Us Part I", genre:"Action", description:"Discover the story of Joel and Ellie in a post-apocalyptic America, filled with dramatic choices, terrifying enemies, and emotional moments.", releaseDate:date("2022-09-02"), developer:"Naughty Dog", publisher:"Sony", price:70, platforms:["PC","PS5"]}),
(:Game {title:"Minecraft", genre:"Sandbox", description:"Unlimited creativity in a world built from blocks — build, craft, explore, and survive in solo or multiplayer modes.", releaseDate:date("2011-11-18"), developer:"Mojang", publisher:"Microsoft", price:25, platforms:["PC","Console"]}),
(:Game {title:"DOOM Eternal", genre:"FPS", description:"Rush through hellish realms as the Doom Slayer, destroying demons with incredible speed and precision in an intense action FPS.", releaseDate:date("2020-03-20"), developer:"id Software", publisher:"Bethesda", price:40, platforms:["PC","PS4","Xbox One"]}),
(:Game {title:"Valorant", genre:"FPS", description:"A tactical shooter combining precision, hero abilities, and team cooperation, where every round requires strategy and quick decisions.", releaseDate:date("2020-06-02"), developer:"Riot Games", publisher:"Riot Games", price:0, platforms:["PC"]}),
(:Game {title:"League of Legends", genre:"MOBA", description:"Compete in team battles in the world of Runeterra, level up your champions, make tactical decisions, and aim to destroy the enemy base.", releaseDate:date("2009-10-27"), developer:"Riot Games", publisher:"Riot Games", price:0, platforms:["PC"]}),
(:Game {title:"Overwatch 2", genre:"FPS", description:"A team-based shooter featuring heroes with unique abilities, fast matches, and strategic approaches to maps and objectives.", releaseDate:date("2022-10-04"), developer:"Blizzard", publisher:"Blizzard", price:0, platforms:["PC","Console"]}),
(:Game {title:"Assassin's Creed Valhalla", genre:"Action RPG", description:"Live the life of Viking Eivor in 9th century England, conquer territories, fight battles, and shape history in an epic historical saga.", releaseDate:date("2020-11-10"), developer:"Ubisoft", publisher:"Ubisoft", price:60, platforms:["PC","PS5","Xbox Series X"]}),
(:Game {title:"FIFA 23", genre:"Sports", description:"The most realistic football simulation with current teams, leagues, and tournaments, allowing play in solo and online modes.", releaseDate:date("2022-09-30"), developer:"EA", publisher:"EA", price:60, platforms:["PC","PS5","Xbox Series X"]});

MATCH
(u1:User {username:"rkowalski"}),
(u2:User {username:"kasia.dev"}),
(u3:User {username:"michal_g"}),
(u4:User {username:"ola_play"}),
(u5:User {username:"piotr89"}),
(u6:User {username:"tomek_fps"}),
(u7:User {username:"zuza_rpg"}),
(u8:User {username:"marek_it"}),
(u9:User {username:"ania_stream"}),
(u10:User {username:"pawel_k"}),
(u11:User {username:"lukasz_rpg"}),
(u12:User {username:"monika_gamer"}),
(u13:User {username:"janek77"}),
(u14:User {username:"annak"}),
(u15:User {username:"admin"})

CREATE
(u1)-[:FOLLOWED]->(u2),
(u1)-[:FOLLOWED]->(u3),
(u1)-[:FOLLOWED]->(u4),
(u1)-[:FOLLOWED]->(u5),
(u14)-[:FOLLOWED]->(u1),
(u14)-[:FOLLOWED]->(u7),
(u14)-[:FOLLOWED]->(u8),
(u13)-[:FOLLOWED]->(u6),
(u13)-[:FOLLOWED]->(u9),
(u13)-[:FOLLOWED]->(u10),
(u6)-[:FOLLOWED]->(u5),
(u6)-[:FOLLOWED]->(u12),
(u6)-[:FOLLOWED]->(u11),
(u7)-[:FOLLOWED]->(u1),
(u7)-[:FOLLOWED]->(u2),
(u7)-[:FOLLOWED]->(u3),
(u8)-[:FOLLOWED]->(u9),
(u8)-[:FOLLOWED]->(u10),
(u9)-[:FOLLOWED]->(u12),
(u10)-[:FOLLOWED]->(u11),
(u11)-[:FOLLOWED]->(u12),
(u12)-[:FOLLOWED]->(u15),
(u15)-[:FOLLOWED]->(u2),
(u15)-[:FOLLOWED]->(u4),
(u15)-[:FOLLOWED]->(u6),
(u2)-[:FOLLOWED]->(u1),
(u3)-[:FOLLOWED]->(u1),
(u12)-[:FOLLOWED]->(u6),
(u1)-[:FOLLOWED]->(u14),
(u1)-[:FOLLOWED]->(u7),
(u6)-[:FOLLOWED]->(u13);

MATCH (g:Game {title:"The Witcher 3"})
WITH g
UNWIND [
  {user:"rkowalski", rating:9},
  {user:"annak", rating:7},
  {user:"janek77", rating:8},
  {user:"tomek_fps", rating:6},
  {user:"piotr89", rating:10}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"Cyberpunk 2077"})
WITH g
UNWIND [
  {user:"rkowalski", rating:7},
  {user:"michal_g", rating:5},
  {user:"kasia.dev", rating:8},
  {user:"annak", rating:6}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"Elden Ring"})
WITH g
UNWIND [
  {user:"janek77", rating:10},
  {user:"tomek_fps", rating:8},
  {user:"lukasz_rpg", rating:9},
  {user:"monika_gamer", rating:7},
  {user:"rkowalski", rating:9},
  {user:"annak", rating:6}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"Dark Souls III"})
WITH g
UNWIND [
  {user:"janek77", rating:9},
  {user:"lukasz_rpg", rating:6},
  {user:"monika_gamer", rating:7}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"Red Dead Redemption 2"})
WITH g
UNWIND [
  {user:"piotr89", rating:9},
  {user:"annak", rating:6},
  {user:"ola_play", rating:7},
  {user:"tomek_fps", rating:8},
  {user:"rkowalski", rating:10}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"GTA V"})
WITH g
UNWIND [
  {user:"piotr89", rating:7},
  {user:"tomek_fps", rating:8},
  {user:"rkowalski", rating:6},
  {user:"monika_gamer", rating:5}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"Hades"})
WITH g
UNWIND [
  {user:"annak", rating:9},
  {user:"lukasz_rpg", rating:7},
  {user:"zuza_rpg", rating:8}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"Hollow Knight"})
WITH g
UNWIND [
  {user:"monika_gamer", rating:8},
  {user:"piotr89", rating:7},
  {user:"tomek_fps", rating:6},
  {user:"annak", rating:9}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"Stardew Valley"})
WITH g
UNWIND [
  {user:"annak", rating:10},
  {user:"marek_it", rating:7},
  {user:"ania_stream", rating:9},
  {user:"piotr89", rating:6},
  {user:"lukasz_rpg", rating:8},
  {user:"rkowalski", rating:9}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"Baldur's Gate 3"})
WITH g
UNWIND [
  {user:"zuza_rpg", rating:10},
  {user:"lukasz_rpg", rating:7},
  {user:"monika_gamer", rating:6},
  {user:"rkowalski", rating:8},
  {user:"annak", rating:9}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"God of War"})
WITH g
UNWIND [
  {user:"rkowalski", rating:9},
  {user:"tomek_fps", rating:7},
  {user:"piotr89", rating:6}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"God of War Ragnarök"})
WITH g
UNWIND [
  {user:"monika_gamer", rating:10},
  {user:"lukasz_rpg", rating:8},
  {user:"annak", rating:7},
  {user:"rkowalski", rating:9}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"The Last of Us Part I"})
WITH g
UNWIND [
  {user:"tomek_fps", rating:9},
  {user:"rkowalski", rating:6},
  {user:"marek_it", rating:7}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"Minecraft"})
WITH g
UNWIND [
  {user:"ania_stream", rating:9},
  {user:"piotr89", rating:7},
  {user:"kasia.dev", rating:8},
  {user:"tomek_fps", rating:10},
  {user:"monika_gamer", rating:7},
  {user:"rkowalski", rating:9}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"DOOM Eternal"})
WITH g
UNWIND [
  {user:"tomek_fps", rating:9},
  {user:"lukasz_rpg", rating:6},
  {user:"janek77", rating:7},
  {user:"rkowalski", rating:8}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"Valorant"})
WITH g
UNWIND [
  {user:"tomek_fps", rating:7},
  {user:"rkowalski", rating:8},
  {user:"marek_it", rating:6}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"League of Legends"})
WITH g
UNWIND [
  {user:"lukasz_rpg", rating:8},
  {user:"monika_gamer", rating:9},
  {user:"ania_stream", rating:7},
  {user:"rkowalski", rating:6},
  {user:"annak", rating:8}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"Overwatch 2"})
WITH g
UNWIND [
  {user:"piotr89", rating:6},
  {user:"tomek_fps", rating:8},
  {user:"rkowalski", rating:7},
  {user:"monika_gamer", rating:8}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"Assassin's Creed Valhalla"})
WITH g
UNWIND [
  {user:"janek77", rating:9},
  {user:"annak", rating:7},
  {user:"marek_it", rating:6}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

MATCH (g:Game {title:"FIFA 23"})
WITH g
UNWIND [
  {user:"piotr89", rating:8},
  {user:"rkowalski", rating:9},
  {user:"ola_play", rating:7},
  {user:"lukasz_rpg", rating:6},
  {user:"monika_gamer", rating:9},
  {user:"tomek_fps", rating:7}
] AS pair
MATCH (u:User {username: pair.user})
CREATE (u)-[:RATED {rating: pair.rating}]->(g);

CREATE CONSTRAINT user_username_unique
FOR (u:User)
REQUIRE u.username IS UNIQUE;

CREATE CONSTRAINT user_email_unique
FOR (u:User)
REQUIRE u.email IS UNIQUE;

CREATE CONSTRAINT game_title_unique
FOR (g:Game)
REQUIRE g.title IS UNIQUE;

CREATE CONSTRAINT rated_rating_required
FOR ()-[r:RATED]-()
REQUIRE r.rating IS NOT NULL;
