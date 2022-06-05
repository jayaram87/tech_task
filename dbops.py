import mysql.connector as connection
import random
import names
from datetime import datetime
import os

class DBOps:
    def __init__(self, host, user, passwd, dbname):
        self.host = host
        self.user = user
        self.pwd = passwd
        self.db = dbname

    def __connection(self):
        try:
            conn = connection.connect(host=self.host, user=self.user, passwd=self.pwd, database=self.db, auth_plugin='mysql_native_password' ,use_pure=True)
        except:
            try:
                conn = connection.connect(host=self.host, user=self.user, passwd=self.pwd, auth_plugin='mysql_native_password', use_pure=True)
                query = 'SHOW DATABASES;'
                cursor = conn.cursor()
                cursor.execute(query)
                if self.db not in [i[0] for i in cursor.fetchall()]:
                    query = 'CREATE DATABASE {}'.format(self.db)
                    cursor = conn.cursor()
                    cursor.execute(query)
                    conn.close()
                    print(f'{self.db} created')
                else:
                    print("Unable to create a db and connect")
                conn = connection.connect(host=self.host, user=self.user, passwd=self.pwd, auth_plugin='mysql_native_password', use_pure=True)
            except Exception as e:
                print(f'{str(e)}')
        finally:
            if conn.is_connected():
                return conn

    def create_table(self, table_name, table_type):
        conn = self.__connection()
        cursor = conn.cursor()
        cursor.execute('USE {}'.format(self.db))
        cursor = conn.cursor()
        cursor.execute('SHOW TABLES;')
        if table_name not in [i[0] for i in cursor.fetchall()]:
            try:
                cursor = conn.cursor()
                if table_type == 'user':
                    query = f"""create table if not exists {self.db}.{table_name}(
                            User_id int PRIMARY KEY auto_increment,
	                        User_name Varchar(50),
                            dob date,
                            user_email Varchar(50),
                            user_create_date date);
                        """
                elif table_type == 'account':
                    query = f"""
                    create table if not exists {self.db}.{table_name}(
	                Bank_account_id int PRIMARY KEY auto_increment,
                    User_id INT,
                    CONSTRAINT UseridFk FOREIGN KEY (User_id) REFERENCES User(User_id) ON UPDATE CASCADE ON DELETE CASCADE,
                    Bank_account_nbr Varchar(50),
                    is_user_active bool,
                    Amount float);
                    """
                elif table_type == 'transaction':
                    query = f"""
                    create table if not exists {self.db}.{table_name}(
                    transaction_id int PRIMARY KEY auto_increment,
	                User_id INT,
                    Bank_account_id int,
                    CONSTRAINT UseridtransFk FOREIGN KEY (User_id) REFERENCES User(User_id) ON UPDATE CASCADE ON DELETE CASCADE,
                    CONSTRAINT BankidtransFk FOREIGN KEY (Bank_account_id) REFERENCES Bank_Account(Bank_account_id) ON UPDATE CASCADE ON DELETE CASCADE,
                    Transaction_date Date,
                    Withdrawn_Amount float);
                    """
                else:
                    print('please create the 3 tables')
                cursor.execute(query)
                cursor.close()
            except Exception as e:
                print(f'incorrect sql query {str(e)}')

    def insert_row(self, table_name, table_type):
        conn = self.__connection()
        cursor = conn.cursor()
        cursor.execute('USE {}'.format(self.db))
        cursor = conn.cursor()
        cursor.execute('SHOW TABLES;')
        if table_name not in [i[0] for i in cursor.fetchall()]:
            try:
                cursor = conn.cursor()
                if table_type == 'user':
                    query = f"""insert into {self.db}.{table_name}(User_name, dob, user_email, user_create_date)
                                values 
                                ('{names.get_full_name()}', '1987-03-26', 'kkk@ggg.com', '2022-05-05');
                        """
                    print(query)
                elif table_type == 'account':
                    query = f"""insert into Bank_Account(User_id, Bank_account_nbr, is_user_active, Amount)
                                values 
                                (1, '{names.get_full_name()}', True, {random.randint(2000,20000)});
                    """
                elif table_type == 'transaction':
                    query = f"""insert into Transaction(User_id, Bank_account_id, Transaction_date, Withdrawn_Amount)
                                values 
                                ({random.randint(1,4)}, {random.randint(1,4)}, '{datetime.now()}', 500)
                    """
                cursor.execute(query)
                cursor.close()
            except Exception as e:
                print(f'incorrect sql query {str(e)}')

    def check_account_balance(self, bank_id):
        conn = self.__connection()
        cursor = conn.cursor()
        cursor.execute('USE {}'.format(self.db))
        try:
            '''with open(os.path.join(os.getcwd(), 'sql_tasks', 'check_balance.sql'), 'r') as f:
                query = f.read()
            cursor.execute(query)
            cursor.close()
            cursor = conn.cursor()'''
            cursor.callproc('balance', (f'{bank_id}', ))
            for result in cursor.stored_results():
                print(result.fetchall())
            cursor.close()
        except Exception as e:
            print(f'{str(e)}')

    def withdraw_amt(self, bank_id, amount):
        conn = self.__connection()
        cursor = conn.cursor()
        cursor.execute('USE {}'.format(self.db))
        try:
            '''with open(os.path.join(os.getcwd(), 'sql_tasks', 'check_balance.sql'), 'r') as f:
                query = f.read()
            cursor.execute(query)
            cursor.close()
            cursor = conn.cursor()'''
            cursor.callproc('withdraw', (f'{bank_id}', f'{amount}', ))
            for result in cursor.stored_results():
                print(result.fetchall())
            cursor.close()
        except Exception as e:
            print(f'{str(e)}')


    def check_transactions(self, bank_id, startdate, enddate):
        conn = self.__connection()
        cursor = conn.cursor()
        cursor.execute('USE {}'.format(self.db))
        try:
            '''with open(os.path.join(os.getcwd(), 'sql_tasks', 'check_balance.sql'), 'r') as f:
                query = f.read()
            cursor.execute(query)
            cursor.close()
            cursor = conn.cursor()'''
            cursor.callproc('check_transactions', (f'{bank_id}', f'{startdate}', f'{enddate}'))
            for result in cursor.stored_results():
                print(result.fetchall())
            cursor.close()
        except Exception as e:
            print(f'{str(e)}')


