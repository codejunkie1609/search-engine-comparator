import json

import numpy as np

def get_ranks(url_list):
    """Returns a dictionary mapping each URL to its 1-based rank."""
    return {url: rank+1 for rank, url in enumerate(url_list)}

def spearman_from_urls(list1, list2):
    """Computes Spearman's Rank Correlation Coefficient manually for two URL lists."""

    # Get ranks for URLs in both lists
    ranks1 = get_ranks(list1)
    ranks2 = get_ranks(list2)

    # Find common URLs in both lists
    common_urls = list(set(list1) & set(list2))
    #print(common_urls)
    

    # Extract corresponding ranks
    rank_list1 = np.array([ranks1[url] for url in common_urls])
    rank_list2 = np.array([ranks2[url] for url in common_urls])

    # Compute rank differences (d) and squared differences (d^2)
    d = rank_list1 - rank_list2
    d_squared = d ** 2

    # Compute Spearman’s rank correlation
    n = len(common_urls)
    sum_d_squared = np.sum(d_squared)
    if n > 1:
        rho = 1 - (6 * sum_d_squared) / (n * (n**2 - 1))
    elif n == 1:
        if ranks1 == ranks2:
            rho = 1
        else:
            rho = 0
    else:
        rho = 0



    return n,  (n/10)*100, rho

with open('hw1-duck.json', 'r') as file:
    data1 = json.load(file)

with open('Google_Result4.json','r') as file:
    data2 = json.load(file)

res = []
with open('100QueriesSet4.txt', 'r') as file:
    for line in file:
        scraped = data1[line]
        searched = data2[line]
        common, percent, rho = spearman_from_urls(searched, scraped)
        res.append([common, percent, rho])

avg1 = 0
avg2 = 0
avg3 = 0

print('Queries, Number of Overlapping Results, Percent Overlap, Spearman Coefficient')

for i in range(len(res)):
    print('Query {}, {}, {}, {}'.format(i+1, res[i][0], res[i][1], res[i][2]))
    
    avg1 += res[i][0]
    avg2 += res[i][1]
    avg3 += res[i][2]  # Corrected from res[i][1] to res[i][2]

# Compute averages
n = len(res)  # Number of queries
if n > 0:  # Avoid division by zero
    avg1 /= n
    avg2 /= n
    avg3 /= n

print('Averages, {}, {}, {}'.format(avg1, avg2, avg3))