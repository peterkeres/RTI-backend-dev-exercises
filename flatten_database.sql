-- --------------------------------------------------------------------------------------------------------
-- This file is just used to set up the flattened table and whatever steps i took to get there.
-- --------------------------------------------------------------------------------------------------------

-- Lets just check what kinda data we got
select * from records limit 10;

-- probably not the cleanest route, but lets join all the tables based on matches
select * from records as main
    inner join workclasses w on main.workclass_id = w.id
    inner join education_levels el on main.education_level_id = el.id
    inner join marital_statuses ms on main.marital_status_id = ms.id
    inner join occupations o on main.occupation_id = o.id
    inner join races r on main.race_id = r.id
    inner join sexes s on main.sex_id = s.id
    inner join countries c on main.country_id = c.id
    limit 30;

-- Drop all the id fields, this should 'flatten' all the data across all the tables
select age, w.name, el.name, education_num, ms.name, o.name, r.name, s.name, capital_gain, capital_loss, hours_week, c.name, over_50k
from records as main
    inner join workclasses w on main.workclass_id = w.id
    inner join education_levels el on main.education_level_id = el.id
    inner join marital_statuses ms on main.marital_status_id = ms.id
    inner join occupations o on main.occupation_id = o.id
    inner join races r on main.race_id = r.id
    inner join sexes s on main.sex_id = s.id
    inner join countries c on main.country_id = c.id;


-- Lets make the table that will hold all the flatten data
--     Note, assuming the old 'id' filed from OG records is nothing but just a auto integer.
create table if not exists main.flatten_data(
  age integer,
  workclass text,
  education_levels text,
  education_num integer,
  marital_status text,
  occupation text,
  race text,
  sex text,
  capital_gain integer,
  captial_loss integer,
  hours_week integer,
  country text,
  over_50k blob
);


-- Throwing all the data into flatten_data table
insert into flatten_data
    select age, w.name, el.name, education_num, ms.name, o.name, r.name, s.name, capital_gain, capital_loss, hours_week, c.name, over_50k
    from records as main
    inner join workclasses w on main.workclass_id = w.id
    inner join education_levels el on main.education_level_id = el.id
    inner join marital_statuses ms on main.marital_status_id = ms.id
    inner join occupations o on main.occupation_id = o.id
    inner join races r on main.race_id = r.id
    inner join sexes s on main.sex_id = s.id
    inner join countries c on main.country_id = c.id;


-- Check that i didnt lose anyone: count should be 48842
select count(*) from flatten_data;
+--------+
|count(*)|
+--------+
|48842   |
+--------+

