
# Automatic CSV cleaning in Microsoft Fabric with mssparkutils.fs

from notebookutils import mssparkutils
from pyspark.sql.functions import col

# 1.OneLake Paths
raw_path = "Files/archiveRetail/"
cleaned_path = "Files/cleanedRetail/"

# 2.List CSV file
files = mssparkutils.fs.ls(raw_path)

# 3.Loop each CSV file
for file in files:
    if file.name.endswith(".csv"):
        file_path = raw_path + file.name
        print(f"\n📥 Traitement du fichier : {file_path}")

        # Read CSV file
        df = spark.read.option("header", True).csv(file_path)

        # Cleaning
        df_cleaned = df.dropna(how="all")

        # Save in Parquet format
        output_path = cleaned_path + file.name.replace(".csv", ".parquet")
        df_cleaned.write.mode("overwrite").parquet(output_path)
        print(f"Fichier nettoyé sauvegardé : {output_path}")

        # Deleting the original CSV file
        mssparkutils.fs.rm(file_path, recurse=True)
        print(f"Fichier original supprimé : {file_path}")

print("\nTous les fichiers ont été traités avec succès.")
