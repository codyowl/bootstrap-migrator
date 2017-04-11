import os
import argparse
import re
#bootstrap 3 
from components import TABLE_CONDENSED as TC, CONTROL_LABEL as CL, RADIO as R, RADIO_INLINE as RL, \
CHECKBOX as C, CHECKBOX_INLINE as CI, INPUT_LG as IL, INPUT_SM as IS, HELP_BLOCK as HB, BUTTON_DEFAULT as BD, \
IMAGE_RESPONSIVE as IR, CENTER_BLOCK as CB, DIVIDER as D, LIST_GROUP_ITEM as LGI, \
BREADCUM as B, ITEM as I
#bootstrap 4 
from components import table_condensed as tc, control_label as cl, radio as r, radio_inline as rl, \
checkbox as c, checkbox_inline as ci, input_lg as il, input_sm as ism, help_block as hb, button_default as bd, \
image_responsive as ir, center_block as cb, divider as d, list_group_item as lgi, \
breadcum as b, item as i 

#listing out the alternate classes 
component_migrator_dict = {
	TC : tc,
	CL : cl,
	R : r,
	C : c,
	CI : ci,
	IL : il,
	IS : ism,
	HB : hb,
	BD : bd,
	IR : ir,
	CB : cb,
	D : d,
	LGI : lgi,
	B : b,
	I : i
}


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

def component_migrator(file, component_migrator_dict):
	regex = re.compile('|'.join(map(re.escape, component_migrator_dict)))
	def match_mapper(match):
		return component_migrator_dict[match.group(0)]
	return regex.sub(match_mapper, file)    

def migrator(file_list, component_migrator_dict):
	for file in file_list:
		file_opener = open(file)
		file_reader = file_opener.read()
		file_opener.close()
		print component_migrator(file_reader, component_migrator_dict)

if __name__ == "__main__":
	file_lister = get_files(source_path)
	print migrator(file_lister, component_migrator_dict)
