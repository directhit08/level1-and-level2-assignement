
member_name = input("Enter Member Name: ")
member_id = int(input("Enter Member ID: "))
contributions = [] 

for i in range(1, 7):
    
    val = float(input(f"Enter contribution for month {i}: "))
    contributions.append(val)

total_savings = sum(contributions)

print(f"\nMember: {member_name} (ID: {member_id})")
print(f"Total Savings: KES {total_savings}")