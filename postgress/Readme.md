
      create postgress db using below helm chart:

      helm install my-release oci://registry-1.docker.io/bitnamicharts/postgresql

      # To get the password
      =====================
      kubectl get secret --namespace default my-postgres-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d

      


      kubectl exec -it my-postgres-postgresql-0 -- bash
      I have no name!@my-postgres-postgresql-0:/$ psql --host 127.0.0.1 -U postgres -d postgres -p 5432
      Password for user postgres:
      psql (16.1)
      Type "help" for help.
      
      postgres=# create table employee(emp_id int,emp_name varchar(40),emp_sal int);
      CREATE TABLE
      postgres=# select * from employee;
       emp_id | emp_name | emp_sal
      --------+----------+---------
      (0 rows)
      
      postgres=# select * from employee;
       emp_id | emp_name | emp_sal
      --------+----------+---------
      (0 rows)
      
      postgres=# select * from employee;
       emp_id | emp_name | emp_sal
      --------+----------+---------
          200 | prsanna  |    2000
          300 | rajesh   |    3000
          400 | srinadh  |    4000
      (3 rows)


       kubectl port-forward svc/my-postgres-postgresql 5432

