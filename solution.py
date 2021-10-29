
import os

class WordIndexer:
    
    def __init__(self):
        self.final_list = {}
        self.visited_word = []

    def sortList(self):
        try:
            self.final_list = dict( sorted(self.final_list.items(), key=lambda x: x[0].lower()) )
        except Exception as e:
            print(e)
    
    
    def ifExcluded(self,word):
        try:
            excluded_words = open("exclude-words.txt","r+") 
            excluded_list = []
            content = excluded_words.read()
            excluded_list = content.split("\n")
            if word.lower() in excluded_list:
                return True
            else:
                return False
        except Exception as e:
            print(e)

    def checkPresent(self,word):
        try:
            if word in self.visited_word:
                return True
            else:
                self.visited_word.append(word)
                return False
        except Exception as e:
            print(e)

    def start_indexing(self,page,page_no):
        try:
            temp = page.readlines()
            word_list=[]
            for i in temp:
                a = i.decode("utf-8")
                word_list += a.split(" ")
            for word in word_list:
                if not word.isalpha():
                    continue
                if self.ifExcluded(word):
                    continue
                elif self.checkPresent(word):
                    temp = self.final_list[word]
                    if str(page_no) in temp:
                        pass
                    else: 
                        temp.append(str(page_no))
                    self.final_list.update({word:temp})
                else:
                    self.final_list.update({word:[str(page_no)]})
            self.sortList()
            text_file = open("index.txt", "w")
            text_file.write('Word : Page Numbers\n')
            text_file.write('-------------------\n')
            for k,v in self.final_list.items():
                str_val = ""
                for ele in range(len(v)):
                    if ele == len(v)-1: 
                        str_val += v[ele]
                    else:
                        str_val += v[ele]+"," 
                data = k+" : " + str_val
                text_file.write(data+'\n')
            text_file.close()
        except Exception as e:
            print(e)

    def readAndStartIndex(self,path):
        try:
            f = []
            for (dirpath, dirnames, filenames) in os.walk(path):
                f.extend(filenames)
                break
            pno = 1
            for p in f:  
                print(path+p)
                page = open(path+p,"rb")
                w.start_indexing(page,pno)
                pno+=1
        except Exception as e:
            print(e)

if __name__ == '__main__':
    w = WordIndexer()
    path = str(os.getcwd())+"\\pages\\"
    w.readAndStartIndex(path)