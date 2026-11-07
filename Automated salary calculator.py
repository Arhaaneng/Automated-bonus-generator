import random 
print ("====Automated salary bonus generator====")

initial_salary= float(input("Enter your initial salary: ₹"))
bonus = random.randint(1000,5000)
final_salary= initial_salary+bonus

print("\nSALARY BONUS REPORT =====")
print("initial salary: ₹", initial_salary)
print("generated salary ₹",bonus)
print("final salary ₹", final_salary)

print("\nBonus successfully generated!")

