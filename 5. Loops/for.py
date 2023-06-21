start = int(input('Type the start number for your range: '))
end = int(input('Type the finish number for your range: ')) + 1

if start < end:
    for i in range(start,end):
        if i%2 == 0:
            continue
        print(i)
else:
    print('The end number must be grater than the start number')