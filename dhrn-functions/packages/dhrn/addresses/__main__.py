import csv 

def main(args):
      address = args.get("address")
      file, csv_file = open_csv()
      results = search_csv(csv_file, address)
      file.close()
      return {"body": results}

# function that opens a csv file and returns a handle to it.
def open_csv():
    f = open('addresses.csv', 'r')
    csv_file = csv.DictReader(f)
    return f, csv_file

# function that takes a line and returns a json object
def line_to_json(parts):
    return {
        "parcel": parts['PARCELID'],
        "owner": parts['OWNERNAME'],
        "nbhd": parts['NBHD'],
        "luc": parts['LUC'],
        "delqamount": parts['HLF1DELQ'],
        "zip": parts['ZIP'],
        "address": parts['LOCATION'],
        "neighborhood": parts['NEIGHBORHOOD']
    }

# function that searches a csv file for a passed string. partial matches are allowed.
def search_csv(f, search_str):
    search_str = search_str.upper()
    results = []
    for row in f:
        if search_str in row['LOCATION']:
            results.append(line_to_json(row))
        if len(results) >= 10:
            break
    return results

