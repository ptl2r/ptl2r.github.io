#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Description

"""

from ptranking.ltr_adversarial.base.ad_player import AdversarialPlayer

class Pair_Discriminator(AdversarialPlayer):
    '''
    A pairwise discriminator
    '''
    def __init__(self, sf_para_dict=None, gpu=False, device=None):
        super(Pair_Discriminator, self).__init__(sf_para_dict=sf_para_dict, gpu=gpu, device=device)
