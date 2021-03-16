def sum_pa(n_max, ratio):
    n = n_max//ratio
    rn_max = n*ratio
    print (rn_max)
    return (ratio + rn_max)*n/2


print(sum_pa(1000, 5) + sum_pa(1000, 3) - sum_pa(1000, 15) - 1000)

