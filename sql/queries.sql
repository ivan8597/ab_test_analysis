-- Основные запросы для анализа A/B теста

-- 1. Общая статистика по группам
SELECT 
    variant_name,
    COUNT(DISTINCT user_id) as unique_users,
    COUNT(*) as total_rows,
    AVG(revenue) as avg_revenue,
    SUM(revenue) as total_revenue
FROM ab_test
GROUP BY variant_name;

-- 2. Пользователи в обеих группах (проблема сплитования)
SELECT user_id, COUNT(DISTINCT variant_name) as groups
FROM ab_test
GROUP BY user_id
HAVING groups > 1;