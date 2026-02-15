

def count_404(log_file):
    count = 0
    with open(log_file, 'r') as f:
        for line in f:
            if '404' in line:
                count += 1
    return count
