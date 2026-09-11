# Outil de Stéganographie par LSB (Least Significant Bit)

**Projet académique - Bachelor Cybersécurité (EPITA x École Polytechnique)**

Ce projet propose un ensemble de scripts en Python permettant de dissimuler et d'extraire des messages textuels au sein de fichiers images. Il repose sur la technique stéganographique du bit de poids faible (LSB - Least Significant Bit).

Ce programme démontre comment manipuler les canaux de couleurs d'une image au niveau binaire pour y cacher de l'information sans altérer l'image de manière perceptible pour l'œil humain.

## 1. Fonctionnalités Principales

*   **Obfuscation de données :** Le script remplace le dernier bit de chaque valeur de couleur (RGB) des pixels de l'image par les bits composant le message secret.
*   **Vérification de capacité :** Le programme calcule automatiquement si la résolution de l'image source est suffisante pour héberger le message complet avant de procéder à l'altération.
*   **Extraction de données :** Un script dédié lit séquentiellement le dernier bit de chaque canal colorimétrique pour reconstruire les octets et restituer la chaîne de caractères initiale.
*   **Gestion des formats :** Le traitement s'effectue sur des images converties au format RGB afin de garantir la cohérence des manipulations binaires.

## 2. Environnement Technique

*   **Langage principal :** Python 3
*   **Dépendance externe :** `Pillow` (module `PIL`) pour le chargement, la manipulation et la sauvegarde des matrices de pixels de l'image.
*   **Encodage :** Conversion des caractères ASCII en séquences binaires de 8 bits lors de l'insertion, et regroupement par blocs de 8 bits lors de l'extraction.

## 3. Prérequis et Déploiement

L'exécution de ces scripts requiert l'installation de la bibliothèque de traitement d'images Pillow.

**Installation des dépendances :**
```bash
pip install Pillow
```

**Exécution du chiffrement (Dissimulation) :**
Lancez le script d'obfuscation. Le programme vous demandera de saisir le message à cacher via l'entrée standard.
```bash
python3 obfuscate.py
```
Le résultat sera sauvegardé sous le nom `image_obfusquee.png` dans le répertoire courant.

**Exécution du déchiffrement (Extraction) :**
Lancez le script de désobscurcissement. Il lira automatiquement le fichier `image_obfusquee.png` et affichera le message caché dans le terminal.
```bash
python3 deobfuscate.py
```

## 4. Architecture du Projet

*   `obfuscate.py` : Script responsable du chargement de l'image source, de la conversion du message en binaire, et de l'altération des bits de poids faible.
*   `deobfuscate.py` : Script responsable de la lecture de l'image altérée et de la reconstruction du message d'origine.
*   `image.png` : Image source par défaut utilisée pour la dissimulation.
*   `image_obfusquee.png` : Fichier généré en sortie contenant l'information dissimulée au format PNG pour éviter la compression destructive.

## 5. Note de Sécurité (Disclaimer)

Ce projet est un démonstrateur technique développé dans un cadre académique. La méthode LSB est une technique de stéganographie élémentaire. Bien qu'elle soit invisible à l'œil nu, l'altération des bits de poids faible modifie l'entropie de l'image.

Ce type d'obfuscation est facilement détectable par des outils d'analyse stéganalytique standards (par exemple, des attaques basées sur le test du $\chi^2$ ou l'isolation des plans de bits). De plus, la stéganographie seule n'offre aucune garantie de confidentialité. Dans un contexte réel, le message devrait être préalablement chiffré (avec un algorithme tel qu'AES) avant d'être dissimulé dans un média.
