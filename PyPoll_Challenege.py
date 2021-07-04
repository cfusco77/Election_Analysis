# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
#County options and county votes 
county_options = []
county_votes = {} 
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Track the largest county turnout, county vote count, and percentage. 
largest_county_turnout = ""
largest_county_count = 0 
largest_county_percentage = 0 

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        #Get the county name from each row. 
        county_name = row[1] 
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        if county_name not in county_options:
            #Add the county name to the county list. 
            county_options.append(county_name) 
            #And begin tracking that candidate's voter count. 
            county_votes[county_name] = 0 
        #Add a vote to that candidate's count 
        county_votes[county_name] += 1 

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)  

        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
    
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)

    for county_name in county_votes:
        #Retrieve vote count and percentage 
        votes = county_votes[county_name]
        vote_percentage = float(votes)/ float(total_votes)*100
        county_results = (
            f"{county_name}: {vote_percentage: .1f}% ({votes:,})\n")

        #Print each county's voter count and percentage to the terminal 
        print(county_results) 

        #Save the county results to the txt file. 
        txt_file.write(county_results)

        #Determine largest county count, largest percentage, and largest county turnout. 
        if (votes > largest_county_count) and (vote_percentage > largest_county_percentage):
            largest_county_count = votes
            largest_county_turnout = county_name
            largest_county_percentage = vote_percentage
        #Print the county results to the terminal 
        largest_county_summary = ( 
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county_turnout}\n"
        f"Largest Country Vote Count: {largest_county_count:,}\n"
        f"Largest County Percentage: {largest_county_percentage:.1f}%\n"
        f"-------------------------\n")
    print(largest_county_summary)

    txt_file.write(largest_county_summary)