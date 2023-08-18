# Luke W. Carani, created 18 August 2023.

import sys
from SurveyAnalysis.__main__ import main

if __name__ == '__main__':
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        # query =  f"Please list all negative feedback " + \
        #     "in a table in markdown and give a single insight for each one, and give a general summary for all. Be concise." 
        # query = 'what is the general sentiment of personnel with "Paygrade of Servicemember"="E5" that took the survey?'
        # query='give me a summary of the overall sentiment of these surveys. \
        #     Be concise. Also give me the complete response of the person \
        #     that had the worst opinion of the Coast Guard, include their employee id number'
        # query = "summarize employee 26's response to question 1"
        query = "summarize how the paygrade E5 employees answered the questions"
    main(query=query)


# query =  "Please list all negative feedback in a table \
# in markdown and get a single insight for each one, and give a general summary for all."
