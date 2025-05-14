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
    with open("../startup_funding.csv", "rt") as csvfile:
      data = csv.reader(csvfile, delimiter=',', quotechar='"')
      # skip header
      next(data)
      csv_data = []
      for row in data:
        csv_data.append(row)

    if 'company_name' in options:
      for row in csv_data:
        if row[1] == options['company_name']:
          mapped = {}
          mapped['permalink'] = row[0]
          mapped['company_name'] = row[1]
          mapped['number_employees'] = row[2]
          mapped['category'] = row[3]
          mapped['city'] = row[4]
          mapped['state'] = row[5]
          mapped['funded_date'] = row[6]
          mapped['raised_amount'] = row[7]
          mapped['raised_currency'] = row[8]
          mapped['round'] = row[9]
          return mapped

    if 'city' in options:
      for row in csv_data:
        if row[4] == options['city']:
          mapped = {}
          mapped['permalink'] = row[0]
          mapped['company_name'] = row[1]
          mapped['number_employees'] = row[2]
          mapped['category'] = row[3]
          mapped['city'] = row[4]
          mapped['state'] = row[5]
          mapped['funded_date'] = row[6]
          mapped['raised_amount'] = row[7]
          mapped['raised_currency'] = row[8]
          mapped['round'] = row[9]
          return mapped

    if 'state' in options:
      for row in csv_data:
        if row[5] == options['state']:
          mapped = {}
          mapped['permalink'] = row[0]
          mapped['company_name'] = row[1]
          mapped['number_employees'] = row[2]
          mapped['category'] = row[3]
          mapped['city'] = row[4]
          mapped['state'] = row[5]
          mapped['funded_date'] = row[6]
          mapped['raised_amount'] = row[7]
          mapped['raised_currency'] = row[8]
          mapped['round'] = row[9]
          return mapped

    if 'round' in options:
      for row in csv_data:
        if row[9] == options['round']:
          mapped = {}
          mapped['permalink'] = row[0]
          mapped['company_name'] = row[1]
          mapped['number_employees'] = row[2]
          mapped['category'] = row[3]
          mapped['city'] = row[4]
          mapped['state'] = row[5]
          mapped['funded_date'] = row[6]
          mapped['raised_amount'] = row[7]
          mapped['raised_currency'] = row[8]
          mapped['round'] = row[9]
          return mapped

    raise RecordNotFound

class RecordNotFound(Exception):
  pass
