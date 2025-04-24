import pandas as pd

df = pd.read_excel(r"C:\Users\diess\Documents\prueba_ventas.xlsx", sheet_name="Totales")

print(df)

# Sumar la columna 'Ventas'
total_ventas = df['Venta 2023'].sum()

# Imprimir el resultado
print(f"Total ventas: {total_ventas}")

result_df = pd.DataFrame({'Total Ventas': [total_ventas]})

with pd.ExcelWriter(r"C:\Users\diess\Documents\prueba_ventas.xlsx", mode='a', engine='openpyxl') as writer:
    result_df.to_excel(writer, sheet_name="Suma", index=False)