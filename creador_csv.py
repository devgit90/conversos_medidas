import pandas as pd

data = {
    "Piezas": ["Pata","Tablero", "Puerta", "Estante", "Panel Lateral"],
    "Centimetros":[40,120,60,30,180]
}

df = pd.DataFrame(data)

df.to_csv("muebles_medidas.csv", index=False)