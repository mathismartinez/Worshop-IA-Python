
---

# Workshop : Création d'une IA pour l'Analyse des Données de Sang avec TensorFlow

## Objectifs
Ce workshop a pour objectif de vous apprendre à créer une intelligence artificielle (IA) capable d'analyser des données. Vous utiliserez Python et les bibliothèques TensorFlow, Pandas et Matplotlib.

## Étapes du Workshop

### 1. Téléchargement des Pièces Jointes
Téléchargez le fichier CSV contenant les données de sang. Vous pouvez obtenir ce fichier dans le repo GitHub.

### 2. Installation des Bibliothèques
Installez les bibliothèques nécessaires en exécutant les commandes suivantes :

```bash
pip install tensorflow
pip install matplotlib
pip install pandas
```

### 3. Extraction et Visualisation des Données (`train_model.py`)
Extrayez les données du fichier CSV et visualisez-les avec Pandas et Matplotlib.

### 4. Création d'un Réseau de Neurones avec TensorFlow (`train_model.py`)
Créez un modèle de réseau de neurones pour analyser les données.

### 5. Entraînement de l'IA (`train_model.py`)
Entraînez votre modèle avec les données.

### 6. Évaluation de l'IA (`train_model.py`)
Évaluez les performances de votre modèle avec Matplotlib.

### 7. Amélioration du Modèle (`train_model.py`)
Si les performances ne sont pas suffisantes, améliorez le modèle en ajustant les hyperparamètres ou en ajoutant des couches supplémentaires.

#### Suggestions d'Amélioration :
- Ajouter plus de couches au réseau de neurones.
- Essayer différentes fonctions d'activation.
- Ajuster les paramètres de l'optimiseur.
- Augmenter le nombre d'époques d'entraînement.

### 8. Utilisation du Modèle Entraîné (`test_model.py`)
Créez un programme `test_model.py` pour charger le modèle entraîné et l'utiliser pour faire des prédictions sur de nouvelles données.

---

En suivant ces étapes, vous serez en mesure de créer deux programmes distincts : l'un pour l'entraînement du modèle (`train_model.py`) et l'autre pour tester et utiliser le modèle (`test_model.py`). N'hésitez pas à expérimenter et à ajuster les paramètres pour améliorer les performances de votre modèle.