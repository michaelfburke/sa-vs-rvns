# hub_operations.py
import random
import numpy as np

# Functions for generating initial solutions and calculating the objective function

# Define function for initial solution
def initial_solution(fm, cm, number_of_hubs):
    """
    Creates an initial solution for the problem.
    
    Parameters:
    fm (np.ndarray): Flow matrix
    cm (np.ndarray): Cost matrix
    number_of_hubs (int): Number of hubs to be selected
    
    Returns:
    solution (list): Initial solution
    """
    # Check if the dimensions of flow matrix and cost matrix are the same
    if fm.shape != cm.shape:
        raise ValueError("Flow matrix and cost matrix must be of same size.")
    
    # Number of nodes
    n = fm.shape[0]
    
    # Randomly select number_of_hubs unique nodes to be hubs
    hubs = random.sample(range(1, n+1), number_of_hubs)
    
    # Create initial solution by randomly assigning each node to a hub
    solution = [random.choice(hubs) if i+1 not in hubs else i+1 for i in range(n)]
    
    return solution

# function to get interhub cost
def interhub_cost(flow):
    if 0 <= flow < 50000:
        return flow
    elif flow < 100000:
        return 0.8*flow + 10000
    elif flow < 200000:
        return 0.6*flow + 30000
    elif 200000 <= flow:
        return 0.4*flow + 70000
    
def total_cost(fm, cm, solution):
    solution = np.array(solution)
    # get number of nodes
    n = len(fm)

    # initialise total cost
    total_cost = 0

    im_cost = cm[np.arange(n), solution-1][:, np.newaxis]
    kj_cost = cm[solution-1, np.arange(n)][np.newaxis, :]
    total_cost += np.sum(fm*(im_cost+kj_cost))

    hubs = set(solution)
    # print('Hubs: ' + str(hubs))
    for k in hubs:
        for m in hubs:
            if k != m:
                flow = fm[solution == k][:, solution == m].sum()
                total_cost += interhub_cost(flow) * cm[k-1, m-1]

    return total_cost

# generating neighbourhood solutions

# function to get a neighbour of a solution by swapping a hub and a node. Neighbourhood structure type 1.
def neighbour(solution): 
    # get number of nodes
    n = len(solution)
    # get list of hubs
    hubs = []
    for i in range(n):
        if i+1 == solution[i]:
            hubs.append(i+1)
    # print('Hubs: ' + str(hubs))
    # swap a hub and a node
    while True:
        # get a random node
        i = random.randint(0, n-1)
        # get a random hub
        j = random.randint(0, len(hubs)-1)
        # if node i is not a hub
        if i+1 != hubs[j]:
            # create a copy of the solution
            neighbour = solution.copy()
            # swap node i and hub j
            neighbour[i] = hubs[j]
            # reassign nodes that were connected to hub j to node i
            for k in range(n):
                if neighbour[k] == hubs[j]:
                    neighbour[k] = i+1
            # test if neighbour is not feasible
            # if not feasible(neighbour, len(hubs)):
            #     # print('Neighbour ' + str(neighbour) + ' is not feasible')
            #     continue

            # test that number of hubs is not changed
            if len(hubs) != len(set(neighbour)):
                continue

            # return neighbour
            return neighbour

# function to get a neighbour of a solution by swapping the hubs of two nodes. Neighbourhood structure type 2.
def neighbour2(solution):
    # get number of nodes
    n = len(solution)
    # get list of hubs
    hubs = []
    for i in range(n):
        if i+1 == solution[i]:
            hubs.append(i+1)
    # print('Hubs: ' + str(hubs))
    # get nodes
    nodes = []
    for i in range(n):
        if i+1 not in hubs:
            nodes.append(i+1)
    # print('Nodes: ' + str(nodes))
    # swap the hubs of two nodes
    while True:
        # get a random node
        i = random.randint(0, len(nodes)-1)
        # get a random node
        j = random.randint(0, len(nodes)-1)
        # if nodes are not the same
        if i != j:
            # create a copy of the solution
            neighbour = solution.copy()
            # swap hubs of nodes i and j
            neighbour[nodes[i]-1] = solution[nodes[j]-1]
            neighbour[nodes[j]-1] = solution[nodes[i]-1]

            # test if neighbour is not feasible
            # if not feasible(neighbour, len(hubs)):
            #     print('Neighbour ' + str(neighbour) + ' is not feasible')
            #     continue

            # test that number of hubs is not changed
            if len(hubs) != len(set(neighbour)):
                print('Number of hubs is changed. Hubs: ' + str(hubs) + ', Neighbours: ' + str(neighbour))
                continue

            # return neighbour
            return neighbour
        

# function to get a neighbour of a solution by allocating a node to a new hub. Neighbourhood structure type 3.
def neighbour3(solution):
    # get number of nodes
    n = len(solution)
    # get list of hubs
    hubs = []
    for i in range(n):
        if i+1 == solution[i]:
            hubs.append(i+1)
    # print('Hubs: ' + str(hubs))
    # get nodes
    nodes = []
    for i in range(n):
        if i+1 not in hubs:
            nodes.append(i+1)
    # print('Nodes: ' + str(nodes))
    # allocate a node to a new hub
    while True:
        # get a random node
        i = random.randint(0, len(nodes)-1)
        # get a random hub that is not connected to node i
        j = random.randint(0, len(hubs)-1)
        # if hub j is not connected to node i
        if solution[nodes[i]-1] != hubs[j]:
            # create a copy of the solution
            neighbour = solution.copy()
            # reassign node i to hub j
            neighbour[nodes[i]-1] = hubs[j]

            # test if neighbour is not feasible
            # if not feasible(neighbour, len(hubs)):
            #     print('Neighbour ' + str(neighbour) + ' is not feasible')
            #     continue

            # test that number of hubs is not changed
            if len(hubs) != len(set(neighbour)):
                print('Number of hubs is changed. Hubs: ' + str(hubs) + ', Neighbours: ' + str(neighbour))
                continue

            # return neighbour
            return neighbour

# function to get a neighbour of a solution by swapping the allocation of nodes to two hubs. Neighbourhood structure type 4.
def neighbour4(solution):
    # get list of hubs
    hubs = []
    for i in range(len(solution)):
        if i+1 == solution[i]:
            hubs.append(i+1)

    # get nodes
    nodes = []
    for i in range(len(solution)):
        if i+1 not in hubs:
            nodes.append(i+1)

    # swap the allocation of nodes to two hubs
    while True:
        # get a random hub
        i = random.randint(0, len(hubs)-1)
        # get a random hub
        j = random.randint(0, len(hubs)-1)

        # if hubs are not the same
        if i != j:
            # create a copy of the solution
            neighbour = solution.copy()

            # reassign nodes that were connected to hub i to hub j
            # for k in range(n) except when k is in hubs
            for k in nodes:
                if neighbour[k-1] == hubs[i]:
                    neighbour[k-1] = hubs[j]
                elif neighbour[k-1] == hubs[j]:
                    neighbour[k-1] = hubs[i]

            # test if neighbour is not feasible
            # if not feasible(neighbour, len(hubs)):
            #     continue

            # test that number of hubs is not changed
            if len(hubs) != len(set(neighbour)):
                continue

            # return neighbour
            return neighbour