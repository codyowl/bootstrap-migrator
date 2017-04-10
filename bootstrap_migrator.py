import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-path', '--path', help="Bootstrap file path", required=False)

arguments = parser.parse_args()

source_path =arguments.path

version_3 = "* Bootstrap v3"
version_4 = "* Bootstrap v4"

def get_files(source_path):
	file_list = []
	for file in os.listdir(source_path):
		if file.endswith(".html"):
			file_list.append(os.path.join(source_path, file))
	return file_list		

#to get version (for later progress)
def version_checker(source_path):
	pass


def component_migrator(file_list):
	for file in file_list:
		file_opener = open(file)
		file_reader = file_opener.readlines()
		for content in file_reader:
			if ".table-condensed" in content:
				pass
			if ".control-label" in content:
				pass
			
			#checkboxes and radio buttons
			if ".radio" in content:
				pass
			if ".radio-inline" in content:
				pass
			if ".checkbox" in content:
				pass
			if ".checkbox-inline" in content:
				pass

			#form control size
			if ".input-lg" in content:
				pass
			if ".input-sm" in content:
				pass

			#help text
			if ".help-block" in content:
				pass

			#buttons
			#semantic styles
			if ".btn-default" or ".btn-info" in content:
				pass
			if ".btn-xs" in content:
				pass

			#images
			#responsive images
			if ".img-responsive" in content:
				pass
			#image alignment
			if ".center-block" in content:
				pass

			#dropdowns
			#Dividers 
			if ".divider" in content:
				pass

			#List Groups
			#Button List Items 
			if ".list-group-item" in content:
				pass

			#Breadcrumbs
			#classes
			if ".breadcrumb" in content:
				pass

			#Carousels
			#Carousel Item
			if ".item" in content:
				pass 
					
					






