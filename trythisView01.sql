create or replace view v_emp_dept AS
    select e.first_name, e.salary, NVL(e.commission_pct,0), d.department_name
      from Employees e inner join Departments d
                          on e.department_id = d.department_id
    WITH READ ONLY;
