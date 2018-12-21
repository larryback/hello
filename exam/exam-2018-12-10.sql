# 문항1. 학생, 과목, 교수, 수강내역 테이블의 관계를 고려하여 생성하는 DDL을 작성하시오 (5점)
create table Student (
	id int unsigned not null auto_increment comment '학번',
    name varchar(32) not null comment '학생명'
    addr varchar(30),
    birth date,
    tel varchar(15),
    email varchar(31),
    regdt timestamp default current-timestamp not null,
    primary key(id)
    );
    
desc Student;

create table Subjects(
	id int(10) unsigned not null auto_increment,
    name varchar(31) collate utf8_bin not null default 0,
    prof int(10) unsigned default null,
    primary key (id),
    key fk_prof(prof),
    contraint subjects_ibfk1 foreign key(prof) references prof(id) on delete set null,
    );
    
desc subjects;

create table Prof(
		id int(10) unsigned not null auto_increment,
        name varchar(31) collate utf8_bin not null default 0,
        likecnt int(11) default 0,
        primary key (id)
        );
        
desc Prof;

create table Enroll(
	id int(10) unsigned not null auto_increment,
    student int(10) unsigned default null,
    subject int(10) unsigned default null,
    primary key(id),
    key fk_student(student) references Student(id) on delete cascade,
    key fk_subjects(subjects) references Subjects(id) on delete cascade,
    );
desc Enroll;

    
# 문항2. 학생테이블고 과목테이블을 활용하여 , 수강내역테이블에 테스트용 데이터를 구성하는 DML을 절차적으로 작성하시오.(10점)alter

insert into Enroll(id, student, subject) # 각 과목에 100명의 학생을 랜덤으로 입력한다. 그래서 10번을 수행하면 학생이 1000명이 된다.

select sbj.id, s.id from Subjects where id not in (select distinct subjects from Enroll) order by id limit 1)sbj, #과목중복방지
											      (select id from Student order by rand() limit 100)s;
                                                  # 학생을 랜덤으로 100명씩 생성
                                                  
#문항3. 동아리(Club)별 회원 테이블(ClubMember)을 다음과 같이 만들고, 동아리별 50명 내외로 가입시키시오.(단, 클럽테이블의 리더칼럼은 
#삭제하고, 리더를 회원테이블의 레벨 2로 등록하시오.)(15점)    

create table Club(
	id int(10) unsigned not null auto-increment,
    club varchar(31) not null comment '동아리',
    student int(10) unsigned default null comment '학생',
    level tinyint unsigned default 0 coment '레벨',
    primary key(id)
    );
    
select * from Club 
	update Club set level = mod(Student, 3) where Student=2 comment'클럽장',
    Student=1 comment'간부',
    Student=0 comment'평회원';
    
#문항4. 학과테이블(Dept)을 만들고 5개 학과 이상 샘플 데이터를 등록하고, 학생테이블에 학과 컬럼(dept)을 추가한 후 모든 학생에 대해
#랜덤하게 과 배정을 시키시오.    

create table Dept(
	id int unsigned not null auto-increment ,
    name int(10) unsigned not null comment '학과명',
    prof int(10) unsigned not null comment '지도교수',
    student int(10) unsigned default null comment '과대표',
    primary key(id)
    );
    
insert into Dept(name) values('수학과');
# 영문학과, 경영학과, 법학과, 국문학과 4회 반복

select * from Dept
	update Dept set level = mod(student, 5) where student = 0 comment '영문학과', student = 1 comment '경영학과',
    student = 2 comment '수학과', student = 3 comment '법학과',
    student = 4 comment '국문학과' ;
    
# 문항5. 강의실 테이블(Classroom)을 만들고, 샘플강의실 10개를 등록하고, 과목별 강의실 배치를 위해 과목(Subject) 테이블에 강의실컬럼
# (classroom) 추가한 후 배정하시오.

create table Classroom (
	id int unsigned not null auto-increment,
    classroom varchar(32) not null comment'강의실'
    primary key (id)
    );

desc Classroom;
    
insert into Classroom (classroom) values('101 강의실');  
# 102~110 강의실까지 9회 반복

alter table Subjects add column classroom int(10) unsigned not null default 0 ;

SELECT 
    Classroom.*, Subject.classroom
FROM
    Classroom
        INNER JOIN
    Subjects ON Classroom.id = Subjects.classroom;

# 문항6. 1) 수강하는 과목별 중간고사, 기말고사 성적을 저장하는 테이블(Grade)을 생성하고  2) 수강테이블 기준으로 샘플 데이터를 
# 중간(midterm), 기말(finalterm) 성적(100점만점)으로 구성하고, 3) 과목별 수강생을 과목/성적 순으로 아래와 같은 형식으로 출력
# 하는 SQL을 작성하시오. 4) 과목별 통계 리포트를  과목순으로 하여 아래와 같이 출력하는 SQL을 작성하시오. 5) 학생별 통계 리포트
# 를 성적순으로 하여 아래와 같이 출력하는 SQL을 작성하시오.

insert into grade(enroll, midterm, finalterm) select id, ceil(rand()*100), ceil(rand()*100) from Enroll order by id asc limit 9999;

update grade
    SET midterm = midterm + 30 + ceil(rand()*10) where midterm between 0 and 30;
update grade
   SET finalterm = finalterm + 30 + ceil(rand()*10) where finalterm between 0 and 30;
            
#REPORT 1
select i.name, sbj.subject, g.midterm, g.finalterm, g.midterm + g.finalterm as total, (g.midterm + g.finalterm)/2  as avg,
    (CASE WHEN (g.midterm + g.finalterm)/2 >= 90 THEN 'A'
        WHEN (g.midterm + g.finalterm)/2 >= 80 and (g.midterm + g.finalterm)/2 < 90 THEN 'B'
       WHEN (g.midterm + g.finalterm)/2 >= 70 and (g.midterm + g.finalterm)/2 < 80 THEN 'C'
       WHEN (g.midterm + g.finalterm)/2 >= 60 and (g.midterm + g.finalterm)/2 < 70 THEN 'D'
       ELSE 'F'
       END) as '학점'
    from Enroll e inner join info i on e.student = i.id
   inner join Subjectname sbj on e.subjectname=sbj.id
   inner join grade g on e.id=g.id order by sbj.subject, avg desc;

#REPORT 2
select T1.subject, T2.mean as '과목당 평균', T1.avg as '최고 점수', T1.name, T2.count
From (select e.id as id, i.name as name, sbj.subject as subject, (g.midterm + g.finalterm)/2 as avg
    from Enroll e inner join info i on e.student = i.id
   inner join Subjectname sbj on e.subjectname=sbj.id
   inner join grade g on e.id=g.id) as T1,
   (select sbj.subject, AVG((g.midterm + g.finalterm)/2) as mean, MAX((g.midterm + g.finalterm)/2) as max , count(*) as count
    from Enroll e inner join info i on e.student = i.id
   inner join Subjectname sbj on e.subjectname=sbj.id
   inner join grade g on e.id=g.id group by e.subjectname) as T2
Where T1.avg = T2.max and T1.subject=T2.subject;

#REPORT 3
SELECT  T3.id as '학생ID', T3.name as '이름', T3.count '수강중인 과목수', T3.totalscore as'총점', T3.avg as '평균',
    (CASE WHEN T3.avg >= 90 THEN 'A'
        WHEN T3.avg >= 80 and T3.avg < 90 THEN 'B'
       WHEN T3.avg >= 70 and T3.avg < 80 THEN 'C'
       WHEN T3.avg >= 60 and T3.avg < 70 THEN 'D'
       ELSE 'F'
       END) as '학점'
FROM
(select i.id as id, i.name as name, count(*) as count, SUM(g.midterm) + SUM(g.finalterm) as totalscore, (AVG(g.midterm) + AVG(g.finalterm))/2 as avg
    from Enroll e inner join info i on e.student = i.id
   inner join Subjectname sbj on e.subjectname=sbj.id
   inner join grade g on e.id=g.id group by i.id ) as T3 order by T3.avg desc;






select sbj.subject, AVG((g.midterm + g.finalterm)/2) as mean, MAX((g.midterm + g.finalterm)/2) as max , count(*)
    from Enroll e inner join info i on e.student = i.id
   inner join Subjectname sbj on e.subjectname=sbj.id
   inner join grade g on e.id=g.id
group by e.subjectname;


select e.id as id, i.name as name, sbj.subject as subject, (g.midterm + g.finalterm)/2 as avg
    from Enroll e inner join info i on e.student = i.id
   inner join Subjectname sbj on e.subjectname=sbj.id
   inner join grade g on e.id=g.id;


select r2.id, r2.subject, group_concat(r2.name, r2.avg)
from
    (select e.id as id, i.name as name, sbj.subject as subject, (g.midterm + g.finalterm)/2 as avg
    from Enroll e inner join info i on e.student = i.id
   inner join Subjectname sbj on e.subjectname=sbj.id
   inner join grade g on e.id=g.id) as r2
where r2.avg = r2.vmax;



select * from grade;
select * from Subjectname;
select * from Enroll;

Message Input

Message 김영모(Youngmo Kim)