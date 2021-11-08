import  json
file = open("text_files/file7.txt", "r")

profit = {}
i = 0
sum = 0
for line in file:
    prof = float(line.split()[2]) - float(line.split()[3])
#    profit.append({line.split()[0]: prof})
    profit[line.split()[0]] = prof
    if float(prof) > 0:
        i += 1
        sum += prof

prof_and_av = [profit]
prof_and_av.append({"average_profit": round(sum/i)})
print(prof_and_av)

json_file = open("text_files/json_file.txt", "w")
json.dump(prof_and_av, json_file)