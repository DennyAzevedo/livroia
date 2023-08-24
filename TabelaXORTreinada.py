import numpy as np

entradas = np.array([[0, 0],
                     [0, 1],
                     [1, 0],
                     [1, 1]])
saidas = np.array([[0], [1], [1], [0]])

pesos0 = np.array([[-13.1663, -1.02841, 5.9636],
                   [5.96543, -1.02829, -13.1609]])
pesos1 = np.array([[16.3146], [-42.3705], [16.3137]])

nTreinos = 1000000
taxaAprendizado = 0.3
momentum = 1


def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))


def sigmoideDerivada(sig):
    return sig * (1 - sig)


sigDerivada = sigmoid(0.5)
sigDerivada1 = sigmoideDerivada(sigDerivada)

camadaEntrada = entradas
somaSinapse0 = np.dot(camadaEntrada, pesos0)
camadaOculta = sigmoid(somaSinapse0)

somaSinapse1 = np.dot(camadaOculta, pesos1)
camadaSaida = sigmoid(somaSinapse1)

erroCamadaSaida = saidas - camadaSaida
mediaAbsoluta = np.mean(np.abs(erroCamadaSaida))

derivadaSaida = sigmoideDerivada(camadaSaida)
deltaSaida = erroCamadaSaida * derivadaSaida



