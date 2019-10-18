import itertools

iters = int(input('How many binary digits shall there be?\n'))
bin_nums = []

for i in range(iters):
    bin_nums.append("0")
    bin_nums.append("1")

print('starting comboing')

statements = list(sorted(itertools.product(['0', '1'], repeat=iters)))

print('done comboing')

f = open(f'my_first_converter_{iters}bit.py', 'w+')

to_compile = ""

to_compile += "print('Welcome to my first converter!!!!')\n"
to_compile += "num = input('Whats your number???')\n\n"

binaries = [('0' * (iters - len(i))) + ''.join(i) for i in [''.join(i) for i in statements]]

for i in binaries:
    to_compile += f"if '{i}' == num:\n"

    fin_num = 0

    for pos, value in enumerate(i[::-1]):
        fin_num += (int(value) * 2) ** pos

    fn = (fin_num if i[-1] == '1' else fin_num - 1)
    to_compile += f"    print('The number is {fn}!!!')\n\n"

to_compile += "print('Thanks for using my calculator!!!!')\n"

f.write(to_compile)
f.close()
print('Your converter is done!')
