use task;

insert into USER(User_name, dob, user_email, user_create_date)
values 
('jay1', '1987-03-26', 'jj@ss.com', '2022-06-04'),
('jay11', '1989-03-26', 'jj1@ss.com', '2019-06-04'),
('jay11', '1988-03-26', 'jj11@ss.com', '2020-06-04'),
('jay111', '1990-03-26', 'jj111@ss.com', '2021-06-04')

insert into Bank_Account(User_id, Bank_account_nbr, is_user_active, Amount)
values 
(1, 'xxx1', True, 20000),
(1, 'xxx2', True, 10000),
(2, 'xxx3', True, 50000),
(3, 'xxx4', True, 500)

insert into Transaction(User_id, Bank_account_id, Transaction_date, Withdrawn_Amount)
values 
(1, 1, '2022-06-04', 5000)