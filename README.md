

# Chirp File Converter For Wouxon KG-Q10H

A versatile Python tool designed to transform Chirp-exported CSV files into a format compatible with the Wouxon KG-Q10H radio. This converter simplifies the process of programming amateur radio frequencies by accurately mapping key repeater data from RepeaterBook exports to the radio's programming requirements. Ideal for ham radio enthusiasts looking to streamline their setup.

This tool converts CSV files from Chirp to a format compatible with the Wouxon KG-Q10H radio, streamlining the process of programming amateur radios by accurately mapping RepeaterBook data for efficient frequency setup.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Pandas Library**: A Python library used for data manipulation and analysis.

## Setup

### Installing Python

1. Download Python from [python.org](https://www.python.org/downloads/).
2. During installation, select "Add Python to PATH".

### Installing Pandas

Use pip to install the Pandas library:

```bash
pip install pandas
```

## How to Use

1. Place your 'RepeaterBook 100 mile.csv' file in the same directory as the script.
2. Open a terminal or command prompt.
3. Navigate to the script's directory:

   ```bash
   cd /path/to/your/script
   ```

4. Execute the script:

   ```bash
   python convert_repeaterbook.py
   ```

Your converted file, 'Output Wouxon KG-Q10H.csv', will be available in the same directory.

## Field Mapping

The following table outlines how fields from RepeaterBook are mapped to the programming format:

| RepeaterBook Field | Test Export Field         | Description                                       |
|-------------------|--------------------------|---------------------------------------------------|
| Name              | Channel_Name             | Identifier of the repeater                        |
| Frequency         | Channel_RxFreq           | Listening frequency                               |
| Duplex + Offset   | Channel_TxFreq           | Calculated transmit frequency                     |
| Tone              | Channel_RxQt             | Receive CTCSS/DCS tone or code                    |
| rToneFreq         | Channel_RxQt             | CTCSS tone for receiving                          |
| cToneFreq         | Channel_TxQt             | CTCSS tone for transmitting                       |
| DtcsCode          | Channel_RxQt / Channel_TxQt | DCS code for Rx/Tx                            |
| Mode              | Channel_Band             | Wide or Narrow band FM                            |

Fields not mentioned are set to default values for typical radio programming.

## Troubleshooting

- **Python Not Recognized**: Make sure Python is added to your PATH. You may need to reinstall Python, ensuring the "Add Python to PATH" option is selected.
- **Issues Installing Pandas**: Check your internet connection and access to [PyPI](https://pypi.org/). If pip is not recognized, follow the [pip installation guide](https://pip.pypa.io/en/stable/installation/).

