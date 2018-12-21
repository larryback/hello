create table Club(
	id smallint unsigned not null auto_increment primary key,
    name varchar(31) not null,
    createdate timestamp not null default current_timestamp,
    leader int unsigned,
    constraint foreign key fk_leader_student(leader) references Student(id)
    on delete restrict
    
);

insert into Club(name, leader) values('요트부', 150);
insert into Club(name, leader) values('기타부', 300);
insert into Club(name, leader) values('음악부', 200);
     
select * from Club;

select c.*, s.name as 'student name' from Club c inner join Student s on c.leader = s.id;



 create table Enroll(
	id int unsigned not null auto_increment primary key,
    student int unsigned,
    subjects int unsigned,
    constraint foreign key fk_student(student) references Student(id)
    on delete cascade,
    constraint foreign key fk_subjects(subjects) references subjects(id)
    on delete cascade
);   

#alter table Enroll add constraint foreign key fk_student(student) references Student(id)
#    on delete cascade;
#alter table Enroll addconstraint foreign key fk_subjects(subjects) references subjects(id)
#    on delete cascade;


 create table subjects(
	id int unsigned not null auto_increment primary key,
    name varchar(31) not null default 0,
    prof int unsigned,
    constraint foreign key fk_prof(prof) references prof(id)
    on delete set null 
); 

select * from prof;

insert into subjects(name, prof)
select '국어', id from prof order by rand() limit 10;

update subjects set name = '화학' where name = '국어' and id <> 10 limit 1;

select * from sujects;
 
insert into Enroll(student, subjects) 
select id from Student order by rand() limit 10;
select  subject from subjects like '화학' or '국어';    


create table prof(
	id int unsigned not null auto_increment primary key,
    name varchar(31) not null default 0,
    likecont int default 0
    );
    
select ceil(rand() * 100) from dual;
    
insert into prof(name, likecont) select name, ceil(rand() * 100) from Student order by rand() limit 100;    