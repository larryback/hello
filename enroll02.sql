 # 각 과목에  100명의 학생을 랜덤으로 입력한다.  그래서 10번을 수행하면 학생이 1000명이 된다.

insert into Enroll(subjects, student)
select sbj.id, s.id
  from (select id from subjects where id not in (select distinct subjects from Enroll) order by id limit 1) sbj, # 과목 중복 방지
       (select id from Student order by rand() limit 100) s;  # 학생을 랜덤으로 100씩 생성
       
      