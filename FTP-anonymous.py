#!/bash/python
#
#=============================================
# Finder FTP Anonimo v1.0
# 
# Codeado By s1kr10s
#
# Web: dth-security.blogspot.com
# Twitter: @s1kr10s
#
# Uso: python FTP-anonymous.py lista-ip.txt
#=============================================

import ftplib
import sys
import os 

if os.name==('ce','nt','dos'):os.system('cls')
elif os.name=='posix': os.system('clear')

contadoryes=0
contadornot=0
nombre=""

print chr(27)+"[1;36m"+"\n     Finder FTP Anonimo v1.0"+chr(27)+"[0m"
print chr(27)+"[1;36m"+" Web: dth-security.blogspot.com"+chr(27)+"[0m"
print chr(27)+"[1;36m"+"  Twitter: @s1kr10s By s1kr10s"+chr(27)+"[0m"

nombre = raw_input("\nNombre de File con IP: ")

try:
	filex = open(nombre);
	for linea in filex:
	   ftp_servidor = linea
	   ftp_usuario  = 'anonymous'
	   ftp_clave    = ''
	   try:
	 	 print "Conectando con: "+linea
		 ftp = ftplib.FTP(ftp_servidor) #servidor ip
		 ftp.login(ftp_usuario,ftp_clave) # user anonymous, passwd anonymous@
		 files = ftp.dir()       # listamos el directorio
		 print files
		 print "\nSe Listo Directorio: "+linea
		 contadoryes = contadoryes + 1
		 reporte=open("reporte.log","a") #creamos el reporte
		 reporte.write('Success IP: '+linea)
                 reporte.close()
		 print "=========================================================\n"
	   except:
		 contadornot = contadornot + 1
		 print chr(27)+"[0;31m"+"Warning: Servidor Bloqueado "+linea+chr(27)+"[0m"
		 print "=========================================================\n"
	filex.close()

	total = str(contadoryes+contadornot)
	print chr(27)+"[0;33m"+"Exito   : "+str(contadoryes)+" de "+total+chr(27)+"[0m"
	print chr(27)+"[0;33m"+"Fallidos: "+str(contadornot)+" de "+total+"\n"+chr(27)+"[0m"
	print chr(27)+"[32;40m"+"(IP guardadas en alrchivo reporte.log)"+chr(27)+"[0m"
	print "\n"
except:
        print chr(27)+"[0;31m"+"\nEl archivo ("+nombre+") no se encuentra - Vuelva Intentar\n"+chr(27)+"[0m"
