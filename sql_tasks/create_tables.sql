use task;

create table if not exists USER(
    User_id int PRIMARY KEY auto_increment,
	User_name Varchar(50),
    dob date,
    user_email Varchar(50),
    user_create_date date
);

create table if not exists Bank_Account(
	Bank_account_id int PRIMARY KEY auto_increment,
    User_id INT,
    CONSTRAINT UseridFk FOREIGN KEY (User_id) REFERENCES User(User_id) ON UPDATE CASCADE ON DELETE CASCADE,
    Bank_account_nbr Varchar(50),
    is_user_active bool,
    Amount float
);

create table if not exists Transaction(
    transaction_id int PRIMARY KEY auto_increment,
	User_id INT,
    Bank_account_id int,
    CONSTRAINT UseridtransFk FOREIGN KEY (User_id) REFERENCES User(User_id) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT BankidtransFk FOREIGN KEY (Bank_account_id) REFERENCES Bank_Account(Bank_account_id) ON UPDATE CASCADE ON DELETE CASCADE,
    Transaction_date Date,
    Withdrawn_Amount float
)