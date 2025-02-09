T = int(input())
#number_list = [int(input()) for i in range(T)]

def see_allnumber(number):
    original_number = number
    count = 0
    see_number = set()

    while(len(see_number) != 10):
        count += 1
        for n in str(number):  
            see_number.add(int(n))

        number = original_number*(count+1)
        
    return count*original_number

# for num in number_list:
#     print(f'#{number_list.index(num)+1} {see_allnumber(num)}')

for test_case in range(1, T+1):
    N = int(input())
    print(f'#{test_case} {see_allnumber(N)}')
