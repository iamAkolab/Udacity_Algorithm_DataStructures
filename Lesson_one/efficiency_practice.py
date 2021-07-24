"""input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)"""

def example1(manatees):
    for manatee in manatees:
        print manatee['name']

def example2(manatees):
    print manatees[0]['name']
    print manatees[0]['age']

def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print manatee_property, ": ", manatee[manatee_property]

def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print oldest_manatee

 


""" Solution """
""" Check your answer to Example 1. Since there is a for loop that iterates over the manatees list, you'll probably need n in your efficiency!
Check your answer to Example 2. Remember to approximate - you should reduce any numbers that you multiply by to 1, and anything you add by to 0.
Check your answer to Example 3. Since there is a for loop that iterates over the manatees list, you'll probably need n in your efficiency!
Check your answer to Example 4. Remember the notation for efficiency: O(x), where x will be some combination of numbers, n, and m."""

