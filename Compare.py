# Compare CSV Files
import sys
import os
if len(sys.argv) < 6:
   print("Usage:\n \t" + sys.argv[0] + " <Input1.csv> <MatchIndex1> <Input2.csv> <MatchIndex2> <Output.csv>")
   sys.exit(1);

output = open(sys.argv[5], 'w')
input1 = open(sys.argv[1], 'r')
for line in input1:
    line = line.rstrip('\n')
    fields = line.split(',')
    input2 = open(sys.argv[3], 'r')
    for line2 in input2:
        line2 = line2.rstrip('\n')
        fields2 = line2.split(',')
        if fields[(int(sys.argv[2]) - 1)] == fields2[(int(sys.argv[4]) - 1)]:
            del(fields2[(int(sys.argv[4]) - 1)])
            fields3 = fields + fields2
            for data in fields3:
                output.write(data + ',')
            output.seek(-1,1)
            output.truncate()
            output.write(os.linesep)
output.close()

