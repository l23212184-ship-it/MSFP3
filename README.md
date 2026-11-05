# Práctica 3 · Modelado y control del sistema musculoesquelético

**Tecnológico Nacional de México — Instituto Tecnológico de Tijuana**  
Departamento de Ingeniería Eléctrica y Electrónica · Ingeniería Biomédica  
**Asignatura:** Modelado de Sistemas Fisiológicos (IBF-1020)

| Información académica | Datos |
|:--|:--|
| **Estudiante** | Castro Alcántar Daniel Hiram |
| **Número de control** | 23212184 |
| **Correo institucional** | l23212184@tectijuana.edu.mx |
| **Docente** | Dr. Paul Antonio Valle Trujillo |
| **Modalidad** | Trabajo individual |
| **Fecha** | Noviembre de 2026 |

> **Descripción.** Modelado matemático y simulación *in silico* de un sistema musculoesquelético mediante una analogía electromecánica. Se compara la respuesta de un individuo sano (control) con un caso simulado de atrofia muscular y se estudia la compensación de su respuesta mediante control PI.

**Palabras clave:** Sistema musculoesquelético · Modelo matemático · Analogía electromecánica · Función de transferencia · Controlador PI · Simulaciones numéricas.

**Contenido:** [Objetivos](#objetivos) · [Modelo fisiológico](#modelo-fisiológico) · [Desarrollo matemático](#desarrollo-matemático) · [Análisis dinámico](#análisis-dinámico) · [Simulación y resultados](#simulación-y-resultados) · [Archivos y ejecución](#archivos-y-ejecución) · [Referencias](#referencias)

---

## Descripción de la asignatura

El modelado de sistemas fisiológicos permite representar el comportamiento de procesos biológicos mediante ecuaciones diferenciales, funciones de transferencia y analogías con sistemas físicos. La asignatura integra fundamentos de Ingeniería de Control, Electrónica y Ciencias de la Computación con Anatomía y Fisiología, utilizando simulaciones para estudiar la dinámica y evaluar estrategias de retroalimentación.

Esta práctica toma como base la **sección 5.5 del syllabus (2026)** y emplea un modelo simplificado formado por un elemento contráctil, un amortiguador viscoso y dos elementos elásticos. La experimentación es exclusivamente computacional; no representa la evaluación clínica de una persona.

## Objetivos

**Objetivo general:** modelar y analizar la dinámica del sistema musculoesquelético, comparar las condiciones control y caso, y estudiar una estrategia de control mediante MATLAB/Simulink y Python.

**Objetivos específicos:**

1. Identificar los elementos fisiológicos y las variables mecánicas del sistema.
2. Establecer la analogía fuerza–voltaje y su circuito equivalente.
3. Obtener las ecuaciones dinámicas y las funciones de transferencia implementadas.
4. Analizar los polos, la estabilidad y el error en estado estacionario.
5. Comparar las respuestas temporales de un individuo sano y un caso simulado de atrofia muscular.
6. Implementar las representaciones del modelo en MATLAB, Simulink, Simscape Electrical y Python.
7. Evaluar la aproximación de la respuesta del caso a la referencia mediante un controlador PI.
8. Documentar los resultados y el modelo fisiológico mediante gráficas y BioRender.

## Modelo fisiológico

El modelo descrito en la figura 5.3 del syllabus representa las propiedades **contráctiles, viscosas y elásticas** de una unidad musculotendinosa.

[![Diagrama biológico y modelo mecánico del sistema musculoesquelético](biorender/Biorender.png)](biorender/Biorender.png)

<p align="center"><em>Figura 1. Diagrama fisiológico y modelo mecánico equivalente: componente contráctil, amortiguamiento viscoso, estructuras elásticas musculares y tendón.</em></p>

| Elemento | Símbolo | Interpretación fisiológica |
|:--|:--:|:--|
| Elemento contráctil | **F₀(t)** | Componente activa de la fuerza muscular. |
| Fuerza del sistema | **F(t)** | Fuerza considerada en el modelo mecánico. |
| Amortiguador | **R** | Componente viscosa del tejido. |
| Elasticidad paralela | **Cₚ** | Compliancia de las estructuras musculares elásticas. |
| Elasticidad en serie | **Cₛ** | Compliancia asociada al tendón. |
| Desplazamiento total | **x(t)** | Deformación total del sistema. |
| Desplazamiento del elemento en serie | **x₁(t)** | Deformación del elemento Cₛ. |

En el modelo del profesor, la fuerza contráctil se expresa mediante una fracción de la fuerza del sistema:

<p align="center">
  <strong>F<sub>0</sub>(t) = α · F(t) &nbsp;&nbsp; (0 &lt; α &lt; 1)</strong>
</p>

La deformación del amortiguador corresponde a **x(t) − x₁(t)**; su velocidad relativa es:

<p align="center">
  <strong>v<sub>R</sub>(t) = d[x(t) − x<sub>1</sub>(t)] / dt</strong>
</p>

### Analogía electromecánica

La conversión al circuito equivalente utiliza la **analogía fuerza–voltaje**:

| Magnitud mecánica | Equivalente eléctrico |
|:--|:--|
| Fuerza | Voltaje |
| Velocidad | Corriente |
| Desplazamiento | Carga eléctrica |
| Amortiguador viscoso | Resistencia |
| Compliancia mecánica | Capacitancia |
| Masa, cuando está presente | Inductancia |

En esta analogía, las conexiones mecánicas en serie y paralelo **no necesariamente conservan la misma topología** al pasar al circuito eléctrico; deben respetarse las restricciones de fuerza y desplazamiento de cada rama.

### Parámetros de simulación

De acuerdo con la sección 5.5.2 del syllabus, la variación entre el individuo sano y el caso de atrofia muscular simulada se introduce únicamente en el parámetro resistivo **R**.

| Parámetro | Control (sano) | Caso (atrofia simulada) |
|:--|--:|--:|
| Entrada de referencia | 1 V | 1 V |
| Coeficiente α | 0.25 | 0.25 |
| Capacitancia Cₛ | 10 µF | 10 µF |
| Capacitancia Cₚ | 100 µF | 100 µF |
| Resistencia R | 100 Ω | 10 kΩ |

> Los valores se expresan en unidades del **circuito eléctrico equivalente** y corresponden a un ejercicio didáctico, no a mediciones fisiológicas directas de un paciente.

## Desarrollo matemático

El análisis manuscrito emplea el **principio de superposición** para obtener dos contribuciones a la fuerza de salida equivalente **Fₛ(t)**.

**[Consultar el desarrollo matemático completo (PDF)](analisis/Analisismatematico.pdf)**

### 1. Contribuciones del sistema

Con condiciones iniciales nulas, las dos ramas consideradas se expresan mediante:

**Contribución de la rama 1:**

<p align="center">
  <strong>F<sub>s1</sub>(s) / F(s) = [R · C<sub>s</sub> · s + 1] / [R · (C<sub>p</sub> + C<sub>s</sub>) · s + 1]</strong>
</p>

**Contribución de la rama 2:**

<p align="center">
  <strong>F<sub>s2</sub>(s) / F(s) = −α / [R · (C<sub>p</sub> + C<sub>s</sub>) · s + 1]</strong>
</p>

### 2. Función de transferencia equivalente

Al sumar ambas contribuciones se obtiene la relación entrada–salida utilizada en las simulaciones de fuerza:

<p align="center">
  <strong>G<sub>F</sub>(s) = F<sub>s</sub>(s) / F(s) = [R · C<sub>s</sub> · s + (1 − α)] / [R · (C<sub>p</sub> + C<sub>s</sub>) · s + 1]</strong>
</p>

En el dominio del tiempo, la ecuación diferencial correspondiente es:

<p align="center">
  <strong>R · (C<sub>p</sub> + C<sub>s</sub>) · dF<sub>s</sub>(t)/dt + F<sub>s</sub>(t) = R · C<sub>s</sub> · dF(t)/dt + (1 − α) · F(t)</strong>
</p>

### 3. Funciones de transferencia del control y del caso

Sustituyendo los valores de la tabla anterior:

**Individuo sano (control)**

<p align="center">
  <strong>G<sub>control</sub>(s) = (0.001s + 0.75) / (0.011s + 1)</strong>
</p>

**Atrofia muscular simulada (caso)**

<p align="center">
  <strong>G<sub>caso</sub>(s) = (0.1s + 0.75) / (1.1s + 1)</strong>
</p>

Estas son las funciones definidas en [**modeladopython.py**](python/modeladopython.py) y empleadas en las simulaciones incluidas en el repositorio.

### 4. Representación mediante ecuaciones diferenciales

Para la implementación numérica puede introducirse un estado auxiliar **z(t)** y la constante de tiempo **τ**:

<p align="center">
  <strong>τ · dz(t)/dt + z(t) = F(t)</strong>
</p>

<p align="center">
  <strong>F<sub>s</sub>(t) = [C<sub>s</sub> / (C<sub>p</sub> + C<sub>s</sub>)] · F(t) + [1 − α − C<sub>s</sub> / (C<sub>p</sub> + C<sub>s</sub>)] · z(t)</strong>
</p>

<p align="center">
  <strong>τ = R · (C<sub>p</sub> + C<sub>s</sub>)</strong>
</p>

Esta formulación permite reproducir la transferencia de fuerza mediante bloques de integradores, ganancias y sumadores en Simulink.

> **Nota sobre la variable de salida:** el syllabus contempla la transferencia **X(s)/F(s)** cuando se analiza desplazamiento. El desarrollo y los programas entregados para esta práctica muestran principalmente la transferencia de **fuerza equivalente Fₛ(s)/F(s)**. Se distingue explícitamente entre ambas variables para no confundir fuerza con desplazamiento.

## Análisis dinámico

### Polos y estabilidad

Ambas funciones de transferencia son de **primer orden**. El polo y la constante de tiempo del modelo general se calculan como:

<p align="center">
  <strong>p = −1 / [R · (C<sub>p</sub> + C<sub>s</sub>)] &nbsp;&nbsp; ; &nbsp;&nbsp; τ = R · (C<sub>p</sub> + C<sub>s</sub>)</strong>
</p>

| Característica | Control | Caso |
|:--|--:|--:|
| Constante de tiempo τ | **0.011 s** | **1.1 s** |
| Polo | −90.9091 s⁻¹ | −0.9091 s⁻¹ |
| Cero | −750 s⁻¹ | −7.5 s⁻¹ |
| Ganancia estática | 0.75 | 0.75 |
| Estabilidad | Estable | Estable |

Los polos están ubicados en el **semiplano izquierdo**, por lo que ambos sistemas son estables. El caso simulado tiene una constante de tiempo **100 veces mayor**, lo que explica una respuesta transitoria considerablemente más lenta.

### Error en estado estacionario

Ante una **entrada escalón unitario sostenida**, la ganancia estática de ambas funciones es:

<p align="center">
  <strong>G<sub>F</sub>(0) = 1 − α = 0.75</strong>
</p>

Si el error se define como la diferencia entre la entrada unitaria y la fuerza de salida, resulta:

<p align="center">
  <strong>e<sub>ss</sub> = 1 − G<sub>F</sub>(0) = 0.25</strong>
</p>

En cambio, la diferencia estacionaria **entre el control y el caso** es nula bajo ese mismo escalón, dado que sus ganancias estáticas son iguales. La principal diferencia aparece durante el transitorio.

## Simulación y resultados

### Herramientas utilizadas

| Herramienta | Aplicación en la práctica |
|:--|:--|
| **MATLAB** | Ejecución del cuaderno, procesamiento de señales y exportación de gráficas. |
| **Simulink** | Modelos por ecuaciones, funciones de transferencia y retroalimentación. |
| **Simscape Electrical** | Representación del circuito eléctrico equivalente. |
| **Python** | Simulación mediante las bibliotecas `numpy`, `control` y `matplotlib`. |
| **BioRender** | Ilustración del modelo fisiológico y sus elementos mecánicos. |

### Condiciones de simulación

El código Python adjunto utiliza un intervalo de **0 a 10 segundos**, con un paso de **0.001 s** y una señal rectangular unitaria aplicada aproximadamente entre **t = 1 s** y **t = 2 s**. La señal se utiliza para comparar las respuestas de las dos condiciones.

El syllabus solicita analizar la respuesta a un impulso unitario; el código aportado utiliza, en su lugar, un **pulso rectangular de duración finita**. No se consideran equivalentes sin especificar la duración y amplitud del pulso.

### Compensación mediante control PI

Se considera la salida del individuo sano como referencia y se utiliza retroalimentación para reducir la diferencia respecto al caso simulado. Los modelos entregados incorporan acción **proporcional–integral (PI)**:

<p align="center">
  <strong>K<sub>PI</sub>(s) = K<sub>p</sub> + K<sub>i</sub> / s</strong>
</p>

Para retroalimentación unitaria, la transferencia del sistema compensado se expresa como:

<p align="center">
  <strong>T(s) = [K<sub>PI</sub>(s) · G<sub>caso</sub>(s)] / [1 + K<sub>PI</sub>(s) · G<sub>caso</sub>(s)]</strong>
</p>

Las configuraciones concretas de los controladores pueden consultarse en los archivos de MATLAB/Simulink y Python. No se atribuyen aquí ganancias de capturas de sintonización ajenas al conjunto de archivos entregado.

### Comparación de las respuestas

[![Entrada, respuesta del control, respuesta del caso y sistema compensado](figuras/respuesta_simulink.png)](figuras/respuesta_simulink.png)

*Figura 2. Comparación de las respuestas obtenidas en MATLAB/Simulink ante la señal de entrada. Se muestran el individuo sano, el caso simulado y la salida compensada.*

**Observaciones principales:**

- La señal de referencia aplicada es un pulso rectangular.
- El modelo **control** responde rápidamente debido a su menor constante de tiempo.
- El modelo **caso** presenta una evolución más lenta por el aumento de R.
- La curva del **sistema compensado** se aproxima visualmente a la respuesta del control en la gráfica suministrada.

**Gráficas originales:** [MATLAB/Simulink (PDF)](figuras/_matlabsimulink.pdf) · [Modelo por EDO (PDF)](figuras/_matlabEDOsys.pdf) · [MATLAB (PDF)](figuras/_matlab.pdf).

La comparación cuantitativa entre plataformas requeriría utilizar exactamente las mismas condiciones iniciales, señales de entrada y configuraciones de controlador en cada implementación.

## Archivos y ejecución

### Organización del repositorio

```text
MSFP3/
├── README.md
├── CITATION.cff
├── analisis/
│   └── Analisis_matematico.pdf
├── biorender/
│   └── Biorender.png
├── figuras/
│   ├── respuesta_simulink.png
│   ├── _matlab.pdf
│   ├── _matlabEDOsys.pdf
│   └── _matlabsimulink.pdf
├── matlab/
│   ├── Castro23212184.mlx
│   └── elsistema.slx
└── python/
    └── modeladopython.py
```

**Archivos principales:** [Cuaderno de MATLAB](matlab/Castro23212184.mlx) · [Modelo de Simulink](matlab/elsistema.slx) · [Script de Python](python/modeladopython.py) · [Análisis matemático](analisis/Analisis_matematico.pdf) · [BioRender](biorender/Biorender.png).

### Reproducir en MATLAB / Simulink

1. Abrir MATLAB con Simulink y Simscape Electrical disponibles.
2. Establecer la carpeta `matlab/` como directorio de trabajo.
3. Abrir el archivo `Castro23212184.mlx` y comprobar que `elsistema.slx` se encuentre en esa misma carpeta.
4. Ejecutar el cuaderno y consultar las gráficas y las señales almacenadas.

### Reproducir en Python

Desde el directorio principal del repositorio:

```bash
python -m pip install numpy matplotlib control
python python/modeladopython.py
```

El programa guarda la figura `Musculoesqueletico_python.pdf` en el directorio desde el cual se ejecuta.

## Conclusiones

La analogía electromecánica permite representar las propiedades contráctiles, elásticas y viscosas del sistema musculoesquelético mediante un modelo dinámico de parámetros concentrados. Los resultados analíticos muestran que el aumento de **R** conserva la ganancia estática de la transferencia de fuerza, pero incrementa notablemente la constante de tiempo y reduce la rapidez de respuesta.

Las simulaciones permiten comparar las condiciones sano y caso, así como estudiar una compensación por retroalimentación. La verificación de equivalencia estricta entre MATLAB/Simulink y Python exige unificar los parámetros y contrastar directamente sus datos numéricos.

> **Alcance académico:** la condición denominada *atrofia muscular* es una simplificación para experimentación *in silico*. El modelo y el controlador no constituyen un diagnóstico ni una propuesta de tratamiento médico.

## Referencias

1. Valle Trujillo, P. A. (2026). *Syllabus para Modelado de Sistemas Fisiológicos*. Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, sección 5.5, pp. 87–95. [Repositorio de la asignatura](https://github.com/DrPaulValle/MSF-IBF1020).
2. Khoo, M. C. K. (2018). *Physiological Control Systems: Analysis, Simulation, and Estimation* (2nd ed.). IEEE Press.
3. Hoppensteadt, F. C., & Peskin, C. S. (2002). *Modeling and Simulation in Medicine and the Life Sciences* (2nd ed.). Springer.
4. Ogata, K. (2010). *Ingeniería de control moderna* (5.ª ed.). Pearson.
5. Nise, N. S. (2020). *Control Systems Engineering* (8th ed.). Wiley.

---

**Autor:** Castro Alcántar Daniel Hiram · **23212184**  
Ingeniería Biomédica · Instituto Tecnológico de Tijuana · Noviembre de 2026
