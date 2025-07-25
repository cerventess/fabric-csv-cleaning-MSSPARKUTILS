# fabric-csv-cleaning-MSSPARKUTILS
Automatiser le nettoyage de fichiers CSV dans Microsoft Fabric avec mssparkutils.fs

# 🚀 Nettoyage Automatique de Fichiers CSV dans Microsoft Fabric avec mssparkutils.fs

Ce projet montre comment automatiser l’ingestion et le nettoyage de fichiers CSV dans Microsoft Fabric à l’aide d’un notebook PySpark et de la librairie `mssparkutils.fs`.

## 🎯 Objectif

- Scanner un dossier `archiveRetail/` contenant des fichiers `.csv`
- Supprimer les lignes vides dans chaque fichier avec PySpark
- Sauvegarder les fichiers nettoyés au format `.parquet` dans `cleanedRetail/`
- Supprimer les fichiers CSV d’origine après traitement

## 📁 Structure OneLake

```
Files/
├── archiveRetail/        # Fichiers CSV bruts
├── cleanedRetail/        # Fichiers nettoyés en Parquet
```

## 🧰 Outils utilisés

| Outil | Description |
|-------|-------------|
| `mssparkutils.fs.ls()` | Liste les fichiers |
| `spark.read.csv()`     | Lecture des CSV |
| `dropna(how="all")`    | Suppression des lignes vides |
| `.write.parquet()`     | Export des fichiers nettoyés |
| `mssparkutils.fs.rm()` | Suppression des fichiers bruts |

## 💡 Exemple d'exécution

Une fois lancé dans un notebook Fabric, le script va :
1. Lister tous les fichiers CSV dans `Files/archiveRetail/`
2. Nettoyer chaque fichier
3. Sauvegarder le résultat dans `Files/cleanedRetail/`
4. Supprimer le fichier original

## 🛠️ Dépendances

- Microsoft Fabric
- Un Lakehouse avec les dossiers `archiveRetail/` et `cleanedRetail/`
- Runtime PySpark (dans notebook Fabric)

## 📷 Capture d'écran

*(Ajoutez une image de votre notebook ou de la structure OneLake ici)*

## 📌 Auteur

Oussema Chtioui  
[🔗 Profil LinkedIn](https://www.linkedin.com/in/oussama-chtioui-91a256aa/)  
[🏆 #MVPFabricSeries](https://www.linkedin.com/feed/hashtag/mvpfabricseries/)
