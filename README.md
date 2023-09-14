## JCodeLib-utils

Some of the utility code used to run the [JCodeLib](https://github.com/seoultech-selab/JCodeLib) project.



### 1. save_old_and_new_code.py

Reads data from the files, commits table via the file_id in files, and then saves the old and new code of the target project.

1. Read the data from the files, commits table through SQL Query from the DB, and then save it as a csv.

   ```sql
   ## This is example of SQL query
   ## Get project_name, file_id, file_path, old_commit_hash, new_commit_hash
   select c.project_name, f.file_id, f.file_path, c.old_commit, c.new_commit
   from files as f
   inner join commits c
   on f.commit_id = c.commit_id
   where f.file_id in (1393134,1397131);
   ```

2. Place the Target project (.git folder) under Desktop.
   * Or anywhere if you want, but you should revise Python codes.

3. Run Program
   * old/new codes are saved under the folder which location is: `project/[target_project]/[fild_id]/old/test.java`, `project/[target_project]/[fild_id]/new/test.java`


   
