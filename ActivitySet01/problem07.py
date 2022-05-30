# Strings

text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find(':')
piece = text[ipos+1:]
end =float(piece)
print(end)