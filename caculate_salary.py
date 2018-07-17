def total_year(income,base):
    base_year = base * 12
    add_half = (income - base*4.2)*1.2
    if add_half < 0:
        add_half = 0
    kpi = 0
    if income >= base * 6:
        kpi = base * 0.25
    total = kpi * 12 + base_year + add_half*2
    return total
    
name = "iris"
base = 5000
income = 30000
for income in range(20000,70001,5000):
    print("如果{}的月回款是：".format(name)+ str(income))
    print(name + "的年收入是：" + str(total_year(income,base)))
