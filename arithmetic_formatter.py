def arithmetic_arranger(problems, answer=False):
    if len(problems) > 5:
        return "Error: Too many problems"
    else:
        arranged_problems = ""
        top_list = ""
        bottom_list = ""
        dash_list = ""
        calculation_list = ""
        for index, value in enumerate(problems):
            valid_operations = ["+","-"]
            split_operation = value.split(" ")
            if not split_operation[0].isdigit() or not split_operation[2].isdigit():
                return "Error: Numbers must only contain digits"
            if split_operation[1] not in valid_operations:
                return "Error: Operator must be '+' or '-'"
            for i in split_operation:
                if len(i) > 4:
                    return "Error: Numbers cannot be more than 4 digits"
            term1 = split_operation[0]
            operation = split_operation[1]
            term2 = split_operation[2]
            dashes = ""
            spaces_top = ""
            spaces_bottom = ""
            longest_digit = len(max(split_operation,key=len))
            for i in range(longest_digit):
                dashes += "-"
            
            length_difference = abs(len(split_operation[0]) - len(split_operation[2]))

            if len(split_operation[0]) > len(split_operation[2]):
                for i in range(length_difference):
                    spaces_bottom += " "
            if len (split_operation[0]) < len(split_operation[2]):
                for i in range(length_difference):
                    spaces_top += " "

            top = "  {}{}".format(spaces_top,term1)
            bottom = "{} {}{}".format(operation,spaces_bottom,term2)
            dash =  "--" + dashes
            
            if index < len(problems)-1: 
                top_list += "{}    ".format(top)
                bottom_list += "{}    ".format(bottom)
                dash_list += "{}    ".format(dash)
            else:
                top_list += "{}".format(top)
                bottom_list += "{}".format(bottom)
                dash_list += "{}".format(dash)

            if answer == True:
                if operation == "+":
                    spaces = ""
                    length_difference = int((len(str(int(split_operation[0]) + int(split_operation[2])))) - len(max(split_operation,key=len)))
                    if length_difference > 0:
                        calculation = " {}".format(str(int(split_operation[0]) + int(split_operation[2])))
                    else: calculation = "  {}".format(str(int(split_operation[0]) + int(split_operation[2])))
                if operation == '-':
                    calculation = " {}".format(str(int(split_operation[0]) - int(split_operation[2])))
                if index < len(problems)-1:
                    calculation_list += "{}    ".format(calculation)
                else:
                    calculation_list += "{}".format(calculation)
        arranged_problems = (top_list + "\n" + bottom_list + "\n" + dash_list + "\n" + calculation_list).rstrip()
    return arranged_problems



test_operations = ["20 + 4", "500 + 20", "65 + 200", "20 + 784", "90 + 5"]

print(arithmetic_arranger(test_operations, True)
