from ctypes import sizeof
from pickle import NONE
import sqlite3
import sys

conexion=sqlite3.connect('MusicaFa')
unCursor=conexion.cursor()

    #CREAR
#unCursor.execute("create table MUSICA (CANCION VARCHAR(20), CANTANTE VARCHAR(20), FAVORITO BOOLEAN)")

cancion='JUAN'
cantante='Two Door Cinema Club'
favorito=0            #1=True; 0=False

#Hola BIENVENIDOS 22/05/2022
unCursor.execute("select * from MUSICA where CANCION='{}' AND CANTANTE='{}' ".format(cancion,cantante ))
#listaMusic=unCursor.fetchone()
listaMusic=unCursor.fetchall()
if(len(listaMusic)==0):
    unCursor.execute("insert into MUSICA values('{}','{}',{})".format(cancion,cantante,favorito ))

#ELIMINAR
#unCursor.execute("delete from MUSICA where CANCION='{}' and CANTANTE='{}'".format(cancion,cantante))


#unCursor.execute("select * from MUSICA where CANCION='{}' AND CANTANTE='{}' ".format(cancion,cantante ))
#listaMusic=unCursor.fetchall()
#for music in listaMusic:
#    print(music[0]+";"+music[1]+";"+str(bool(int(music[2]))) )

conexion.commit() #confirma los cambios
conexion.close()

# Hola!