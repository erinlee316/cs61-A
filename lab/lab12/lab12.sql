CREATE TABLE finals AS
  SELECT "RSF" AS hall, "61A" as course UNION
  SELECT "Wheeler"    , "61A"           UNION
  SELECT "Pimentel"   , "61A"           UNION
  SELECT "Li Ka Shing", "61A"           UNION
  SELECT "Stanley"    , "61A"           UNION
  SELECT "RSF"        , "61B"           UNION
  SELECT "Wheeler"    , "61B"           UNION
  SELECT "Morgan"     , "61B"           UNION
  SELECT "Wheeler"    , "61C"           UNION
  SELECT "Pimentel"   , "61C"           UNION
  SELECT "Soda 310"   , "61C"           UNION
  SELECT "Soda 306"   , "10"            UNION
  SELECT "RSF"        , "70";

CREATE TABLE sizes AS
  SELECT "RSF" AS room, 900 as seats    UNION
  SELECT "Wheeler"    , 700             UNION
  SELECT "Pimentel"   , 500             UNION
  SELECT "Li Ka Shing", 300             UNION
  SELECT "Stanley"    , 300             UNION
  SELECT "Morgan"     , 100             UNION
  SELECT "Soda 306"   , 80              UNION
  SELECT "Soda 310"   , 40              UNION
  SELECT "Soda 320"   , 30;

CREATE TABLE sharing AS
  -- selects each courses and distinct halls shared by same course
  SELECT a.course, COUNT(DISTINCT a.hall) AS shared
  FROM finals AS a, finals AS b
  -- filter out columns where halls match, but courses are different
  WHERE a.hall = b.hall AND a.course != b.course
  -- groups each course
  GROUP BY a.course;


CREATE TABLE pairs AS
  -- output string as rows in rooms column
  SELECT a.room || " and " || b.room || " together have " || (a.seats + b.seats) || " seats" AS rooms
  -- get columns from size table
  FROM sizes AS a, sizes as b
  -- filter out columns where rooms are alphabetical order and have 1000+ seats
  WHERE a.room < b.room AND (a.seats + b.seats) >= 1000
  -- sorts seats with 1000+ in descending order
  ORDER BY (a.seats + b.seats) DESC;


CREATE TABLE big AS
  -- table only inclused course column
  SELECT course
  -- get info from finals and sizes tables
  FROM finals, sizes
  -- joing table where hall and room match
  WHERE hall=room 
  -- groups courses to occur once
  GROUP BY course
  -- filter out the seats from aggregate function that are 1000+
  HAVING SUM(seats) >= 1000;


CREATE TABLE remaining AS
  -- select course and remaining
  SELECT course, (SUM(seats) - MAX(seats)) AS remaining
  -- get info from finals and sizes table
  FROM finals, sizes
  -- get info where hall and room match
  WHERE hall=room 
  -- ensures that each course is output once
  GROUP BY course;
