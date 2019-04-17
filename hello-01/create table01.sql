create table Test(
	id tinyint(0) unsigned not null auto_increment,
    name char(5) not null,
    primary key(id)
);    
   
desc Test;   

insert into Test(name) values('김일수');

CREATE TABLE `Test2` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `num1` tinyint(4) NOT NULL COMMENT 'tiny',
  `num2` bigint(10) DEFAULT NULL COMMENT 'big',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `Student` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` tinyint(4) NOT NULL COMMENT 'tiny',
  `addr` bigint(10) DEFAULT NULL COMMENT 'big',
  `birth` 
  `tel`
  `email`
  `regdt`
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;