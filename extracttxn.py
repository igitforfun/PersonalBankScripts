import re
import pandas as pd
import argparse


def parser_init():
    parser = argparse.ArgumentParser(description= 'filter and calculate the matched transactions')
    parser.add_argument('-f', '--file', dest='input_file', help = 'excel file to be processed')
    parser.add_argument('-w', '--word', dest='regex_word', help= 'TXN string or substring')
    return parser

def main():
    parser = parser_init()
    args = parser.parse_args()
    if args.input_file:
        exceldata = pd.read_excel(args.input_file)
        totalcost=0.0
        print("------------------------------------------------------------------------")
        for i in range(len(exceldata['Unnamed: 2'])): #Run through description column
            if (i >= 9):
                if args.regex_word:
                    if ((re.search(str(args.regex_word), str(exceldata['Unnamed: 2'][i]), re.IGNORECASE)) or not (args.regex_word)):
                        print(f"\033[93m{exceldata['Unnamed: 1'][i]}\033[0m | {exceldata['Unnamed: 2'][i]} : \033[96m{exceldata['Unnamed: 6'][i]}\033[0m")
                        print("------------------------------------------------------------------------")
                        totalcost += float(exceldata['Unnamed: 6'][i])
                else:
                    print(f"\033[93m{exceldata['Unnamed: 1'][i]}\033[0m | {exceldata['Unnamed: 2'][i]} : \033[96m{exceldata['Unnamed: 6'][i]}\033[0m")
                    print("------------------------------------------------------------------------")
                    totalcost += float(exceldata['Unnamed: 6'][i])
        print(f"Total cost = \033[92m{round(totalcost,3)}\033[0m")
    else:
        print("no input files")

if __name__ == "__main__":
    main()
