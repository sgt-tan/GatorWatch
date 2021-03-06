# -*- coding: utf-8 -*-
#!/usr/bin/python3

from packages import GuideScraper
from packages import LocalMoviesScraper
from packages import tmdbutils
from packages import nlu
import speech_recognition as sr
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QPushButton, QAction, QTableWidget,QTableWidgetItem
from PyQt5.QtGui import QPainter, QColor, QPen, QPalette
import sys
from playsound import playsound
import time
from packages import GenerateAudio
import random
from packages import Logging
from packages import CalendarSystem
import datetime
import os

class ShowListing:
    name = ""
    episode_name = ""
    episode = ""
    description = ""
    channel = ""
    date = ""
    time = ""

    def __init__(self, name, episode_name, episode, description, channel, date, time):
        self.name = name
        self.episode_name = episode_name
        self.episode = episode
        self.description = description
        self.channel = channel
        self.date = date
        self.time = time



class App(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.showMaximized()

class Bubble(QtWidgets.QLabel):
    def __init__(self,text):
        super(Bubble,self).__init__(text)
        self.setContentsMargins(5,5,5,5)
        self.setWordWrap(True)
        self.setSizePolicy

    def paintEvent(self, e):

        p = QtGui.QPainter(self)
        p.setRenderHint(QtGui.QPainter.Antialiasing,True)
        p.drawRoundedRect(0,0,self.width()-1,self.height()-1,5,5)

        super(Bubble,self).paintEvent(e)        

class MyWidget(QtWidgets.QWidget):

    def __init__(self,text,left=True):
        super(MyWidget,self).__init__()

        hbox = QtWidgets.QHBoxLayout()

        label = Bubble(text)

        if not left:
            hbox.addSpacerItem(QtWidgets.QSpacerItem(1,1,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Preferred))

        hbox.addWidget(label)

        if left:
            hbox.addSpacerItem(QtWidgets.QSpacerItem(1,1,QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Preferred))            

        hbox.setContentsMargins(0,0,0,0)

        self.setLayout(hbox)
        self.setContentsMargins(0,0,0,0)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1233, 869)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(220, 199, 170);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.infoScrollLayout = QtWidgets.QVBoxLayout()
        self.infoScrollLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.infoScrollLayout.setObjectName("infoScrollLayout")
        self.infoScrollArea = QtWidgets.QScrollArea(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoScrollArea.sizePolicy().hasHeightForWidth())
        self.infoScrollArea.setSizePolicy(sizePolicy)
        self.infoScrollArea.setMinimumSize(QtCore.QSize(600, 845))
        self.infoScrollArea.setAutoFillBackground(True)
        self.infoScrollArea.setStyleSheet("background-color: rgb(107, 122, 143);")
        self.infoScrollArea.setWidgetResizable(True)
        self.infoScrollArea.setObjectName("infoScrollArea")
        self.infoScrollContents = QtWidgets.QWidget()
        self.infoScrollContents.setGeometry(QtCore.QRect(0, 0, 598, 843))
        self.infoScrollContents.setObjectName("infoScrollContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.infoScrollContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.infoLayout = QtWidgets.QVBoxLayout()
        self.infoLayout.setObjectName("infoLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.infoScrollContents)
        self.tableWidget.setAutoFillBackground(True)
        self.tableWidget.setStyleSheet("background-color: rgb(107, 122, 143);")
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setRowCount(500)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setObjectName("tableWidget")
        self.infoLayout.addWidget(self.tableWidget)
        self.verticalLayout_3.addLayout(self.infoLayout)
        self.infoScrollArea.setWidget(self.infoScrollContents)
        self.infoScrollLayout.addWidget(self.infoScrollArea)
        self.gridLayout.addLayout(self.infoScrollLayout, 0, 1, 1, 1)
        self.msgScrollLayout = QtWidgets.QVBoxLayout()
        self.msgScrollLayout.setObjectName("msgScrollLayout")
        self.msgScrollArea = QtWidgets.QScrollArea(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.msgScrollArea.sizePolicy().hasHeightForWidth())
        self.msgScrollArea.setSizePolicy(sizePolicy)
        self.msgScrollArea.setMinimumSize(QtCore.QSize(600, 845))
        self.msgScrollArea.setAutoFillBackground(True)
        self.msgScrollArea.setStyleSheet("background-color: rgb(247, 136, 47);")
        self.msgScrollArea.setWidgetResizable(True)
        self.msgScrollArea.setObjectName("msgScrollArea")
        self.msgScrollContents = QtWidgets.QWidget()
        self.msgScrollContents.setGeometry(QtCore.QRect(0, 0, 598, 843))
        self.msgScrollContents.setObjectName("msgScrollContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.msgScrollContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.msgLayout = QtWidgets.QVBoxLayout()
        self.msgLayout.setObjectName("msgLayout")
        self.verticalLayout_2.addLayout(self.msgLayout)
        self.speakBtn = QtWidgets.QPushButton(self.msgScrollContents)
        self.speakBtn.setObjectName("speakBtn")
        self.verticalLayout_2.addWidget(self.speakBtn)
        self.msgScrollArea.setWidget(self.msgScrollContents)
        self.msgScrollLayout.addWidget(self.msgScrollArea)
        self.gridLayout.addLayout(self.msgScrollLayout, 0, 0, 1, 1)
        #self.msgLayout.addWidget(self.speakBtn)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.speakBtn.clicked.connect(self.buttonClick)
        self.currRow = 0
        #variable to know which table header to print 3=tmdb_movies, 1=local_movies, 2= tv show, 3 =calender
        self.tableMode= 0
        self.isListening = False
        self.speechApp()
        self.speakBtn.setToolTip("Not listening right now...")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "GatorWatch"))
        self.speakBtn.setText(_translate("Form", "Speak"))

    def buttonClick(self):
        self.speechApp()

    def toolTipToggle(self):
        if(self.isListening == False):
            self.speakBtn.setToolTip("Listening to User...")
            self.isListening=True
        else:
            self.speakBtn.setToolTip("Not listening right now...")
            self.isListening = False

    def rerun(self):
        global timeouts
        try:
            with m as source: 
                #self.toolTipToggle()
                audio = r.listen(source)
            userInput = r.recognize_google(audio)
            #self.toolTipToggle()
            # userInput = input("Input: ")
            return userInput

        except sr.UnknownValueError:
            print("Oops! Didn't catch that")

            self.msgLayout.addWidget(MyWidget("I'm sorry, I didn't get that. Can say that again? You can also cancel what I am doing.\n"))
            Logging.write("System", "I'm sorry, I didn't get that. Can say that again? You can also cancel what I am doing.")
            playsound("packages/audio_files/misunderstood1.mp3")

            userInput = None
            timeouts += 1
            return userInput

        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
            self.msgLayout.addWidget(MyWidget("Couldn't request results from Google Speech Recognition service. {0}\n".format(e)))
            Logging.write("System", "Couldn't request results from Google Speech Recognition service.")
            playsound("packages/audio_files/google_fail.mp3")
            userInput = None
            return userInput

    def readjustConfidence(self, userInput, interpretation):
        userInput = userInput.split()

        CONFIDENCE_BOOST = 0.20

        lookupKeywords = ["lookup", "details", "description", "overview", "info", "more"]
        addCalendarKeywords = ["add", "save"]
        removeCalendarKeywords = ["remove", "delete"]
        viewCalendarKeywords = ["view"]
        instructionsKeywords = ["help", "instructions", "commands"]

        # Save the index for each intent so we don't need to constantly run a for loop
        intentIndexMap = {}
        i = 0
        for intent in interpretation["intent_ranking"]:
            intentIndexMap[intent["name"]] = i
            i += 1

        # If the userInput matches one of the keywords, increase that particular intent
        for word in userInput:
            word = word.lower()
            try:
                if word in lookupKeywords:
                    interpretation["intent_ranking"][intentIndexMap["lookup_details"]] += CONFIDENCE_BOOST
                if word == "calendar":
                    interpretation["intent_ranking"][intentIndexMap["add_to_calendar"]]["confidence"] += CONFIDENCE_BOOST
                    interpretation["intent_ranking"][intentIndexMap["remove_from_calendar"]]["confidence"] += CONFIDENCE_BOOST
                    interpretation["intent_ranking"][intentIndexMap["view_calendar"]]["confidence"] += CONFIDENCE_BOOST
                if word in addCalendarKeywords:
                    interpretation["intent_ranking"][intentIndexMap["add_to_calendar"]]["confidence"] += CONFIDENCE_BOOST
                elif word in removeCalendarKeywords:
                    interpretation["intent_ranking"][intentIndexMap["remove_from_calendar"]]["confidence"] += CONFIDENCE_BOOST
                elif word in viewCalendarKeywords:
                    interpretation["intent_ranking"][intentIndexMap["view_calendar"]]["confidence"] += CONFIDENCE_BOOST
                elif word in instructionsKeywords:
                    interpretation["intent_ranking"][intentIndexMap["show_instructions"]]["confidence"] += CONFIDENCE_BOOST
            except:
                print("No intent")

        # After readjusting the confidences, find the intent name with the highest confidence
        newIntent = interpretation["intent"]["name"]
        largestConfidence = interpretation["intent"]["confidence"]
        for intent in interpretation["intent_ranking"]:
            if intent["confidence"] > largestConfidence:
                largestConfidence = intent["confidence"]
                newIntent = intent["name"]

        interpretation["intent"]["name"] = newIntent
        interpretation["intent"]["confidence"] = largestConfidence

        return interpretation

    def decipherTime(self, input_audio):
        input_audio = input_audio.lower()
        print(input_audio)
        hour = ""
        if "o'clock" in input_audio or "o clock" in input_audio or "clock " in input_audio:
            i = 0
            while input_audio[i] != " ":
                hour += input_audio[i]
                i += 1
            hour += ":00"
        else:
            tokens = input_audio.split()
            hour = tokens[0]

        if ":" not in hour:
            hour += ":00"

        if "p.m." in input_audio or "pm" in input_audio or "P.M." in input_audio or "PM" in input_audio:
            hour += "pm"
        else:
            hour += "am"

        print(hour)

        return hour

    def speechApp(self):
        global previousIntent
        global theaters
        global listings
        global start
        global negations
        global misunderstands
        global timeouts
        global num
        
        if start:
            Logging.write("System", "Hello! I’m GatorWatch - I help you find movies and TV shows!")
            self.msgLayout.addWidget(MyWidget("Hello! I’m GatorWatch - I help you find movies and TV shows!"))
            playsound("packages/audio_files/start1.mp3")

            Logging.write("System", "If you need help about with what you can do, ask!")
            self.msgLayout.addWidget(MyWidget("If you need help about with what you can do, ask!"))
            playsound("packages/audio_files/start2.mp3")

            start = False
            return

        try:
            print("Say something!")
            
            with m as source:  
                #self.toolTipToggle()
                audio = r.listen(source)

            try:
                # recognize speech using Google Speech Recognition                 
                # self.toolTipToggle()
                userInput = r.recognize_google(audio)
                # userInput = input("Input: ")
                Logging.write("User", userInput)

                print("You said {}".format(userInput))
                self.msgLayout.addWidget(MyWidget(format(userInput), left=False))

                # Get the intent from a model
                interpretation = nlu.getInterpretation(userInput)
                interpretation = self.readjustConfidence(userInput, interpretation)
                print(interpretation)
                intent = interpretation["intent"]["name"]
                confidence = interpretation["intent"]["confidence"]
                entities = interpretation["entities"]
                print("The intent was " + str(intent))

                CONFIDENCE_THRESHHOLD = 0.15

                if (previousIntent is None):
                    previousIntent = intent

                # TODO: Find a way to handle low confidence intents


                if (confidence < CONFIDENCE_THRESHHOLD):

                    Logging.write("System", "I'm sorry, I didn't get that. Can you rephrase that?")
                    self.msgLayout.addWidget(MyWidget("I'm sorry, I didn't get that. Can you rephrase that?"))
                    playsound("packages/audio_files/misunderstood.mp3")

                # Display list of popular movies
                elif (intent == "recommend_movie"):
                    #print tmdb_movie table header
                    if (self.currRow == 499):
                        self.tableWidget.clear()
                        self.currRow = 0
                        if (self.tableMode != 3):
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Title"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Rating Average"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Summary"))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem("Genres"))
                            self.currRow+=1

                            self.tableMode = 3
                    else:    
                        if (self.tableMode != 3):
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Title"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Rating Average"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Summary"))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem("Genres"))
                            self.currRow+=1
                            self.tableMode = 3

                    # Attempt to extract genres from the user input
                    # If we find genres, do a search with that list
                    # Otherwise return the default popular list
                    genreStringList = tmdbutils.getGenreStringList()
                    userGenres = []

                    for item in entities:
                        if (item["entity"] == "genre" and item["value"].title() in genreStringList):
                            userGenres.append(item["value"].title())

                    # If no genres specified, do default search
                    if not userGenres:
                        popularMovies = tmdbutils.getPopularMovies()

                        # Pick a random movie to say
                        random.seed()
                        number = random.randint(0, len(popularMovies))

                        output = GenerateAudio.generate(intent=intent, entities=[popularMovies[number].title, popularMovies[number].voteAverage], num=num)
                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))

                        path = "audio_files/temp" + str(num) + ".mp3"
                        playsound(path)
                        num += 1
                        #os.remove("audio_files/temp.mp3")


                        itemLength = len(popularMovies)
                        #populate table with popularmovies items
                        if (itemLength+self.currRow < 499):
                            for movieItem in popularMovies:
                                self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(movieItem.title))
                                self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(str(movieItem.voteAverage)))
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(movieItem.overview))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(str(movieItem.genreStrings)))
                                self.currRow+=1
                        else:
                            self.tableWidget.clear()
                            self.currRow = 0
                            for movieItem in popularMovies:
                                self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(movieItem.title))
                                self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(str(movieItem.voteAverage)))
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(movieItem.overview))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(str(movieItem.genreStrings)))
                                self.currRow+=1
                        self.tableWidget.resizeColumnsToContents()
                    else:
                        popularMoviesWithGenres = tmdbutils.getPopularMoviesWithGenre(userGenres)

                        random.seed()
                        number = random.randint(0, len(popularMoviesWithGenres))
                        output = GenerateAudio.generate(intent="recommend_movie_genre", entities=[userGenres[0], popularMoviesWithGenres[number].title, popularMoviesWithGenres[number].voteAverage], num=num)
                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))

                        path = "audio_files/temp" + str(num) + ".mp3"
                        playsound(path)
                        num += 1

                        #populate table with popularMoviesWithGenres items
                        itemLength = len(popularMoviesWithGenres)
                        if (itemLength+self.currRow < 499):
                            for movieItem in popularMoviesWithGenres:
                                self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(movieItem.title))
                                self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(str(movieItem.voteAverage)))
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(movieItem.overview))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(str(movieItem.genreStrings)))
                                self.currRow+=1
                        else:
                            self.tableWidget.clear()
                            self.currRow = 0
                            for movieItem in popularMoviesWithGenres:
                                self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(movieItem.title))
                                self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(str(movieItem.voteAverage)))
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(movieItem.overview))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(str(movieItem.genreStrings)))
                                self.currRow+=1
                        self.tableWidget.resizeColumnsToContents()

                elif (intent == "lookup_details"):
                    movieToLookup = None

                    if (len(entities) != 0):
                        if (entities[0]["entity"] == "movie"):
                            movieToLookup = entities[0]["value"]

                    if movieToLookup is None or movieToLookup == "":

                        Logging.write("System", "Okay, what movie do you want to know more about?")
                        self.msgLayout.addWidget(MyWidget("Okay, what movie do you want to know more about?"))
                        playsound("packages/audio_files/find_movie.mp3")

                        while (movieToLookup is None or movieToLookup == ""):
                            movieToLookup = self.rerun()

                        Logging.write("User", movieToLookup)
                        self.msgLayout.addWidget(MyWidget(format(movieToLookup), left=False))

                        if "cancel" in movieToLookup or "stop" in movieToLookup:
                            Logging.write("System", "Okay, I've stopped what I was doing. What do you want to do now?")
                            self.msgLayout.addWidget(MyWidget("Okay, I've stopped what I was doing. What do you want to do now?"))
                            playsound("packages/audio_files/cancellation.mp3")
                            return

                        # Print what user says
                        self.msgLayout.addWidget(MyWidget(format(movieToLookup), left=False))
                    #print tmdb_movie table header
                    if (self.currRow == 499):
                        self.tableWidget.clear()
                        self.currRow = 0
                        if (self.tableMode != 3):
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Title"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Rating Average"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Summary"))
                            self.currRow+=1

                            self.tableMode = 3
                    else:    
                        if (self.tableMode != 3):

                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Title"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Rating Average"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Summary"))
                            self.currRow+=1

                            self.tableMode = 3   

                    temp_movie = movieToLookup
                    movieToLookup = tmdbutils.searchForMovie(movieToLookup)

                    if movieToLookup == []:
                        #print("There is no movie")
                        output = GenerateAudio.generate("no_movie", entities=[temp_movie], num=num)
                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))
                        path = "audio_files/temp" + str(num) + ".mp3"
                        playsound(path)
                        num += 1

                    else:
                        output = GenerateAudio.generate(intent, entities=[movieToLookup[0].title], num=num)
                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))
                        path = "audio_files/temp" + str(num) + ".mp3"
                        playsound(path)
                        num += 1
                        #self.infoLayout.addWidget(MyWidget("Name: " + movieToLookup.title + "\nDescription: " + movieToLookup.overview))

                        #os.remove("audio_files/temp.mp3")

                        #populate table with movieToLookup items
                        itemLength = len(movieToLookup)
                        if (itemLength+self.currRow < 499):
                            for movieItem in movieToLookup:
                                self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(movieItem.title))
                                self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(str(movieItem.voteAverage)))
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(movieItem.overview))
                                self.currRow+=1
                        else:
                            self.tableWidget.clear()
                            self.currRow = 0
                            for movieItem in movieToLookup:
                                self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(movieItem.title))
                                self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(str(movieItem.voteAverage)))
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(movieItem.overview))
                                self.currRow+=1
                        self.tableWidget.resizeColumnsToContents()

                # Command: Search show [show name]
                elif (intent == "show_tv"):
                    userTvShow = None

                    if (len(entities) != 0):
                        if (entities[0]["entity"] == "tv_show"):
                            userTvShow = entities[0]["value"]

                    if userTvShow is None or userTvShow == "":
                        Logging.write("System", "Okay, what show do you want to look up?")
                        self.msgLayout.addWidget(MyWidget("Okay, what show do you want to look up?"))
                        playsound("packages/audio_files/show_tv_question.mp3")

                        while (userTvShow is None or userTvShow == ""):
                            userTvShow = self.rerun()


                        Logging.write("User", userTvShow)
                        self.msgLayout.addWidget(MyWidget(format(userTvShow), left=False))

                        if "cancel" in userTvShow.lower() or "stop" in userTvShow.lower():
                            Logging.write("System", "Okay, I've stopped what I was doing. What do you want to do now?")
                            self.msgLayout.addWidget(MyWidget("Okay, I've stopped what I was doing. What do you want to do now?"))
                            playsound("packages/audio_files/cancellation.mp3")
                            return

                        # Print what user says
                    #print tv_listings table header
                    if (self.currRow == 499):
                        self.tableWidget.clear()
                        self.currRow = 0
                        if (self.tableMode != 2):
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Name"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Episode Name"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Episode #"))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem("Description"))
                            self.tableWidget.setItem(self.currRow,4, QTableWidgetItem("Channel"))
                            self.tableWidget.setItem(self.currRow,5, QTableWidgetItem("Date"))
                            self.tableWidget.setItem(self.currRow,6, QTableWidgetItem("Time"))
                            self.currRow+=1
                            self.tableMode = 2
                    else:
                        if (self.tableMode != 2):
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Name"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Episode Name"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Episode #"))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem("Description"))
                            self.tableWidget.setItem(self.currRow,4, QTableWidgetItem("Channel"))
                            self.tableWidget.setItem(self.currRow,5, QTableWidgetItem("Date"))
                            self.tableWidget.setItem(self.currRow,6, QTableWidgetItem("Time"))
                            self.currRow+=1
                            self.tableMode = 2
                    listings = GuideScraper.searchTVGuide(userTvShow)
                    itemLength = len(listings)
                    if listings is None or len(listings) == 0:
                        # Couldn't find any TV shows
                        output = GenerateAudio.generate("no_tv_shows", entities=[userTvShow], num=num)

                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))
                        path = "audio_files/temp" + str(num) + ".mp3"
                        playsound(path)
                        num += 1
                        #os.remove("audio_files/temp.mp3")

                    else:
                        # Found TV shows
                        output = GenerateAudio.generate(intent=intent, entities=[listings[0].name, listings[0].time, listings[0].date], num=num)

                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))

                        path = "audio_files/temp" + str(num) + ".mp3"
                        playsound(path)
                        num += 1
                        #os.remove("audio_files/temp.mp3")
                        #populate table with listings items

                        if(itemLength+self.currRow < 499):
                            for listing in listings:
                                self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(listing.name))
                                self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(listing.episode_name))
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(listing.episode))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(listing.description))
                                self.tableWidget.setItem(self.currRow,4, QTableWidgetItem(listing.channel))
                                self.tableWidget.setItem(self.currRow,5, QTableWidgetItem(listing.date))
                                self.tableWidget.setItem(self.currRow,6, QTableWidgetItem(listing.time))
                                self.currRow+=1
                        else:
                            self.tableWidget.clear()
                            self.currRow = 0
                            for listing in listings:
                                self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(listing.name))
                                self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(listing.episode_name))
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(listing.episode))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(listing.description))
                                self.tableWidget.setItem(self.currRow,4, QTableWidgetItem(listing.channel))
                                self.tableWidget.setItem(self.currRow,5, QTableWidgetItem(listing.date))
                                self.tableWidget.setItem(self.currRow,6, QTableWidgetItem(listing.time))
                                self.currRow+=1
                        self.tableWidget.resizeColumnsToContents()
                # Command: Search local movies
                elif (intent == "show_local"):

                    theaters = LocalMoviesScraper.searchLocalMovies()
                    Logging.write("System", "Here are the Gainesville theaters and the movies they’re showing today.")
                    self.msgLayout.addWidget(MyWidget("Here are the Gainesville theaters and the movies they’re showing today."))
                    playsound("packages/audio_files/local_movies.mp3")
                    #print local_movies table header
                    if (self.currRow == 499):
                        self.tableWidget.clear()
                        self.currRow = 0
                        if (self.tableMode != 1):
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Theater"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Address"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Movie Name"))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem("Duration"))
                            self.tableWidget.setItem(self.currRow,4, QTableWidgetItem("Time"))
                            self.currRow+=1
                            self.tableMode = 1
                    else:
                        if (self.tableMode != 1):
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Theater"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Address"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Movie Name"))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem("Duration"))
                            self.tableWidget.setItem(self.currRow,4, QTableWidgetItem("Time"))
                            self.currRow+=1
                            self.tableMode = 1
                    #populate table with theater and its movies
                    if(self.currRow+90 < 499):
                        for theater in theaters:
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(theater.name))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(theater.address))
                            for movie in theater.movies:
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(movie.name))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(movie.duration))
                                for time in movie.times:
                                    self.tableWidget.setItem(self.currRow,4, QTableWidgetItem(time))
                                    self.currRow+=1
                                self.currRow+=1
                            self.currRow+=1
                    else:
                        self.tableWidget.clear()
                        self.currRow= 0
                        for theater in theaters:
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(theater.name))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(theater.address))
                            for movie in theater.movies:
                                self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(movie.name))
                                self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(movie.duration))
                                for time in movie.times:
                                    self.tableWidget.setItem(self.currRow,4, QTableWidgetItem(time))
                                    self.currRow+=1
                                self.currRow+=1
                            self.currRow+=1
                    self.tableWidget.resizeColumnsToContents()
                elif intent == "view_calendar":
                    events = CalendarSystem.getCalendar()
                    Logging.write("System", "Okay, here is your calendar.")
                    playsound("packages/audio_files/show_calendar.mp3")
                    #print tv_listings table header
                    if (self.currRow == 499):
                        self.tableWidget.clear()
                        self.currRow = 0
                        if (self.tableMode != 2):
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Name"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Episode Name"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Episode #"))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem("Description"))
                            self.tableWidget.setItem(self.currRow,4, QTableWidgetItem("Channel"))
                            self.tableWidget.setItem(self.currRow,5, QTableWidgetItem("Date"))
                            self.tableWidget.setItem(self.currRow,6, QTableWidgetItem("Time"))
                            self.currRow+=1
                            self.tableMode = 2
                    else:
                        if (self.tableMode != 2):
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem("Name"))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem("Episode Name"))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem("Episode #"))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem("Description"))
                            self.tableWidget.setItem(self.currRow,4, QTableWidgetItem("Channel"))
                            self.tableWidget.setItem(self.currRow,5, QTableWidgetItem("Date"))
                            self.tableWidget.setItem(self.currRow,6, QTableWidgetItem("Time"))
                            self.currRow+=1
                            self.tableMode = 2
                    #populate table with calender events items
                    itemLength = len(events)
                    if(itemLength+self.currRow < 499):
                        for listing in events:
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(listing.name))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(listing.episode_name))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(listing.episode))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(listing.description))
                            self.tableWidget.setItem(self.currRow,4, QTableWidgetItem(listing.channel))
                            self.tableWidget.setItem(self.currRow,5, QTableWidgetItem(listing.date))
                            self.tableWidget.setItem(self.currRow,6, QTableWidgetItem(listing.time))
                            self.currRow+=1
                    else:
                        self.tableWidget.clear()
                        self.currRow = 0
                        for listing in events:
                            self.tableWidget.setItem(self.currRow,0, QTableWidgetItem(listing.name))
                            self.tableWidget.setItem(self.currRow,1, QTableWidgetItem(listing.episode_name))
                            self.tableWidget.setItem(self.currRow,2, QTableWidgetItem(listing.episode))
                            self.tableWidget.setItem(self.currRow,3, QTableWidgetItem(listing.description))
                            self.tableWidget.setItem(self.currRow,4, QTableWidgetItem(listing.channel))
                            self.tableWidget.setItem(self.currRow,5, QTableWidgetItem(listing.date))
                            self.tableWidget.setItem(self.currRow,6, QTableWidgetItem(listing.time))
                            self.currRow+=1
                    self.tableWidget.resizeColumnsToContents()
                elif intent == "add_to_calendar":
                    if previousIntent == "show_local":
                        #print("Ask for theater")
                        Logging.write("System", "Okay, what's the movie theater? The Hippodrome, Royal Park, or Butler Town?")
                        self.msgLayout.addWidget(MyWidget("Okay, what's the movie theater? The Hippodrome, Royal Park, or Butler Town?"))
                        playsound("packages/audio_files/movie_theater_question.mp3")

                        theater_name = None
                        while True:
                            theater_name = None
                            # Get input and verify

                            while theater_name is None:
                                # print("What movie do you want to look up")
                                theater_name = self.rerun()

                            Logging.write("User", theater_name)
                            self.msgLayout.addWidget(MyWidget(format(theater_name), left=False))

                            if "cancel" in theater_name.lower() or "stop" in theater_name.lower():
                                Logging.write("System",
                                              "Okay, I've stopped what I was doing. What do you want to do now?")
                                self.msgLayout.addWidget(
                                    MyWidget("Okay, I've stopped what I was doing. What do you want to do now?"))
                                playsound("packages/audio_files/cancellation.mp3")
                                return

                            # Need to verify if theater is one of the three - if it isn't, keep asking the user
                            # if theater_name.lower() != "hippodrome" and theater_name.lower() != "royal park" and theater_name.lower() != "butler town":
                            if "hippodrome" not in theater_name.lower() and "royal park" not in theater_name.lower() and "butler town" not in theater_name.lower():
                                Logging.write("System", "I'm sorry, that theater is not in Gainesville. The Gainesville theaters are: The Hippodrome, Royal Park, and Butler Town. You can also cancel what I am doing.")
                                self.msgLayout.addWidget(MyWidget("I'm sorry, that theater is not in Gainesville. The Gainesville theaters are: The Hippodrome, Royal Park, and Butler Town. You can also cancel what I am doing."))
                                playsound("packages/audio_files/invalid_theater.mp3")
                                misunderstands += 1

                            else:
                                break

                        # Ask for movie name
                        movie_name = None
                        Logging.write("System", "And the movie name?")
                        self.msgLayout.addWidget(MyWidget("And the movie name?"))
                        playsound("packages/audio_files/movie_name_question.mp3")

                        while True:
                            movie_name = None
                            while movie_name is None:
                                movie_name = self.rerun()

                            movie_exists = False

                            Logging.write("User", movie_name)
                            self.msgLayout.addWidget(MyWidget(format(movie_name), left=False))

                            if "cancel" in movie_name.lower() or "stop" in movie_name.lower():
                                Logging.write("System",
                                              "Okay, I've stopped what I was doing. What do you want to do now?")
                                self.msgLayout.addWidget(
                                    MyWidget("Okay, I've stopped what I was doing. What do you want to do now?"))
                                playsound("packages/audio_files/cancellation.mp3")
                                return


                            # Need to verify if movie name exists
                            for theater in theaters:
                                if theater_name.lower() == theater.name.lower():
                                    for movie in theater.movies:
                                        tokens = movie_name.lower().split()

                                        for token in tokens:
                                            if token in movie.name.lower():
                                                #print("Movie exists")
                                                movie_exists = True
                                                break

                            if movie_exists:
                                break

                            else:
                                Logging.write("System", "I'm sorry, that movie does not exist. Please state one on the list. You can also cancel what I am doing.")
                                self.msgLayout.addWidget(MyWidget("I'm sorry, that movie does not exist. Please state one on the list. You can also cancel what I am doing."))
                                playsound("packages/audio_files/invalid_movie_name.mp3")
                                misunderstands += 1

                        # Ask for time

                        movie_time = None
                        Logging.write("System", "And the time of the movie?")
                        self.msgLayout.addWidget(MyWidget("And the time of the movie?"))
                        playsound("packages/audio_files/movie_time_question.mp3")

                        while True:
                            movie_time = None
                            while movie_time is None:
                                movie_time = self.rerun()

                            Logging.write("User", movie_time)
                            self.msgLayout.addWidget(MyWidget(format(movie_time), left=False))

                            if "cancel" in movie_time.lower() or "stop" in movie_time.lower():
                                Logging.write("System",
                                              "Okay, I've stopped what I was doing. What do you want to do now?")
                                self.msgLayout.addWidget(
                                    MyWidget("Okay, I've stopped what I was doing. What do you want to do now?"))
                                playsound("packages/audio_files/cancellation.mp3")
                                return

                            movie_time_exists = False
                            movie_time = self.decipherTime(movie_time)
                            # Verify if listing exists
                            for theater in theaters:
                                if theater_name.lower() == theater.name.lower():
                                    for movie in theater.movies:
                                        # Might need to tokenize movie_name

                                        tokens = movie_name.lower().split()

                                        for token in tokens:
                                            if token in movie.name.lower():
                                                #print("Movie exists")
                                                for start_time in movie.times:
                                                    if movie_time == start_time:
                                                        movie_time_exists = True
                                                        break

                            if movie_time_exists:
                                break

                            else:
                                #print("Err")
                                Logging.write("User", "That time is not available. Please state one on the list. You can also cancel what I am doing.")
                                self.msgLayout.addWidget(MyWidget("That time is not available. Please state one on the list. You can also cancel what I am doing."))
                                playsound("packages/audio_files/invalid_movie_time.mp3")
                                misunderstands += 1
                                # Movie time does not exist

                        #print("Confirm")
                        output = GenerateAudio.generate("confirm_movie", entities=[theater_name, movie_name, movie_time], num=num)
                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))
                        path = "audio_files/temp" + str(num) + ".mp3"
                        playsound(path)
                        num += 1
                        #os.remove("audio_files/temp.mp3")

                        confidence = 0

                        while confidence <= CONFIDENCE_THRESHHOLD:
                            userInput = None
                            while userInput is None:
                                userInput = self.rerun()

                            Logging.write("User", userInput)
                            self.msgLayout.addWidget(MyWidget(format(userInput), left=False))

                            if "cancel" in userInput.lower() or "stop" in userInput.lower():
                                Logging.write("System",
                                              "Okay, I've stopped what I was doing. What do you want to do now?")
                                self.msgLayout.addWidget(
                                    MyWidget("Okay, I've stopped what I was doing. What do you want to do now?"))
                                playsound("packages/audio_files/cancellation.mp3")
                                return

                            # Need to find intent
                            interpretation = nlu.getInterpretation(userInput)
                            intent = interpretation["intent"]["name"]

                            # Incorporate confidence here

                            confidence = interpretation["intent"]["confidence"]

                            if (confidence < CONFIDENCE_THRESHHOLD):

                                # print("Sorry, could you rephrase that?")
                                Logging.write("System", "I'm sorry, I didn't get that. Can you rephrase that?")
                                self.msgLayout.addWidget(MyWidget("I'm sorry, I didn't get that. Can you rephrase that?"))
                                playsound("packages/audio_files/misunderstood.mp3")
                                confidence = 0
                                misunderstands += 1

                        if intent == "affirm":
                            # Add to calendar
                            # Calculate current date
                            months = {1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"}
                            now = datetime.datetime.now()
                            month = now.month
                            day = now.day
                            date = ""

                            month = months[month]
                            day = str(day)

                            date += month + " " + day

                            listing = ShowListing(movie_name, "", "", "", theater_name, date, movie_time)
                            saved = CalendarSystem.saveCalendar(listing)

                            if saved == "True":
                                Logging.write("System","Okay, it has been added to your calendar. I will remind you about it 30 minutes before the event.")
                                self.msgLayout.addWidget(MyWidget("Okay, it has been added to your calendar. I will remind you about it 30 minutes before the event."))
                                playsound("packages/audio_files/add_to_calendar.mp3")

                            else:
                                output = GenerateAudio.generate("calendar_overlap", entities=[saved], num=num)
                                Logging.write("System", output)
                                self.msgLayout.addWidget(MyWidget(output))
                                path = "audio_files/temp" + str(num) + ".mp3"
                                playsound(path)
                                num += 1
                                #os.remove("audio_files/temp.mp3")

                        else:
                            intent = "show_local"
                            Logging.write("System", "Okay, not creating the event. What else do you want to do?")
                            self.msgLayout.addWidget(MyWidget("Okay, not creating the event. What else do you want to do?"))
                            playsound("packages/audio_files/not_creating_event.mp3")


                            #print("Do you want to change the theater, movie name, time, or cancel the event?")


                    elif previousIntent == "show_tv":
                        Logging.write("System", "Okay, what's the the name of the show that you want to add?")
                        self.msgLayout.addWidget(MyWidget("Okay, what's the the name of the show that you want to add?"))
                        playsound("packages/audio_files/show_name_question.mp3")

                        show_name = None
                        while True:
                            show_name = None
                            # Get input and verify
                            show_name_exists = False
                            while show_name is None:
                                # print("What show do you want to look up")
                                show_name = self.rerun()

                            Logging.write("User", show_name)
                            self.msgLayout.addWidget(MyWidget(format(show_name), left=False))

                            if "cancel" in show_name.lower() or "stop" in show_name.lower():
                                Logging.write("System",
                                              "Okay, I've stopped what I was doing. What do you want to do now?")
                                self.msgLayout.addWidget(
                                    MyWidget("Okay, I've stopped what I was doing. What do you want to do now?"))
                                playsound("packages/audio_files/cancellation.mp3")
                                return

                            for listing in listings:
                                tokens = show_name.lower().split()
                                for token in tokens:
                                    if token in listing.name.lower():
                                        show_name_exists = True
                                        break

                            if show_name_exists:
                                break

                            else:
                                # show does not exist
                                Logging.write("System", "I'm sorry, I didn't find that TV show. Please choose from one of the listings I found. You can also cancel what I am doing.")
                                self.msgLayout.addWidget(MyWidget("I'm sorry, I didn't find that TV show. Please choose from one of the listings I found. You can also cancel what I am doing."))
                                playsound("packages/audio_files/invalid_show_name.mp3")
                                misunderstands += 1

                        Logging.write("System", "And the day of the show?")
                        self.msgLayout.addWidget(MyWidget("And the day of the show?"))
                        playsound("packages/audio_files/show_day_question.mp3")

                        show_day = None
                        while True:
                            show_day = None
                            show_day_exists = False
                            while show_day is None:
                                show_day = self.rerun()

                            Logging.write("User", show_day)
                            self.msgLayout.addWidget(MyWidget(format(show_day), left=False))

                            if "cancel" in show_day.lower() or "stop" in show_day.lower():
                                Logging.write("System",
                                              "Okay, I've stopped what I was doing. What do you want to do now?")
                                self.msgLayout.addWidget(
                                    MyWidget("Okay, I've stopped what I was doing. What do you want to do now?"))
                                playsound("packages/audio_files/cancellation.mp3")
                                return

                            temp_day = ""

                            show_day_tokens = show_day.split()

                            if "January" in show_day_tokens:
                                temp_day += "Jan "
                            elif "February" in show_day_tokens:
                                temp_day += "Feb "
                            elif "March" in show_day_tokens:
                                temp_day += "Mar "
                            elif "April" in show_day_tokens:
                                temp_day += "Apr "
                            elif "May" in show_day_tokens:
                                temp_day += "May "
                            elif "June" in show_day_tokens:
                                temp_day += "Jun "
                            elif "July" in show_day_tokens:
                                temp_day += "Jul "
                            elif "August" in show_day_tokens:
                                temp_day += "Aug "
                            elif "September" in show_day_tokens:
                                temp_day += "Sep "
                            elif "October" in show_day_tokens:
                                temp_day += "Oct "
                            elif "November" in show_day_tokens:
                                temp_day += "Nov "
                            elif "December" in show_day_tokens:
                                temp_day += "Dec "

                            temp_day += show_day_tokens[len(show_day_tokens)-1]

                            for listing in listings:
                                tokens = show_name.lower().split()
                                for token in tokens:
                                    if token in listing.name.lower():
                                        if temp_day == listing.date:
                                            show_day_exists = True
                                            break

                            if show_day_exists:
                                break

                            else:
                                Logging.write("System", "I'm sorry, I didn't find that there is a showing on that day. Please say another day. You can also cancel what I am doing.")
                                self.msgLayout.addWidget(MyWidget("I'm sorry, I didn't find that there is a showing on that day. Please say another day. You can also cancel what I am doing."))
                                playsound("packages/audio_files/invalid_show_day.mp3")
                                misunderstands += 1

                        Logging.write("System", "And the time of the show?")
                        self.msgLayout.addWidget(MyWidget("And the time of the show?"))
                        playsound("packages/audio_files/show_time_question.mp3")

                        show_time = None
                        while True:
                            show_time = None
                            show_time_exists = False
                            while show_time is None:
                                show_time = self.rerun()

                            Logging.write("User", show_time)
                            self.msgLayout.addWidget(MyWidget(format(show_time), left=False))

                            if "cancel" in show_time.lower() or "stop" in show_time.lower():
                                Logging.write("System",
                                              "Okay, I've stopped what I was doing. What do you want to do now?")
                                self.msgLayout.addWidget(
                                    MyWidget("Okay, I've stopped what I was doing. What do you want to do now?"))
                                playsound("packages/audio_files/cancellation.mp3")
                                return

                            show_time = self.decipherTime(show_time)

                            event = None
                            for listing in listings:
                                tokens = show_name.lower().split()
                                for token in tokens:
                                    if token in listing.name.lower():
                                        if temp_day == listing.date:
                                            if show_time == listing.time:
                                                show_time_exists = True
                                                event = listing
                                                break

                            if show_time_exists:
                                break

                            else:
                                Logging.write("System", "I'm sorry, I didn't find that there is a showing at that time. Please say another time. You can also cancel what I am doing.")
                                self.msgLayout.addWidget(MyWidget("I'm sorry, I didn't find that there is a showing at that time. Please say another time. You can also cancel what I am doing."))
                                playsound("packages/audio_files/invalid_show_time.mp3")
                                misunderstands += 1

                        #print("Confirm")
                        output = GenerateAudio.generate("confirm_show", entities=[show_name, show_day, show_time], num=num)
                        Logging.write("System", output)
                        self.msgLayout.addWidget(MyWidget(output))
                        path = "audio_files/temp" + str(num) + ".mp3"
                        playsound(path)
                        num += 1
                        #os.remove("audio_files/temp.mp3")

                        confidence = 0

                        while confidence <= CONFIDENCE_THRESHHOLD:
                            userInput = None
                            while userInput is None:
                                userInput = self.rerun()

                            Logging.write("User", userInput)
                            self.msgLayout.addWidget(MyWidget(format(userInput), left=False))

                            if "cancel" in userInput.lower() or "stop" in userInput.lower():
                                Logging.write("System",
                                              "Okay, I've stopped what I was doing. What do you want to do now?")
                                self.msgLayout.addWidget(
                                    MyWidget("Okay, I've stopped what I was doing. What do you want to do now?"))
                                playsound("packages/audio_files/cancellation.mp3")
                                return

                            # Need to find intent
                            interpretation = nlu.getInterpretation(userInput)
                            intent = interpretation["intent"]["name"]

                            # Incorporate confidence here

                            confidence = interpretation["intent"]["confidence"]

                            if (confidence < CONFIDENCE_THRESHHOLD):
                                # print("Sorry, could you rephrase that?")
                                Logging.write("System", "I'm sorry, I didn't get that. Can you rephrase that?")
                                self.msgLayout.addWidget(MyWidget("I'm sorry, I didn't get that. Can you rephrase that?"))
                                playsound("packages/audio_files/misunderstood.mp3")
                                confidence = 0
                                misunderstands += 1


                        if intent == "affirm":
                            saved = CalendarSystem.saveCalendar(event)

                            if saved == "True":
                                Logging.write("System","Okay, it has been added to your calendar. I will remind you about it 30 minutes before the event.")
                                self.msgLayout.addWidget(MyWidget("Okay, it has been added to your calendar. I will remind you about it 30 minutes before the event."))
                                playsound("packages/audio_files/add_to_calendar.mp3")

                            else:
                                output = GenerateAudio.generate("calendar_overlap", entities=[saved], num=num)
                                Logging.write("System", output)
                                self.msgLayout.addWidget(MyWidget(output))
                                path = "audio_files/temp" + str(num) + ".mp3"
                                playsound(path)
                                num += 1
                                #os.remove("audio_files/temp.mp3")

                        else:
                            negations += 1
                            intent = "show_tv"
                            Logging.write("System", "Okay, not creating the event. What else do you want to do?")
                            self.msgLayout.addWidget(MyWidget("Okay, not creating the event. What else do you want to do?"))
                            playsound("packages/audio_files/not_creating_event.mp3")

                    else:
                        #print("Cannot do that")
                        Logging.write("System", "You can only add events to the calendar after viewing local movies or looking up a TV show.")
                        self.msgLayout.addWidget(MyWidget("You can only add events to the calendar after viewing local movies or looking up a TV show."))
                        playsound("packages/audio_files/cannot_add_event.mp3")

                elif intent == "remove_from_calendar":
                    if previousIntent == "view_calendar":
                        events = CalendarSystem.getCalendar()
                        if len(events) == 0:
                            Logging.write("System", "You have no events to delete!")
                            self.msgLayout.addWidget(MyWidget("You have no events to delete!"))
                            playsound("packages/audio_files/no_events.mp3")

                        else:
                            #print("Ask for day")
                            Logging.write("System", "Okay, what is the day of the event that you want to delete?")
                            self.msgLayout.addWidget(MyWidget("Okay, what is the day of the event that you want to delete?"))
                            playsound("packages/audio_files/event_day_question.mp3")

                            event_day = None
                            while True:
                                event_day = None
                                event_day_exists = False

                                while event_day is None:
                                    event_day = self.rerun()

                                Logging.write("User", event_day)
                                self.msgLayout.addWidget(MyWidget(format(event_day), left=False))

                                if "cancel" in event_day.lower() or "stop" in event_day.lower():
                                    Logging.write("System",
                                                  "Okay, I've stopped what I was doing. What do you want to do now?")
                                    self.msgLayout.addWidget(
                                        MyWidget("Okay, I've stopped what I was doing. What do you want to do now?"))
                                    playsound("packages/audio_files/cancellation.mp3")
                                    return

                                temp_day = ""

                                event_day_tokens = event_day.split()

                                if "January" in event_day_tokens:
                                    temp_day += "Jan "
                                elif "February" in event_day_tokens:
                                    temp_day += "Feb "
                                elif "March" in event_day_tokens:
                                    temp_day += "Mar "
                                elif "April" in event_day_tokens:
                                    temp_day += "Apr "
                                elif "May" in event_day_tokens:
                                    temp_day += "May "
                                elif "June" in event_day_tokens:
                                    temp_day += "Jun "
                                elif "July" in event_day_tokens:
                                    temp_day += "Jul "
                                elif "August" in event_day_tokens:
                                    temp_day += "Aug "
                                elif "September" in event_day_tokens:
                                    temp_day += "Sep "
                                elif "October" in event_day_tokens:
                                    temp_day += "Oct "
                                elif "November" in event_day_tokens:
                                    temp_day += "Nov "
                                elif "December" in event_day_tokens:
                                    temp_day += "Dec "

                                temp_day += event_day_tokens[len(event_day_tokens) - 1]

                                for temp_event in events:
                                    if temp_day == temp_event.date:
                                        event_day_exists = True
                                        break

                                if event_day_exists:
                                    break
                                else:
                                    Logging.write("System", "You have no event at on that date. Please state another date. You can also cancel what I am doing.")
                                    self.msgLayout.addWidget(MyWidget("You have no event on that date. Please state another date. You can also cancel what I am doing."))
                                    playsound("packages/audio_files/invalid_event_day.mp3")
                                    misunderstands += 1
                                    event_day = None


                            #print("Ask for time")
                            Logging.write("System", "And the time of the event?")
                            self.msgLayout.addWidget(MyWidget("And the time of the event?"))
                            playsound("packages/audio_files/event_time_question.mp3")

                            event_time = None
                            while True:
                                event_time = None
                                event_time_exists = False

                                while event_time is None:
                                    event_time = self.rerun()

                                Logging.write("User", event_time)
                                self.msgLayout.addWidget(MyWidget(format(event_time), left=False))

                                if "cancel" in event_time.lower() or "stop" in event_time.lower():
                                    Logging.write("System",
                                                  "Okay, I've stopped what I was doing. What do you want to do now?")
                                    self.msgLayout.addWidget(
                                        MyWidget("Okay, I've stopped what I was doing. What do you want to do now?"))
                                    playsound("packages/audio_files/cancellation.mp3")
                                    return

                                event_time = self.decipherTime(event_time)

                                for temp_event in events:
                                    if temp_day == temp_event.date:
                                        if event_time == temp_event.time:
                                            event_time_exists = True
                                            break

                                if event_time_exists:
                                    break

                                else:
                                    Logging.write("System", "You have no event at that time. Please state another time. You can also cancel what I am doing.")
                                    self.msgLayout.addWidget(MyWidget("You have no event at that time. Please state another time. You can also cancel what I am doing."))
                                    playsound("packages/audio_files/invalid_event_time.mp3")
                                    misunderstands += 1
                                    event_time = None

                            output = GenerateAudio.generate("confirm_deletion", entities=[event_day, event_time], num=num)
                            Logging.write("System", output)
                            self.msgLayout.addWidget(MyWidget(output))
                            path = "audio_files/temp" + str(num) + ".mp3"
                            playsound(path)
                            num += 1
                            #os.remove("audio_files/temp.mp3")

                            confidence = 0

                            while confidence <= CONFIDENCE_THRESHHOLD:
                                userInput = None
                                while userInput is None:
                                    userInput = self.rerun()

                                Logging.write("User", userInput)
                                self.msgLayout.addWidget(MyWidget(format(userInput), left=False))

                                if "cancel" in userInput.lower() or "stop" in userInput.lower():
                                    Logging.write("System",
                                                  "Okay, I've stopped what I was doing. What do you want to do now?")
                                    self.msgLayout.addWidget(
                                        MyWidget("Okay, I've stopped what I was doing. What do you want to do now?"))
                                    playsound("packages/audio_files/cancellation.mp3")
                                    return

                                # Need to find intent
                                interpretation = nlu.getInterpretation(userInput)
                                intent = interpretation["intent"]["name"]

                                confidence = interpretation["intent"]["confidence"]

                                if (confidence < CONFIDENCE_THRESHHOLD):
                                    # print("Sorry, could you rephrase that?")
                                    Logging.write("System", "I'm sorry, I didn't get that. Can you rephrase that?")
                                    self.msgLayout.addWidget(
                                        MyWidget("I'm sorry, I didn't get that. Can you rephrase that?"))
                                    playsound("packages/audio_files/misunderstood.mp3")
                                    confidence = 0
                                    misunderstands += 1


                            if intent == "affirm":
                                CalendarSystem.deleteEvent(temp_day, event_time)
                                Logging.write("System", "Okay, the event has been deleted from your calendar.")
                                self.msgLayout.addWidget(MyWidget("Okay, the event has been deleted from your calendar."))
                                playsound("packages/audio_files/event_deleted.mp3")

                            else:
                                negations += 1
                                intent = "view_calendar"
                                Logging.write("System", "Okay, the event won't be deleted. What else do you want to do?")
                                self.msgLayout.addWidget(MyWidget("Okay, the event won't be deleted. What else do you want to do?"))
                                playsound("packages/audio_files/not_deleting_event.mp3")

                    # Cannot delete event unless the user has just viewed local movies or TV listings
                    else:
                        Logging.write("System", "I'm sorry, you cannot delete an event unless you have just viewed the calendar. View your calendar first before deleting.")
                        self.msgLayout.addWidget(MyWidget("I'm sorry, you cannot delete an event unless you have just viewed the calendar. View your calendar first before deleting."))
                        playsound("packages/audio_files/cannot_delete.mp3")

                elif intent == "show_instructions":
                    Logging.write("System", "You can ask for what’s showing around here today, movie suggestions, or information about a TV show or movie. You also have a calendar to store TV shows or movie events.")
                    self.msgLayout.addWidget(MyWidget("You can ask for what’s showing around here today, movie suggestions, or information about a TV show or movie. You also have a calendar to store TV shows or movie events."))
                    playsound("packages/audio_files/commands.mp3")

                elif intent == "show_calendar_instructions":
                    Logging.write("System", "The calendar stores listings for TV shows and local movies and reminds you thirty minutes before they happen. You can tell me to add any TV show or local movie listing to the calendar.")
                    self.msgLayout.addWidget(MyWidget("The calendar stores listings for TV shows and local movies and reminds you thirty minutes before they happen. You can tell me to add any TV show or local movie listing to the calendar."))
                    playsound("packages/audio_files/calendar.mp3")

                elif intent == "bye":
                    Logging.write("System", "Okay, see you later!")
                    self.msgLayout.addWidget(MyWidget("Okay, see you later!"))
                    playsound("packages/audio_files/bye.mp3")
                    Logging.end(negations, misunderstands, timeouts)
                    sys.exit()

                previousIntent = intent

                # Check time every time after user hits speak button and finished
                reminder = CalendarSystem.checkTime()
                if type(reminder) is not int:
                    # You have an event coming up in 30 minutes to watch [name] on [channel_name]
                    output = GenerateAudio.generate(intent="reminder", entities=[reminder.name, reminder.channel], num=num)
                    Logging.write("System", output)
                    self.msgLayout.addWidget(MyWidget(output))
                    path = "audio_files/temp" + str(num) + ".mp3"
                    playsound(path)
                    num += 1

            except sr.UnknownValueError:
                print("Oops! Didn't catch that")
                self.msgLayout.addWidget(MyWidget("I'm sorry, I didn't get that. Can you rephrase that?\n"))
                Logging.write("System", "I'm sorry, I didn't get that. Can you rephrase that?")
                playsound("packages/audio_files/misunderstood.mp3")
                timeouts += 1

            except sr.RequestError as e:
                print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
                self.msgLayout.addWidget(MyWidget("Couldn't request results from Google Speech Recognition service. {0}\n".format(e)))
                Logging.write("System", "Couldn't request results from Google Speech Recognition service.")
                playsound("packages/audio_files/google_fail.mp3")

        except KeyboardInterrupt:
            pass

if __name__ == '__main__':
    print(isUserAdmin())
    # if(os.path.isfile('audio_files/temp.mp3') == True):
    #     os.remove("audio_files/temp.mp3")
    app = QApplication(sys.argv)
    r = sr.Recognizer() 
    m = sr.Microphone()
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source)
    print("Set minimum energy threshold to {}".format(r.energy_threshold))

    theaters = []
    listings = []
    previousIntent = None
    start = True


    num = 0

    negations = 0
    misunderstands = 0
    timeouts = 0

    try:
        os.remove("audio_files/temp.mp3")
    except:
        print("No file to remove")


    ex = App()
    try:
        ex.show()
        sys.exit(app.exec_())
    finally:
        Logging.end(negations, misunderstands, timeouts)
