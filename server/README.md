# Installation and Running Instructions
1. Install python3
2. Run `pip3 install -r requirements.txt`
3. Install MySQL (for mac `brew install mysql`) works. For others, try here: (https://dev.mysql.com/doc/mysql-getting-started/en/)
4. Start the server: `mysql.server start`. You can stop it with `mysql.server stop`
5. Run `mysql -uroot` and then enter the following command: `CREATE database teaching_assignments;`
6. Run `python3 server.py`. This should create the tables for you. Then you can either insert entries with the mysql command line or through the API functions we've created.
