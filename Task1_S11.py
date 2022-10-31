# Постройте график функции 𝑓(𝑥)=5𝑥^2+10𝑥−30
# По графику определите, при каких значения x значение функции отрицательно

import matplotlib.pyplot as m
X = list(i for i in range (-10,10))
graph = list(5*X[i]*X[i]+10*X[i]-30 for i in range(len(X)))
m.plot(X,graph)
m.show()