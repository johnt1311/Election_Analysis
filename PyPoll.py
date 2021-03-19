# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize the total votes counter
total_votes = 0

#Candidate list
candidate_options = []

# declare the empty diction
candidate_votes = {}

#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1

        #print the candidate name from each row
        candidate_name = row[2]

        #if the candidate does not match any existin candidate...
        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

         # add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    #save the results to our text file
with open(file_to_save, "w") as txt_file:
#print the final vote count to the terminal 
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
    #save the final vote count to the text file
    txt_file.write(election_results)
    
    # Determine the percentage of votes for each candidate by looping through the counts
    #iterate through the candidate list
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do: print out each candidate's name, vote count, and percentage ofvotes to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        #determine winning vote count and candidate
        #determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set the winning_count = votes and winning_perent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name
    #print the winning candidates results to the terminal    
    winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------\n")
    print(winning_candidate_summary)
    #save the winning candidate's results to the text file
    txt_file.write(winning_candidate_summary)