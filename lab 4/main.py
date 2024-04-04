from Regex import SimpleRegexGenerator

# pattern = 'M?N{2}(O|P){3}Q*R+' #pattern 1
pattern = '(X|Y|Z){3}8+(9|0)' #pattern 2
# pattern = '(H|i)(J|K)L*N' #pattern 3
generator = SimpleRegexGenerator(pattern)
generator.run()