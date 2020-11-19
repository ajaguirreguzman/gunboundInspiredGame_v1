# Andres Aguirre
# April 2011

# commentary in spanish (sorry!)

# El siguiente link conlleva a una pagina web que sirvio como guia para el desarrollo de este trabajo (juego), la cual explica de forma clara y sencilla como usar Tkinter: http://www.tutorialspoint.com/python/python_gui_programming.htm
from numpy import *
from math import *
from Tkinter import *
import tkMessageBox
import tkFont

# Luego de elegir una opcion en el "panel de control" del juego, se abre una de las siguientes ventanas. Sin embargo, si se presiona el boton de disparar (Fire!) el programa salta a datos1() o datos2(), lo que lleva al comienzo del ciclo while y por ende al desenvolvimiento del juego.

def detalles():
	tkMessageBox.showinfo("Details", "1. En el transcurso del juego no se indica de quien es el turno.\n\n2. Cuando alguien gana el juego, baja una imagen que dice GAME OVER y si se presiona PLAY AGAIN aparece de nuevo el lienzo (ambiente o fondo) del juego. Cada vez que esto se repite, las imagenes de GAME OVER y fondo del juego, se van montando una sobre otra, lo que hace que (despues de haber jugado un par de veces) el juego se vaya haciendo cada vez mas lento.")

def instrucciones():
	tkMessageBox.showinfo( "Instructions", "Este juego consiste en disparar al adversario balas de ca#on hasta lograr golperlo. Esto se hace modificando la velocidad inicial del proyectil disparado por el ca#on y el angulo de inclinacion del disparo.\n\nNota: La velocidad y el angulo a ingresar deben ser magnitudes enteras. Por otro lado, los jugadores deben estar atentos al juego, ya que este no indica de quien es el turno en un momento dado.")

def creador():
	tkMessageBox.showinfo( "Creator", "Andres J. Aguirre G.\nEstudiante\nFacultad de Ciencia y Tecnologia, Universidad de Carabobo\n\n	References:\nWebsites:\n1)http://www.tutorialspoint.com/python/python_gui_programming.htm\n2)http://www.pythonware.com/library/tkinter/introduction/x1164-data-entry.htm\n\nTkinter handbooks:\n1)an-introduction-to-tkinter.pdf\n2)tkinter.pdf\n3)tcl-tk-reference-guide.pdf")

def cerrar():
	if tkMessageBox.askyesno("Salir", "Esta seguro de que quiere salir del juego?"):
		window.destroy()

def salir():
	exit()

# Si ninguno de los jugadores gana el juego aparecen estos botones sobre los botones "Fire!" para que los jugadores sepan que no deben disparar de nuevo, ya que el juego ha terminado
def gameover():
	velocidad=300
	g=9.8
	deltat=0.05
	xn=0.0
	yn=0.0
	detener3=False
	while not detener3:
		
		xn3=xn+0
		
		yn3=yn+(deltat*velocidad)
		
		vy13=velocidad+(g*deltat)
		
		lienzo.create_image(w1/2, yn3-552, anchor=S, image=fin)
		
		velocidad=vy13
		
		xn=xn3
		
		yn=yn3
		
		lienzo.after(10)
		lienzo.update()
		
		if (yn3-552)>h1:
			detener3=True
	
	B13 = Button(window, width=15, text="PLAY AGAIN!", activebackground="cyan", command = jugar)
	B13.grid(row=7, column=0)
	B14 = Button(window, width=15, text="PLAY AGAIN!", activebackground="cyan", command = jugar)
	B14.grid(row=7, column=2)

def datos1():
	lienzo.create_image(xfp1+6, yop1-10, anchor=CENTER, image=pum1)
	B9 = Button(window, width=15, text="Wait!")
	B9.grid(row=7, column=0)
	B12 = Button(window, width=15, text="Wait!")
	B12.grid(row=7, column=2)
	# Datos ingresados, conversion de los angulos a radianes y constantes (gravedad)
	v11=v1.get()
	theta11=theta1.get()
	angulo1=theta11*pi/180
	vx1=v11*cos(angulo1)
	vy1=-v11*sin(angulo1)
	g=9.8
	deltat=0.05
	xn=0.0
	yn=0.0
	
	# Ciclo "while not". Indagando por internet y por la pagina de referencia dada al comienzo me he topado con este ciclo "while not" que hasta el momento no habia visto y me parecio realmente util al momento de especificar cuando debe parar el ciclo; me parece que con esto se tiene mejor control del "Como detengo el juego?", especificamente el ciclo con el que se logra el movimiento del proyectil.
	detener1=False
	
	while not detener1:
		
		xn1=xn+(deltat*vx1)
		
		yn1=yn+(deltat*vy1)
		
		vy11=vy1+(g*deltat)
		
		lienzo.move("proyectil1",xn1-xn,yn1-yn)
		
		vy1=vy11
		
		xn=xn1
		
		yn=yn1
		
		xxo,yyo,xx1,yy1=lienzo.bbox("proyectil1")
		
		lienzo.after(10)
		lienzo.update()
		
		# Condicion para que cuando el proyectil impacte al enemigo, salga un mensaje indidicando que se ha ganado el juego
		if (((yos-37)-yop1)<=yn1<=((yos)-yfp1) and ((w1-55)-xop1)<=xn1<=((w1-15)-xfp1)):
			lienzo.create_image(w1-60, yos-37, anchor=CENTER, image=fuego)
			lienzo.create_text(30, yos-135, anchor=NW, font="boldface", fill="black", text="Winner!")
			B7 = Button(window, width=15, text="Winner!")
			B7.grid(row=7, column=0)
			B8 = Button(window, width=15, text="You're dead!")
			B8.grid(row=7, column=2)
			gameover()
			detener1=True

		# Condicion para que el "while not detener1" pare cuando el proyectil golpea al arbol, salga de la ventana (lienzo) o caiga al suelo
		if (((yos-117-yop1)<=yn1<=(yos-yfp1) and ((w1/2)-40-xop1)<=xn1<=((w1/2)+40-xfp1)) or xn1>=(w1-xop1) or xn1<=-xfp1 or yn1>=(yos-yfp1) or yn1<=-yfp1):
			jugar()
			detener1=True
		
def datos2():
	lienzo.create_image(xop2-5, yop2-10, anchor=CENTER, image=pum2)
	B12 = Button(window, width=15, text="Wait!")
	B12.grid(row=7, column=2)
	B9 = Button(window, width=15, text="Wait!")
	B9.grid(row=7, column=0)
	# Datos ingresados, conversion de los angulos a radianes y constantes (gravedad)
	v22=v2.get()
	theta22=theta2.get()
	angulo2=(180-theta22)*pi/180
	vx2=v22*cos(angulo2)
	vy2=-v22*sin(angulo2)
	g=9.8
	deltat=0.05
	xn=0.0
	yn=0.0
	
	# Ciclo "while not"
	detener2=False

	while not detener2:
		
		xn2=xn+(deltat*vx2)
		
		yn2=yn+(deltat*vy2)
		
		vy12=vy2+(g*deltat)
		
		lienzo.move("proyectil2",xn2-xn,yn2-yn)
		
		vy2=vy12
		
		xn=xn2
		
		yn=yn2
		
		xxo,yyo,xx1,yy1=lienzo.bbox("proyectil2")
		
		lienzo.after(10)
		lienzo.update()
		
		# Condicion para que cuando el proyectil impacte al enemigo, salga un mensaje indidicando que se ha ganado el juego
		if (-(xop2-(15))<=xn2<=-(xfp2-(55)) and ((yos-37)-yop2)<=yn2<=((yos)-yfp2)):
			lienzo.create_image(60, yos-37, anchor=CENTER, image=fuego)
			lienzo.create_text(w1-30, yos-135, anchor=NE, font="boldface", fill="black", text="Winner!")
			B10 = Button(window, width=15, text="Winner!")
			B10.grid(row=7, column=2)
			B11 = Button(window, width=15, text="You're dead!")
			B11.grid(row=7, column=0)
			gameover()
			detener2=True
		
		# Condicion para que el juego pare cuando el proyectil golpea al arbol, salga de la ventana (lienzo) o caiga al suelo
		if ((-(xop2-((w1/2)-40))<=xn2<=-(xfp2-((w1/2)+40)) and ((yos-117)-yop2)<=yn2<=(yos-yfp2)) or xn2>=(w1-xop2+1) or xn2<=-xfp2 or yn2>=(yos-yfp2) or yn2<=-yfp2):
			jugar()
			detener2=True

def presentacion():
	velocidadp=400
	g=9.8
	deltat=0.05
	xn=0.0
	yn=0.0
	detenerp=False
	while not detenerp:
		
		xnp=xn+0
		
		ynp=yn+(deltat*velocidadp)
		
		vy1p=velocidadp+(g*deltat)
		
		lienzop.create_image(wp/2, ynp, anchor=S, image=fondomovilp)
		
		velocidad=vy1p
		
		xn=xnp
		
		yn=ynp
		
		lienzop.after(10)
		lienzop.update()
		
		if (ynp-1296)>hp:
			jugar()
			detenerp=True

def jugar():
	
	# Titulo de la ventana
	window.title("ANDRES AGUIRRE / Asignatura: Fisica Computacional")

	# Llamando a los nombres
	nombre1=name1.get()
	nombre2=name2.get()
	
	# Ambiente del panel de control
	lienzo2.create_image(w1/2, h2/2, anchor=CENTER, image=enjoy)
	lienzo2.create_image(w1/2, h2/2, anchor=CENTER, image=cruz)
	lienzo2.create_image(w1-75, h2-20, anchor=CENTER, image=tanque)
	lienzo2.create_image(40, h2-25, anchor=CENTER, image=fuego)
	
	# Estableciendo el fondo del juego
	valor1 = press1.get()
	if valor1==1:
		fondo = wallpaper1
	
	valor2 = press2.get()
	if valor2==1:
		fondo = wallpaper2
	
	valor3 = press3.get()
	if valor3==1:
		fondo = wallpaper3
	
	valor4 = press4.get()
	if valor4==1:
		fondo = wallpaper4
	
	valor5 = press5.get()
	if valor5==1:
		fondo = wallpaper5
	
	valor6 = press6.get()
	if valor6==1:
		fondo = wallpaper6
	
	# Fondo por defecto (en caso de que no se elija ningun fondo al inicio del programa)
	if (valor1==0 and valor2==0 and valor3==0 and valor4==0 and valor5==0 and valor6==0):
		fondo = wallpaper6
	
	# Ambiente (fondo) del juego
	lienzo.create_image(w1/2, 0, anchor=N, image=fondo)
	
	# Superficie
	lienzo.create_rectangle(xos, yos, xfs, yfs, fill="green", tag="superficie")
	
	# Nombre de los jugadores en la parte superior del juego
	lienzo.create_text(w1/2-18, h1/15, anchor=E, font="boldface", fill="white", text=nombre1)
	lienzo.create_text(w1/2, h1/15, anchor=CENTER, font="boldface", fill="white", text="vs")
	lienzo.create_text(w1/2+18, h1/15, anchor=W, font="boldface", fill="white", text=nombre2)
	
	# Creando el proyectil 1
	lienzo.create_oval(xop1, yop1, xfp1, yfp1, fill="yellow", tag="proyectil1")
	
	# Creando el proyectil 2
	lienzo.create_oval(xop2, yop2, xfp2, yfp2, fill="red", tag="proyectil2")
	
	# Creando el ca#on 1
	lienzo.create_image(5, yos+11, anchor=SW, image=canon1)
	
	# Creando el ca#on 2
	lienzo.create_image(w1-5, yos+11, anchor=SE, image=canon2)
	
	# Creando el obstaculo (arbol)
	lienzo.create_image(w1/2, yos+12, anchor=S, image=tree)
	
	# Asintotas, esta es el area donde deben dar los proyectiles para que algun jugador gane
	#lienzo.create_rectangle(15, yos-37, 55, yos, fill="white", tag="asintota1")
	#lienzo.create_rectangle(w1-55, yos-37, w1-15, yos, fill="white", tag="asintota2")
	
	# Asintota, area donde esta el arbol.
	#lienzo.create_rectangle((w1/2)-40, yos-117, (w1/2)+40, yos, fill="white", tag="asintota3")
	
	# Etiquetas
	L1 = Label(window, text=nombre1, font="boldface", bg="skyblue")
	L2 = Label(window, text="Initial velocity of projectile:", bg="skyblue")
	L3 = Label(window, text="Elevation angle of cannon:", bg="skyblue")
	L4 = Label(window, text=nombre2, font="boldface", bg="skyblue")
	L5 = Label(window, text="Initial velocity of projectile:", bg="skyblue")
	L6 = Label(window, text="Elevation angle of cannon:", bg="skyblue")
	
	# Entradas de datos
	E1 = Entry(window, textvariable=v1, bd = 3, bg="white", show="*")
	E2 = Entry(window, textvariable=theta1, bd = 3, bg="white", show="*")
	E3 = Entry(window, textvariable=v2, bd = 3, bg="white", show="*")
	E4 = Entry(window, textvariable=theta2, bd = 3, bg="white", show="*")
	
	# Botones
	B1 = Button(window, bitmap="questhead", command = detalles)
	B2 = Button(window, text="Fire!", activebackground="orange", width=15, command = datos1)
	B3 = Button(window, text="Fire!", activebackground="orange", width=15, command = datos2)
	B4 = Button(window, text="Instructions", activebackground="cyan", command = instrucciones)
	B5 = Button(window, text="Creator", activebackground="cyan", command = creador)
	B6 = Button(window, text="Exit", activebackground="red", command = cerrar)
	
	# Asignacion de filas y columnas para el lienzo, etiquetas, botones y entradas de datos
	lienzo.grid(row=0, columnspan=3)
	lienzo2.grid(rowspan=9, columnspan=3)
	B1.grid(row=1, sticky=W, ipadx=10)
	B4.grid(row=6, column=1)
	B5.grid(row=7, column=1)
	B6.grid(row=8, column=1)
	L1.grid(row=1, column=0)
	L2.grid(row=2, column=0)
	E1.grid(row=3, column=0)
	L3.grid(row=5, column=0)
	E2.grid(row=6, column=0)
	B2.grid(row=7, column=0)
	L4.grid(row=1, column=2)
	L5.grid(row=2, column=2)
	E3.grid(row=3, column=2)
	L6.grid(row=5, column=2)
	E4.grid(row=6, column=2)
	B3.grid(row=7, column=2)

window=Tk()
# Titulo de la ventana principal
window.title("GAME by Andres Aguirre")

# Esto permite mostrar un mensaje cuando se presiona el boton "Exit" en el panel de control o el boton cerrar de la ventana
window.protocol("WM_DELETE_WINDOW", cerrar)

# Importando imagenes
fondop = PhotoImage(file = "evolution.gif")
fondomovilp = PhotoImage(file = "present.gif")
wallpaper1 = PhotoImage(file = "fondos/atard.gif")
wallpaper2 = PhotoImage(file = "fondos/bluesky.gif")
wallpaper3 = PhotoImage(file = "fondos/ocean.gif")
wallpaper4 = PhotoImage(file = "fondos/pastel.gif")
wallpaper5 = PhotoImage(file = "fondos/pnubes.gif")
wallpaper6 = PhotoImage(file = "fondos/red.gif")
canon1 = PhotoImage(file = "canon1.gif")
canon2 = PhotoImage(file = "canon2.gif")
tree = PhotoImage(file = "arbol.gif")
pum1 = PhotoImage(file = "llama1.gif")
pum2 = PhotoImage(file = "llama2.gif")
fuego = PhotoImage(file = "explosion.gif")
enjoy = PhotoImage(file = "enjoy.gif")
cruz = PhotoImage(file = "canonm.gif")
tanque = PhotoImage(file = "tanque.gif")
fin = PhotoImage(file = "gameover2.gif")

# Prenguntando al usuario la resolucion de su pantalla
print("\nIngrese la resolucion (ANCHOxALTO) de su monitor (o pantalla) para un mejor ajuste de la ventana del juego.\nNota: puede que la ventana no se ajuste a la perfeccion, ya que esto depende de  muchos factores. Ademas, si su monitor es peque#o, tambien se pueden ver afectadas ciertas imagenes mostradas en el transcurso del juego.\n")
ancho=float(raw_input('Ingrese el ANCHO de su patalla:'))
alto=float(raw_input('Ingrese el ALTO de su patalla:'))

if (ancho<600 or alto<600):
	print("\n--LA RESOLUCION DE SU MONITOR ES MUY BAJA--\n")
	exit()

print("\nPor favor, minimice esta ventana (el terminal o consola).\n")

## Definiendo las variables a usar a lo largo del programa  (en donde van las magnitudes "1280" y "800" colocar la resolucion del monitor donde se esta viendo el juego; para asi lograr que la ventana juego abarque "todo" el monitor)
#Lienzos
wp=ancho-10
hp=alto-200-85
w1=ancho-10
h1=alto-200-85
h2=alto-h1-85
#Superficie
xos=0
yos=h1*0.9
xfs=w1+1
yfs=h1+1
#Proyectiles
xop1=70
yop1=yos-47
xfp1=xop1+10
yfp1=yop1+10
xop2=w1-70-11
yop2=yos-47
xfp2=xop2+10
yfp2=yop2+10

## Definiendo variables
#Tipo "text" para las entradas de nombres -Entry-
name1 = StringVar()
name2 = StringVar()
#Tipo numericas para elegir el fondo -Checkbutton- . Estas pueden ser 1 o 0
press1 = IntVar()
press2 = IntVar()
press3 = IntVar()
press4 = IntVar()
press5 = IntVar()
press6 = IntVar()
#Tipo numericas para elegir la velocidad y el angulo -Entry-
v1 = IntVar()
v2 = IntVar()
theta1 = IntVar()
theta2 = IntVar()

# Lienzo principal
lienzop=Canvas(window, width=wp, height=hp, bg="white")
lienzop.create_image(wp/2, hp/2, anchor=CENTER, image=fondop)

# Etiquetas
lienzop.create_text(wp/6-15, hp-120, anchor=CENTER, font="boldface", fill="white", text="Nombre del jugador 1")
lienzop.create_text((wp*5)/6+15, hp-120, anchor=CENTER, font="boldface", fill="white", text="Nombre del jugador 2")

# Entradas de nombres
E1p = Entry(window, textvariable=name1, bd = 3, bg="white")
E2p = Entry(window, textvariable=name2, bd = 3, bg="white")

# Botones principales
B1p = Button(window, text="PLAY", activebackground="blue", command = presentacion)
B2p = Button(window, text="EXIT", activebackground="red", command = salir)

# Checkbuttons
C1 = Checkbutton(window, text="atard  ", variable=press1, bg="black", activebackground="black", activeforeground="white")
C2 = Checkbutton(window, text="bluesky", variable=press2, bg="black", activebackground="black", activeforeground="white")
C3 = Checkbutton(window, text="ocean  ", variable=press3, bg="black", activebackground="black", activeforeground="white")
C4 = Checkbutton(window, text="pastel ", variable=press4, bg="black", activebackground="black", activeforeground="white")
C5 = Checkbutton(window, text="pnubes ", variable=press5, bg="black", activebackground="black", activeforeground="white")
C6 = Checkbutton(window, text="red    ", variable=press6, bg="black", activebackground="black", activeforeground="white")

## Creando lienzos del ventana del juego
#Lienzo del juego
lienzo=Canvas(window, width=w1, height=h1, bg="white")
#Lienzo del panel de control
lienzo2=Canvas(window, width=w1, height=h2, bg="skyblue")

# Asignacion de filas y columnas en el lienzo principal
lienzop.grid(row=0, columnspan=3)
E1p.grid(row=0, column=0, sticky=S, pady=75)
E2p.grid(row=0, column=2, sticky=S, pady=75)
B1p.grid(row=0, column=1, sticky=S, ipadx=100, pady=100)
B2p.grid(row=0, column=1, sticky=S, ipadx=50, pady=50)
C1.grid(row=0, column=0, sticky=SW, pady=100)
C2.grid(row=0, column=0, sticky=SW, pady=80)
C3.grid(row=0, column=0, sticky=SW, pady=60)
C4.grid(row=0, column=0, sticky=SW, pady=40)
C5.grid(row=0, column=0, sticky=SW, pady=20)
C6.grid(row=0, column=0, sticky=SW, pady=0)

window.mainloop()

