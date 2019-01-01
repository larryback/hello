    
    
    
    
 #문항 1번. 학번, 학생명, 수강과목수, 전과목 평균점수 컬럼(총 4개 칼럼)을 갖는 View를 작성하시오.   
drop view if exists v_students;

create view v_students AS

	select e.student '학번', max(s.name) '학생명', count(*) '수강과목수',
			round(avg(g.midterm+finalterm)/2) '전과목평균점수'
     
		from Enroll e inner join Student s on e.student = s.id
                      inner join Grade g on e.id = g.enroll
        group by e.student;              
                
select * from v_students;             

select * from v_inform1;
select * from Subject;
select * from Student;
select * from Club;
select * from ClubMember;
select * from Student;
select * from Grade;
select * from Prof;
select * from Enroll;
# 문항 2번. 학번을 주면 해당 학생의 전과목 평균을 반환하는 Stored Function을 작성하시오.
#(호출 예. f_student_avg(학번))
drop function if exists f_student_avg;

delimiter //
Create function f_student_avg(_stu int(100) unsigned)
 Returns int(100)
 
Begin
	return (select avg(g.midterm + g.finalterm)/2 '전과목평균'
	from Grade g inner join Enroll e on g.enroll = e.id
    where e.student = _stu)  ; 
End //
Delimiter ;

select name, id, f_student_avg(id) from Student limit 10;
 
 
#문항 3번. 클럽(Club)을 하나 추가하면 클럽회원(ClubMember)으로 임의의 한 학생(Student)을
#회장으로 자동 등록하는 Trigger 를 작성하시오. 
drop trigger if exists tr_club_member_rand1;

Delimiter //

 create trigger tr_club_member_rand1
	after insert on Club for each row
     
Begin
	
    
		insert into ClubMember(club, student, level)
		select NEW.id, id, 2
        from Student
        where id not in (select student from ClubMember where level in (1,2))
        order by rand() limit 1;
        
    
End //
  
Delimiter ;  

insert into Club(name) values('1부');

select * from Club order by id desc;

select * from ClubMember where club = (select max(id) from Club);

#문항 4번. 지난 학기 데이터 (수강학생수, 성적등)를 기준으로 인기교수 (강좌) Top 3
#을 추천하는 Stored Procedure 를 작성하시오. 단, 데이타의 가중치는 자유롭게 부여 하시오.

Drop procedure if exits sp_top3_subject

Delimiter //

Create Procedure sp_top3_subject

Begin

	select e.subject, sum(p.likecnt) from Enrolle e
    inner join Subject j on e.subject = j.id
    inner join Prof p on j.prof = p.id
    
    rank over (order by sum(p.likecnt)) ranking 
    where ranking <= 3 ;
    
End //

Delimiter ;

call sp_top3_subject;    

















#문항 6번. 과목별 Top 3 학생의 이름과 성적을 한줄로 표현하는 리포트를 아래와 같이 출력되는 
#프로시저를 작성하시오. ( 단, 성적은 중간, 기말평균이며, 과목명 오름차순으로 정렬하시오.)

drop procedure if exists sp_top3_grade;
DELIMITER $$
CREATE PROCEDURE sp_top3_grade()
begin
   declare _isdone boolean default False;
   declare _avr tinyint;
    declare _subject varchar(10);
   declare _tier varchar(10);
   declare _grade varchar(10);


   declare cur_avrs cursor for
       select j.name, s.name, v.avr from v_grade_enroll v inner join Student s on v.student = s.id
                                                           inner join Subject j on v.subject = j.id
         order by j.name, v.avr desc;

   declare continue handler
       for not found set _isdone = True;

   drop table if exists t_grade;

   create temporary table t_grade (
        subject varchar(10) default '',
       tier1 varchar(10) default '',
       grade1 tinyint default 0,
       tier2 varchar(10) default '',
       grade2 tinyint default 0,
       tier3 varchar(10) default '',
       grade3 tinyint default 0
   );

   open cur_avrs ;

   loop1: LOOP
       FETCH cur_avrs into _subject, _tier, _avr;
       set _subject = _subject;
       set _grade = floor(_avr);
       set _tier = _tier;

       if not exists (select * from t_grade where subject = _subject) then
           insert into t_grade(subject, tier1, grade1) value(_subject, _tier, _grade);

        elseif exists (select * from t_grade where tier2 = '') then
            update t_grade set tier2 = _tier, grade2 = _grade where subject = _subject;

        elseif exists (select * from t_grade where tier3 = '') then
            update t_grade set tier3 = _tier, grade3 = _grade where subject = _subject;

       end if;

        IF _isdone THEN
           LEAVE loop1;
       END IF;

   END LOOP loop1;

   close cur_avrs;

   select subject '과목명', tier1 '1등', grade1 '점수', tier2 '2등', grade2 '점수', tier3 '3등', grade3 '점수'
     from t_grade;

end$$
DELIMITER ;
call sp_top3_grade();