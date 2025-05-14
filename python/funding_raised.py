import pandas as pd
import csv

def read_data(file_path : str = "../startup_funding.csv"):
  """Read CSV data and return a DataFrame."""
  data = pd.read_csv(file_path, delimiter=',', quotechar='"', dtype=str)
  return data

def find_data_in_csv(dataframe: pd.DataFrame, column_name: str, value: str) -> pd.DataFrame:
  """Filter dataframe based on column value and return matching rows as a DataFrame.
  Args:
      dataframe (pd.DataFrame): The DataFrame to filter.
      column_name (str): The name of the column to filter by.
      value (str): The value to match in the specified column.
  Returns:
      pd.DataFrame: A DataFrame containing the rows that match the specified column value.
  """
  return dataframe[dataframe[column_name] == value]

class FundingRaised:
  
  @staticmethod
  def where(options = {}, file_path = "../startup_funding.csv"):
    """Filter the CSV data based on the provided options and return the matching rows.
    Args:
        options (dict): A dictionary containing the filter options. The keys can be 'company_name', 'city', 'state', or 'round'.
        file_path (str): The path to the CSV file. Default is "../startup_funding.csv".
    Returns:
        list: A list of dictionaries representing the matching rows in the CSV file.
    """
    csv_data = read_data(file_path=file_path)

    if 'company_name' in options:
      csv_data = find_data_in_csv(csv_data, 'company_name', options['company_name'])

    if 'city' in options:
      csv_data = find_data_in_csv(csv_data, 'city', options['city'])

    if 'state' in options:
      csv_data = find_data_in_csv(csv_data, 'state', options['state'])

    if 'round' in options:
      csv_data = find_data_in_csv(csv_data, 'round', options['round'])

    # Convert the DataFrame to a list of dictionaries
    output = csv_data.to_dict(orient='records')

    return output

  @staticmethod
  def find_by(options, file_path = "../startup_funding.csv"):
    """Find a single record in the CSV data based on the provided options. If multiple records match, return the first one.
    Args:
        options (dict): A dictionary containing the filter options. The keys can be 'company_name', 'city', 'state', or 'round'.
        file_path (str): The path to the CSV file. Default is "../startup_funding.csv".
    Returns:
        dict: A dictionary representing the first matching row in the CSV file.
    Raises:
        RecordNotFound: If no matching record is found.
    """
    all_matches = FundingRaised.where(options, file_path)
    if len(all_matches) > 0:
      return all_matches[0]
    else:
      raise RecordNotFound

class RecordNotFound(Exception):
  pass
