DELIMITER $$
CREATE Function f_student_count(_name varchar(100))
 RETURNS smallint
BEGIN
	RETURN (select count(*) from Enroll
            where subject = ( select id from Subject where name = _name));
END $$
DELIMITER ;

select * from Enroll;

select f_student_count('물리');
select name, f_student_count(name) from Subject;
