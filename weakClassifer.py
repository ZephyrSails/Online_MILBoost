


class weakClassier(object):

    def __init__(self, learningRate):
        """
        initialize haar like feature
        and use it to build weak classifer
        """
        # Gaussian for positive training data
        self.mu1
        self.sigma1
        # Gaussian for negative training data
        self.mu2
        self.sigma2

        self.haar = self.__randomHaar()
        self.a = learningRate


    def __randomHaar(self):
        """
        return a haar like feature
        """


    def __calcHaar(self, img):
        """
        imput an image, calc it's haar like feature
        """


    def __getGaussian(self, haarFeatures):
        """
        Given a haar like features, return new gaussian
        """


    def __updateGaussian(self, mu, sigma):
        """
        update gaussian, based on learning rate
        """


    def update(self, positive, negative):
        positiveFeatures = map(self.__calcHaar, positive)
        negativeFeatures = map(self.__calcHaar, negative)

        mu1, sigma1 = self.__getGaussian(positiveFeatures)
        mu2, sigma2 = self.__getGaussian(negativeFeatures)

        self.mu1, self.sigma1 = self.__updateGaussian(mu1, sigma1)
        self.mu2, self.sigma2 = self.__updateGaussian(mu2, sigma2)


    def predict(self, img):
        """
        use two gaussians to do prediction
        """
