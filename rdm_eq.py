from itertools import chain, permutations

x = '40 1 3 4 20'


def powerset(iterable):
  xs = list(iterable)
  return chain.from_iterable(permutations(xs,n) for n in range(len(xs)+1) )


lst_expr = []
for operands in map(list, powerset(x.split())):
    n = len(operands)
    #print operands
    if n == 5:
        all_operators = map(list, permutations(['+','-','*','/'],n-1))
        #print all_operators, operands
        for operators in all_operators:
            exp = operands[0]
            numbers = (operands[0],)
            i = 1
            for operator in operators:
                exp += operator + operands[i]
                numbers += (operands[i],)
                i += 1

            lst_expr += [{'exp': exp, 'numbers': tuple(sorted(numbers))}]

lst_stages=[]
numbers_sets = set()
a = 0
for item in lst_expr:
    equation = item['exp']
    numbers = item['numbers']
    if numbers not in numbers_sets and eval(equation) == 42:
        lst_stages.append(equation)
        eq = str(equation) + '=' + str(eval(equation))
        a += 1
        numbers_sets.add(numbers)

if a >= 1:
    print('YES')
else:
    print('NO')
