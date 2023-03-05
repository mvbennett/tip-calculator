total_string = input("How much was the meal total?")

if total_string[0] == '$':
    total = float(total_string - "$")
else:
    total = float(total_string)

eighteen = total * 0.18
twenty = total * 0.2
twenty_two = total * 0.22

print(f"""acceptable tips are:
18%: {eighteen:.2f}
20%: {twenty:.2f}
22%: {twenty_two:.2f}""")
