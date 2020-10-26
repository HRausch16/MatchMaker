INTRODUCTION = '''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The purpose of this application is to see how 
compatable we are. The instructions are simple:
After each statement, you will be prompted to 
enter a number. The number should be between 1 
and 5. 1 means that you strongly disagree, 2 
means that you disagree, 3 means that you are 
neutral, 4 means that you agree, and 5 means 
that you strongly agree!
Once you've gotten through all 5 comments, 
you'll learn your compatability! The goal is 
100%!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
QUESTION = [
    'Chicago Blackhawks hockey is the best! ',
    'Superman is the best superhero! ',
    'Spaghetti is the best food on Earth! ',
    'The best book series is The Witcher series! ',
    'JoJos Bizarre Adventure is the greatest anime! ',
]
DESIRED_RESPONSE = [
    5, 
    2, 
    1, 
    4, 
    5, 
]
QUESTION_WEIGHT = [
    0.3,
    0.02,
    0.01,
    0.22,
    0.45
]
MAX_SCORE = 5 * len(QUESTION)
print(INTRODUCTION)
response = []
compatibility = []
for i in range(len(QUESTION)):
    userResponse = int(input(QUESTION[i]))
    if userResponse > 5 or userResponse < 1:
        print('Please enter a number between 1 and 5.\n')
        userResponse = int(input(QUESTION[i]))
    response.append(userResponse)

    questionCompatability = 5 - abs(userResponse - DESIRED_RESPONSE[i])

    compatibility.append(questionCompatability)

    print('Question %d compatability %d\n' % (i+1, questionCompatability))

totalCompatability = 0
for c in compatibility:
    totalCompatability += c

totalCompatability *= 100 / MAX_SCORE
print('Total Compatability: %d\n' % (totalCompatability))
if totalCompatability < 50:
    print('Sorry, I do not see us being compatable...')
elif totalCompatability > 50 and totalCompatability < 80:
    print('We are definitely going to be friends.')
else:
    print('How about we go out some time?')