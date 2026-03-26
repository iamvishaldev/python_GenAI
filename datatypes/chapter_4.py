# Boolean

import sys

is_boiling = True

stir_count = 5

total_actions = stir_count + is_boiling #upcasting

print(f'total_actions',{total_actions})

milk_present = 0

print(f'is there a milk present?',{bool(milk_present)})

water_hot = True
tea_added = False
can_serve = water_hot or tea_added
print(f'chan serve chai?',{can_serve})

print(sys.float_info)
