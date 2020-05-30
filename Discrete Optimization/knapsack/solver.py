#!/usr/bin/python
# -*- coding: utf-8 -*-
import pulp as plp
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])
import pandas as pd

def dp(items, capacity):
    value = 0
    weight = 0
    taken = [0]*len(items)

    w, h =len(items) + 1, capacity + 1;

    # Matrix = [[0 for x in range(w)] for y in range(h)]
    matrix = [[0]*w for i in range(h)]
    for i in range(h):
        matrix[i][0] = 0
    for j in range(w):
        matrix[0][j] = 0

    for j in range(1,w):

        ### choose item j
        item = items[j-1]

        for i in range(1,h):
            ### check capacity i
            if item.weight <= i:
                matrix[i][j] = max(matrix[i][j-1], item.value + matrix[i - item.weight][j - 1])
            else:
                matrix[i][j] = matrix[i][j-1]

    a,b = w-1,h-1
    trace = []
    while True:
        if (a <= 0) or (b <= 0):
            break
        term = matrix[b][a]
        if term == matrix[b][a-1]:
            a = a - 1
            b = b
        else:
            trace.append((b,a))
            b = b - items[a-1].weight
            a = a - 1
    taken = [0]*len(items)

    for i in trace:
        taken[i[1]-1] = 1
    value = matrix[h-1][w-1]
    return value, taken

def optimization_tool(items, capacity):


    weight = [i.weight for i in items]
    value = [i.value for i in items]

    opt_model = plp.LpProblem("Profit maximising problem", plp.LpMaximize)


    x_vars  = {(i):
    plp.LpVariable(cat=plp.LpBinary, name="x_{0}".format(i))
    for i in range(len(items))}


    # constraints = {j : opt_model.addConstraint(
    # plp.LpConstraint(
    #              e=m(a[i,j] * x_vars[i,j] for i in set_I),
    #              sense=plp.plp.LpConstraintLE,
    #              rhs=b[j],
    #              name="constraint_{0}".format(j)))
    #        for j in set_J}

    # for i in range(len(items)):
    #     opt_model.addConstraint(plp.LpConstraint(
    #         e=x_vars[i]*weight[i],
    #         sense=plp.LpConstraintEQ,
    #         name='inv_balance_' + str(i),
    #         rhs=capacity))

    e_i = [x_vars[i]*weight[i] for i in range(len(items))]
    sum_e = sum(e_i)
    constrains = plp.LpConstraint(
        e= sum_e,
        sense=plp.LpConstraintEQ,
        name='inv_balance',
        rhs=capacity)
    opt_model.addConstraint(constrains)

    objective = plp.lpSum(x_vars[i] * value[i]
                        for i in range(len(items)))


    # if x is Binary
    # x_vars  = {(i,j):
    # plp.LpVariable(cat=plp.LpBinary, name="x_{0}_{1}".format(i,j))
    # for i in set_I for j in set_J}
    # constraints = {j : opt_model.addConstraint(
    # plp.LpConstraint(
    #              e=m(a[i,j] * x_vars[i,j] for i in set_I),
    #              sense=plp.plp.LpConstraintLE,
    #              rhs=b[j],
    #              name="constraint_{0}".format(j)))
    #        for j in set_J}
    # objective = plp.lpSum(x_vars[i,j] * c[i,j]
    #                     for i in set_I
    #                     for j in set_J)

    # for maximization
    opt_model.sense = plp.LpMaximize
    # for minimization
    # opt_model.sense = plp.LpMinimize
    opt_model.setObjective(objective)

    # solving with CBC
    opt_model.solve()

    # for i in x_vars:
    #     print(i.varValue)

    a = x_vars.values()
    taken = [int(i.varValue) for i in a]
    # print(a)
    # print(x_vars.values())

    status = 1 if plp.LpStatus[opt_model.status] == 'Optimal' else 0
    # print("Objective {}".format(opt_model.objective))
    # # solving with Glpk
    # # opt_model.solve(solver = GLPK_CMD())
    # opt_df = pd.DataFrame.from_dict(x_vars, orient="index",
    #                                 columns = ["variable_object"])
    #
    # print(x_vars)
    #
    # # print(x_vars.varValue)
    #
    #
    # opt_df["solution_value"] = opt_df["variable_object"].apply(lambda item: item.varValue)
    # print(opt_df)

    return int(plp.value(opt_model.objective)),status,taken




def solve_it(input_data):
    lines = input_data.split('\n')
    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])
    items = []
    opt = 0
    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))
    if len(items) < 100:
        value, taken = dp(items, capacity)
    else:
        value, opt, taken = optimization_tool(items, capacity)

    output_data = str(value) + ' ' + str(opt) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
