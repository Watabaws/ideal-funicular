UPPER = "QWERTYUIOPASDFGHJKLZXCVBNM"
LOWER = "qwertyuiopasdfghjklzxcvbnm"
NUMS = "1234567890"
SYMS = ".?!&#,;:-_*"


print "Enter your password idea"
pword = raw_input()

def  min_thresh(pword):
    uppers = [True if x in UPPER else False for x in pword]
    lowers = [True if x in LOWER else False for x in pword]
    nums = [True if x in NUMS else False for x in pword]
    return any(uppers) and any(lowers) and any(nums)

def pass_strength(pword):
    max_val = len(pword)
    upper_score = [True for x in pword if x in UPPER]
    lower_score = [True for x in pword if x in LOWER]
    num_score = [True for x in pword if x in NUMS]
    sym_score = [True for x in pword if x in SYMS]
    score = 0
    scores = [upper_score, lower_score, num_score, sym_score]
    for i in scores:
        score += 2.5 if any(i) else 0
    return score

print "Binary feedback: this is a good score."
print min_thresh(pword)
print "\n"
print "The strength is: "
print pass_strength(pword)
