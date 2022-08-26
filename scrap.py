import numpy as np
x = [0, 1, 2, 3, 4, 4, 5]
y = [0, 1, 3, 3, 12, 6, 7]

def integrate(x, y):
    area = np.trapz(y=y, x=x)
    return area
print(integrate(x, y))


# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# from sklearn.metrics import precision_recall_curve
# from sklearn import metrics
# from sklearn.metrics import auc
# #101 - phaco ok, rhexis ok
#
# a = [(0.9898114800453186, True), (0.9833932518959045, True), (0.9814953207969666, True), (0.9732239842414856, True), (0.9709620475769043, True), (0.9655173420906067, True), (0.9587313532829285, True), (0.958454430103302, True), (0.9576375484466553, True), (0.9480304718017578, True), (0.9473555684089661, True), (0.9468650817871094, True), (0.945201575756073, True), (0.9451861381530762, True), (0.9326368570327759, True), (0.9302435517311096, True), (0.9111341238021851, True), (0.9094101190567017, True), (0.9055312871932983, True), (0.8983771204948425, True), (0.8962711095809937, True), (
# 0.8879259824752808, True), (0.868625283241272, True), (0.8553661108016968, True), (0.8416890501976013, True), (0.8359520435333252, True), (0.8354359269142151, True), (0.8344388008117676, True), (0.8219512104988098, True), (0.8001927733421326, True), (0.7769960761070251, True), (0.7372075319290161, True), (0.6423512101173401, True), (0.544752299785614, False)]
#
#
# print(a)
#
# score, y = zip(*a)
# print(1*(y))
#
#
# precision, recall, thresholds = precision_recall_curve(
#     y, score)
# precision = np.insert(precision,0, 0, axis=0)
# recall = np.insert(recall, 0, 1, axis=0)
# AUPR = auc(recall, precision)
# print('AUPR: ', AUPR)
# plt.plot(recall, precision)#, marker='-')
# plt.xlim([0, 1.01])
# plt.ylim([0, 1.1])
# plt.title("Precision-Recall curve for " )
# plt.ylabel('Precision')
# plt.xlabel('Recall')
# #add confidence
# #plt.fill_between(recall, (precision-ci_PR), (precision+ci_PR), color='b', alpha=.1)
# plt.show()