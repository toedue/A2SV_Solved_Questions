def split_and_join(line):
    # write your code here
    # line_list = line.split(" ")
    # result = "-".join(line_list)
    #return result
    
    return "-".join(line.split(" "))
    
    
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
