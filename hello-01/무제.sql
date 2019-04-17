alter table Subject add column students smallint default 0 not null;

desc Subject;

Delimiter //
create trigger tr_enroll_subject_students
	after insert on Enroll for Each Row
Begin

End//
Enroll Delimiter ;    
    
select count(*) from Enroll where subject = (select subject from Enroll where id = 23);



insert into Enroll(subject, student) values(1, 101)

update Subject s 
	set students = (select count(*) from Enroll where subject = s.id group by subject);


select subjects, count(*) from Enroll group by subjects;

alter table Student add column subjects smallint default 0 not null ;
desc Student;
select * from Student;
update Student s set subjects =( select count(*) from Enroll where student = s.id group by student);


CREATE DEFINER = CURRENT_USER TRIGGER `dooodb`.`Enroll_BEFORE_DELETE` BEFORE DELETE ON `Enroll` FOR EACH ROW
BEGIN
	delete from Grade
    where enroll = OLD.id;
    
    update Subject
      set students =
          (
          select count(*) - 1 from Enroll
          where subject = (select subject from Enroll where id = OLD.id)
          )
          
	where id = (select subject from Enroll where id = OLD.id);

END
