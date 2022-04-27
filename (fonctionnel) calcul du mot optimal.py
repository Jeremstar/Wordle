#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 14:11:24 2022

@author: nerhal
"""

import numpy as np
import statistics as stc

fichier_allowed_words = open("allowed_words.txt","r")
allowed_words = fichier_allowed_words.read()
allowed_words = allowed_words.split("\n")
fichier_allowed_words.close()

fichier_possible_words = open("possible_words.txt","r")
possible_words = fichier_possible_words.read()
possible_words = possible_words.split("\n")
fichier_possible_words.close()

mots_outils = allowed_words.copy()
mots_solutions = possible_words.copy()

jaune = {1: None, 2: None, 3: None, 4: None, 5: None}
vert = {1: None, 2: None, 3: None, 4: None, 5: None}
gris = []

def split(mot):
    return [lettre for lettre in mot]

def info_1v1(mot_essai, mot_cible) :
    #Découpage des mots
    mot_essai_tranché = []
    for lettre in mot_essai :
        mot_essai_tranché.append(lettre)
    mot_cible_tranché = []
    for lettre in mot_cible :
        mot_cible_tranché.append(lettre)
    
    #Mise à jour des infos de couleur
    rang = 0
    jaune_temporaire = jaune.copy()
    gris_temporaire = gris.copy()
    vert_temporaire = vert.copy()
    for lettre in mot_essai_tranché :
        if lettre == mot_cible_tranché[rang] :
            vert_temporaire[rang+1] = lettre
        elif lettre not in mot_cible_tranché :
            gris_temporaire.append(lettre)
        else :
            jaune_temporaire[rang+1] = lettre
        rang = rang + 1
    #print("gris =",gris_temporaire, "vert =",vert_temporaire, "jaune=",jaune_temporaire)
    
    #Épuration des solutions possibles
    mots_solutions_temporaire = mots_solutions.copy()
    mots_exclus = []
    rang_liste = -1
    for mot in mots_solutions_temporaire :
        rang_lettre = 0
        rang_liste = rang_liste + 1
        for lettre in mot :
            if lettre in gris_temporaire :
                mots_exclus.append(mot)
                break
            elif vert_temporaire[rang_lettre+1] != lettre and vert_temporaire[rang_lettre+1] != None:
                mots_exclus.append(mot)
                break
            elif jaune_temporaire[rang_lettre+1]!= None : 
                if jaune_temporaire[rang_lettre+1] == lettre or jaune_temporaire[rang_lettre+1] not in split(mot) :
                    mots_exclus.append(mot)
                break
            rang_lettre = rang_lettre + 1
            if rang_lettre == 5 :
                rang_lettre = 0
                
    information_1v1 = len(mots_exclus)
    #print(mots_exclus)
    return(information_1v1)
    
def info_1vTotal(mot_essai, liste_mots_cible) :
    information_1vTotal = []
    for mot in liste_mots_cible :
        information_1vTotal.append(info_1v1(mot_essai, mot))
    information_1vTotal = stc.mean(information_1vTotal)
    return(information_1vTotal)

def info_maximale(liste_mots_outils, liste_mots_cible):
    repertoire_info = []
    passage = 0
    for mot in liste_mots_outils :
        passage = passage + 1
        print(passage)
        repertoire_info.append(info_1vTotal(mot, liste_mots_cible))
    information_maximale = max(repertoire_info)
    rang_info_max = repertoire_info.index(information_maximale)
    mot_optimal = allowed_words[rang_info_max]
    print(mot_optimal)
    return(mot_optimal)