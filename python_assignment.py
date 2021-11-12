import json
rtCounts = [] #empty list for retweeted count
quotes = []   #empty list for quote count
# I tried to create the object for quotes first but it did not work. 
def myAnalysis(data):
        for a in data:  
            rtCounts.append(a["retweet_count"])    
        for b in data:
            if b["is_quote_status"] == True:
                quotes.append("1")
        print("Greta Thunberg has been retweeted " + str(sum(rtCounts)) + " times.")
        print("It is " + str(round((sum(rtCounts))/len(rtCounts), 2)) + " times in average.")
        print("Of all tweets, " + str(len(quotes)) + " of them are quotes.")  
with open('C:/Users/faran/Desktop/assignment_starter/assignment_data/twitter_summaryGretaThunberg.json', 'r') as dataFile:
    raw_data = json.loads(dataFile.read())
    myAnalysis(raw_data)
