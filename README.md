# A/B Test Analysis - Marketpele Feed

## Описание проекта
Анализ A/B-теста для изменения порядка элементов в ленте (группа A vs группа B).

### Основные выводы
- **Группа B (Variant)** показывает **+20.2%** к средней выручке
- Результат статистически значим (p-value < 0.001)
- Обнаружена проблема сплитования (24.37% пользователей попали в обе группы)

## Структура проекта
```
ab_test_analysis/
├── data/                  # Исходные данные
├── scripts/               # Python-скрипты анализа
├── sql/                   # SQL-запросы
├── reports/               # Графики и отчёты
├── notebooks/             # Jupyter notebooks
└── README.md
```

## Как запустить
```bash
pip install pandas scipy matplotlib seaborn
python scripts/analyze_ab_test.py
```

## Ключевые метрики
- RPM, RPS, CTR (Paid & Organic)
- Revenue per user
- Views per session

**Рекомендация:** Запускать изменение в продакшен.