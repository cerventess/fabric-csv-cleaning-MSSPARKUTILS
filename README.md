# fabric-csv-cleaning-MSSPARKUTILS
Automatiser le nettoyage de fichiers CSV dans Microsoft Fabric avec mssparkutils.fs - 
Ce projet montre comment automatiser l’ingestion et le nettoyage de fichiers CSV dans Microsoft Fabric à l’aide d’un notebook PySpark et de la librairie `mssparkutils.fs`.

## Objectif:
- Scanner un dossier OneLake `Files/archiveRetail/` contenant des fichiers `.csv`
- Supprimer les lignes vides dans chaque fichier avec PySpark
- Sauvegarder les fichiers nettoyés au format `.parquet` dans OneLake `Files/cleanedRetail/`
- Supprimer les fichiers CSV d’origine après traitement


## Auteur:
Oussema Chtioui  
[🔗 Profil LinkedIn](https://www.linkedin.com/in/oussama-chtioui-91a256aa/)  
[🏆 #MVPFabricSeries](https://www.linkedin.com/feed/hashtag/mvpfabricseries/)
