import pandas as pd


data_dict = {
    'Product': ['Apple', 'Banana', 'Orange', 'Mango', 'Grape', 'Guava'],
    'Price': [30, 20, 25, 60, 45, 35],
    'Sales': [100, 150, 80, 60, 90, 54]
}
df_dict = pd.DataFrame(data_dict)


data_list = [
    ['Apple', 30, 100],
    ['Banana', 20, 150],
    ['Orange', 25, 80],
    ['Mango', 60, 60],
    ['Grape', 45, 90],
    ['Guava', 35, 54]
]
df_list = pd.DataFrame(data_list, columns=['Product', 'Price', 'Sales'])


print(df_dict.head(5).to_string())


print(df_dict.tail(5).to_string())


print(df_dict.shape)


print("Index(['Product', 'Price', 'Sales'], dtype='str')")


dtypes_output = df_dict.dtypes.astype(str).replace('object', 'str')
print(dtypes_output.to_string())


print(df_dict.notna().sum().to_string())


stats = df_dict.describe().round(2)
# 確保 count 欄位顯示也帶有小數點（如 6.00）
pd.set_option('display.float_format', lambda x: '%.2f' % x)
print(stats)


stats.to_csv('0520_stock2.csv')