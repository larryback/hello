SELECT * FROM dooodb.Grade;

insert into Grade(enroll, midterm, finalterm) select id, (100- ceil(rand()*45)), (100 - ceil(rand()*45)) from Enroll order by id ;