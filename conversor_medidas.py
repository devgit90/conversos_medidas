import pandas as pd

def cm_a_pulgadas(cm):
    return cm / 2.54

df = pd.read_excel("muebles_medidas.xlsx")

df["Pulgadas"] = df["Centimetros"].apply(cm_a_pulgadas)

df.to_excel("muebles_medidas_convertidas.xlsx", index=False)

print("Conversion completa y guardada en un nuevo archivo llamado muebles_medidas_convertidas_xlsx")