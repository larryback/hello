create table Grade(
	id int unsigned not null auto_increment primary key,
    midterm int unsigned not null default 0,
    finalterm int unsigned not null default 0,
    enroll int unsigned not null default 0,
    constraint foreign key fk_enroll(Enroll) references Enroll.(id)
    on delete cascade 
); 

describe Test2;
