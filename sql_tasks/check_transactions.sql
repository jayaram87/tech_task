DELIMITER //
DROP PROCEDURE IF EXISTS task.check_transactions;
CREATE PROCEDURE check_transactions(IN userid int, startdate Date, enddate Date)
BEGIN
    set @startdate = cast(startdate as datetime);
    set @enddate = cast(enddate as datetime);
	SELECT * from Transaction where User_id=userid and Transaction_date >= @startdate AND Transaction_date <= @enddate;
END //
DELIMITER ;