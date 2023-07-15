CREATE DATABASE IF NOT EXISTS develop;
USE develop;

CREATE TABLE IF NOT EXISTS visits (
  count INT
);

INSERT IGNORE INTO visits (count) VALUES (0);

CREATE TABLE IF NOT EXISTS solar_system (
  id INT AUTO_INCREMENT PRIMARY KEY,
  fun_facts TEXT
);

INSERT INTO solar_system (fun_facts) VALUES
  ('The Sun is so large that approximately 1.3 million Earths could fit inside it.'),
  ('The largest volcano in the solar system is Olympus Mons on Mars.'),
  ('Venus rotates in the opposite direction compared to most other planets.'),
  ('Jupiter has a massive storm known as the Great Red Spot.'),
  ('Saturn''s rings are made up of countless small particles of ice and rock.'),
  ('Neptune experiences the strongest winds in the solar system.'),
  ('The asteroid belt is located between Mars and Jupiter.'),
  ('Pluto is now classified as a dwarf planet.'),
  ('Ganymede is the largest moon in the solar system.'),
  ('Voyager 1 is the farthest man-made object from Earth.');

