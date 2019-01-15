    
    
    
    
 #문항 1번. 학번, 학생명, 수강과목수, 전과목 평균점수 컬럼(총 4개 칼럼)을 갖는 View를 작성하시오.   

create view v_enroll_subject_student AS

select s.id '학번', s.name '학생명', sum(j.name) '수강과목수', (g.midterm+finalterm)/2 '전과목평균점수'
     
 from Enroll e inner join Student s on e.student = s.id
               inner join Subject j on e.subject = j.id
                inner join Grade g on e.id = g.enroll;
                
             

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

delimiter //
Create function f_student_avg(_student_id int(100))
 Returns int(100)
 
Begin
	return (select s.id, (midterm + finalterm)/2 '전과목평균'
from Student s inner join Enroll e on  s.id = e.student 
               inner join Grade g on g.enroll = e.id  
               where s.id = _student_id );
            
End //
Delimiter ;

select f_student_avg(_student_id);
 
 
#문항 3번. 클럽(Club)을 하나 추가하면 클럽회원(ClubMember)으로 임의의 한 학생(Student)을
#회장으로 자동 등록하는 Trigger 를 작성하시오. 

Delimiter //

  create trigger tr_club_clubmember
  
	Before insert
    
    on Club for each row
    
  Begin
  
	insert into Clubmember values (New.name)
    set New.name = ( select id from Student s 
    inner join ClubMember cm on s.id = cm.student
    where cm.level is not 1 and 2
    order by rand() limit 1);
    
End //
  
Delimiter ;  


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