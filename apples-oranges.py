from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0]] # 1 smooth, 0 bumpy
labels = [0, 0, 1, 1] # 0 apples, 1 orange

clf = tree.DecisionTreeClassifier()
