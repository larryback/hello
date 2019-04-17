drop procedure if exists sp_club_members;
delimiter $$
create procedure sp_club_members(_club_name varchar(31))
begin
    select s.name, 
        (case cm.level
            when 2 then '회장' 
            when 1 then '간부'
            else '평회원' end) level_name
      from ClubMember cm inner join Student s on cm.student = s.id
     where club = (select id from Club where name = _club_name)
     order by cm.level desc;
end $$
delimiter ;

-- call sp_cnt('select * from Subject');
call sp_club_members('요트부');

-- select * from Club;
-- select * from ClubMember;

CREATE TABLE Member (

   userid VARCHAR(20),

   `point` INT

) ENGINE = InnoDB ROW_FORMAT = DEFAULT;






