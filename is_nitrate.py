import pandas as pd

def is_nitrate_present(csv_file):
    """
    Checks for the presence of nitrate in the Raman spectra using a CSV file.
    Args:
        csv_file: A CSV file containing the Raman spectra data, including a 'Wavenumber' column.
    Returns:
        1 if nitrate is present, 0 otherwise.
    """
    # Read the CSV file into a DataFrame.
    data = pd.read_csv(csv_file)

    # Identify the characteristic peaks for nitrate in the Raman spectra.
    nitrate_peaks = [1387, 1048, 724, 1387.41, 1372.92]

    # Check for the presence of these peaks in the 'Wavenumber' column of the DataFrame.
    if data['Wavenumber'].isin(nitrate_peaks).any():
        return 1

    # If none of the characteristic peaks are present, then nitrate is not present.
    return 0

# Example usage:
result = is_nitrate_present('data/isNitrate - Sheet1.csv')
print(result)
