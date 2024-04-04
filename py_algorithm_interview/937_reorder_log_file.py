class Solution(object):
    def reorderLogFiles(self, logs):
        result=[]

        text_log=[log for log in logs if log.split()[1].isalpha()]
        digit_log=[log for log in logs if log.split()[1].isdigit()]

        text_log=sorted(text_log,key=lambda x:(x.split()[1:],x.split()[0]))


        text_log.extend(digit_log)
        return text_log
            