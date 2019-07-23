import json
#pdf file directory here
pdfDir = "C:/Users/DELL/Downloads/Compressed/Skill Portal/cvs/"

#text file dicretory where you want to put
txtDir = "C:/Users/DELL/Downloads/Compressed/Skill Portal/text/"
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text

#converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
def convertMultiple(pdfDir, txtDir):
    files = []
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        files.append(pdf)
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf
            text = convert(pdfFilename) #get string of text content of pdf
            textFilename = txtDir + pdf.split(".")[0] + ".txt"
            textFile = open(textFilename, "w" , encoding="utf-8") #make text file
            textFile.write(text) #write text to text file
            # print(textFile)
    # return textFile

# convertMultiple(pdfDir,txtDir)
    cosine=[]
    # files = []
    for txt in os.listdir(txtDir):
    #     txt = "C:/Users/DELL/Downloads/Compressed/Skill Portal/text/Abu-Bah.txt"
        # print(txt)

        # files.append(txt)
        fileName = open(txtDir+txt, 'r' ,encoding="utf8")#textFilename
        # fileName = open(txt, 'r', encoding="utf8")
        lineList=list()
        with fileName as f:
            for line in f:
                lineList.append(line.lower().replace(',','\n').rstrip('\n'))


        keyword=["technical skills", "top skills", "skills","special skills", "skills and abilities", "education", "academic qualification", "academic", "experience", "work experience"]
        keywordSkill= ["technical Skills", "top skills", "skills"]
        keywordEducation = ["education", "academic qualification", "academic"]
        keywordExperience=["experience", "work experience"]
        ListOfSkill=[]
        indexValue=[]
        topicName=[]


        #index in format {'skill': 6}
        for i in lineList:
            for m in keyword:
                if i== m:
                    topicName.append(i)

                    indexValue.append(lineList.index(i))

        merged = dict(zip(topicName, indexValue))#merged topicName and its Index value
        # print(json.loads(merged))


        def next_value(dictionary, current_key):

            # Get the list of keys from the OrderedDict
            keys = list(dictionary.keys())

            # Get an index of the current key and offset it by -1
            index = keys.index(current_key) + 1

            # return the previous key's value
            return dictionary[keys[index]]

        # def extract(merged):
        skill=[]
        for i in merged:
            try:
                second = next_value(merged,i)
            except IndexError:
                second=None
            read = lineList[merged[i] + 1:second]
            merged[i]=read

        # print(merged)
        skill=[]

        education=[]
        experience=[]
        for i in merged.keys():
            for j in keywordSkill:
                if i==j:
                    skill = (merged[i])
                    skillName=i
                    break
            for m in keywordEducation:
                if i==m:
                    education = merged[i]
                    educationName=i
                    break
            for n in keywordExperience:
                if i==n:
                    experience = merged[i]
                    experienceName=i
                    break
        ListSkill=[]
        print(txt)

        for i in skill:
            ListSkill+=i.split()
        print(skillName,':',ListSkill)

        ListEducation=[]
        for i in education:
            ListEducation+=i.split()
        print(educationName,':',ListEducation)

        print(experienceName,':',experience)

        SkillWords=[
        'cobra','javascript','jscript','julia','matlab','numpy','r','sas','access','excel','outlook','powerpoint','Access',
        'Excel','Outlook','powerpoint','databases','sap','SciPy','matplotlib','sckit-learn','graphlab','image processing','html','css',
        'php','python','c','c++','java','mysql','sql','jquery', 'json', 'linux',]
        FilteredSkill=[]
        for i in SkillWords:
            if i in ListSkill:
                FilteredSkill.append(i)

        print("Filtered Skill:",FilteredSkill)
    # 'BE','B.E.', 'B.E', 'BS', 'B.S', 'ME', 'M.E', 'M.E.', 'MS', 'M.S', 'BTECH', 'MTECH',
    #                     'SSC', 'HSC', 'CBSE', 'ICSE', 'X', 'XII', 'BACHELORS'

        EducationWords=['bachelor\'s', 'bachelor', 'master','enginering', 'diploma','computer', 'science', 'bim', 'b.e', 'b.e.',
                        'master\'s', 'btech', 'ms','m.s', 'me', 'm.e', 'm.e.']
        FilteredEducation=[]
        for i in EducationWords:
            if i in ListEducation:
                FilteredEducation.append(i)
        skillset='skillset'
        print("Filtered Education:",FilteredEducation)
        for i in merged:
            if i in keywordSkill:
                merged[i]=FilteredSkill
                i=skillset

            if i in keywordEducation:
                merged[i]=FilteredEducation
                # education=i
            if i in keywordExperience:
                merged[i]=0
        SkillEducation=FilteredSkill+FilteredEducation
        print('List of Skill and Education from CV',SkillEducation)

        # if merged dic is to pass to json for elastic search
        # print(merged)
        # with open('data.json','w') as file:
        #
        #     json.dump(merged,file)

        #ahileko kaam chalauko lagi
        job_description_skill=['php','json','python']
        # sum_skill=FilteredSkill+job_description_skill


        job_description_education=['bachelor\'s']
        print('skill from job desciption',job_description_skill)
        print('education from job description', job_description_education)

        job_description_SkillEducation=job_description_skill+job_description_education
        print('List of Skill and education from Job description',job_description_SkillEducation)

        #cosine simiarity
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
        # vocab=['php','json','python']#jobdescription
        vectoriser = CountVectorizer().fit(job_description_SkillEducation)
        vectoriser.vocabulary_ # show the word-matrix position pairs

        # Analyse  list_1
        # list_1 = ['javascript', 'html', 'css', 'php', 'c++', 'mysql', 'jquery', 'json', 'linux']#skill form cv1
        SkillEducation_vect, SkillEducation_cos = vect_cos(vectoriser, [' '.join(SkillEducation)])

        # Analyse list_2
        # list_2 =['javascript', 'html', 'css', 'php', 'c++']#skill from cV2
        # list_2_vect, list_2_cos = vect_cos(vectoriser, [' '.join(list_2)])

        print('The cosine similarity for the first list is {}.'.format(SkillEducation_cos),'\n')
        # print('\nThe cosine similarity for the second list is {}.'.format(list_2_cos))

        # cosine=[]
        cosine.append(SkillEducation_cos)
        # combine=dict()

    print(cosine)
    combine = dict(zip(files, cosine))

    # #sorting in descending order
    # def bubble_sort(listt):
    #     for i, num in enumerate(listt):
    #         try:
    #             if listt[i+1] > num:
    #                 listt[i] = listt[i+1]
    #                 listt[i+1] = num
    #
    #
    #                 bubble_sort(listt)
    #         except IndexError:
    #             pass
    #     return listt
    # bubble_sort(combine)
    combine_sorted = sorted(combine, key=combine.get, reverse=True)
    for r in combine_sorted:
        print(r, combine[r])
    # combine = dict(zip(files, cosine))

    # for i in combine:
    #     print(i,combine[i])
    # for j in files:
    #     for i in range(0, len(cosine)):
    #         print(j,cosine[i], end=' ')#rank


convertMultiple(pdfDir,txtDir)

# for i in cosine:
#     if i<0.5:
#         print(i)


# SkillCount=0
# for i in FilteredSkill:
#     if i in job_description_skill:
#         SkillCount+=1
# print('NO. of Matced Skill', SkillCount)
# EducationCount=0
# for i in FilteredEducation:
#     if i in job_description_education:
#         EducationCount+=1
# print('NO. of Matched Education',EducationCount)
# print('\n')
# bestScore=0
# pass



#split each sentence into words


    # yesto chaeyeko
    # skills = [skills ko list]
    #education=[education ko list]


# result = extract(merged)
# result1= extract(merged)
# print(result1)

