import csv 
def creat_dict():
    with open('contacts.csv', mode='r') as infile:
        reader =csv.reader('infile')
        with open('mycontact.csv',mode='w') as outfile:
            writer=csv.writer(outfile)
            mydict={rows[0]:rows[1] for rows in reader}


if __name__=="__main__":
    creat_dict()