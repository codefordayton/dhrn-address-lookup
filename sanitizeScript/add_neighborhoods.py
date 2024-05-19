import csv

def find_record_by_parcel_id(parcel_id):
    with open('selected.csv', 'r') as addresses:
        addresses_csv = csv.DictReader(addresses)
        for row in addresses_csv:
            if row['TAXPINNO'] == parcel_id:
                return row
        return None

def id_to_neighborhood(id):
    if id == '1':
        return 'Old North Dayton'
    elif id == '2':
        return 'Five Oaks'
    elif id == '3':
        return 'Wolf Creek'
    elif id == '4':
        return 'Carillon'
    elif id == '5':
        return 'Edgemont'
    elif id == '6':
        return 'Miami Chapel'

with open('../dhrn-functions/packages/dhrn/addresses/addresses.csv', 'r') as addresses:
    addresses_csv = csv.DictReader(addresses)
    with open('addr.csv', 'w') as neighborhoods:
        fieldnames = addresses_csv.fieldnames + ['NEIGHBORHOOD']
        writer = csv.DictWriter(neighborhoods, fieldnames=fieldnames)
        writer.writeheader()
        for row in addresses_csv:
            parcel_id = row['PARCELID']
            record = find_record_by_parcel_id(parcel_id)
            print(f"Searching for parcel {parcel_id}", record)
            row['NEIGHBORHOOD'] = None if record is None else id_to_neighborhood(record['id'])
            writer.writerow(row)
