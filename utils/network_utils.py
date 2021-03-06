from models.cifar import (alexnet, densenet, resnet,
                          vgg11, vgg16, vgg11_0, vgg16_0, vgg16_bn, vgg19_bn,
                          wrn)


def get_network(network, **kwargs):
    networks = {
        'alexnet': alexnet,
        'densenet': densenet,
        'resnet': resnet,
        'vgg11': vgg11,
        'vgg16': vgg16,
        'vgg11_0': vgg11_0,
        'vgg16_0': vgg16_0,
        'vgg16_bn': vgg16_bn,
        'vgg19_bn': vgg19_bn,
        'wrn': wrn

    }

    return networks[network](**kwargs)

