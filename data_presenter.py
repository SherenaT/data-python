open_file = open("CupcakeInvoices.csv")

cupcakes_type = []
invoice_total = 0
chocolate_total = 0
vanilla_total = 0
strawberry_total = 0

for line in open_file:
  line = line.rstrip('\n').split(',')
  invoice_total += int(line[3])*float(line[4])
  cupcakes_type.append(line[2])
  if line[2] == "Chocolate":
    chocolate_total += round(int(line[3])*float(line[4]))
  elif line[2] == "Vanilla":
    vanilla_total += round(int(line[3])*float(line[4]))
  elif line[2] == "Strawberry":
    strawberry_total += round(int(line[3])*float(line[4]))

print(invoice_total)
print(cupcakes_type)
print(chocolate_total, vanilla_total, strawberry_total)



open_file.close()