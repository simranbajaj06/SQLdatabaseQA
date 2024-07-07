few_shots = [
    {'Question' : "give the first names in upper letters of all the workers?",
     'SQLQuery' : "select UPPER(fname) from worker;",
     'SQLResult': "Result of the SQL query",
     'Answer' : "['MONIKA','NIHARIKA','VISHAL','AMITABH','VIVEK','VIPUL','SATISH','GEETIKA']"},
    {'Question': "give me names of all the workers who have salary between 100000 and 500000",
     'SQLQuery':"SELECT fname, lname FROM worker WHERE SALARY BETWEEN 100000 AND 500000",
     'SQLResult': "Result of the SQL query",
     'Answer': "[monika arora, vishal singhal,amitabh singh , vivek bhati , vipul diwan]"},
    
      {'Question': "give me top 5 records of a table order by salary" ,
        'SQLQuery': "SELECT * FROM worker ORDER BY SALARY DESC LIMIT 5",
        'SQLResult': "Result of the SQL query",
        'Answer' : "[7	satish	kumar	750000	2014-01-20 09:00:00	account, 4	amitabh	singh 500000	2014-02-20 09:00:00	admin,5	vivek	bhati	500000	2014-06-11 09:00:00	admin,3	vishal	singhal	300000	2014-02-20 09:00:00	hr,6	vipul	diwan	200000	2014-06-11 09:00:00	account]"},
    {'Question': "give the names of employees who have same salary",
     'SQLQuery' : "select w1.* from worker w1, worker w2 where w1.salary = w2.salary and w1.worker_id != w2.worker_id;",
     'SQLResult': "Result of the SQL query",
     'Answer' : "[5	vivek	bhati	500000	2014-06-11 09:00:00	admin, 4	amitabh	singh	500000	2014-02-20 09:00:00	admin]"
     }
]