import pandas as pd

# Function to calculate transmit frequency based on the repeater's frequency, offset, and duplex settings
def calculate_tx_frequency(freq, offset, duplex):
    if duplex == '-':
        return freq + offset
    elif duplex == '+':
        return freq - offset
    else:
        return freq  # For simplex or unspecified duplex, return the original frequency

# Function to determine the appropriate CTCSS/DCS tones
def determine_ctcss_dcs(row):
    if row['Tone'] == 'Tone':
        return row['rToneFreq'], row['cToneFreq']
    elif row['Tone'] == 'DTCS':
        return row['DtcsCode'], row['DtcsCode']  # Assuming the same code for Rx and Tx
    else:
        return 'OFF', 'OFF'

def main():
    # Load the RepeaterBook file
    repeaterbook_df = pd.read_csv('ReapeterBoook_Export.csv')

  # Print column names to help debug
    print("Column names in the CSV file:", repeaterbook_df.columns.tolist())

    # Create a new DataFrame for the converted data
    converted_data = pd.DataFrame()

    # Calculate transmit frequency and apply CTCSS/DCS settings
    converted_data['Channel_RxFreq'] = repeaterbook_df['Frequency']
    converted_data['Channel_TxFreq'] = repeaterbook_df.apply(lambda row: calculate_tx_frequency(row['Frequency'], row['Offset'], row['Duplex']), axis=1)
    converted_data[['Channel_RxQt', 'Channel_TxQt']] = repeaterbook_df.apply(determine_ctcss_dcs, axis=1, result_type='expand')
    
    # Set additional default values and map directly translatable fields
    converted_data['Channel_Name'] = repeaterbook_df['Name']
    converted_data['Channel_Power'] = 'High'
    converted_data['Channel_Band'] = repeaterbook_df['Mode'].apply(lambda x: 'Wide' if x == 'FM' else 'Narrow')
    converted_data['Channel_MuteMode'] = 'QT'
    converted_data['Channel_Scream'] = 'OFF'
    converted_data['Channel_ScanAdd'] = 'ON'
    converted_data['Channel_Compand'] = 'OFF'
    converted_data['Channel_AM'] = 'OFF'
    converted_data['Channel_FAV'] = 'OFF'
    converted_data['Channel_SendLoc'] = 'OFF'
    converted_data['Channel_CallCodeSn'] = 1
    converted_data['Channel_SN'] = range(1, len(converted_data) + 1)

    # Save the converted data to a CSV file
    output_filename = 'Output Wouxon KG-Q10H.csv'
    converted_data.to_csv(output_filename, index=False)
    print(f"File converted and saved as '{output_filename}'")

if __name__ == "__main__":
    main()
