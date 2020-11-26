"""Books"""
def main(books, page, num_x, num_y):
    """main"""
    import math as m
    check = page
    gene = 0
    result = 0
    if books != 0:
        books -= 1
        while check > 0:
            check -= m.ceil(((num_x+gene)/(num_y+gene))*page)
            result += 1
            if m.ceil(((num_x+gene)/(num_y+gene))*page) >= page:
                result += books
                break
            elif books > 0 and check <= 0:
                check = page
                books -= 1
                num_x = num_x+gene
                num_y = num_y+gene
                gene = 0
            gene += 1
    print(result)
main(int(input()), int(input()), int(input()), int(input()))
