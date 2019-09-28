#!/usr/bin/env python3

class Student
	def __init__(self, name, courses, email):
		self.__set_name(name)
		self.__set_courses(courses)
		self.__set_email(email)

	def __set_name(self, name):
		self.__name = name
	def __set_courses(self, courses):
		self.__courses = courses
	def __set_email(self, email):
		self.__email = email
	
	def __get_name(self):
		return self.__name
	def __get_courses(self):
		return self.__courses
	def __get_email(self):
		return self.__email	
