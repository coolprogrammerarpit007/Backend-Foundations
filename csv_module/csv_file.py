import csv


# first need to open, then read the csv file
# with open('names.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file)
    
#     # writing a new csv file
#     with open('updated_names.csv','w') as new_file:
#         csv_writer = csv.writer(new_file,delimiter='-')
#         for line in csv_reader:
#             csv_writer.writerow(line)


# dictionary reader and writer

with open('names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # for line in csv_reader:
    #     print(line['first_name'])
    
    with open('new_names.csv','w') as new_file:
        field_names = ['first_name','last_name','email']
        csv_writer = csv.DictWriter(new_file,fieldnames=field_names,delimiter='\t')
        csv_writer.writeheader() # write header
        
        for line in csv_reader:
            csv_writer.writerow(line)