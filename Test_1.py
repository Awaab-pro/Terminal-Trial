# #for any_number in range (1,11):
# #  for k in range(1,11):
# #    print(any_number,'*',k,'=',any_number * k)

# def cell(n, k):
#     return f'{n} * {k} = {n * k} \t| '

# for k in range(1,11):
#   print(cell(1, k),
#         cell(2, k),
#         cell(3, k),
#         cell(4, k),
#         cell(5,k))

# print('\n')

# for k in range(1,11):
#   print(cell(6, k),
#         cell(7, k),
#         cell(8, k),
#         cell(9, k),
#         cell(10,k))

def solution(N):     
    br = str(bin(N))[2:]
    br_group = False
    br_highest = 0
    bin_zero_counter = 0
    for char in br:
        if char == '1':
            if br_highest < bin_zero_counter:
                br_highest = bin_zero_counter
            br_group = True
            bin_zero_counter = 0
        elif br_group:
            bin_zero_counter += 1
    return br_highest
pass  

def SOLU(N):
    indices = [bit for bit, x in enumerate(f'{N:0b}') if x == '1']
    lengths = (end - beg for beg, end in zip(indices, indices[1:]))
    return max(lengths, default=1) - 1
print(SOLU(1041))
