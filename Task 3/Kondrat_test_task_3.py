import pandas as pd
df = pd.read_csv('cars.csv', index_col=False )
print(df)
print

make = input("Please type in maker: ")
model = 'accord'
if (make in df.make.values) :
     print ("{0} {1}price is {2}".format(make,model, df.loc[model,'price'] ))
else:
    print('not found')