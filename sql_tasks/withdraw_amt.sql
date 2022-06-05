DELIMITER //
DROP PROCEDURE IF EXISTS task.withdraw;
CREATE PROCEDURE withdraw(IN bank_id int, amt float)
BEGIN
	DECLARE acc_balance float;
    DECLARE userid INT;
    set @date = cast(NOW() as datetime);
	SELECT Amount into acc_balance from Bank_Account where Bank_account_id=bank_id;
    SELECT User_id into userid from Bank_Account where Bank_account_id=bank_id;
    if acc_balance > 5000 then
		START transaction;
			UPDATE Bank_Account
            SET Amount = Amount - amt
            where Bank_account_id = bank_id;

            INSERT into Transaction(User_id, Bank_account_id, Transaction_date, Withdrawn_Amount) values(userid, bank_id, @date, amt);
        COMMIT;
	END IF;
END //
DELIMITER ;