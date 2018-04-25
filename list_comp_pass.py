## Strings of the kinds of characters!!
UPPER = "QWERTYUIOPASDFGHJKLZXCVBNM"
LOWER = "qwertyuiopasdfghjklzxcvbnm"
NUMS = "1234567890"
SYMS = ".?!&#,;:-_*"


print "Enter your password idea"
pword = raw_input()

def  min_thresh(pword):
    uppers = [True if x in UPPER else False for x in pword] #List of booleans repping uppercase letters
    lowers = [True if x in LOWER else False for x in pword] # " " lowercase letters
    nums = [True if x in NUMS else False for x in pword] # " " numbers
    return any(uppers) and any(lowers) and any(nums) # Run OR statements over all of the lists, then AND all of those together to make sure everything is true.

def pass_strength(pword):
    upper_score = [True for x in pword if x in UPPER] #Empty list if no upper case,  a list of >0 Trues otherwse
    lower_score = [True for x in pword if x in LOWER] # " " but with lower case
    num_score = [True for x in pword if x in NUMS] # " " but with numbers
    sym_score = [True for x in pword if x in SYMS] # " " but with symbols
    score = 0 # Your total score
    scores = [upper_score, lower_score, num_score, sym_score] # All of the boolean lists
    for i in scores: #iterate through all 4 lists
        score += 2.5 if any(i) else 0 #add 2.5 if that character was found
    return score

print "Binary feedback: this is a good score."
print min_thresh(pword)
print "\n"
print "The strength is: "
print pass_strength(pword)
