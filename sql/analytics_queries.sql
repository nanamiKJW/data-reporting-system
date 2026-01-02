-- 1. Total transactions by system type
SELECT system_type, COUNT(*) AS total_transactions
FROM transactions
GROUP BY system_type;

-- 2. Failure rate by system
SELECT system_type,
       ROUND(
           SUM(CASE WHEN status = 'failed' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
           2
       ) AS failure_rate_percent
FROM transactions
GROUP BY system_type;

-- 3. Average transaction amount by system
SELECT system_type, ROUND(AVG(amount), 2) AS avg_amount
FROM transactions
GROUP BY system_type;

-- 4. Transactions per hour (monitoring-style)
SELECT substr(timestamp, 1, 13) AS hour, COUNT(*) AS total
FROM transactions
GROUP BY hour
ORDER BY hour;
