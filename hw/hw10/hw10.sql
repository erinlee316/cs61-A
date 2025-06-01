CREATE TABLE parents AS
  SELECT "ace" AS parent, "bella" AS child UNION
  SELECT "ace"          , "charlie"        UNION
  SELECT "daisy"        , "hank"           UNION
  SELECT "finn"         , "ace"            UNION
  SELECT "finn"         , "daisy"          UNION
  SELECT "finn"         , "ginger"         UNION
  SELECT "ellie"        , "finn";

CREATE TABLE dogs AS
  SELECT "ace" AS name, "long" AS fur, 26 AS height UNION
  SELECT "bella"      , "short"      , 52           UNION
  SELECT "charlie"    , "long"       , 47           UNION
  SELECT "daisy"      , "long"       , 46           UNION
  SELECT "ellie"      , "short"      , 35           UNION
  SELECT "finn"       , "curly"      , 32           UNION
  SELECT "ginger"     , "short"      , 28           UNION
  SELECT "hank"       , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  -- select child column from combined table
  SELECT child FROM dogs, parents 
  -- matches name = parent
  WHERE name = parent 
  -- sort results in descending order of parent's height
  ORDER BY height DESC;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  -- select name and size from combined table
  SELECT name, size FROM dogs, sizes
  -- check that dog's height fits within the height range
  WHERE height > min AND height <= max;


-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT p1.child AS p1_child, -- sibling 1
         p1.parent AS parent, -- same parent
         p2.child AS p2_child -- sibling 2
  -- alias because using two columns with same name 
  FROM parents AS p1, parents AS p2
  -- siblings have same parent and do not share same name as themselves
  WHERE p1.child < p2.child AND p1.parent = p2.parent;


-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  -- print string output
  SELECT "The two siblings, " || siblings.p1_child || " and " || siblings.p2_child || ", have the same size: " || s1.size
  -- join siblings and size_of_dogs table together
  FROM siblings
  -- make alias where size_of_dogs column matches with siblings 
  JOIN size_of_dogs AS s1 ON s1.name = siblings.p1_child
    -- make alias where size_of_dogs column matches with siblings 
  JOIN size_of_dogs AS s2 ON s2.name = siblings.p2_child
  -- keeps only the siblings that have the same size
  WHERE s1.size = s2.size;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  -- select two columns fur and height_range
  SELECT fur, MAX(height) - MIN(height) AS height_range
  -- use data from dogs table
  FROM dogs
  -- group info by each type of fur
  GROUP BY fur
  -- only takes in heights that fit criteria
  HAVING MAX(height) < AVG(height) * 1.3 AND MIN(height) > AVG(height) * 0.7;

