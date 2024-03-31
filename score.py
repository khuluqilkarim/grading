import pandas as pd

# Data JSON
data_json = [{"nama":"khuluqil karim","total_score":"135"},{"nama":"jihan","total_score":"20"}]

# Konversi JSON menjadi DataFrame
df = pd.DataFrame(data_json)

# Tampilkan DataFrame sebagai tabel
print(df)
