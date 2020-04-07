import pandas as pd
import quandl

quandl.ApiConfig.api_key = "WLJMuhZbyKPneqQNBEAZ"
mydata = quandl.get("WIKI/GOOGL")

print(mydata.head())