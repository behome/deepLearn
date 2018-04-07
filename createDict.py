#sys.setdefaultencoding('utf-8')
#encoding=utf-8
import jieba
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def createDict(data_dir):
	word_dict = {}
	a=0
	for file_name in os.listdir(data_dir):
		file_path = os.path.join(data_dir, file_name)
		if not os.path.isfile(file_path):
			continue
		print file_name
		with open(file_path,'r') as f:
			for line in f:
				line_split = line.strip().split("\t")
				doc = line_split[1]
				for sent in doc.strip().split('。'):
					for w in jieba.lcut(sent, cut_all=False):
						if word_dict.has_key(w):
							continue
						word_dict[w] = a;
						a+=1;
	return word_dict
def main():
	word_dict = createDict('data')
	with open("word_dict.txt",'w+') as f:
		for k,v in word_dict.items():
			f.write(str(k).decode('utf-8') + "\t" + str(v) + "\n")

if __name__ == '__main__':
	main()

