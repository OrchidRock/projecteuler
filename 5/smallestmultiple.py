terms = range(1,51)
#terms = [756,4400,19845,9000]

primestable = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

def factoring(n):
    countstable = []
    for factor_index in range(0,len(primestable)):
	factor_power = 1
	factor = primestable[factor_index]
	while n % factor == 0:
	    factor_power *= factor
	    n /= factor
	countstable += [factor_power]
	if n == 1:
	    break
    return countstable

result_factor = []
for term in terms:
    countstable = factoring(term)
    for index in range(0,len(countstable)):
	if len(result_factor) <= index:
	    result_factor += [countstable[index]]
	elif result_factor[index] < countstable[index]:
	    result_factor[index] = countstable[index]
	else:
	    pass
result_factor_multi = 1
print result_factor
for t in result_factor:
    result_factor_multi *= t
print result_factor_multi
