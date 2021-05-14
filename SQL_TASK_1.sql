WITH
latest_rates as (
	SELECT DISTINCT ON(from_currency) ts, from_currency, rate
	FROM exchange_rates
	WHERE to_currency = 'GBP'
	ORDER BY 2, 1 DESC
),
currency_grouped_transactions as (
	SELECT currency, user_id, sum(amount) as amount
	FROM transactions
	GROUP BY currency, user_id
)

SELECT user_id, SUM(amount * COALESCE(rate, 1)) as total_spent_gbp
FROM currency_grouped_transactions cgt
LEFT JOIN latest_rates lr ON cgt.currency = lr.from_currency
GROUP BY user_id
ORDER BY user_id;
