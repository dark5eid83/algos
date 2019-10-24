# Cut the rope

# Given a rope with length n, find the maximum value maxProduct, that can be achieved for a product
# len[0] * len[1] *...*len[m-1], where the len[] is the array of lengths obtained by cutting
# the given rope into m parts

# Notes: 
# there should be at least one cut, i.e. m>= 2
# all < parts obtained after the cut should have non-zero integer valued lengths


# Explanation:
# For n = 4, there are two cuts possible: 1 + 3 and 2 + 2.
# We'll pick 2 + 2, because their product 2 * 2 = 4 is greater than product of the first one 1 * 3 = 3.
# (So our m = 2, n[0] = 2 and n[1] = 2 and product is n[0] * n[1] = 4.)



def max_product_from_cut_pieces(n):
    if n == 2:
        return 1
    if n == 3:
        return 2

    max_product = [0 for _ in range(n+1)]
    
    max_product[1] = 1
    max_product[2] = 2
    max_product[3] = 3

    for i in range(4, n+1):
        max_prod = 0 
        for j in range(1, i):
            max_prod = max(max_prod, j * max_product[i - j])
        if max_prod > 0:
            max_product[i] = max_prod
    return max_product[n]