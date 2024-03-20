#CS175L
#Conor Jacob
#AverageFromInput

def main():
    try:
        
        total_num = 0
        count_nums = 0
        
        with open(r"C:\Users\cdjac\Downloads\numbers.txt", "r") as file:
            for line in file:
                try:
            
                    num = float(line.strip())
                    total_num += num
                    count_nums +=1
                    print(f"I read {count_nums} number(s) Current number is : {num:9.2f} Total is : {total_num:9.2f}")

                except ValueError:
                    print(f"Bad Data: {line.strip()} skipping")

        avr(total_num, count_nums)
        
    except FileNotFoundError:
        print("SystemExit: File not found: numbers.txt - exiting")

    


def avr(total_num, count_nums):
    avr = total_num/count_nums if count_nums>0 else 0
    print(f"Average: {avr:.1f}")


main()
