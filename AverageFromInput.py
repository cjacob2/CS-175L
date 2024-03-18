#CS175L
#Conor Jacob
#AverageFromInput


def main():
    total_num = 0
    count_nums = 0 
    with open(r"C:\Users\cdjac\Downloads\numbers.txt", "r") as file:
        for line in file:
            num = float(line.strip())
            total_num += num
            count_nums +=1
            print(f"I read {count_nums} number(s) Current number is : {num:9.2f} Total is : {total_num:9.2f}")

    avr = total_num/count_nums if count_nums>0 else 0
    print(f"Average: {avr:.1f}")

if  1 == 1 :
    main()
