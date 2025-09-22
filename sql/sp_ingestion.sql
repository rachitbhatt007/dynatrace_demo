CREATE OR REPLACE PROCEDURE sp_ingestion()
RETURNS STRING
LANGUAGE SQL
AS
$$
BEGIN
    RETURN 'Ingestion completed successfully';
END;
$$;