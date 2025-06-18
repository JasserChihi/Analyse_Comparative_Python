# Comparaison des Méthodes de Résolution de Systèmes Linéaires : Élimination de Gauss vs Factorisation LU
Ce dépôt contient un projet d'analyse comparative des performances des algorithmes de résolution de systèmes linéaires

## Table des matières

- [Présentation](#présentation)
- [Objectifs](#objectifs)
- [Résultats](#résultats)
- [Caractéristiques de la Machine](#caractéristiques-de-la-machine)
- [Analyse des résultats](#analyse-des-résultats)
- [Interprétation](#interprétation)
- [Conclusion](#conclusion)
- [Démo vidéo](#démo-vidéo)

## Présentation

Ce projet propose une étude comparative entre l'élimination de Gauss et la factorisation LU pour la résolution de systèmes linéaires. Il vise à analyser les temps d'exécution et les performances de chaque méthode en fonction de la taille des matrices, afin de déterminer la méthode la plus efficace selon le contexte d’utilisation.

## Objectifs

- Implémenter et comparer les deux méthodes de résolution de systèmes linéaires.
- Mesurer et analyser les temps d’exécution pour différentes tailles de matrices.
- Interpréter les résultats et proposer des recommandations d’utilisation.

## Résultats

### Temps d'exécution

Gauss Elimination : [0.018, 0.268, 0.413, 0.842, 1.883, 4.740, 42.917] secondes  
LU Factorization : [0.021, 0.209, 0.351, 0.693, 1.622, 14.666, 41.465] secondes

Le graphique montre que la factorisation LU est plus rapide pour les petites et moyennes matrices, tandis que les deux méthodes sont comparables pour les grandes matrices.

![Image1](https://github.com/user-attachments/assets/53ad5a0f-c14f-44f3-82ba-cee116cc79f9)


## Caractéristiques de la Machine

### Caractéristiques Matérielles
- CPU : Intel Core i5-1235U
- GPU : Intel Iris Xe Graphics
- RAM : 16 Go
- Système d'exploitation : Windows 11

### Caractéristiques Logicielles
- Langage de programmation : Python
- Bibliothèques utilisées : NumPy, Matplotlib
- Version de Python : 3.13.2


## Analyse des résultats

### Temps d'exécution

- **Gauss Elimination** : Les temps d'exécution augmentent de manière significative avec la taille de la matrice. Pour une matrice de taille 2000, le temps d'exécution atteint 42.91 secondes.
- **LU Factorisation** : Les temps d'exécution sont généralement inférieurs à ceux de l'élimination de Gauss pour les petites et moyennes tailles de matrices. Cependant, pour une matrice de taille 2000, le temps d'exécution est de 41.46 secondes, ce qui est légèrement inférieur à celui de l'élimination de Gauss.

### Comparaison des performances

- Pour les petites matrices (jusqu'à 1000), la factorisation LU est plus rapide que l'élimination de Gauss.
- Pour les grandes matrices (1500 et 2000), les deux méthodes ont des temps d'exécution similaires, avec un léger avantage pour la factorisation LU.


## Interprétation

La factorisation LU est généralement plus efficace pour les matrices de petite et moyenne taille en raison de sa structure qui permet une décomposition en deux matrices triangulaires.

Pour les très grandes matrices, les deux méthodes montrent des temps d'exécution comparables, ce qui peut être dû à la complexité accrue des opérations et à la gestion de la mémoire.


## Conclusion

La factorisation LU est généralement plus efficace pour les matrices de petite et moyenne taille, tandis que l'élimination de Gauss montre des performances similaires pour les très grandes matrices. Les résultats peuvent varier en fonction des caractéristiques matérielles et logicielles de la machine utilisée.

## Démo vidéo

[![Voir la démo](https://img.youtube.com/vi/I_K7tSshOaA/0.jpg)](https://www.youtube.com/watch?v=I_K7tSshOaA)



---

## Auteurs

- [Jasser Chihi]
