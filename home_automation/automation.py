# import csv

# with open('names.csv','r',encoding="utf-8-sig") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
    
#     with open('updated_clients.csv','w') as new_file:
#         field_names = ['first_name','last_name','mobile_number']
#         csv_writer = csv.DictWriter(new_file,fieldnames=field_names)
#         csv_writer.writeheader()
    
#         for line in csv_reader:
#             if line['Mobile Phone'] == '':
#                 line['Business Phone'] = line['Mobile Phone']



# import csv
# import sys

# with open('names.csv', 'r', encoding="utf-8-sig") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
    

#     with open('updated_clients.csv', 'w', newline='', encoding="utf-8") as new_file:
#         field_names = ['display_name', 'mobile_number']
#         csv_writer = csv.DictWriter(new_file, fieldnames=field_names)
#         csv_writer.writeheader()

#         for line in csv_reader:
            
#             # Extract fields from input CSV
#             first_name = line.get('First Name', '').strip()
#             last_name = line.get('Last Name', '').strip()
#             mobile = line.get('Mobile Phone', '').strip()
#             business = line.get('Home Phone', '').strip()
            
#             display_name = ''
#             if first_name or last_name:
#                 display_name = first_name + last_name

#             # Apply your logic
#             if mobile:
#                 mobile_number = mobile
#             elif business:
#                 mobile_number = business
#             else:
#                 mobile_number = 'N/A'  # If both are empty

#             # Write to the new CSV
#             csv_writer.writerow({
#                 'display_name': display_name,
#                 'mobile_number': mobile_number
#             })
import csv

def clean_mobile(num):
    num = num.strip()
    if len(num) == 12 and num.startswith("91"):
        return num[2:]   
    return num

with open('names.csv', 'r', encoding="utf-8-sig") as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('updated_clients.csv', 'w', newline='', encoding="utf-8") as new_file:
        field_names = ['display_name', 'mobile_number']
        csv_writer = csv.DictWriter(new_file, fieldnames=field_names)
        csv_writer.writeheader()

        for line in csv_reader:
            first_name = line.get('First Name', '').strip()
            last_name = line.get('Last Name', '').strip()
            mobile = line.get('Mobile Phone', '').strip()
            business = line.get('Home Phone', '').strip()
            
            display_name = ''
            if first_name or last_name:
                display_name = first_name + last_name

            if mobile:
                mobile_number = clean_mobile(mobile)
            elif business:
                mobile_number = clean_mobile(business)
            else:
                mobile_number = None

            csv_writer.writerow({
                'display_name': display_name,
                'mobile_number': mobile_number
            })
