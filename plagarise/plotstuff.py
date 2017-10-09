from matplotlib import pyplot
import sys
import nltk
# textpath = str(sys.argv[1])
# logs = open(textpath, "r").read()
#
# c=logs[1:(len(logs)-1)]
# B=c.split(',')
# h=[]
# b=0
#
# for i in B:
#     b=1+b
#     h.append(b)
#
#
#
# pyplot.xlabel("Iteration")
# pyplot.title("Obama RNN error")
# pyplot.ylabel("Error")
# pyplot.show(pyplot.scatter(h,B))
# # nltk.download()

def check_iterations():
    getsome = open("slog.txt", "r").read()
    A = getsome[1:(len(getsome) - 1)]
    B = A.split(',')
    h = []
    b = 0

    for i in B:
        b = 1 + b
        h.append(b)
    return b
def check_iterationsfile(input):
    textpath = str(input())
    b = len(textpath)
    getsome = open("log-files/log" + textpath[b - 9:b], "r").read()
    A = getsome[1:(len(getsome) - 1)]
    B = A.split(',')
    h = []
    b = 0

    for i in B:
        b = 1 + b
        h.append(b)
    return b
