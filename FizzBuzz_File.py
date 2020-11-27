
def FizzBuzz(start, finish):
    output_list=[]
    input_list=list(range(start,finish+1))

    for index,value in enumerate(input_list):
        if value % 15 == 0:
            output_list.append("fizzbuzz")
        elif value % 5 == 0:
            output_list.append("buzz")
        elif value % 3 ==0:
            output_list.append("fizz")
        else:
            output_list.append(value)

    return(output_list)
