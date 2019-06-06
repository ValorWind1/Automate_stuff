import random
"""
creates quizees with questions and answers in random order along with the answer key
"""

Us_states = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe',
             'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
             'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


#generating 35 quiz files
for quiznum in range(35):
    # creating quiz
    quizfile = open("capitalsquiz%s.txt" % (quiznum + 1 ),"w")
    answer_file = open("capital_answer%s.txt" % (quiznum + 1),"w")

    # writing header for quiz
    quizfile.write("Name:\n\nDate:\n\nPeriod:\n\n")
    quizfile.write((" "* 20)+ "State Capitals Quiz ( Form %s)" % (quiznum + 1 ))
    quizfile.write("\n\n")

    #shuffle order states
    states = list(Us_states.keys())
    random.shuffle(states)


    # looping through 50 states and a question for each
    for questionNum in range (50):
        # get right and wrong answers
        correct = Us_states[states[questionNum]] # creating the corerct answers
        wrong = list(Us_states.values()) # wrong are more difficult , we duplicate the values
        del wrong[wrong.index(correct)]  # delete the correct answers
        wrong = random.sample(wrong,3) # select 3 random values from it
        options = wrong + [correct] # gen the 4 options
        random.shuffle(options) # shuffle them


    #loop though all 50 states making a questions for each
    # write the question and the answer options to the quiz file
        quizfile.write("%s. What is the capital of %s?\n" %(questionNum +1,states[questionNum]))

        for i in range(4):
            quizfile.write(" %s. %s\n" % ("ABCD"[i],options[i]))
        quizfile.write("\n")

        # write the answer key to a file
        answer_file.write("%s. %s\n" % (questionNum+1,"ABCD"[options.index(correct)]))

quizfile.close()
answer_file.close()





