    #iterate file name to 10
for file_counter in range(1,10):
    file_name=str(file_counter)+".in"
    file=open(file_name, 'r')
    total_num=file.readline()
    lines=file.readlines()
    total_coverage=0
    shift_detail=[0]*1000000000
    lifeguard_counter=0
    for line in lines:
        lifeguard_counter+=1
        time_pt=list(map(int,line.split()))
        for x in range(time_pt[0],time_pt[1]):
            shiftdetail=shift_detail[x]
            if (shiftdetail==-1):
                pass
            elif (shiftdetail==0):
            ## if this shift just turned one, add it to total_coverage
                total_coverage+=1
                shift_detail[x]=lifeguard_counter
            else:
                shift_detail[x]=-1
    final_cal=[0]*(lifeguard_counter)
    for shift in shift_detail:
        if (shift > 0): ##if shift is 0, no solo; if it's -1, not covered
            final_cal[shift-1]+=1
    shortest_coverage=final_cal[0]     
    for each_solo_time in final_cal:
        if (each_solo_time < shortest_coverage):
            shortest_coverage=each_solo_time ##new_solo
    file.close()
    answer=total_coverage-shortest_coverage
    print("Answer for " + file_name + " is " + str(answer) + ".")
    answer_file="out_answers/"+str(file_counter)+".out"
    a_file=open(answer_file,"r")
    answer_str=a_file.readline().strip()
    a_file.close()
    print("Correct answer is: " +answer_str + ". Did i get it right?: "+str(answer_str==str(answer)) + ". \n")
