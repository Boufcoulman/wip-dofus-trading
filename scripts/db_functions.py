import sqlite3

# dbpath = 'E:/Donnees/Programmation/dofus-trading-database/dofus-trading.db'
dbpath = '../dofus-trading.db'


def add_ressource_line(ressource, timestamp, moyen, unite, dix, cent):
    """
    Permet d'ajouter la recupération d'une donnée dans la base
    """
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    # Ajout de la récupération de données
    cursor.execute("""
    INSERT INTO dofus_trading_table(
        timestamp,
        ressource,
        prix_moyen,
        prix_unitaire,
        prix_dizaine,
        prix_centaine
        ) VALUES(?, ?, ?, ?, ?, ?)""",
                   (timestamp, ressource, moyen, unite, dix, cent)
                   )
    conn.commit()
    conn.close()


def init_db():
    """
    Fonction à utiliser manuellement pour créer la base
    """
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    # Création de la table ressource si non existante
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dofus_trading_table(
         timestamp TEXT,
         ressource TEXT,
         prix_moyen INTEGER,
         prix_unitaire INTEGER,
         prix_dizaine INTEGER,
         prix_centaine INTEGER
    )
    """)


if __name__ == "__main__":

    init_db()
