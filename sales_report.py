# """
# sales_report.py - Generates sales report showing the total number
#                   of melons each sales person sold.
# """

# salespeople = []    #empty list for sales peoples names
# melons_sold = []    #empty lists for number of melons sold

# f = open("sales-report.txt")        #opens sales report file
# for line in f:                      #for each line in sales report...
#     line = line.rstrip()            #strip away empty space
#     entries = line.split("|")       #split each line by pipe, add to list entries
#     salesperson = entries[0]        #the first item in entries, add to list salesperson
#     melons = int(entries[2])        #the third item in list, add to list melons

#     if salesperson in salespeople:      #check if salesperson in salespeople: yes
#         position = salespeople.index(salesperson)   #checks position in list
#         melons_sold[position] += melons     #check melons sold, move to same position as sales people, that equals melons sold and add on melons found
#     else:                               #if not in list
#         salespeople.append(salesperson) # add person to sales people list
#         melons_sold.append(melons)      # add melons to melons sold list


# for i in range(len(salespeople)):       #iterate through sales people list
#     print("{} sold {} melons".format(salespeople[i], melons_sold[i])) #print melons


"""
This code depends on the list salespeople being in the same order as melons sold.
If ether list is wrong, the data will not match the sales-report.txt. 
"""

#dictionary version
sales_report_dict = {}

f = open("sales-report.txt")        #opens sales report file
for line in f:                      #for each line in sales report...
    line = line.rstrip()            #strip away empty space
    entries = line.split("|")       #split each line by pipe, add to list entries
    salesperson = entries[0]        #the first item in entries, add to list salesperson
    amount_made = entries [1]       #saves the amount the salesperson made
    melons = int(entries[2])        #the third item in list, add to list melons

    if salesperson in sales_report_dict:      #check if salesperson in salespeople
        sales_report_dict[salesperson] += melons #adds melons to the salespersons melon count

    else:                               #if not in list
        sales_report_dict[salesperson] = melons #make a new key with that person and value is their melons
   
for salesperson, melon_count in sales_report_dict.items():
    print("{} sold {:,} melons".format(salesperson, melon_count))
    


# print_sales_report("sales-report.txt")





