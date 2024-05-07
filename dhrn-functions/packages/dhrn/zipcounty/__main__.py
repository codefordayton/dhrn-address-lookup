import csv 

def main(args):
      zip = args.get("zip")
      file, csv_file = open_csv()
      results = search_csv(csv_file, zip)
      file.close()
      return {"body": results}

# function that opens a csv file and returns a handle to it.
def open_csv():
    f = open('zips.csv', 'r')
    csv_file = csv.DictReader(f)
    return f, csv_file

# function that takes a zip code and returns the county using an exact match
def search_csv(f, zipcode):
    for row in f:
        if zipcode == row['zip']:
           return {'result': row['county_name']}
    return {'result': None}