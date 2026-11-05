"""Práctica 3: SISTEMA MUSCULOESQUELÉTICO
Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Castro Alcántar Daniel Hiram
Número de control: 23212184
Correo institucional: l23212184@tijuana.tecnm.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""

#   Librerías  
import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

# Datos generales de la simulación
x0,t0,tend,dt,w,h = 0,0,10,1e-3,7,3.5
N = round((tend-t0)/dt) + 1
t = np.linspace(t0,tend,N)

# señal de entrada
F = np.zeros(N)
F[1000:2000] = 1

# función de transferencia del control
num = [0.001, 0.75]
den = [0.011, 1]
syscontrol = ctrl.tf(num,den)

# función de transferencia del caso
num = [0.1, 0.75]
den = [1.1, 1]
syscaso = ctrl.tf(num,den)

# controlador PI
Kp = 0.021971
Ki = 41303.6113

PI = ctrl.tf([Kp,Ki],[1,0])
sysPID = ctrl.feedback(ctrl.series(PI,syscaso),1)

# respuestas de los sistemas
_,Fsx = ctrl.forced_response(syscontrol,t,F,x0)
_,FsY = ctrl.forced_response(syscaso,t,F,x0)
_,PID = ctrl.forced_response(sysPID,t,Fsx,x0)

# colores
clr1 = np.array([0,125,204])/255
clr2 = np.array([235,185,0])/255
clr3 = np.array([209,0,86])/255
clr4 = np.array([80,0,113])/255

fg = plt.figure()

plt.plot(t,F,"-",linewidth=1.5,color=clr1,label="F(t)")
plt.plot(t,Fsx,"-",linewidth=1.5,color=clr2,label="Fs(t): Control")
plt.plot(t,FsY,"-",linewidth=1.5,color=clr3,label="Fs(t): Caso")
plt.plot(t,PID,":",linewidth=2.5,color=clr4,label="PID: Transferencia")

plt.grid(False)
plt.xlim(-0.25,10); plt.xticks(np.arange(0,11,1))
plt.ylim(0,1.2); plt.yticks(np.arange(0,1.3,0.1))
plt.xlabel("t [s]")
plt.ylabel("Fi(t) [V]")
plt.legend(loc="upper center",ncol=4,fontsize=8)
plt.legend(bbox_to_anchor=(0.5, 1.1),
           loc="center", ncol=4, fontsize=8)
fg.set_size_inches(w,h)
fg.tight_layout()
fg.savefig("Musculoesqueletico_python.pdf")
plt.show()
