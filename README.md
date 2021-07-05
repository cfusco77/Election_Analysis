# Election_Analysis
## Project Overview 
A Colarado board of Election employees has given you the following tasks to complete the election audit of a recent local congressional election. 
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes. 
3. Calculate the total number of votes each candidate recieved. 
4. Calculate the percentage of votes each candidate won.  
5. Determine the winner of the election based on the popular vote. 

## Resources
* Data Source: election_results.csv
* Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Summary 
The analysis of the election shows that:
* There were 369,711 votes cast in the election
* The candidate were:
  * Charles Casper Stockham
  * Diana DeGette  
  * Raymon Anthony Doane 
* The candidate results were:
  Candidate Stockham recieved 23.0% of the vote and 85,213 votes
  Candidate DeGette receved 73.8% of the vote and 272,892 votes
  Candidate Doane recieved 3.1% of the votes and 11,606 votes 

* The winner of the election was: 
  Candidate DeGette won the election with 73.8% of the vote and 272,892 votes. 

## Challenge Overview 
Using the skills attained in this module, conduct a similiar election audit focused on county level results. 
## Challenge Summary 
1. Calculate the total number of votes cast.
2. Get a complete list of counties where votes were cast. 
3. Calculate the total number of votes cast from each county. 
4. Calculate the percentage of votes cast in each county.
5. Determine which county had the largest voter turnout. 

## Summary 
The analysis of the election shows that:
* The counties participating in this election were 
  * Jefferson
  * Denver
  * Arapahoe 
* The number of votes cast in each county were:
  * 38,855 in Jefferson, 10.5% of the total votes 
  * 306,055 in Denver, 82.8% of the total votes 
  * 24,801 in Arapahoe, 6.7% of the total votes 
* The county with the largest turnout was Denver.  

## Election-Analysis Audit Summary and Reccomendations 
This script can be easily modified to use in future elections. First count the total number of votes. Then following the same rubric, create lists of possible options of categorical elements you would wish to aggegate on. Create dictionaries that use categorical dimensions such as candidate_name, county_name, state_name, party_affiliation as the key and votes_cast as the definition. Retrieve vote counts and percentages against any of the aformentioned dimensions. Use logic to declare highest/lowest, winner/loser. 

This script could also easily be applied to elections that have more than 3 candidates or more than three counties. If we were to use this same script for all the counties in the US, my reommendation would be to add code which sorts by vote count descending for readability. 

This analysis could aid in campaigning strategies for candidates the following year. Understanding voter turnout by county would allow candidates to focus their campaigning efforts in areas with higher voter turnout. 

Lastly, candidates might want to see a breakdown of votes earned by county to get a better understanding of what demographics they are resonating with and where they are falling short. 
