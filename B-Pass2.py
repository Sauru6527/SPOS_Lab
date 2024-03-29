# Read Macro Definition Table (mdt)
with open("mdt.txt", "r") as mdt_file:
    mdt_lines = mdt_file.readlines()
mdt = [line.strip() for line in mdt_lines]

# Read Macro Name Table (mnt)
with open("mnt.txt", "r") as mnt_file:
    mnt_lines = mnt_file.readlines()
mnt = [line.strip().split() for line in mnt_lines]

# Read Argument List Array (ala)
with open("ala.txt", "r") as ala_file:
    ala_lines = ala_file.readlines()
ala = [line.strip().split() for line in ala_lines]

# Read Input Code
with open("input.txt", "r") as input_file:
    input_lines = input_file.readlines()

# Macro Processing
flag = 0
output = []

for line in input_lines:
    line = line.replace("\n", "")

    if line == "START":
        flag = 1

    if flag == 1:
        found = 0
        for m in mnt:
            if line.split()[0] == m[1]:
                passed = line.split()[1:]
                argumentList = []
                defaultVals = []

                for al in ala:
                    if al[1] == m[0]:
                        argumentList.append(al[2])
                        if len(al) == 4:
                            defaultVals.append(al[3])
                        else:
                            defaultVals.append("-")

                params = {}
                cntr = 0

                for arg in argumentList:
                    try:
                        params[arg] = passed[cntr]
                    except IndexError:
                        params[arg] = defaultVals[cntr]
                    cntr += 1

                mdt_cntr = int(m[2]) + 1

                while mdt[mdt_cntr] != "MEND":
                    macro_line = mdt[mdt_cntr]
                    for k, v in params.items():
                        macro_line = macro_line.replace(k, v)
                    output.append(macro_line)
                    mdt_cntr += 1

                found = 1

        if found == 0:
            output.append(line)

# Write Output to File
with open("output.txt", "w") as output_file:
    for line in output:
        output_file.write(line + "\n")

"""
input
START
INCR1 10, 20
PRINT "Done"
INCR2 5, 8
END

mnt
1 INCR1 0
2 INCR2 4

mdt
INCR1 &FIRST &SECOND=DATA9
A 1 &FIRST
L 2 &SECOND
MEND
INCR2 &ARG1 &ARG2=DATA5
L 3 &ARG1
ST 4 &ARG2
MEND

ala
0 1 &FIRST
1 1 &SECOND DATA9
2 2 &ARG1
3 2 &ARG2 DATA5



"""
