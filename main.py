import pandas as pd
import matplotlib.pyplot as plt
from pyparsing import col

df = pd.read_csv("/Users/Jung/GDP_and_CO2/wdi_small_tidy_2015.csv")

df.head()
df.columns

df_new = df[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]

df_new.columns = ["mortality", "gdp", "country"]
<<<<<<< HEAD
plt.plot(df_new.mortality, df_new)
plt.title"this is my plot")
plt.show()

=======
plt.plot(df_new.mortality, df_new.gdp)
plt.title("This is my plot")
plt.show()
>>>>>>> fd5394eff5c87be06fce6250de082511f01190c7
