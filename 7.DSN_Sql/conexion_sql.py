import pyodbc


def conectar():
    return pyodbc.connect(
        r'DRIVER={SQL Server Native Client 10.0};'
        r'SERVER=EXODUS-PC\SQL2008;'
        r'DATABASE=MercadoPublico;'
        r'UID=sa;'
        r'PWD=exodus'
    )
