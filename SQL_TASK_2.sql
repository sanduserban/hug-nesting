WITH
    ordered_rates AS (
      SELECT ts, from_currency, to_currency, rate
        FROM exchange_rates er
        UNION (SELECT '1970-01-01 00:00:00', 'GBP', 'GBP', 1)
        ORDER BY ts DESC
    ),
    converted_tx AS (
      SELECT tr.ts, tr.user_id, tr.amount * (
            SELECT rate
              FROM ordered_rates orr
              WHERE tr.currency = orr.from_currency AND orr.to_currency = 'GBP' AND orr.ts <= tr.ts
              LIMIT 1
        ) AS gbp
        FROM transactions tr)

SELECT user_id, SUM(gbp) as total_spent_gbp
  FROM converted_tx
  GROUP BY user_id
  ORDER BY user_id;
