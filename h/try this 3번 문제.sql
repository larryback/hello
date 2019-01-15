#Try this  문제 3번.

delimiter \\
create trigger tr_subject_prof_null
		before insert
		on Subject for each row
Begin
		if NEW.prof is null Then
			Set NEW.prof = (select id from Prof order by rand() limit 1);
        End if;
		
        if NEW.students is null Then
			set NEW.students = 0;
        End if;   
        
End;

select * from Subject;

        