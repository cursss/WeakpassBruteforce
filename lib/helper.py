from tqdm import tqdm

# Convert file to list
def file_to_list(filename : str):
    l = []
    with open(filename, 'r') as f:
        for s in f.readlines():
            l.append(s.strip())
    return l

# combine two lists into one
def lists_conbine(list_a : list, list_b : list):
    l = []
    for a in list_a:
        for b in list_b:
            l.append((a,b))
    return l

# customized printing, will add log recording function
def print_c(s : str):
    return tqdm.write(s)