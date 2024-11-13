import csv
import sys

# CSV file containing the processed data
input_csv = sys.argv[1]

def get_sign(val):
    if val > 0.0:
        return 1
    elif val < 0.0:
        return -1

with open(input_csv, 'r') as csvfile:
    with open("new_integral_data.csv", 'w', newline='') as csvfilenew:
        csv_reader = csv.reader(csvfile)
        csv_writer = csv.writer(csvfilenew)
        
        header = next(csv_reader)  # First row is the header
        csv_writer.writerow(header)

        for row in csv_reader:
        # for row in (r for r in csv_reader if r[0] == "(6, 6, 5, 1)"):

            new_row = row
            exception = False
            sign_1 = None
            sign_2 = None
            sign_3 = None
            number_1 = None
            number_2 = None
            number_3 = None
            checked_all = False

            while checked_all == False:
                # print(row)
                # print(new_row)
                for count, value in enumerate(map(float, row[-1:0:-1])):
                    # print(count,value)
                    if count == 0:
                        number_1 = value
                        sign_1 = get_sign(value)
                    elif count == 1:
                        number_2 = value
                        sign_2 = get_sign(value)
                        if sign_2 != sign_1:
                            exception = True
                    elif count < len(row[-1:0:-1])-1 and count > 1:
                        number_3 = value
                        # print("     ",number_3,number_2,number_1)
                        sign_3 = get_sign(value)
                        if exception:
                            if sign_3 != sign_2:
                                # print(number_3, number_2)
                                sys.exit("Error with baseline and excpetion")
                            else:
                                exception = False
                                number_1 = number_2
                                number_2 = number_3
                        if not exception:
                            if sign_3 != sign_2:
                                # print("HERE",number_3,number_2,number_1)

                                diff_1 = number_2 - number_1
                                diff_2 = number_3 - number_2
                                ratio  = diff_2/diff_1
                                
                                # print(diff_1, diff_2, ratio)
                                if ratio < 0.8 or ratio > 1.2:
            #                 # if get_sign(str(float(number_2) - float(number_1) + float(number_2))) != sign_3:
            #                 # if (float(number_2) - float(number_1)) > float(number_2):
            #                 # if get_sign(str(float(number_2) - float(number_1))) != get_sign(str(float(number_3) - float(number_2))):
                                    # print("switching sign", ratio)
                                    value_index = row.index(str(number_3))+1

                                    for sub_count, sub_value in enumerate(map(float, row[1:value_index])):
                                        # print(sub_count, sub_value)
                                        new_row[sub_count+1] = str(-1*sub_value)
                                    # new_number_3 = -1*value
                                    # new_row[new_row.index(str(number_3))] = str(new_number_3)
                                    # number_3 = new_number_3
                                    # sign_3 *= -1
                                    row = new_row
                                    break
                                else:
                                    number_1 = number_2
                                    sign_1 = sign_2
                                    number_2 = number_3
                                    sign_2 = sign_3
                            else:
                                number_1 = number_2
                                sign_1 = sign_2
                                number_2 = number_3
                                sign_2 = sign_3

                    elif count == len(row[-1:0:-1])-1:
                        number_3 = value
                        # print("     ",number_3,number_2,number_1)
                        sign_3 = get_sign(value)

                        if sign_3 != sign_2:
                            # print("HERE",number_3,number_2,number_1)
                            diff_1 = number_2 - number_1
                            diff_2 = number_3 - number_2
                            ratio  = diff_2/diff_1
                            if ratio < 0.8 or ratio > 1.2:
                                # print("switching sign", row)
                                value_index = row.index(str(number_3))+1
                                for sub_count, sub_value in enumerate(map(float, row[1:value_index])):
                                    # print(sub_count, sub_value)
                                    new_row[sub_count+1] = str(-1*sub_value)

                        row = new_row
                        checked_all = True

            csv_writer.writerow(row)

            

