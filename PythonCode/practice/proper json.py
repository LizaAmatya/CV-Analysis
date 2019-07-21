#
# import pandas

rawData = open("Chandan Singh.txt").read()
rawData[0:500]
print(rawData[0:500])

parsedData = rawData.replace('\t', '\n').split('\n')
print (parsedData)

labellist = parsedData[0::2]
textlist = parsedData[1::2]

print (labellist[0:5])
print (textlist[0:5])
#
# # fullCorpus = pd.DataFrame({
# #     'label' : labellist, #first column
# #     'body_list' : textlist #second column. it will create dataframe
# # })
# # fullCorpus.head()
#
# print(len(labellist))
# print(len(textlist))
#
# print(labellist[-5:])
#
# fullCorpus = pd.DataFrame(
#     {
#         'label' : labellist[:-1],
#         'body_list' : textlist
#     }
# )
#
# fullCorpus.head()

# dataset = pd.read_json("", sep='\t', header=None)