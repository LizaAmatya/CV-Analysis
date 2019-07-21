
import os

from multiplePdf import PdfToText
#
# pdf and txt file directory path are given to convert to text
#
# pdfDir = "C:/Users/Liza/Desktop/MajorCVAnalysis/Code/MajorProject/cv/"

txtDir = "C:/Users/Liza/Desktop/MajorCVAnalysis/Code/MajorProject/text/"
# PdfToText.convertMultiple(pdfDir, txtDir)

for txt in os.listdir(txtDir):
    print(txt)
    fileName = open(txtDir + txt, 'r', encoding="utf8")
    lineList = list()
    with fileName as f:
        for line in f:
            lineList.append(line.lower().replace(',', '\n').rstrip('\n'))

    keyword = ["technical skills", "top skills", "skills", "special skills", "education", "academic qualification",
               "academic", "experience", "work experience"]
    keywordSkill = ["technical Skills", "top skills", "skills"]
    keywordEducation = ["education", "academic qualification", "academic"]
    keywordExperience = ["experience", "work experience"]
    ListOfSkill = []
    indexValue = []
    topicName = []
    # index in format {'skill': 6}
    for i in lineList:
        for m in keyword:
            if i == m:
                topicName.append(i)

                indexValue.append(lineList.index(i))

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
    skill = []
    for i in merged:
        try:
            second = next_value(merged, i)
        except IndexError:
            second = None
        read = lineList[merged[i] + 1:second]
        merged[i] = read
        # info = []
        # for m in read:
        #     info += m.split()
        #     merged[i]=info

    skill = []
    education = []
    experience = []
    for i in merged:
        for j in keywordSkill:
            if i == j:
                skill = (merged[i])
                skillName = i
                break
            else:
                print('No Skill found')

        for m in keywordEducation:
            if i == m:
                education = merged[i]
                educationName = i
                break
        for n in keywordExperience:
            if i == n:
                experience = merged[i]
                experienceName = i
                break
    ListSkill = []

    for i in skill:
        ListSkill += i.split()
    print(skillName, ':', ListSkill)

    ListEducation = []
    for i in education:
        ListEducation += i.split()
    print(educationName, ':', ListEducation)

    print(experienceName, ':', experience)

    SkillWords = [
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
    FilteredSkill = []
    for i in SkillWords:
        if i in ListSkill:
            FilteredSkill.append(i)

    print("Filtered Skill:", FilteredSkill)

    EducationWords = ['bachelor\'s', 'master', 'enginnering', 'diploma', 'computer', 'science']

    FilteredEducation = []
    for i in EducationWords:
        if i in ListEducation:
            FilteredEducation.append(i)

    print("Filtered Education:", FilteredEducation)

    job_description_skill = ['css', 'php']
    job_description_education = ['bachelor\'s']
    print('skill from job desciption', job_description_skill)
    print('education from job description', job_description_education)

    SkillCount = 0
    for i in FilteredSkill:
        if i in job_description_skill:
            SkillCount += 1
    print('NO. of Matched Skill', SkillCount)
    EducationCount = 0
    for i in FilteredEducation:
        if i in job_description_education:
            EducationCount += 1
    print('NO. of Matched Education', EducationCount)
    print('\n')
    bestScore = 0

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def vect_cos(vect, test_list):
    """ Vectorise text and compute the cosine similarity """
    query_0 = vect.transform([' '.join(vect.get_feature_names())])
    query_1 = vect.transform(test_list)
    cos_sim = cosine_similarity(query_0.A, query_1.A)  # displays the resulting matrix
    return query_1, np.round(cos_sim.squeeze(), 3)


# Train the vectorizer
vocab = ['php', 'json', 'python']  # jobdescription
vectoriser = CountVectorizer().fit(vocab)
vectoriser.vocabulary_  # show the word-matrix position pairs

# Analyse  list_1
list_1 = ['javascript', 'html', 'css', 'php', 'c++', 'mysql', 'jquery', 'json', 'linux']  # skill form cv1
list_1_vect, list_1_cos = vect_cos(vectoriser, [' '.join(list_1)])

# Analyse list_2
list_2 = ['javascript', 'html', 'css', 'php', 'c++']  # skill from cV2
list_2_vect, list_2_cos = vect_cos(vectoriser, [' '.join(list_2)])

print('\nThe cosine similarity for the first list is {}.'.format(list_1_cos))
print('\nThe cosine similarity for the second list is {}.'.format(list_2_cos))

# pass


# split each sentence into words


# yesto chaeyeko
# skills = [skills ko list]
# education=[education ko list]


# result = extract(merged)
# result1= extract(merged)
# print(result1)

