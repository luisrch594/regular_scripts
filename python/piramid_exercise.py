


def height_piramid(quantity: int):
    if (quantity%2!=0):
        return 0
    else:
        height=0
        limit_blocks=1
        quantity_per_level=0
        while (quantity>0):
            quantity-=1
            quantity_per_level+=1
            if quantity_per_level==limit_blocks:
                limit_blocks+=1
                quantity_per_level=0
                height+=1
        
        return height

print(height_piramid(6))
print(height_piramid(20))
print(height_piramid(1000))
print(height_piramid(2))
