select sbj.name, (case when s.gender = 1 then '남' else '여' end), count(*) 
      from Enroll e inner join subjects sbj on sbj.id = e.subjects
					inner join Student s on s.id = e.student 
                    where s.addr = '서울'
                    group by sbj.name, s.gender
                    order by sbj.name, s.gender desc;

# named은 인덱스가 없어서  소팅하는데 시간이 오래 걸린다. 대신에 sbj.id 로 하면 인덱스 기능이 있어서  소팅하는데 시간이 덜 걸린다.