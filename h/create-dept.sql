create table Dept(
	id int(10) unsigned not null auto_increment,
    name varchar(31) not null comment'학과명',
    primary key(id)
    );
    
CREATE TABLE `Dept` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(31) COLLATE utf8_bin NOT NULL DEFAULT '0',
  `likecont` int(11) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8 COLLATE=utf8_bin    

insert into Dept(name) values('영문학과')