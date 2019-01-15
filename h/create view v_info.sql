create view v_enroll_subjects AS 
	select e.*, s.name, s.prof
    from Enroll e inner join Subjects s on e.subject = s.id;
    
desc v_enroll_subjects;

show create view  v_enroll_subjects;  

create v_grade_enroll AS
	select g.*, e.subject, e.student
    from Grade g inner join Enroll e on 
    
 select * from Grade;   
 select * from Subject; 
# Student, subjects, Enroll, 
    
create v_ enroll_subjects_student AS
	select 
    from Enroll e inner join subjects s on e.subjects = s.id;
    
create view v_info AS
select s.id '학번', s.name '이름', j.id '과목번호', j.name '과목이름', g.midterm '중간', g.finalterm '기말', g.midterm+finalterm '총점', (g.midterm+finalterm)/2 '평균',
      (case when (g.midterm+finalterm)/2 > 90 then 'A'
             when (g.midterm+finalterm)/2 > 80 then 'B'
            when (g.midterm+finalterm)/2 > 70 then 'C'
            when (g.midterm+finalterm)/2 > 60 then 'D'
            else 'F' end) '학점'
 from Enroll e inner join Student s on e.student = s.id
               inner join Subject j on e.subject = j.id
                inner join Grade g on e.id = g.enroll;
                
select * from v_info where 과목이름 = '화학' order by 평균 desc;              