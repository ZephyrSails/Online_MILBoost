from weakClassier import *

# RECT = trackRect()
TOP, DOWN, LEFT, RIGHT = 0, 100, 0, 100
M = 250 # we are using M weak classifiers
K = 50  # we are using top K weak classifiers to build strong classifer
alpha = 0.1 # learning rate


class trackRect(object):
    def __init__(self, top, down, left, right):
        self.left = left
        self.right = right
        self.top = top
        self.down = down

    def update(self, strong):



def readFrames(fileName):
    """
    read video and split it into frames
    """

    return frames


def initWeakClassifiers(M):
    return [weakClassier(alpha) for _ in xrange(M)]


def update(weaks):
    for wc in weaks:
        wc.update(positive, negative)


def getOnlineTrainingData(rect):
    """
    Collect positive and negative data around rect
    """


def loss(bagPredictions, groudTruth):
    """
    loss function
    """


def predictBag(bagSet, m, hSet):
    ans = []
    for bag, H in zip(bagSet):
        instancePredictions = map(m.predict, bag)
        ans.append(instance2Bag(instancePredictions))
    return ans 


def instance2Bag(instancePredictions):
    """
    1 - [(1 - pij) * (1 - pij) * (1 - pij)..]
    """



def main():
    frames = readFrames(fileName)
    rect = trackRect(TOP, DOWN, LEFT, RIGHT)

    weaks = initWeakClassifiers(M)

    for frame in frames:
        truePositive, trueNegative = getOnlineTrainingData(rect)

        hSet = list([0] * len(truePositive)) + [0] * len(trueNegative)
        # trainingSet = truePositive + trueNegative
        bagSet = map(list, list(truePositive) + trueNegative)
        groudTruth = [1.] + [0.] * len(trueNegative)

        update(weaks, truePositive, trueNegative)

        strong = []
        for k in xrange(K):
            minLoss, minIndex = float('inf'), 0
            for i, m in enumerate(M):
                bagPredictions = predictBag(bagSet, m, hSet)
                currLoss = loss(bagPredictions, groudTruth)
                if currLoss < minLoss:
                    minIndex = i

            strong.append(M[minIndex])

        rect.update(strong)


if __name__ == '__main__':
    main()
