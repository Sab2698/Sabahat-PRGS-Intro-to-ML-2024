
import pandas as pd
import os
os.getcwd()
# Import and identify 'STCOFIPS' as string
nri_data = pd.read_csv('C:/Users/sabahat/Desktop/ML-Folder/Sabahat-PRGS-Intro-to-ML-2024/data/raw/NRI_Table_Counties.csv', dtype={'STCOFIPS': str})
# Subsetting the NRI data to include 'STCOFIPS' and columns ending with '_AFREQ' and '_RISKR'
subset_columns = ['STCOFIPS']  # Start with 'STCOFIPS'
subset_columns.extend([col for col in nri_data.columns if col.endswith('_AFREQ') or col.endswith('_RISKR')])
# Create the subset of the data
nri_subset = nri_data[subset_columns]
# Check the first few rows to confirm
print(nri_subset.head())
# Define the file path to the SVI data
svi_data = pd.read_csv('C:/Users/sabahat/Desktop/ML-Folder/Sabahat-PRGS-Intro-to-ML-2024/data/raw/SVI_2022_US_county.csv', dtype={'FIPS': str})
svi_columns = [
    'ST', 'STATE', 'ST_ABBR', 'STCNTY', 'COUNTY', 'FIPS', 'LOCATION', 'AREA_SQMI', 'E_TOTPOP', 
    'EP_POV150', 'EP_UNEMP', 'EP_HBURD', 'EP_NOHSDP', 'EP_UNINSUR', 'EP_AGE65', 'EP_AGE17', 
    'EP_DISABL', 'EP_SNGPNT', 'EP_LIMENG', 'EP_MINRTY', 'EP_MUNIT', 'EP_MOBILE', 'EP_CROWD', 
    'EP_NOVEH', 'EP_GROUPQ', 'EP_NOINT', 'EP_AFAM', 'EP_HISP', 'EP_ASIAN', 'EP_AIAN', 'EP_NHPI', 
    'EP_TWOMORE', 'EP_OTHERRACE'
]

# Subset the SVI data to include only these columns
svi_subset = svi_data[svi_columns]
 #Merge the NRI and SVI data on the FIPS code
merged_data = pd.merge(nri_subset, svi_subset, left_on='STCOFIPS', right_on='FIPS', how='outer')

# Check the first few rows to confirm the merge
print(merged_data.head())
