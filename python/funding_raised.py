import pandas as pd

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
    csv_data = pd.read_csv(file_path, delimiter=',', quotechar='"', dtype=str)

    for category in ['company_name', 'city', 'state', 'round']:
      if category in options:
        # Convert the column to string type to avoid comparison issues
        csv_data = csv_data[csv_data[category] == options[category]]

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
