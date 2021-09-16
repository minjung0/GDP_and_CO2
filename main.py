import pandas as pd
import matplotlib.pyplot as plt

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
plt.plot(df_new.mortality, df_new.gdp)
plt.title("This is my plot")
plt.show()
