    
    
    
    
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


