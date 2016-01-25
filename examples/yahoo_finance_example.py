import baseexample as baseexample

print 'Inputs: '

for i in be.yahoo_finance.get_input_names():
    print i

print 'Outputs: '

for o in be.yahoo_finance.get_output_names():
    print o

print be.yahoo_finance.query(['WMT'])
print be.yahoo_finance.query(['WMY', 'RIG', 'AAPL'])