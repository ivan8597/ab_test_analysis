import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
df = pd.read_csv('../data/AB_Test_revenue_only.csv', sep=';')

print("=== A/B Test Analysis ===")
print(f"Всего строк: {len(df)}")

# Проверка пересечения пользователей
users_in_both = df.groupby('user_id')['variant_name'].nunique()
overlaps = users_in_both[users_in_both > 1]
print(f"Пользователей в обеих группах: {len(overlaps)} ({len(overlaps)/len(df)*100:.2f}%)")

# Очистка данных
clean_df = df.groupby('user_id').filter(lambda x: len(x) == 1)

control = clean_df[clean_df['variant_name'] == 'control']['revenue']
variant = clean_df[clean_df['variant_name'] == 'variant']['revenue']

print(f"\nControl: n={len(control)}, mean={control.mean():.4f}")
print(f"Variant: n={len(variant)}, mean={variant.mean():.4f}")
print(f"Lift: {(variant.mean()/control.mean()-1)*100:.1f}%")

# Статистический тест
t_stat, p_value = stats.ttest_ind(variant, control)
print(f"p-value: {p_value:.6f} → {'Значимо' if p_value < 0.05 else 'Не значимо'}")

# Сохранение очищенных данных
clean_df.to_csv('../data/clean_ab_test.csv', index=False)
print("Анализ завершён!")