from odd_to_odd_func import odd_to_odd_step_counter



def rm_dict_builder(q, n_max):
    from statistics import mode
    from collections import defaultdict

    #Setup odds to extract r,m info from
    odd_range = range(1, n_max, 2)

    #Loop through odds and collect the r (steps) for each odd
    r_step_dict = defaultdict(list)
    for n in odd_range:
        odd_0, odd_1, steps = odd_to_odd_step_counter(n,q)
        r_step_dict[steps].append(odd_0)

    r_step_dict = dict(sorted(r_step_dict.items())) #sort r (step) dict numerically

    #Assume we can write out every odd number as: base_odd + even_offset*m
    #Exract out the even_offset from the list of all odds in a r (step) family
    rm_dict = defaultdict(list)
    for r in r_step_dict:
        r_odds = r_step_dict[r] #all odds in an r (step) family

        diff_list = [r_odds[i+1] - r_odds[i] for i in range(len(r_odds)-1)] #compute the difference between odds in an r (step) family

        if diff_list:
            base_odd = r_odds[0] #This is the base odd
            even_offset = mode(diff_list) #Get the even_offset as the most likely difference between odds

            #Add r, base_odd, and even_offset as lists to a dict
            rm_dict['r'].append(r)
            rm_dict['base_odd'].append(base_odd)
            rm_dict['odds_diff'].append(even_offset)

    rm_dict = dict(rm_dict) #Convert rm_dict list to dictionary

    return rm_dict, r_step_dict
