import argparse
from dbops import DBOps

def main(host, user, passwd, dbname, bank_id, amount, startdate, enddate, function_type):
    dbops = DBOps(host, user, passwd, dbname)
    dbops.create_table('User', 'user')
    dbops.create_table('Bank_Account', 'account')
    dbops.create_table('Transaction', 'transaction')

    """
    I am getting syntax error when reading the sql query from the python app so manually created the stored procedure
    in mysql console, but i am able to call the procedure from the console app
    """
    if function_type == 'check_balance':
        dbops.check_account_balance(bank_id)
    elif function_type == 'withdraw_amount':
        dbops.withdraw_account(bank_id, amount)
    elif function_type == 'check_transations':
        dbops.check_transactions(bank_id, startdate, enddate)
    

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument('--host', '-hh', default='localhost')
    args.add_argument('--user', '-u', default='root')
    args.add_argument('--passwd', '-p', default='manutd87')
    args.add_argument('--dbname', '-d', default='task')
    args.add_argument('--bank_id', '-b', default=int('1'))
    args.add_argument('--amount', '-a', default=float('500'))
    args.add_argument('--startdate', '-s', default='2020-06-01')
    args.add_argument('--enddate', '-e', default='2020-06-05')
    args.add_argument('--function_type', '-f', default='check_balance')
    parsed_args = args.parse_args()
    try:
        main(parsed_args.host, parsed_args.user, parsed_args.passwd, parsed_args.dbname, parsed_args.bank_id, parsed_args.amount, parsed_args.startdate, parsed_args.enddate, parsed_args.function_type)
    except Exception as e:
        print(f'{str(e)}')