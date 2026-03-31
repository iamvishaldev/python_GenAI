# revison
square = [n*n for n in range(1,11)]

odd_num = [n for n in range(1,21) if n%2 != 0]

even_odd = [n*2 if n%2 == 0 else n for n in range(1,11)]

nums = [1,2,2,3,4,4,5]
unique_set = {n for n in nums}

div_by_3 = {n for n in range(1,21) if n % 3 == 0}

dict_num = {n: n*n for n in range(1,6)}

even_odd_dict = {n:"Even" if n%2 == 0 else "Odd" for n in range(1,11)}

# gen_num = (n*n for n in range(1,6))
# for n in gen_num:
#     print(n)

daily_sales = [5,10,12,7,3,8,9,15]

# for n in daily_sales:
#     if n>3:
#         print(n)

total_cups = list(sale for sale in daily_sales if sale>3)
print(f"Total cup sales : {total_cups}")