
# 과목별 담당 교수명
select s.*, p.name as 'prof.name'
   from Subject s inner join Prof p on s.prof = p.id;
 
 
 # 과목별 학생수
select subject, max(s.name) as 'subject name', count(*) as '학생수'
	from Enroll e inner join subjects s on e.subject = s.id
    group by e.subject;
 
# 역사과목의 학생목록 
select s.name, s.birth
		from Enroll e inner join Student s on e.student = s.id
					  inner join Subject sbj on e.subject = sbj.id 
        where e.subject = '역사';
 
# 특정과목(국어)를 듣는 서울 거주 학생 목록 (과목명, 학번, 학생명) 
select s.name, s.birth
		from Enroll e inner join Student s on e.student = s.id
					  inner join Subject sbj on e.subject = sbj.id 
        where e.subject = '국어' and  s.addr = '서울' ;
        
# 역사과목을 수강중인  지역별 학생들수 

select substring(s.addr,1,2) as a, count(*) as student_cnt
  from Enroll e inner join Student s on e.student = s.id
                inner join Subject sbj on e.subject = sbj.id
 where sbj.name = '역사' group by a;
