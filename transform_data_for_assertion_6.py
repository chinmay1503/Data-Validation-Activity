import pandas as pd

#Read data from file
df = pd.read_csv(r'.\Oregon Hwy 26 Crash Data for 2019 - Crashes on Hwy 26 during 2019.csv')
print(df)

#Create dataframes for each record type
CrashesDF = df[df['Record Type'] == 1]
VehiclesDF = df[df['Record Type'] == 2]
ParticipantsDF = df[df['Record Type'] == 3]

CrashesDF = CrashesDF.dropna(axis=1,how='all')
VehiclesDF = VehiclesDF.dropna(axis=1,how='all')
ParticipantsDF = ParticipantsDF.dropna(axis=1,how='all')

# Get all unique crash ids
UniqueCrashIds = VehiclesDF['Crash ID'].drop_duplicates()

# Create a crash Id to Vehicle Count map based on unique vehicle ids mentioned.
idToVehicleMap = {}
for index, value in UniqueCrashIds.items():
    uniqueVechilesCountPerId = VehiclesDF.loc[VehiclesDF['Crash ID'] == value    , 'Vehicle ID']
    idToVehicleMap[value] = uniqueVechilesCountPerId.drop_duplicates().count()
	
	
# 
for index, value in UniqueCrashIds.items():
    count = CrashesDF.loc[CrashesDF['Crash ID'] == value    , 'Total Vehicle Count']
    if idToVehicleMap.get(value) == int(count.tolist()[0]):
        print('isValid')
    else:
        print("For crash id {0}, count value is {1}, but in vehicle column value is {2}".format(value, idToVehicleMap.get(value), int(count.tolist()[0])))
        CrashesDF.loc[CrashesDF['Crash ID'] == value    , 'Total Vehicle Count'] = idToVehicleMap.get(value)