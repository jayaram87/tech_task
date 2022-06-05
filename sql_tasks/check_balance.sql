DELIMITER //
DROP PROCEDURE IF EXISTS task.balance;
CREATE PROCEDURE balance(IN id int)
BEGIN
	SELECT User_id, Bank_account_id, Amount from bank_account where Bank_account_id=id;
END //
DELIMITER ;