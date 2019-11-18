gloveFile = "data\\glove.6B.50d.txt"
import numpy as np
import scipy
import re
import sys
from nltk.corpus import stopwords
import convertapi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox,QLineEdit
from framfile import Ui_MainWindowSecond
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
class Sentence:
    convertapi.api_secret = 'pktrevhuuFmDvpxB'
    def loadGloveModel(self,gloveFile):
        print ("Loading Glove Model")
        with open(gloveFile, encoding="utf8" ) as f:
            content = f.readlines()
        model = {}
        for line in content:
            splitLine = line.split()
            word = splitLine[0]
            embedding = np.array([float(val) for val in splitLine[1:]])
            model[word] = embedding
        print("Done.", len(model), " words loaded!")
        return model
    def preprocess(self,raw_text):
        # keep only words
        letters_only_text = re.sub("[^a-zA-Z]", " ", raw_text)

        # convert to lower case and split
        words = letters_only_text.lower().split()

        # remove stopwords
        stopword_set = set(stopwords.words("english"))
        cleaned_words = list(set([w for w in words if w not in stopword_set]))

        return cleaned_words

    # def cosine_distance_between_two_words(word1, word2):
    #     return (1- scipy.spatial.distance.cosine(model[word1], model[word2]))
    # def calculate_heat_matrix_for_two_sentences(s1,s2):
    #     s1 = preprocess(s1)
    #     s2 = preprocess(s2)
    #     result_list = [[cosine_distance_between_two_words(word1, word2) for word2 in s2] for word1 in s1]
    #     result_df = pd.DataFrame(result_list)
    #     result_df.columns = s2
    #     result_df.index = s1
    #     return result_df

    def cosine_distance_wordembedding_method(self, s1, s2, list_widget = None,list_widget2 = None):
        model = self.loadGloveModel(gloveFile)
        try:
            vector_1 = np.mean([model[word] for word in self.preprocess(s1)],axis=0)
            vector_2 = np.mean([model[word] for word in self.preprocess(s2)],axis=0)
        except:
            vector_1=[0]
            vector_2=[1]
        cosine = scipy.spatial.distance.cosine(vector_1, vector_2)
        similarity=round((1-cosine)*100,2)
        print('Word Embedding method with a cosine distance asses that our two documents are similar to',similarity,'%')
        if list_widget and list_widget2:
            if similarity == 100:
                list_widget.setStyleSheet("color:#fcdf03;")
                list_widget2.setStyleSheet("color:#fcdf03")
            elif similarity >= 80 and similarity < 100:
                list_widget.setStyleSheet("color:#aa00ff;")
                list_widget2.setStyleSheet("color:#aa00ff")
            elif similarity >= 70 and similarity < 80:
                list_widget.setStyleSheet("color:#18aac7;")
                list_widget2.setStyleSheet("color:#18aac7")
            elif similarity >= 60 and similarity < 70:
                list_widget.setStyleSheet("color:#1f992d;")
                list_widget2.setStyleSheet("color:#1f992d")





            else:
                list_widget.setStyleSheet("color:#d41717;")
                list_widget2.setStyleSheet("color:#d41717")
        # if similarity > 90:
        #     self.app = QtWidgets.QApplication(sys.argv)
        #     self.MainWindow = QtWidgets.QMainWindow()
        #     self.ui = Ui_MainWindowSecond()
        #     self.ui.setupUi(self.MainWindow)
        #     self.my_line_edit = QtGui.QLineEdit()
        #     self.my_line_edit.listWidget.setStyleSheet("color: rgb(255, 97, 208);")


    # def heat_map_matrix_between_two_sentences(s1,s2):
    #     # df = calculate_heat_matrix_for_two_sentences(s1,s2)
    #     #
    #     # fig, ax = plt.subplots(figsize=(5,5))
    #     # ax_blue = sns.heatmap(df, cmap="YlGnBu")
    #     # ax_red = sns.heatmap(df)
    #     print(cosine_distance_wordembedding_method(s1, s2))
        # return ax_blue
    # result = convertapi.convert('txt', { 'File': r'C:\Users\Cyberprism\Downloads\mca 2019\blind\blind.docx'})
    # # save to file
    # path=r'C:\Users\Cyberprism\Documents\mca2019 project\TextSimilarity\text1.txt'
    # result.file.save(path)
    # f1=open(path, encoding="utf8")
    # # f2=open(r'C:\Users\Cyberprism\Documents\mca2019 project\TextSimilarity\text.txt')
    # ss1=f1.read()
    # # ss2=f2.read()
    # # ss1 = 'The president greets the press in Chicago'
    # ss2 = 'Obama speaks to the media in Illinois'
    # model = loadGloveModel(gloveFile)
    # heat_map_matrix_between_two_sentences(ss1,ss2)
if __name__== "__main__":
    se=Sentence()
    path =  r'C:\Users\Cyberprism\Downloads\mca 2019\blind\blind.docx'
    result = convertapi.convert('txt', {'File': path})
    # save to file
    path = r'C:\Users\Cyberprism\Documents\mca2019 project\TextSimilarity\text1.txt'
    # result.file.save(path)
    result.save_files(path)
    f1 = open(path, encoding="utf8")
    # f2=open(r'C:\Users\Cyberprism\Documents\mca2019 project\TextSimilarity\text.txt')
    ss1 = f1.read()
    # ss2=f2.read()
    # ss1 = 'The president greets the press in Chicago'
    ss2 = 'Obama speaks to the media in Illinois'
    se.cosine_distance_wordembedding_method(ss1, ss2)
