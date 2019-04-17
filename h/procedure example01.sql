DROP Procedure IF EXISTS sp_test(_subject_name varchar(31))

DELIMITER $$
CREATE Procedure sp_test(_subject_name varchar(31)) 
BEGIN
    declare v_sbj_id smallint default 0;
    
    select id into v_sbj_id from Subject where name = _subject_name;
    
	select count(*) stu_cnt, (avg(g.midterm + g.finalterm) / 2) avr
      from Enroll e inner join Grade g on e.id = g.enroll
     where e.subject = v_sbj_id;
END $$
DELIMITER ;

call sp_test('국어');
select name, f_student_count(name) from Subject;