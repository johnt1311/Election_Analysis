#The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote

import csv
import os

#assign a variable for the file to load and the path
#file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file.
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data:
    #to do: read and analyze the data her
    file_reader = csv.reader(election_data)

    #print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
    #print the header row
    headers = next(file_reader)
    print(headers)
    

#Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")
#open the file to write as a text file
#outfile = open(file_to_save, "w")
#write some data to the file
#outfile.write("Hello World")
with open(file_to_save, "w") as txt_file:

    #write some data to the file
    #txt_file.write("Hello World")
    #write these counties to the file
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson")
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson")


#close the file
#outfile.close()



#close the file
election_data.close()
