
import os

from multiplePdf import PdfToText

# pdf and txt file directory path are given to convert to text
#
# pdfDir = "C:/Users/Liza/Desktop/MajorCVAnalysis/Code/MajorProject/cv/"

# txtDir = "C:/Users/Liza/Desktop/MajorCVAnalysis/Code/MajorProject/text/"
# PdfToText.convertMultiple(pdfDir, txtDir)
from sample import lineList

keyword=["technical skills", "top skills", "skills","special skills","skills and abilities","knowledge and skills","technical expertise","special knowledge","technical qualification", "education", "academic qualification", "academic", "experience", "work experience"]
keywordSkill= ["technical Skills", "top skills", "skills", "skill and abilities","knowledge and skills","technical expertise","special knowledge","technical qualification"]
keywordEdu = ["education", "academic qualification", "academic","qualification"]
keywordExp=["experience", "work experience"]
ListOfSkill=[]
indexValue=[]
topicName=[]

def extract():

    txtDir = "C:/Users/Liza/Desktop/MajorCVAnalysis/Code/MajorProject/text/"

    for txt in os.listdir(txtDir):
        # print(txt)
        fileExtension = txt.split(".")[-1]
        if fileExtension == 'txt':
            file = open(txtDir+txt,'r',encoding="utf8")
            lineList=list()
            with file as f:
                for line in f:
                    lineList.append(line.lower().replace(',','\n').rstrip('\n'))

                print(lineList)


                # index in format {'skill': 6}
                for i in lineList:
                    for m in keyword:
                        if i == m:
                            topicName.append(i)

                            indexValue.append(lineList.index(i))

                return lineList
extract()

merged = dict(zip(topicName, indexValue))  # merged topicName and its Index value


def next_value(dictionary, current_key):
    # Get the list of keys from the OrderedDict
    keys = list(dictionary.keys())

    # Get an index of the current key and offset it by -1
    index = keys.index(current_key) + 1

    # return the previous key's value
    return dictionary[keys[index]]
import json
# def extract(merged):
skill=[]
for i in merged:
    try:
        second = next_value(merged,i)
    except IndexError:
        second=None
    read = lineList[merged[i] + 1:second]
    merged[i]=read
    # info = []
    # for m in read:
    #     info += m.split()
    #     merged[i]=info

skill=[]
education=[]
experience=[]
for i in merged:
    for j in keywordSkill:
        if i==j:
            skill = (merged[i])
            skillName=i
            break
    for m in keywordEdu:
        if i==m:
            education = merged[i]
            educationName=i
            break
    for n in keywordExp:
        if i==n:
            experience = merged[i]
            experienceName=i
            break
ListSkill=[]

for i in skill:
    ListSkill+=i.split()
print(skillName,':',ListSkill)

ListEducation=[]
for i in education:
    ListEducation+=i.split()
print(educationName,':',ListEducation)

print(experienceName,':',experience)

SkillWords=[
'cobra',
'javascript',
'jscript',
'julia',
'matlab',
'numpy',
'r',
'sas',
'access',
'excel',
'outlook',
'powerpoint',
'Access',
'Excel',
'Outlook',
'powerpoint',
'databases',
'sap',
'SciPy',
'matplotlib',
'sckit-learn',
'graphlab',
'image processing',
'html',
'css',
'php',
'python',
'c',
'c++',
'java']
FilteredSkill=[]
for i in SkillWords:
    if i in ListSkill:
        FilteredSkill.append(i)

print("Filtered Skill:",FilteredSkill)

EducationWords=['bachelor\'s','master','enginnering', 'diploma','computer', 'science']

FilteredEducation=[]
for i in EducationWords:
    if i in ListEducation:
        FilteredEducation.append(i)

print("Filtered Education:",FilteredEducation)

job_description_skill=['css','php']
job_description_education=['bachelor\'s']
print('skill from job desciption',job_description_skill)
print('education from job description', job_description_education)

SkillCount=0
for i in FilteredSkill:
    if i in job_description_skill:
        SkillCount+=1
print('NO. of Matched Skill', SkillCount)
EducationCount=0
for i in FilteredEducation:
    if i in job_description_education:
        EducationCount+=1
print('NO. of Matched Education',EducationCount)
print('\n')
bestScore=0




# # # pass
#
#
#
#     #split each sentence into words
#
#
#         # yesto chaeyeko
#         # skills = [skills ko list]
#         #education=[education ko list]
#
#
#     # result = extract(merged)
#     # result1= extract(merged)
#     # print(result1)
#
