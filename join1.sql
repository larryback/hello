
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
select sbj.name, s.id, s.name 
		from Enroll e inner join 