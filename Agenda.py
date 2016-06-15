# -*- coding: cp1252 -*-
## Importar librerias Tkinter y Pickle

from Tkinter import*
import pickle

##Funcion que recibe como argumento una ventana y la muestra
def mostrar(ventana):
    ventana.deiconify()

##Funcion que recibe como argumento una ventana y la oculta
def ocultar(ventana):
    ventana.withdraw()

##Funcion que recibe como argumento un StringVar y limpia lo que contenga
def limpiar(entry):
    entry.set("")

##Variables Globales utilizadas en distintas secciones    
listaDoctores=[]
listaPacientes=[]
listaCitas=[]
listaObjetosInfoDoctor=[]
listaObjetosInfoPaciente=[]
listaObjetosInfoCita=[]
listaTemporal=[]
listaObjetosInfoTratamientos=[]
CitaTemporal=""
DoctorTemporal=""
indiceDoctorTemporal=""
PacienteTemporal=""
indicePacienteTemporal=""

#Carga el archivo con la informacion de las citas mediante la libreria Pickle
def cargarArchivoCitas():
    global listaCitas
    archivo=file("listaCitas.txt")
    listaCitas=pickle.load(archivo)

#Carga el archivo con la informacion de los doctores mediante la libreria Pickle
def cargarArchivoDoctores():
    global listaDoctores
    archivo=file("listaDoctores.txt")
    listaDoctores=pickle.load(archivo)

#Carga el archivo con la informacion de los pacientes mediante la libreria Pickle
def cargarArchivoPacientes():
    global listaPacientes
    archivo=file("listaPacientes.txt")
    listaPacientes=pickle.load(archivo)

##Termina la aplicacion y guarda en archivos todos los cambios hechos a las listas
def salir():
    global listaDoctores
    global listaPacientes
    global listaCitas
    archivo=file("listaDoctores.txt",'w')
    archivo2=file("listaPacientes.txt",'w')
    archivo3=file("listaCitas.txt",'w')
    pickle.dump(listaCitas,archivo3)
    pickle.dump(listaPacientes,archivo2)
    pickle.dump(listaDoctores,archivo)
    v0.destroy()

##Se define la clase Doctor
class Doctor():
    def __init__(self,identificacion,nombre,fechaNacimiento,direccion,especialidad):
        self.identificacion=identificacion
        self.nombre=nombre
        self.listaTelefonos=[]
        self.listaCorreos=[]
        self.fechaNacimiento=fechaNacimiento
        self.direccion=direccion
        self.especialidad=especialidad
    def obtenerInfo(self):
        return self.identificacion,self.nombre,self.listaTelefonos,self.listaCorreos,self.fechaNacimiento,self.direccion,self.especialidad
    def obtenerNombre(self):
        return self.nombre

##Se define la clase tratamiento
class Tratamiento():
    def __init__(self,fecha,doctor,descripcion):
        self.fecha=fecha
        self.doctor=doctor
        self.descripcion=descripcion
        self.estado="Activo"
    def obtenerInfo(self):
        return self.fecha,self.doctor,self.descripcion,self.estado

#Se define la clase Paciente
class Paciente():
    def __init__(self,identificacion,nombre,fechaNacimiento,direccion,ocupacion):
        self.identificacion=identificacion
        self.nombre=nombre
        self.listaTelefonos=[]
        self.listaCorreos=[]
        self.listaTratamientos=[]
        self.fechaNacimiento=fechaNacimiento
        self.direccion=direccion
        self.ocupacion=ocupacion
    def obtenerInfo(self):
        return self.identificacion,self.nombre,self.listaTelefonos,self.listaCorreos,self.fechaNacimiento,self.direccion,self.ocupacion,self.listaTratamientos

#Se define la clase cita
class Cita():
    def __init__(self,fecha,hora,paciente,doctor):
        self.fecha=fecha
        self.hora=hora
        self.paciente=paciente
        self.doctor=doctor
        self.estado="Pendiente"
    def obtenerInfo(self):
        return self.fecha,self.hora,self.paciente,self.doctor,self.estado

#Toma una lista con objetos y elimina todos sus objetos de la respectiva ventana
def olvidarGrids(lista):
    for objeto in lista:
        objeto.pack_forget()
    lista=[]

def olvidarObjetos(lista):
    for objeto in lista:
        objeto.grid_forget()
    lista=[]

##Limpia Entrys
def limpiarEntry(entry):
    entry.set("")

def limpiarEntryDoctores():
    global vsNombreDoctor
    global vsIdentificacionDoctor
    global vsCorreoDoctor1
    global vsCorreoDoctor2
    global vsCorreoDoctor3
    global vsTelefonoDoctor1
    global vsTelefonoDoctor2
    global vsTelefonoDoctor3
    global vsfnacimientoDoctor
    global vsDireccionDoctor
    global vsEspecialidadDoctor
    vsNombreDoctor.set("")
    vsIdentificacionDoctor.set("")
    vsCorreoDoctor1.set("")
    vsCorreoDoctor2.set("")
    vsCorreoDoctor3.set("")
    vsTelefonoDoctor1.set("")
    vsTelefonoDoctor2.set("")
    vsTelefonoDoctor3.set("")
    vsfnacimientoDoctor.set("")
    vsDireccionDoctor.set("")
    vsEspecialidadDoctor.set("")

def limpiarEntryPacientes():
    global vsNombrePaciente
    global vsIdentificacionPaciente
    global vsCorreoPaciente1
    global vsCorreoPaciente2
    global vsCorreoPaciente3
    global vsTelefonoPaciente1
    global vsTelefonoPaciente2
    global vsTelefonoPaciente3
    global vsfnacimientoPaciente
    global vsDireccionPaciente
    global vsOcupacionPaciente
    vsNombrePaciente.set("")
    vsIdentificacionPaciente.set("")
    vsCorreoPaciente1.set("")
    vsCorreoPaciente2.set("")
    vsCorreoPaciente3.set("")
    vsTelefonoPaciente1.set("")
    vsTelefonoPaciente2.set("")
    vsTelefonoPaciente3.set("")
    vsfnacimientoPaciente.set("")
    vsDireccionPaciente.set("")
    vsOcupacionPaciente.set("")

def limpiarEntryCitas():
    global vsFechaCita
    global vsHoraCita
    vsFechaCita.set("")
    vsHoraCita.set("")

##Muestra todas las citas pendientes
def mostrarCitasPendientes():
    global listaCitas
    global listaObjetosInfoCita
    for cita in listaCitas:
        if cita.estado=="Pendiente":
            obj1=Label(vCitas,text="Doctor: "+cita.doctor.nombre,font=('Cambria',14),bg="lightblue")
            obj1.grid()
            obj2=Label(vCitas,text="Paciente: "+cita.paciente.nombre,font=('Cambria',14),bg="lightblue")
            obj2.grid()
            obj3=Label(vCitas,text="Fecha: "+cita.fecha,font=('Cambria',14),bg="lightblue")
            obj3.grid()
            obj4=Label(vCitas,text="Hora: "+cita.hora,font=('Cambria',14),bg="lightblue")
            obj4.grid()
            obj5=Label(vCitas,text="Estado: Pendiente",font=('Cambria',14),bg="lightblue")
            obj5.grid()
            obj6=Button(vCitas,text="Modificar Fecha u Hora",command=lambda:mostrarDatosCitaModificar(cita) or ocultar(vCitas) or seleccionarCita(cita))
            obj6.grid()
            obj7=Button(vCitas,text="Eliminar Cita",command=lambda:seleccionarCita(cita) or eliminarCita(cita) or ocultar(vCitas))
            obj7.grid()
            obj8=Button(vCitas,text="Cambiar Estado",command=lambda:seleccionarPaciente(cita.paciente.nombre,0) or seleccionarCita(cita) or mostrar(vConfirmarCambiarEstadoCita) or ocultar(vCitas))
            obj8.grid()
            listaObjetosInfoCita.append(obj1)
            listaObjetosInfoCita.append(obj2)
            listaObjetosInfoCita.append(obj3)
            listaObjetosInfoCita.append(obj4)
            listaObjetosInfoCita.append(obj5)
            listaObjetosInfoCita.append(obj6)
            listaObjetosInfoCita.append(obj7)
            listaObjetosInfoCita.append(obj8)
    mostrar(vCitas)

#Muestra todas las citas en las q el paciente ya ha asistido
def mostrarCitasRealizadas():
    global listaCitas
    global listaObjetosInfoCita
    for cita in listaCitas:
        if cita.estado=="Realizada":
            obj1=Label(vCitas,text="Doctor: "+cita.doctor.nombre,font=('Cambria',14),bg="lightblue")
            obj1.grid()
            obj2=Label(vCitas,text="Paciente: "+cita.paciente.nombre,font=('Cambria',14),bg="lightblue")
            obj2.grid()
            obj3=Label(vCitas,text="Fecha: "+cita.fecha,font=('Cambria',14),bg="lightblue")
            obj3.grid()
            obj4=Label(vCitas,text="Hora: "+cita.hora,font=('Cambria',14),bg="lightblue")
            obj4.grid()
            obj5=Label(vCitas,text="Estado: Realizada",font=('Cambria',14),bg="lightblue")
            obj5.grid()
            obj6=Button(vCitas,text="Eliminar Cita",command=lambda:seleccionarCita(cita) or eliminarCita(cita) or ocultar(vCitas))
            obj6.grid()
            listaObjetosInfoCita.append(obj1)
            listaObjetosInfoCita.append(obj2)
            listaObjetosInfoCita.append(obj3)
            listaObjetosInfoCita.append(obj4)
            listaObjetosInfoCita.append(obj5)
            listaObjetosInfoCita.append(obj6)
    mostrar(vCitas)

#Muestra todas las citas de un determinado dia
def mostrarCitasPorDia(Dia):
    global listaCitas
    global listaObjetosInfoCita
    for cita in listaCitas:
        if cita.fecha==Dia:
            obj1=Label(vCitas,text="Doctor: "+cita.doctor.nombre,font=('Cambria',14),bg="lightblue")
            obj1.grid()
            obj2=Label(vCitas,text="Paciente: "+cita.paciente.nombre,font=('Cambria',14),bg="lightblue")
            obj2.grid()
            obj3=Label(vCitas,text="Fecha: "+cita.fecha,font=('Cambria',14),bg="lightblue")
            obj3.grid()
            obj4=Label(vCitas,text="Hora: "+cita.hora,font=('Cambria',14),bg="lightblue")
            obj4.grid()
            obj5=Label(vCitas,text="Estado: "+cita.estado,font=('Cambria',14),bg="lightblue")
            obj5.grid()
            obj6=Button(vCitas,text="Eliminar Cita",command=lambda:seleccionarCita(cita) or eliminarCita(cita) or ocultar(vCitas))
            obj6.grid()
            if cita.estado=="Pendiente":
                obj7=Button(vCitas,text="Modificar Fecha u Hora",command=lambda:mostrarDatosCitaModificar(cita) or ocultar(vCitas) or seleccionarCita(cita))
                obj7.grid()
                obj8=Button(vCitas,text="Cambiar Estado",command=lambda:seleccionarPaciente(cita.paciente.nombre,0) or seleccionarCita(cita) or mostrar(vConfirmarCambiarEstadoCita) or ocultar(vCitas))
                obj8.grid()
                listaObjetosInfoCita.append(obj7)
                listaObjetosInfoCita.append(obj8)
            listaObjetosInfoCita.append(obj1)
            listaObjetosInfoCita.append(obj2)
            listaObjetosInfoCita.append(obj3)
            listaObjetosInfoCita.append(obj4)
            listaObjetosInfoCita.append(obj5)
            listaObjetosInfoCita.append(obj6)
    mostrar(vCitas)

#Muestra Todas las citas de un determinado Doctor
def mostrarCitasDoctor(Doctor):
    global listaCitas
    global listaObjetosInfoCita
    for cita in listaCitas:
        if cita.doctor.nombre==Doctor and cita.estado=="Pendiente":
            obj1=Label(vCitas,text="Doctor: "+cita.doctor.nombre,font=('Cambria',14),bg="lightblue")
            obj1.grid()
            obj2=Label(vCitas,text="Paciente: "+cita.paciente.nombre,font=('Cambria',14),bg="lightblue")
            obj2.grid()
            obj3=Label(vCitas,text="Fecha: "+cita.fecha,font=('Cambria',14),bg="lightblue")
            obj3.grid()
            obj4=Label(vCitas,text="Hora: "+cita.hora,font=('Cambria',14),bg="lightblue")
            obj4.grid()
            obj5=Label(vCitas,text="Estado: Pendiente",font=('Cambria',14),bg="lightblue")
            obj5.grid()
            obj6=Button(vCitas,text="Eliminar Cita",command=lambda:seleccionarCita(cita) or eliminarCita(cita) or ocultar(vCitas))
            obj6.grid()
            obj7=Button(vCitas,text="Modificar Fecha u Hora",command=lambda:mostrarDatosCitaModificar(cita) or ocultar(vCitas) or seleccionarCita(cita))
            obj7.grid()
            obj8=Button(vCitas,text="Cambiar Estado",command=lambda:seleccionarPaciente(cita.paciente.nombre,0) or seleccionarCita(cita) or mostrar(vConfirmarCambiarEstadoCita) or ocultar(vCitas))
            obj8.grid()
            listaObjetosInfoCita.append(obj7)
            listaObjetosInfoCita.append(obj8)
            listaObjetosInfoCita.append(obj1)
            listaObjetosInfoCita.append(obj2)
            listaObjetosInfoCita.append(obj3)
            listaObjetosInfoCita.append(obj4)
            listaObjetosInfoCita.append(obj5)
            listaObjetosInfoCita.append(obj6)
    mostrar(vCitas)
#Muestra Todas las citas de un determinado paciente
def mostrarCitasPaciente(Paciente):
    global listaCitas
    global listaObjetosInfoCita
    for cita in listaCitas:
        if cita.paciente.nombre==Paciente and cita.estado=="Pendiente":
            obj1=Label(vCitas,text="Doctor: "+cita.doctor.nombre,font=('Cambria',14),bg="lightblue")
            obj1.grid()
            obj2=Label(vCitas,text="Paciente: "+cita.paciente.nombre,font=('Cambria',14),bg="lightblue")
            obj2.grid()
            obj3=Label(vCitas,text="Fecha: "+cita.fecha,font=('Cambria',14),bg="lightblue")
            obj3.grid()
            obj4=Label(vCitas,text="Hora: "+cita.hora,font=('Cambria',14),bg="lightblue")
            obj4.grid()
            obj5=Label(vCitas,text="Estado: Pendiente",font=('Cambria',14),bg="lightblue")
            obj5.grid()
            obj6=Button(vCitas,text="Eliminar Cita",command=lambda:seleccionarCita(cita) or eliminarCita(cita) or ocultar(vCitas))
            obj6.grid()
            obj7=Button(vCitas,text="Modificar Fecha u Hora",command=lambda:mostrarDatosCitaModificar(cita) or ocultar(vCitas) or seleccionarCita(cita))
            obj7.grid()
            obj8=Button(vCitas,text="Cambiar Estado",command=lambda:seleccionarPaciente(cita.paciente.nombre,0) or seleccionarCita(cita) or mostrar(vConfirmarCambiarEstadoCita) or ocultar(vCitas))
            obj8.grid()
            listaObjetosInfoCita.append(obj7)
            listaObjetosInfoCita.append(obj8)
            listaObjetosInfoCita.append(obj1)
            listaObjetosInfoCita.append(obj2)
            listaObjetosInfoCita.append(obj3)
            listaObjetosInfoCita.append(obj4)
            listaObjetosInfoCita.append(obj5)
            listaObjetosInfoCita.append(obj6)
    mostrar(vCitas)

#Cambia el estado de una cita a realizada
def CambiarEstadoCita():
    global CitaTemporal
    global listaCitas
    
    for cita in listaCitas:
        if cita.doctor.nombre==CitaTemporal.doctor.nombre and cita.fecha==CitaTemporal.fecha and cita.hora==CitaTemporal.hora:
            cita.estado="Realizada"
    mostrar(vDeseaAsignarTratamiento)

#Asigna un tratamiento a un paciente
def asignarTratamiento(descripcion):
    global CitaTemporal
    global PacienteTemporal
    global listaPacientes

    if descripcion=="":
        return mostrar(vFaltaInfoDescripcion)

    nuevoTratamiento=Tratamiento(CitaTemporal.fecha,f.doctor,descripcion)

    for paciente in listaPacientes:
        if paciente.nombre==PacienteTemporal:
            paciente.listaTratamientos.append(nuevoTratamiento)
            for trata in paciente.listaTratamientos:
                print trata.doctor
                print trata.fecha
                print trata.descripcion
            break

    mostrar(vTratamientoAsignado)

#Declara como finalizado un tratamiento        
def cancelarTratamiento(Tratamiento):
    Tratamiento.estado="Finalizado"
    mostrar(vTratamientoCancelado)

##Selecciona una cita para trabajar con esta globalmente    
def seleccionarCita(cita):
    global CitaTemporal
    CitaTemporal=cita
#Muestra un listbox con los doctores registrados   
def mostrarDoctores():
    global ListBoxDoctores
    global ListBoxDoctores2
    global listaDoctores
    for doctor in listaDoctores:
        ListBoxDoctores.insert(END,doctor.nombre)
        ListBoxDoctores2.insert(END,doctor.nombre)
#Muestra un listbox con los pacientes registrados        
def mostrarPacientes():
    global ListBoxPacientes
    global ListBoxPacientes2
    global listaPacientes
    for paciente in listaPacientes:
        ListBoxPacientes.insert(END,paciente.nombre)
        ListBoxPacientes2.insert(END,paciente.nombre)
##Muestra un listbox con fechas
def mostrarFechas():
    global ListBoxFechas
    global listaCitas
    global listaTemporal
    for cita in listaCitas:
        if cita.fecha not in listaTemporal:
            listaTemporal.append(cita.fecha)
    for fecha in listaTemporal:
        ListBoxFechas.insert(END,fecha)
##Funcion para crear una nueva instancia de la clase doctor
def agregarDoctor(nombre,identificacion,correo1,correo2,correo3,telefono1,telefono2,telefono3,fechaNacimiento,direccion,especialidad,lista):
    global ListBoxDoctores
    global listaDoctores
    
    if nombre=="" or identificacion=="" or correo1=="" or telefono1=="" or fechaNacimiento=="" or direccion=="" or especialidad=="":
        return mostrar(vFaltaInfoDoctor)
    
    for doctor in listaDoctores:
        if doctor.identificacion==identificacion:
            return mostrar(vDoctorRepetido)

    for doctor in listaDoctores:
        if doctor.nombre==nombre:
            return mostrar(vNombreDoctorRepetido)
        
    if correo1==correo2 or correo1==correo3:
        return mostrar(vInfoDoctorRepetida)

    if telefono1==telefono2 or telefono1==telefono3:
        return mostrar(vInfoDoctorRepetida)
            
    else:
        nuevoDoctor=Doctor(identificacion,nombre,fechaNacimiento,direccion,especialidad)
        nuevoDoctor.listaCorreos.append(correo1)
        nuevoDoctor.listaTelefonos.append(telefono1)
        if correo2!="":
            nuevoDoctor.listaCorreos.append(correo2)
        if correo3!="":
            nuevoDoctor.listaCorreos.append(correo3)
        if telefono2!="":
            nuevoDoctor.listaTelefonos.append(telefono2)
        if telefono3!="":
            nuevoDoctor.listaTelefonos.append(telefono3)
        lista.append(nuevoDoctor)
        ListBoxDoctores.insert(END,nuevoDoctor.nombre)
        return mostrar(vDoctorAgregado)

#Funcion para agregar una nueva instancia de la clase paciente
def agregarPaciente(nombre,identificacion,correo1,correo2,correo3,telefono1,telefono2,telefono3,fechaNacimiento,direccion,ocupacion,lista):
    global ListBoxPacientes
    global listaPacientes
    
    if nombre=="" or identificacion=="" or correo1=="" or telefono1=="" or fechaNacimiento=="" or direccion=="" or ocupacion=="":
        return mostrar(vFaltaInfoPaciente)
    
    for paciente in listaPacientes:
        if paciente.identificacion==identificacion:
            return mostrar(vPacienteRepetido)

    for paciente in listaPacientes:
        if paciente.nombre==nombre:
            return mostrar(vNombrePacienteRepetido)
        
    if correo1==correo2 or correo1==correo3:
        return mostrar(vInfoPacienteRepetida)

    if telefono1==telefono2 or telefono1==telefono3:
        return mostrar(vInfoPacienteRepetida)
            
    else:
        nuevoPaciente=Paciente(identificacion,nombre,fechaNacimiento,direccion,ocupacion)
        nuevoPaciente.listaCorreos.append(correo1)
        nuevoPaciente.listaTelefonos.append(telefono1)
        if correo2!="":
            nuevoPaciente.listaCorreos.append(correo2)
        if correo3!="":
            nuevoPaciente.listaCorreos.append(correo3)
        if telefono2!="":
            nuevoPaciente.listaTelefonos.append(telefono2)
        if telefono3!="":
            nuevoPaciente.listaTelefonos.append(telefono3)
        lista.append(nuevoPaciente)
        ListBoxPacientes.insert(END,nuevoPaciente.nombre)
        print nuevoPaciente.listaTelefonos
        return mostrar(vPacienteAgregado)

#Funcion para agregar una nueva instancia de la clase Cita
def agregarCita(fecha,hora,paciente,doctor,lista):
    global listaCitas
    global listaTemporal
    global listaDoctores
    global listaPacientes
    global ListBoxFechas
    listaCitasTemporal=[]
    
    if fecha=="" or hora=="":
        return mostrar(vFaltaInfoCita)

    for cita in listaCitas:
        if cita.doctor.nombre==doctor:
            listaCitasTemporal.append(cita)

    for cita in listaCitasTemporal:
        if cita.fecha==fecha and cita.hora==hora:
            limpiarEntryCitas()
            return mostrar(vDoctorOcupado)
    listaCitasTemporal=[]

    for cita in listaCitas:
        if cita.paciente.nombre==paciente:
            listaCitasTemporal.append(cita)

    for cita in listaCitasTemporal:
        if cita.fecha==fecha and cita.hora==hora:
            limpiarEntryCitas()
            return mostrar(vPacienteOcupado)
    listaCitasTemporal=[]

    for PACIENTE in listaPacientes:
        if PACIENTE.nombre==paciente:
            paciente=PACIENTE
            break

    for DOCTOR in listaDoctores:
        if DOCTOR.nombre==doctor:
            doctor=DOCTOR
            break
    
    nuevaCita=Cita(fecha,hora,paciente,doctor)
    lista.append(nuevaCita)
    limpiarEntryCitas()
    if fecha not in listaTemporal:
        ListBoxFechas.insert(END,fecha)
    return mostrar(vCitaAgregada)

#Funcion para buscar un doctor mediante su identificacion    
def buscar_doctor(identificacion):
    global DoctorTemporal
    global listaDoctores
    for doctor in listaDoctores:
        if doctor.identificacion==identificacion:
            DoctorTemporal=doctor.nombre
            return mostrar(vDoctorEncontrado)
    return mostrar(vDoctorNoEncontrado)
#Funcion para buscar un paciente mediante su identificacion
def buscar_paciente(identificacion):
    global PacienteTemporal
    global listaPacientes
    for Paciente in listaPacientes:
        if Paciente.identificacion==identificacion:
            PacienteTemporal=Paciente.nombre
            return mostrar(vPacienteEncontrado)
    return mostrar(vPacienteNoEncontrado)
#Funcion que reescribe la info de una instancia de tipo doctor  
def modificarInfoDoctor(nombre,identificacion,correo1,correo2,correo3,telefono1,telefono2,telefono3,fechaNacimiento,direccion,especialidad):
    global DoctorTemporal
    global listaDoctores

    if nombre=="" or identificacion=="" or correo1=="" or telefono1=="" or fechaNacimiento=="" or direccion=="" or especialidad=="":
        return mostrar(vFaltaInfoDoctor2)

    if nombre!=DoctorTemporal:    
        for doctor in listaDoctores:
            if doctor.nombre==nombre:
                return mostrar(vNombreDoctorRepetido2)
        
    if correo1==correo2 or correo1==correo3:
        return mostrar(vInfoDoctorRepetida2)

    if telefono1==telefono2 or telefono1==telefono3:
        return mostrar(vInfoDoctorRepetida2)
    
    for doctor in listaDoctores:
        if doctor.nombre==DoctorTemporal:                
            doctor.nombre=nombre
            if identificacion!=doctor.identificacion:
                for DOCTOR in listaDoctores:
                    if DOCTOR.identificacion==identificacion:
                        return mostrar(vDoctorRepetido2)
            doctor.identificacion=identificacion
            doctor.fechaNacimiento=fechaNacimiento
            doctor.direccion=direccion
            doctor.especialidad=especialidad
            doctor.listaCorreos=[]
            doctor.listaCorreos.append(correo1)
            doctor.listaCorreos.append(correo2)
            doctor.listaCorreos.append(correo3)
            doctor.listaTelefonos=[]
            doctor.listaTelefonos.append(telefono1)
            doctor.listaTelefonos.append(telefono2)
            doctor.listaTelefonos.append(telefono3)
            DoctorTemporal=doctor.nombre
            break
    
    mostrar(vDoctorModificado)
#Funcion que reescribe la info de una instancia de tipo paciente  
def modificarInfoPaciente(nombre,identificacion,correo1,correo2,correo3,telefono1,telefono2,telefono3,fechaNacimiento,direccion,ocupacion):
    global PacienteTemporal
    global listaPacientes

    if nombre=="" or identificacion=="" or correo1=="" or telefono1=="" or fechaNacimiento=="" or direccion=="" or ocupacion=="":
        return mostrar(vFaltaInfoPaciente2)

    if nombre!=PacienteTemporal:    
        for Paciente in listaPacientes:
            if Paciente.nombre==nombre:
                return mostrar(vNombrePacienteRepetido2)
        
    if correo1==correo2 or correo1==correo3:
        return mostrar(vInfoPacienteRepetida2)

    if telefono1==telefono2 or telefono1==telefono3:
        return mostrar(vInfoPacienteRepetida2)
    
    for Paciente in listaPacientes:
        if Paciente.nombre==PacienteTemporal:                
            Paciente.nombre=nombre
            if identificacion!=Paciente.identificacion:
                for PACIENTE in listaPacientes:
                    if PACIENTE.identificacion==identificacion:
                        return mostrar(vPacienteRepetido2)
            Paciente.identificacion=identificacion
            Paciente.fechaNacimiento=fechaNacimiento
            Paciente.direccion=direccion
            Paciente.ocupacion=ocupacion
            Paciente.listaCorreos=[]
            Paciente.listaCorreos.append(correo1)
            Paciente.listaCorreos.append(correo2)
            Paciente.listaCorreos.append(correo3)
            Paciente.listaTelefonos=[]
            Paciente.listaTelefonos.append(telefono1)
            Paciente.listaTelefonos.append(telefono2)
            Paciente.listaTelefonos.append(telefono3)
            PacienteTemporal=Paciente.nombre
            break
        
    mostrar(vPacienteModificado)
#Funcion que muestra todos los tratamientos de un paciente
def mostrarTratamientos():
    global PacienteTemporal
    global listaPacientes
    global listaObjetosInfoTratamientos

    for paciente in listaPacientes:
        if paciente.nombre==PacienteTemporal:
            for tratamiento in paciente.listaTratamientos:
                obj1=Label(vVerTratamientos,font=('Cambria',14),bg="lightblue",text=tratamiento.doctor.nombre)
                obj1.grid()
                obj2=Label(vVerTratamientos,font=('Cambria',14),bg="lightblue",text=tratamiento.fecha)
                obj2.grid()
                obj5=Label(vVerTratamientos,font=('Cambria',14),bg="lightblue",text=tratamiento.descripcion)
                obj5.grid()
                obj3=Label(vVerTratamientos,font=('Cambria',14),bg="lightblue",text=tratamiento.estado)
                obj3.grid()
                if tratamiento.estado=="Activo":
                    obj4=Button(vVerTratamientos,text="Cancelar este Tratamiento",command=lambda:cancelarTratamiento(tratamiento) or ocultar(vVerTratamientos) or olvidarObjetos(listaObjetosInfoTratamientos))
                    obj4.grid()
                    listaObjetosInfoTratamientos.append(obj4)
                listaObjetosInfoTratamientos.append(obj1)
                listaObjetosInfoTratamientos.append(obj2)
                listaObjetosInfoTratamientos.append(obj3)
                listaObjetosInfoTratamientos.append(obj5)
    mostrar(vVerTratamientos)
    
#Muestra los datos actuales de un doctor para q se modifiquen
def mostrarDatosDoctorModificar():
    global vsNombreDoctor2
    global vsIdentificacionDoctor2
    global vsCorreoDoctor1_2
    global vsCorreoDoctor2_2
    global vsCorreoDoctor3_2
    global vsTelefonoDoctor1_2
    global vsTelefonoDoctor2_2
    global vsTelefonoDoctor3_2
    global vsfnacimientoDoctor2
    global vsDireccionDoctor2
    global vsEspecialidadDoctor2
    global DoctorTemporal
    global listaDoctores
    
    DoctorActual=""
    for Doctor in listaDoctores:
        if Doctor.nombre==DoctorTemporal:
            DoctorActual=Doctor
            break
    vsNombreDoctor2.set(DoctorActual.nombre)
    vsIdentificacionDoctor2.set(DoctorActual.identificacion)
    vsCorreoDoctor1_2.set(DoctorActual.listaCorreos[0])
    if len(DoctorActual.listaCorreos)>=2:
        vsCorreoDoctor2_2.set(DoctorActual.listaCorreos[1])
    if len(DoctorActual.listaCorreos)>=3:
        vsCorreoDoctor3_2.set(DoctorActual.listaCorreos[2])
    vsTelefonoDoctor1_2.set(DoctorActual.listaTelefonos[0])
    if len(DoctorActual.listaTelefonos)>=2:
        vsTelefonoDoctor2_2.set(DoctorActual.listaTelefonos[1])
    if len(DoctorActual.listaTelefonos)>=3:
        vsTelefonoDoctor3_2.set(DoctorActual.listaTelefonos[2])
    vsfnacimientoDoctor2.set(DoctorActual.fechaNacimiento)
    vsDireccionDoctor2.set(DoctorActual.direccion)
    vsEspecialidadDoctor2.set(DoctorActual.especialidad)
    mostrar(vModificarDoctor)
#Muestra los datos actuales de un paciente para q se modifiquen
def mostrarDatosPacienteModificar():
    global vsNombrePaciente2
    global vsIdentificacionPaciente2
    global vsCorreoPaciente1_2
    global vsCorreoPaciente2_2
    global vsCorreoPaciente3_2
    global vsTelefonoPaciente1_2
    global vsTelefonoPaciente2_2
    global vsTelefonoPaciente3_2
    global vsfnacimientoPaciente2
    global vsDireccionPaciente2
    global vsOcupacionPaciente2
    global PacienteTemporal
    global listaPacientes
    
    PacienteActual=""
    for Paciente in listaPacientes:
        if Paciente.nombre==PacienteTemporal:
            PacienteActual=Paciente
            break
    vsNombrePaciente2.set(PacienteActual.nombre)
    vsIdentificacionPaciente2.set(PacienteActual.identificacion)
    vsCorreoPaciente1_2.set(PacienteActual.listaCorreos[0])
    if len(PacienteActual.listaCorreos)>=2:
        vsCorreoPaciente2_2.set(PacienteActual.listaCorreos[1])
    if len(PacienteActual.listaCorreos)>=3:
        vsCorreoPaciente3_2.set(PacienteActual.listaCorreos[2])
    vsTelefonoPaciente1_2.set(PacienteActual.listaTelefonos[0])
    if len(PacienteActual.listaTelefonos)>=2:
        vsTelefonoPaciente2_2.set(PacienteActual.listaTelefonos[1])
    if len(PacienteActual.listaTelefonos)>=3:
        vsTelefonoPaciente3_2.set(PacienteActual.listaTelefonos[2])
    vsfnacimientoPaciente2.set(PacienteActual.fechaNacimiento)
    vsDireccionPaciente2.set(PacienteActual.direccion)
    vsOcupacionPaciente2.set(PacienteActual.ocupacion)
    mostrar(vModificarPaciente)
#Muestra los datos actuales de una cita para q se modifiquen
def mostrarDatosCitaModificar(cita):
    global vsFechaCita2
    global vsHoraCita2

    vsFechaCita2.set(cita.fecha)
    vsHoraCita2.set(cita.hora)
    mostrar(vModificarCita)
##Reescribe los datos de una instancia de tipo cita
def modificarCita(fechaModificada,horaModificada):
    global CitaTemporal
    global listaCitas
    listaCitasTemporal=[]
    for cita in listaCitas:
        if cita.doctor.nombre==CitaTemporal.doctor.nombre and cita.fecha==CitaTemporal.fecha and cita.hora==CitaTemporal.hora:
            if cita.fecha!=fechaModificada or cita.hora!=horaModificada:
                 for CITA in listaCitas:
                    if CITA.doctor.nombre==cita.doctor:
                        listaCitasTemporal.append(cita)

                 for citaSameDoctor in listaCitasTemporal:
                    if citaSameDoctor.fecha==fecha and citaSameDoctor.hora==hora:
                        return mostrar(vDoctorOcupado2)
                 listaCitasTemporal=[]

                 for CITA in listaCitas:
                    if CITA.paciente.nombre==cita.paciente:
                        listaCitasTemporal.append(cita)

                 for citaSamePaciente in listaCitasTemporal:
                    if citaSamePaciente.fecha==fecha and citaSamePaciente.hora==hora:
                        return mostrar(vPacienteOcupado2)
            cita.fecha=fechaModificada
            cita.hora=horaModificada
            break
    mostrar(vCitaModificada)
#Selecciona un  doctor para trabajar con el globalmente  
def seleccionarDoctor(nombre,indice):
    global DoctorTemporal
    global indiceDoctorTemporal
    DoctorTemporal=nombre
    indiceDoctorTemporal=indice

#Selecciona un paciente para trabajar con el globalmente
def seleccionarPaciente(nombre,indice):
    global PacienteTemporal
    global indicePacienteTemporal
    PacienteTemporal=nombre
    indicePacienteTemporal=indice
#Elimina una cita
def eliminarCita(CITA):
    global listaCitas
    global listaObjetosInfoCita
    i=0
    for cita in listaCitas:
        if cita.fecha==CITA.fecha and cita.hora==CITA.hora and cita.doctor.nombre==CITA.doctor.nombre:
            del listaCitas[i]
            break
        i+=1

    for objeto in listaObjetosInfoCita:
        objeto.grid_forget()

    return mostrar(vCitaEliminada)
#Elimina un doctor
def eliminarDoctor():
    global listaDoctores
    global DoctorTemporal
    global ListBoxDoctores
    global ListBoxDoctores2
    global indiceDoctorTemporal
    i=0
    for doctor in listaDoctores:
        if doctor.nombre==DoctorTemporal:
            del listaDoctores[i]
            break
        i+=1
    ListBoxDoctores.delete(indiceDoctorTemporal)
    ListBoxDoctores2.delete(indiceDoctorTemporal)
    return mostrar(vDoctorEliminado)
#Elimina un paciente
def eliminarPaciente():
    global listaPacientes
    global PacienteTemporal
    global ListBoxPacientes
    global ListBoxPacientes2
    global indicePacienteTemporal
    i=0
    for Paciente in listaPacientes:
        if Paciente.nombre==PacienteTemporal:
            del listaPacientes[i]
            break
        i+=1
    ListBoxPacientes.delete(indicePacienteTemporal)
    ListBoxPacientes2.delete(indicePacienteTemporal)
    return mostrar(vPacienteEliminado)
#Actualiza el listbox de doctores cuando se modifique la info de estos
def actualizarListboxDoctores():
    global DoctorTemporal
    global ListBoxDoctores
    global ListBoxDoctores2
    global indiceDoctorTemporal
    ListBoxDoctores.delete(indiceDoctorTemporal)
    ListBoxDoctores.insert(END,DoctorTemporal)
    ListBoxDoctores2.delete(indiceDoctorTemporal)
    ListBoxDoctores2.insert(END,DoctorTemporal)
    return mostrar(vDoctores)
#Actualiza el listbox de pacientes cuando se modifique la info de estos
def actualizarListboxPacientes():
    global PacienteTemporal
    global ListBoxPacientes
    global ListBoxPacientes2
    global indicePacienteTemporal
    ListBoxPacientes.delete(indicePacienteTemporal)
    ListBoxPacientes.insert(END,PacienteTemporal)
    ListBoxPacientes2.delete(indicePacienteTemporal)
    ListBoxPacientes2.insert(END,PacienteTemporal)
    return mostrar(vPacientes)
#MUestra la info detallada un determinado doctor
def mostrarInfoDoctor(Doctor):
    global listaDoctores
    global listaObjetosInfoDoctor
    global DoctorTemporal
    DoctorActual=''
    for doctor in listaDoctores:
        if doctor.nombre==Doctor:
            DoctorActual=doctor
    Nombre="Nombre:  "+DoctorActual.nombre
    lVerInfoDoctorNombre=Label(vVerInfoDoctor,font=('Cambria',14),bg="lightblue",text=Nombre)
    lVerInfoDoctorNombre.pack()
    listaObjetosInfoDoctor.append(lVerInfoDoctorNombre)
    Identificacion="Identificacion:  "+DoctorActual.identificacion
    lVerInfoDoctorId=Label(vVerInfoDoctor,font=('Cambria',14),bg="lightblue",text=Identificacion)
    lVerInfoDoctorId.pack()
    listaObjetosInfoDoctor.append(lVerInfoDoctorId)
    Telefonos="Telefonos:  "
    for telefono in DoctorActual.listaTelefonos:
        if telefono==DoctorActual.listaTelefonos[-1]:
            Telefonos=Telefonos+telefono
        else:
            Telefonos=Telefonos+telefono+ ", "
    lVerInfoDoctorTelefono=Label(vVerInfoDoctor,font=('Cambria',14),bg="lightblue",text=Telefonos)
    lVerInfoDoctorTelefono.pack()
    listaObjetosInfoDoctor.append(lVerInfoDoctorTelefono)
    Correos="Correos:  "
    for correo in DoctorActual.listaCorreos:
        if correo==DoctorActual.listaCorreos[-1]:
            Correos=Correos+correo
        else:
            Correos=Correos+correo+", "
    lVerInfoDoctorCorreo=Label(vVerInfoDoctor,font=('Cambria',14),bg="lightblue",text=Correos)
    lVerInfoDoctorCorreo.pack()
    listaObjetosInfoDoctor.append(lVerInfoDoctorCorreo)
    FechaNacimiento="Fecha de Nacimiento:  "+DoctorActual.fechaNacimiento
    lVerInfoDoctorNacimiento=Label(vVerInfoDoctor,font=('Cambria',14),bg="lightblue",text=FechaNacimiento)
    lVerInfoDoctorNacimiento.pack()
    listaObjetosInfoDoctor.append(lVerInfoDoctorNacimiento)
    Direccion="Direccion:  "+DoctorActual.direccion
    lVerInfoDoctorDireccion=Label(vVerInfoDoctor,font=('Cambria',14),bg="lightblue",text=Direccion)
    lVerInfoDoctorDireccion.pack()
    listaObjetosInfoDoctor.append(lVerInfoDoctorDireccion)
    Especialidad="Especialidad:  "+DoctorActual.especialidad
    lVerInfoDoctorEspecialidad=Label(vVerInfoDoctor,font=('Cambria',14),bg="lightblue",text=Especialidad)
    lVerInfoDoctorEspecialidad.pack()
    listaObjetosInfoDoctor.append(lVerInfoDoctorEspecialidad)
    mostrar(vVerInfoDoctor)
#MUestra la info detallada un determinado paciente
def mostrarInfoPaciente(Paciente):
    global listaPacientes
    global listaObjetosInfoPaciente
    global PacienteTemporal
    PacienteActual=""
    for paciente in listaPacientes:
        if paciente.nombre==Paciente:
            PacienteActual=paciente
    Nombre="Nombre:  " +PacienteActual.nombre
    lVerInfoPacienteNombre=Label(vVerInfoPaciente,font=('Cambria',14),bg="lightblue",text=Nombre)
    lVerInfoPacienteNombre.pack()
    listaObjetosInfoPaciente.append(lVerInfoPacienteNombre)
    Identificacion="Identificacion:  "+PacienteActual.identificacion
    lVerInfoPacienteId=Label(vVerInfoPaciente,font=('Cambria',14),bg="lightblue",text=Identificacion)
    lVerInfoPacienteId.pack()
    listaObjetosInfoPaciente.append(lVerInfoPacienteId)
    Telefonos="Telefonos:  "
    for telefono in PacienteActual.listaTelefonos:
        if telefono==PacienteActual.listaTelefonos[-1]:
            Telefonos=Telefonos+telefono
        else:
            Telefonos=Telefonos+telefono+", "
    lVerInfoPacienteTelefono=Label(vVerInfoPaciente,font=('Cambria',14),bg="lightblue",text=Telefonos)
    lVerInfoPacienteTelefono.pack()
    listaObjetosInfoPaciente.append(lVerInfoPacienteTelefono)
    Correos="Correos:  "
    for correo in PacienteActual.listaCorreos:
        if correo==PacienteActual.listaCorreos[-1]:
            Correos=Correos+correo
        else:
            Correos=Correos+correo+", "
    lVerInfoPacienteCorreo=Label(vVerInfoPaciente,font=('Cambria',14),bg="lightblue",text=Correos)
    lVerInfoPacienteCorreo.pack()
    listaObjetosInfoPaciente.append(lVerInfoPacienteCorreo)
    FechaNacimiento="Fecha de Nacimiento:  "+PacienteActual.fechaNacimiento
    lVerInfoPacienteNacimiento=Label(vVerInfoPaciente,font=('Cambria',14),bg="lightblue",text=FechaNacimiento)
    lVerInfoPacienteNacimiento.pack()
    listaObjetosInfoPaciente.append(lVerInfoPacienteNacimiento)
    Direccion="Direccion:  "+PacienteActual.direccion
    lVerInfoPacienteDireccion=Label(vVerInfoPaciente,font=('Cambria',14),bg="lightblue",text=Direccion)
    lVerInfoPacienteDireccion.pack()
    listaObjetosInfoPaciente.append(lVerInfoPacienteDireccion)
    Ocupacion="Ocupacion:  "+PacienteActual.ocupacion
    lVerInfoPacienteOcupacion=Label(vVerInfoPaciente,font=('Cambria',14),bg="lightblue",text=Ocupacion)
    lVerInfoPacienteOcupacion.pack()
    listaObjetosInfoPaciente.append(lVerInfoPacienteOcupacion)
    mostrar(vVerInfoPaciente)
        
v0=Tk()
v0.title("Agenda Medica")
v0.geometry("500x500")
v0.config(bg="lightblue")
labWelcome=Label(v0,font=('Cambria',14),bg="lightblue",text="Que Desea Hacer")
labWelcome.pack()
bVerDoctores=Button(v0,text="Ver Info Doctores",command=lambda:mostrar(vDoctores) or ocultar(v0))
bVerDoctores.pack()
bVerPacientes=Button(v0,text="Ver Info Pacientes",command=lambda:mostrar(vPacientes) or ocultar(v0))
bVerPacientes.pack()
bVerCitas=Button(v0,text="Administrar Citas",command=lambda:mostrar(vOpcionCitas) or ocultar(v0))
bVerCitas.pack()
bSalir=Button(v0,text="Salir",command=lambda:salir())
bSalir.pack()

vDoctores=Toplevel(v0)
vDoctores.config(bg="lightblue")
vDoctores.title("Doctores")
vDoctores.geometry("500x500")
vDoctores.withdraw()

ListBoxDoctores=Listbox(vDoctores)
ListBoxDoctores.pack()

bAgregarDoctor=Button(vDoctores,text="Agregar Nuevo Doctor",command=lambda:mostrar(vAgregarDoctor) or ocultar(vDoctores))
bAgregarDoctor.pack()

bEliminarDoctor=Button(vDoctores,text="Eliminar Doctor",command=lambda:seleccionarDoctor(ListBoxDoctores.get(ListBoxDoctores.curselection()),ListBoxDoctores.curselection()) or mostrar(vConfirmarEliminarDoctor) or ocultar(vDoctores))
bEliminarDoctor.pack()

bVerInfoDoctores=Button(vDoctores,text="Ver Informacion",command=lambda:mostrarInfoDoctor(ListBoxDoctores.get(ListBoxDoctores.curselection())) or ocultar(vDoctores) or seleccionarDoctor(ListBoxDoctores.get(ListBoxDoctores.curselection()),ListBoxDoctores.curselection()))
bVerInfoDoctores.pack()

bBuscarDoctor=Button(vDoctores,text="Buscar Doctor",command=lambda:mostrar(vBuscarDoctor) or ocultar(vDoctores))
bBuscarDoctor.pack()

bInicioDoctores=Button(vDoctores,text="Volver al Inicio",command=lambda:mostrar(v0) or ocultar(vDoctores))
bInicioDoctores.pack()

vAgregarDoctor=Toplevel(v0)
vAgregarDoctor.config(bg="lightblue")
vAgregarDoctor.title("Agregar nuevo doctor")
vAgregarDoctor.geometry("500x700")
vAgregarDoctor.withdraw()

lNombreDoctor=Label(vAgregarDoctor,font=('Cambria',14),bg="lightblue",text="Digite el nombre del Doctor")
lNombreDoctor.pack()
vsNombreDoctor=StringVar()
eNombreDoctor=Entry(vAgregarDoctor,textvariable=vsNombreDoctor,width=20)
eNombreDoctor.pack()
lIdentificacionDoctor=Label(vAgregarDoctor,font=('Cambria',14),bg="lightblue",text="Digite el numero de Identificacion del Doctor")
lIdentificacionDoctor.pack()
vsIdentificacionDoctor=StringVar()
eIdentificacionDoctor=Entry(vAgregarDoctor,textvariable=vsIdentificacionDoctor,width=20)
eIdentificacionDoctor.pack()
lCorreosDoctor=Label(vAgregarDoctor,font=('Cambria',14),bg="lightblue",text="Digite uno o mas correos del Doctor")
lCorreosDoctor.pack()
vsCorreoDoctor1=StringVar()
eCorreoDoctor1=Entry(vAgregarDoctor,textvariable=vsCorreoDoctor1,width=20)
eCorreoDoctor1.pack()
vsCorreoDoctor2=StringVar()
eCorreoDoctor2=Entry(vAgregarDoctor,textvariable=vsCorreoDoctor2,width=20)
eCorreoDoctor2.pack()
vsCorreoDoctor3=StringVar()
eCorreoDoctor3=Entry(vAgregarDoctor,textvariable=vsCorreoDoctor3,width=20)
eCorreoDoctor3.pack()
lTelefonosDoctor=Label(vAgregarDoctor,font=('Cambria',14),bg="lightblue",text="Digite uno o mas telefonos del Doctor")
lTelefonosDoctor.pack()
vsTelefonoDoctor1=StringVar()
eTelefonoDoctor1=Entry(vAgregarDoctor,textvariable=vsTelefonoDoctor1,width=20)
eTelefonoDoctor1.pack()
vsTelefonoDoctor2=StringVar()
eTelefonoDoctor2=Entry(vAgregarDoctor,textvariable=vsTelefonoDoctor2,width=20)
eTelefonoDoctor2.pack()
vsTelefonoDoctor3=StringVar()
eTelefonoDoctor3=Entry(vAgregarDoctor,textvariable=vsTelefonoDoctor3,width=20)
eTelefonoDoctor3.pack()
lfnacimientoDoctor=Label(vAgregarDoctor,font=('Cambria',14),bg="lightblue",text="Digite la fecha de nacimiento del Doctor")
lfnacimientoDoctor.pack()
vsfnacimientoDoctor=StringVar()
efnacimientoDoctor=Entry(vAgregarDoctor,textvariable=vsfnacimientoDoctor,width=20)
efnacimientoDoctor.pack()
lDireccionDoctor=Label(vAgregarDoctor,font=('Cambria',14),bg="lightblue",text="Digite la direccion del Doctor")
lDireccionDoctor.pack()
vsDireccionDoctor=StringVar()
eDireccionDoctor=Entry(vAgregarDoctor,textvariable=vsDireccionDoctor,width=20)
eDireccionDoctor.pack()
lEspecialidadDoctor=Label(vAgregarDoctor,font=('Cambria',14),bg="lightblue",text="Digite la especialidad del Doctor")
lEspecialidadDoctor.pack()
vsEspecialidadDoctor=StringVar()
eEspecialidadDoctor=Entry(vAgregarDoctor,textvariable=vsEspecialidadDoctor,width=20)
eEspecialidadDoctor.pack()
bAgregarDoctor=Button(vAgregarDoctor,text="Agregar",command=lambda:agregarDoctor(vsNombreDoctor.get(),vsIdentificacionDoctor.get(),vsCorreoDoctor1.get(),vsCorreoDoctor2.get(),vsCorreoDoctor3.get(),vsTelefonoDoctor1.get(),vsTelefonoDoctor2.get(),vsTelefonoDoctor3.get(),vsfnacimientoDoctor.get(),vsDireccionDoctor.get(),vsEspecialidadDoctor.get(),listaDoctores) or ocultar(vAgregarDoctor))
bAgregarDoctor.pack()
bVolverDoctores=Button(vAgregarDoctor,text="Volver a Informacion de Doctores",command=lambda:mostrar(vDoctores) or ocultar(vAgregarDoctor))
bVolverDoctores.pack()

vModificarDoctor=Toplevel(v0)
vModificarDoctor.config(bg="lightblue")
vModificarDoctor.title("Modificar Doctor")
vModificarDoctor.geometry("500x700")
vModificarDoctor.withdraw()

lNombreDoctor2=Label(vModificarDoctor,font=('Cambria',14),bg="lightblue",text="Digite el nombre del Doctor")
lNombreDoctor2.pack()
vsNombreDoctor2=StringVar()
eNombreDoctor2=Entry(vModificarDoctor,textvariable=vsNombreDoctor2,width=20)
eNombreDoctor2.pack()
lIdentificacionDoctor2=Label(vModificarDoctor,font=('Cambria',14),bg="lightblue",text="Digite el numero de Identificacion del Doctor")
lIdentificacionDoctor2.pack()
vsIdentificacionDoctor2=StringVar()
eIdentificacionDoctor2=Entry(vModificarDoctor,textvariable=vsIdentificacionDoctor2,width=20)
eIdentificacionDoctor2.pack()
lCorreosDoctor2=Label(vModificarDoctor,font=('Cambria',14),bg="lightblue",text="Digite uno o mas correos del Doctor")
lCorreosDoctor2.pack()
vsCorreoDoctor1_2=StringVar()
eCorreoDoctor1_2=Entry(vModificarDoctor,textvariable=vsCorreoDoctor1_2,width=20)
eCorreoDoctor1_2.pack()
vsCorreoDoctor2_2=StringVar()
eCorreoDoctor2_2=Entry(vModificarDoctor,textvariable=vsCorreoDoctor2_2,width=20)
eCorreoDoctor2_2.pack()
vsCorreoDoctor3_2=StringVar()
eCorreoDoctor3_2=Entry(vModificarDoctor,textvariable=vsCorreoDoctor3_2,width=20)
eCorreoDoctor3_2.pack()
lTelefonosDoctor_2=Label(vModificarDoctor,font=('Cambria',14),bg="lightblue",text="Digite uno o mas telefonos del Doctor")
lTelefonosDoctor_2.pack()
vsTelefonoDoctor1_2=StringVar()
eTelefonoDoctor1_2=Entry(vModificarDoctor,textvariable=vsTelefonoDoctor1_2,width=20)
eTelefonoDoctor1_2.pack()
vsTelefonoDoctor2_2=StringVar()
eTelefonoDoctor2_2=Entry(vModificarDoctor,textvariable=vsTelefonoDoctor2_2,width=20)
eTelefonoDoctor2_2.pack()
vsTelefonoDoctor3_2=StringVar()
eTelefonoDoctor3_2=Entry(vModificarDoctor,textvariable=vsTelefonoDoctor3_2,width=20)
eTelefonoDoctor3_2.pack()
lfnacimientoDoctor2=Label(vModificarDoctor,font=('Cambria',14),bg="lightblue",text="Digite la fecha de nacimiento del Doctor")
lfnacimientoDoctor2.pack()
vsfnacimientoDoctor2=StringVar()
efnacimientoDoctor2=Entry(vModificarDoctor,textvariable=vsfnacimientoDoctor2,width=20)
efnacimientoDoctor2.pack()
lDireccionDoctor2=Label(vModificarDoctor,font=('Cambria',14),bg="lightblue",text="Digite la direccion del Doctor")
lDireccionDoctor2.pack()
vsDireccionDoctor2=StringVar()
eDireccionDoctor2=Entry(vModificarDoctor,textvariable=vsDireccionDoctor2,width=20)
eDireccionDoctor2.pack()
lEspecialidadDoctor2=Label(vModificarDoctor,font=('Cambria',14),bg="lightblue",text="Digite la especialidad del Doctor")
lEspecialidadDoctor2.pack()
vsEspecialidadDoctor2=StringVar()
eEspecialidadDoctor2=Entry(vModificarDoctor,textvariable=vsEspecialidadDoctor2,width=20)
eEspecialidadDoctor2.pack()
bGuardarCambiosDoctor=Button(vModificarDoctor,text="Guardar Cambios",command=lambda:modificarInfoDoctor(vsNombreDoctor2.get(),vsIdentificacionDoctor2.get(),vsCorreoDoctor1_2.get(),vsCorreoDoctor2_2.get(),vsCorreoDoctor3_2.get(),vsTelefonoDoctor1_2.get(),vsTelefonoDoctor2_2.get(),vsTelefonoDoctor3_2.get(),vsfnacimientoDoctor2.get(),vsDireccionDoctor2.get(),vsEspecialidadDoctor2.get()) or ocultar(vModificarDoctor))
bGuardarCambiosDoctor.pack()
bVolverDoctores2=Button(vModificarDoctor,text="Volver a Informacion de Doctores",command=lambda:olvidarGrids(listaObjetosInfoDoctor) or mostrar(vDoctores) or ocultar(vModificarDoctor))
bVolverDoctores2.pack()

vDoctorModificado=Toplevel(v0)
vDoctorModificado.config(bg="lightblue")
vDoctorModificado.title("Doctor Modificado")
vDoctorModificado.geometry("500x500")
vDoctorModificado.withdraw()

lDoctorModificado=Label(vDoctorModificado,font=('Cambria',14),bg="lightblue",text="La informacion ha sido modificada")
lDoctorModificado.pack()

bDoctorModificado=Button(vDoctorModificado,text="Aceptar",command=lambda:olvidarGrids(listaObjetosInfoDoctor) or actualizarListboxDoctores() or ocultar(vDoctorModificado))
bDoctorModificado.pack()

vFaltaInfoDoctor=Toplevel(v0)
vFaltaInfoDoctor.config(bg="lightblue")
vFaltaInfoDoctor.title("Falta Informacion")
vFaltaInfoDoctor.geometry("500x500")
vFaltaInfoDoctor.withdraw()

lFaltaInfoDoctor=Label(vFaltaInfoDoctor,font=('Cambria',14),bg="lightblue",text="Complete todos los espacios")
lFaltaInfoDoctor.pack()

bAceptarFaltaInfoDoctor=Button(vFaltaInfoDoctor,text="Aceptar",command=lambda:mostrar(vAgregarDoctor) or ocultar(vFaltaInfoDoctor))
bAceptarFaltaInfoDoctor.pack()

vFaltaInfoDoctor2=Toplevel(v0)
vFaltaInfoDoctor2.config(bg="lightblue")
vFaltaInfoDoctor2.title("Falta Informacion")
vFaltaInfoDoctor2.geometry("500x150")
vFaltaInfoDoctor2.withdraw()

lFaltaInfoDoctor2=Label(vFaltaInfoDoctor2,font=('Cambria',14),bg="lightblue",text="Complete todos los espacios")
lFaltaInfoDoctor2.pack()

bAceptarFaltaInfoDoctor2=Button(vFaltaInfoDoctor,text="Aceptar",command=lambda:mostrar(vModificarDoctor) or ocultar(vFaltaInfoDoctor2))
bAceptarFaltaInfoDoctor2.pack()

vDoctorRepetido=Toplevel(v0)
vDoctorRepetido.config(bg="lightblue")
vDoctorRepetido.title("Doctor existente")
vDoctorRepetido.geometry("500x150")
vDoctorRepetido.withdraw()

lDoctorRepetido=Label(vDoctorRepetido,font=('Cambria',14),bg="lightblue",text="Ya existe un Doctor con esta identificacion")
lDoctorRepetido.pack()

bDoctorRepetido=Button(vDoctorRepetido,text="Aceptar",command=lambda:mostrar(vAgregarDoctor) or ocultar(vDoctorRepetido))
bDoctorRepetido.pack()

vNombreDoctorRepetido=Toplevel(v0)
vNombreDoctorRepetido.config(bg="lightblue")
vNombreDoctorRepetido.title("Doctor existente")
vNombreDoctorRepetido.geometry("500x150")
vNombreDoctorRepetido.withdraw()

lNombreDoctorRepetido=Label(vNombreDoctorRepetido,font=('Cambria',14),bg="lightblue",text="Ya existe un Doctor con este nombre")
lNombreDoctorRepetido.pack()

bNombreDoctorRepetido=Button(vNombreDoctorRepetido,text="Aceptar",command=lambda:mostrar(vAgregarDoctor) or ocultar(vNombreDoctorRepetido))
bNombreDoctorRepetido.pack()

vNombreDoctorRepetido2=Toplevel(v0)
vNombreDoctorRepetido2.config(bg="lightblue")
vNombreDoctorRepetido2.title("Doctor existente")
vNombreDoctorRepetido2.geometry("500x150")
vNombreDoctorRepetido2.withdraw()

lNombreDoctorRepetido2=Label(vNombreDoctorRepetido2,font=('Cambria',14),bg="lightblue",text="Ya existe un Doctor con este nombre")
lNombreDoctorRepetido2.pack()

bNombreDoctorRepetido2=Button(vNombreDoctorRepetido2,text="Aceptar",command=lambda:mostrar(vModificarDoctor) or ocultar(vNombreDoctorRepetido2))
bNombreDoctorRepetido2.pack()

vDoctorRepetido2=Toplevel(v0)
vDoctorRepetido2.config(bg="lightblue")
vDoctorRepetido2.title("Doctor existente")
vDoctorRepetido2.geometry("500x150")
vDoctorRepetido2.withdraw()

lDoctorRepetido2=Label(vDoctorRepetido2,font=('Cambria',14),bg="lightblue",text="Ya existe un Doctor con esta identificacion")
lDoctorRepetido2.pack()

bDoctorRepetido2=Button(vDoctorRepetido2,text="Aceptar",command=lambda:mostrar(vModificarDoctor) or ocultar(vDoctorRepetido2))
bDoctorRepetido2.pack()

vInfoDoctorRepetida=Toplevel(v0)
vInfoDoctorRepetida.config(bg="lightblue")
vInfoDoctorRepetida.title("Informacion Repetida")
vInfoDoctorRepetida.geometry("500x150")
vInfoDoctorRepetida.withdraw()

lInfoDoctorRepetida=Label(vInfoDoctorRepetida,font=('Cambria',14),bg="lightblue",text="Ha digitado informacion repetida")
lInfoDoctorRepetida.pack()

bInfoDoctorRepetida=Button(vInfoDoctorRepetida,text="Aceptar",command=lambda:mostrar(vAgregarDoctor) or ocultar(vInfoDoctorRepetida))
bInfoDoctorRepetida.pack()

vInfoDoctorRepetida2=Toplevel(v0)
vInfoDoctorRepetida2.config(bg="lightblue")
vInfoDoctorRepetida2.title("Informacion Repetida")
vInfoDoctorRepetida2.geometry("500x150")
vInfoDoctorRepetida2.withdraw()

lInfoDoctorRepetida2=Label(vInfoDoctorRepetida2,font=('Cambria',14),bg="lightblue",text="Ha digitado informacion repetida")
lInfoDoctorRepetida2.pack()

bInfoDoctorRepetida2=Button(vInfoDoctorRepetida2,text="Aceptar",command=lambda:mostrar(vModificarDoctor) or ocultar(vInfoDoctorRepetida2))
bInfoDoctorRepetida2.pack()

vDoctorAgregado=Toplevel(v0)
vDoctorAgregado.config(bg="lightblue")
vDoctorAgregado.title("Doctor Agregado")
vDoctorAgregado.geometry("500x150")
vDoctorAgregado.withdraw()

lDoctorAgregado=Label(vDoctorAgregado,font=('Cambria',14),bg="lightblue",text="Doctor Agregado Exitosamente!")
lDoctorAgregado.pack()

bAceptarDoctorAgregado=Button(vDoctorAgregado,text="Aceptar",command=lambda:limpiarEntryDoctores() or mostrar(vDoctores) or ocultar(vDoctorAgregado))
bAceptarDoctorAgregado.pack()

vConfirmarEliminarDoctor=Toplevel(v0)
vConfirmarEliminarDoctor.config(bg="lightblue")
vConfirmarEliminarDoctor.title("Confirmar")
vConfirmarEliminarDoctor.geometry("500x150")
vConfirmarEliminarDoctor.withdraw()

lConfirmarEliminarDoctor=Label(vConfirmarEliminarDoctor,font=('Cambria',14),bg="lightblue",text="Estas seguro que deseas eliminar toda la informacion de este Doctor?")
lConfirmarEliminarDoctor.pack()

bAceptarEliminarDoctor=Button(vConfirmarEliminarDoctor,text="Aceptar",command=lambda:eliminarDoctor() or ocultar(vConfirmarEliminarDoctor))
bAceptarEliminarDoctor.pack()

bCancelarEliminarDoctor=Button(vConfirmarEliminarDoctor,text="Cancelar",command=lambda:mostrar(vDoctores) or ocultar(vConfirmarEliminarDoctor))
bCancelarEliminarDoctor.pack()

vDoctorEliminado=Toplevel(v0)
vDoctorEliminado.config(bg="lightblue")
vDoctorEliminado.title("Doctor Eliminado")
vDoctorEliminado.geometry("500x150")
vDoctorEliminado.withdraw()

lDoctorEliminado=Label(vDoctorEliminado,font=('Cambria',14),bg="lightblue",text="Doctor Eliminado Correctamente")
lDoctorEliminado.pack()

bAceptarDoctorEliminado=Button(vDoctorEliminado,text="Aceptar",command=lambda:mostrar(vDoctores) or ocultar(vDoctorEliminado))
bAceptarDoctorEliminado.pack()

vDoctorEncontrado=Toplevel(v0)
vDoctorEncontrado.config(bg="lightblue")
vDoctorEncontrado.title("Doctor Encontrado")
vDoctorEncontrado.geometry("500x150")
vDoctorEncontrado.withdraw()

lDoctorEncontrado=Label(vDoctorEncontrado,font=('Cambria',14),bg="lightblue",text="Doctor Encontrado")
lDoctorEncontrado.pack()

bDoctorEncontrado=Button(vDoctorEncontrado,text="Aceptar",command=lambda:mostrarInfoDoctor(DoctorTemporal) or limpiar(vsIdentificacionBuscarDoctor) or  ocultar(vDoctorEncontrado))
bDoctorEncontrado.pack()

vDoctorNoEncontrado=Toplevel(v0)
vDoctorNoEncontrado.config(bg="lightblue")
vDoctorNoEncontrado.title("No existe ningun Doctor con esa Identificacion")
vDoctorNoEncontrado.geometry("500x150")
vDoctorNoEncontrado.withdraw()

lDoctorNoEncontrado=Label(vDoctorNoEncontrado,font=('Cambria',14),bg="lightblue",text="No existe ningun Doctor con esa Identificacion")
lDoctorNoEncontrado.pack()

bDoctorNoEncontrado=Button(vDoctorNoEncontrado,text="Aceptar",command=lambda:mostrar(vDoctores) or limpiar(vsIdentificacionBuscarDoctor) or ocultar(vDoctorNoEncontrado))
bDoctorNoEncontrado.pack()

vVerInfoDoctor=Toplevel(v0)
vVerInfoDoctor.config(bg="lightblue")
vVerInfoDoctor.title("Informacion del Doctor")
vVerInfoDoctor.geometry("500x500")
vVerInfoDoctor.withdraw()

bRegresarVerInfoDoctor=Button(vVerInfoDoctor,text="Regresar",command=lambda:olvidarGrids(listaObjetosInfoDoctor) or mostrar(vDoctores) or ocultar(vVerInfoDoctor))
bRegresarVerInfoDoctor.pack()

bModificarInfoDoctor2=Button(vVerInfoDoctor,text="Modificar la Informacion",command=lambda:mostrarDatosDoctorModificar() or ocultar(vVerInfoDoctor))
bModificarInfoDoctor2.pack()

bVerCitasDoctor=Button(vVerInfoDoctor,text="Ver Citas",command=lambda:mostrarCitasDoctor(DoctorTemporal) or ocultar(vVerInfoDoctor))
bVerCitasDoctor.pack()

lVerInfoDoctor=Label(vVerInfoDoctor,font=('Cambria',14),bg="lightblue",text="Informacion del Doctor")
lVerInfoDoctor.pack()

vBuscarDoctor=Toplevel(v0)
vBuscarDoctor.config(bg="lightblue")
vBuscarDoctor.title("Buscar Doctor")
vBuscarDoctor.geometry("500x500")
vBuscarDoctor.withdraw()

lBuscarDoctor=Label(vBuscarDoctor,font=('Cambria',14),bg="lightblue",text="Digite la identificacion del Doctor a buscar")
lBuscarDoctor.pack()

vsIdentificacionBuscarDoctor=StringVar()
eBuscarDoctor=Entry(vBuscarDoctor,textvariable=vsIdentificacionBuscarDoctor,width=20)
eBuscarDoctor.pack()

bAceptarBuscarDoctor=Button(vBuscarDoctor,text="Aceptar",command=lambda:buscar_doctor(vsIdentificacionBuscarDoctor.get()) or ocultar(vBuscarDoctor))
bAceptarBuscarDoctor.pack()

bRegresarBuscarDoctor=Button(vBuscarDoctor,text="Regresar",command=lambda:mostrar(vDoctores) or ocultar(vBuscarDoctor))
bRegresarBuscarDoctor.pack()

vPacientes=Toplevel(v0)
vPacientes.config(bg="lightblue")
vPacientes.title("Pacientes")
vPacientes.geometry("500x500")
vPacientes.withdraw()

ListBoxPacientes=Listbox(vPacientes)
ListBoxPacientes.pack()

bAgregarPaciente=Button(vPacientes,text="Agregar Nuevo Paciente",command=lambda:mostrar(vAgregarPaciente) or ocultar(vPacientes))
bAgregarPaciente.pack()

bEliminarPaciente=Button(vPacientes,text="Eliminar Paciente",command=lambda:seleccionarPaciente(ListBoxPacientes.get(ListBoxPacientes.curselection()),ListBoxPacientes.curselection()) or mostrar(vConfirmarEliminarPaciente) or ocultar(vPacientes))
bEliminarPaciente.pack()

bVerInfoPacientes=Button(vPacientes,text="Ver Informacion",command=lambda:mostrarInfoPaciente(ListBoxPacientes.get(ListBoxPacientes.curselection())) or ocultar(vPacientes) or seleccionarPaciente(ListBoxPacientes.get(ListBoxPacientes.curselection()),ListBoxPacientes.curselection()))
bVerInfoPacientes.pack()

bBuscarPaciente=Button(vPacientes,text="Buscar Paciente",command=lambda:mostrar(vBuscarPaciente) or ocultar(vPacientes))
bBuscarPaciente.pack()

bInicioPacientes=Button(vPacientes,text="Volver al Inicio",command=lambda:mostrar(v0) or ocultar(vPacientes))
bInicioPacientes.pack()

vAgregarPaciente=Toplevel(v0)
vAgregarPaciente.config(bg="lightblue")
vAgregarPaciente.title("Agregar nuevo Paciente")
vAgregarPaciente.geometry("500x700")
vAgregarPaciente.withdraw()

lNombrePaciente=Label(vAgregarPaciente,font=('Cambria',14),bg="lightblue",text="Digite el nombre del Paciente")
lNombrePaciente.pack()
vsNombrePaciente=StringVar()
eNombrePaciente=Entry(vAgregarPaciente,textvariable=vsNombrePaciente,width=20)
eNombrePaciente.pack()
lIdentificacionPaciente=Label(vAgregarPaciente,font=('Cambria',14),bg="lightblue",text="Digite el numero de Identificacion del Paciente")
lIdentificacionPaciente.pack()
vsIdentificacionPaciente=StringVar()
eIdentificacionPaciente=Entry(vAgregarPaciente,textvariable=vsIdentificacionPaciente,width=20)
eIdentificacionPaciente.pack()
lCorreosPaciente=Label(vAgregarPaciente,font=('Cambria',14),bg="lightblue",text="Digite uno o mas correos del Paciente")
lCorreosPaciente.pack()
vsCorreoPaciente1=StringVar()
eCorreoPaciente1=Entry(vAgregarPaciente,textvariable=vsCorreoPaciente1,width=20)
eCorreoPaciente1.pack()
vsCorreoPaciente2=StringVar()
eCorreoPaciente2=Entry(vAgregarPaciente,textvariable=vsCorreoPaciente2,width=20)
eCorreoPaciente2.pack()
vsCorreoPaciente3=StringVar()
eCorreoPaciente3=Entry(vAgregarPaciente,textvariable=vsCorreoPaciente3,width=20)
eCorreoPaciente3.pack()
lTelefonosPaciente=Label(vAgregarPaciente,font=('Cambria',14),bg="lightblue",text="Digite uno o mas telefonos del Paciente")
lTelefonosPaciente.pack()
vsTelefonoPaciente1=StringVar()
eTelefonoPaciente1=Entry(vAgregarPaciente,textvariable=vsTelefonoPaciente1,width=20)
eTelefonoPaciente1.pack()
vsTelefonoPaciente2=StringVar()
eTelefonoPaciente2=Entry(vAgregarPaciente,textvariable=vsTelefonoPaciente2,width=20)
eTelefonoPaciente2.pack()
vsTelefonoPaciente3=StringVar()
eTelefonoPaciente3=Entry(vAgregarPaciente,textvariable=vsTelefonoPaciente3,width=20)
eTelefonoPaciente3.pack()
lfnacimientoPaciente=Label(vAgregarPaciente,font=('Cambria',14),bg="lightblue",text="Digite la fecha de nacimiento del Paciente")
lfnacimientoPaciente.pack()
vsfnacimientoPaciente=StringVar()
efnacimientoPaciente=Entry(vAgregarPaciente,textvariable=vsfnacimientoPaciente,width=20)
efnacimientoPaciente.pack()
lDireccionPaciente=Label(vAgregarPaciente,font=('Cambria',14),bg="lightblue",text="Digite la direccion del Paciente")
lDireccionPaciente.pack()
vsDireccionPaciente=StringVar()
eDireccionPaciente=Entry(vAgregarPaciente,textvariable=vsDireccionPaciente,width=20)
eDireccionPaciente.pack()
lOcupacionPaciente=Label(vAgregarPaciente,font=('Cambria',14),bg="lightblue",text="Digite la ocupacion del Paciente")
lOcupacionPaciente.pack()
vsOcupacionPaciente=StringVar()
eOcupacionPaciente=Entry(vAgregarPaciente,textvariable=vsOcupacionPaciente,width=20)
eOcupacionPaciente.pack()
bAgregarPaciente=Button(vAgregarPaciente,text="Agregar",command=lambda:agregarPaciente(vsNombrePaciente.get(),vsIdentificacionPaciente.get(),vsCorreoPaciente1.get(),vsCorreoPaciente2.get(),vsCorreoPaciente3.get(),vsTelefonoPaciente1.get(),vsTelefonoPaciente2.get(),vsTelefonoPaciente3.get(),vsfnacimientoPaciente.get(),vsDireccionPaciente.get(),vsOcupacionPaciente.get(),listaPacientes) or ocultar(vAgregarPaciente))
bAgregarPaciente.pack()
bVolverPacientes=Button(vAgregarPaciente,text="Volver a Informacion de Pacientes",command=lambda:mostrar(vPacientes) or ocultar(vAgregarPaciente))
bVolverPacientes.pack()

vModificarPaciente=Toplevel(v0)
vModificarPaciente.config(bg="lightblue")
vModificarPaciente.title("Modificar Paciente")
vModificarPaciente.geometry("500x700")
vModificarPaciente.withdraw()

lNombrePaciente2=Label(vModificarPaciente,font=('Cambria',14),bg="lightblue",text="Digite el nombre del Paciente")
lNombrePaciente2.pack()
vsNombrePaciente2=StringVar()
eNombrePaciente2=Entry(vModificarPaciente,textvariable=vsNombrePaciente2,width=20)
eNombrePaciente2.pack()
lIdentificacionPaciente2=Label(vModificarPaciente,font=('Cambria',14),bg="lightblue",text="Digite el numero de Identificacion del Paciente")
lIdentificacionPaciente2.pack()
vsIdentificacionPaciente2=StringVar()
eIdentificacionPaciente2=Entry(vModificarPaciente,textvariable=vsIdentificacionPaciente2,width=20)
eIdentificacionPaciente2.pack()
lCorreosPaciente2=Label(vModificarPaciente,font=('Cambria',14),bg="lightblue",text="Digite uno o mas correos del Paciente")
lCorreosPaciente2.pack()
vsCorreoPaciente1_2=StringVar()
eCorreoPaciente1_2=Entry(vModificarPaciente,textvariable=vsCorreoPaciente1_2,width=20)
eCorreoPaciente1_2.pack()
vsCorreoPaciente2_2=StringVar()
eCorreoPaciente2_2=Entry(vModificarPaciente,textvariable=vsCorreoPaciente2_2,width=20)
eCorreoPaciente2_2.pack()
vsCorreoPaciente3_2=StringVar()
eCorreoPaciente3_2=Entry(vModificarPaciente,textvariable=vsCorreoPaciente3_2,width=20)
eCorreoPaciente3_2.pack()
lTelefonosPaciente_2=Label(vModificarPaciente,font=('Cambria',14),bg="lightblue",text="Digite uno o mas telefonos del Paciente")
lTelefonosPaciente_2.pack()
vsTelefonoPaciente1_2=StringVar()
eTelefonoPaciente1_2=Entry(vModificarPaciente,textvariable=vsTelefonoPaciente1_2,width=20)
eTelefonoPaciente1_2.pack()
vsTelefonoPaciente2_2=StringVar()
eTelefonoPaciente2_2=Entry(vModificarPaciente,textvariable=vsTelefonoPaciente2_2,width=20)
eTelefonoPaciente2_2.pack()
vsTelefonoPaciente3_2=StringVar()
eTelefonoPaciente3_2=Entry(vModificarPaciente,textvariable=vsTelefonoPaciente3_2,width=20)
eTelefonoPaciente3_2.pack()
lfnacimientoPaciente2=Label(vModificarPaciente,font=('Cambria',14),bg="lightblue",text="Digite la fecha de nacimiento del Paciente")
lfnacimientoPaciente2.pack()
vsfnacimientoPaciente2=StringVar()
efnacimientoPaciente2=Entry(vModificarPaciente,textvariable=vsfnacimientoPaciente2,width=20)
efnacimientoPaciente2.pack()
lDireccionPaciente2=Label(vModificarPaciente,font=('Cambria',14),bg="lightblue",text="Digite la direccion del Paciente")
lDireccionPaciente2.pack()
vsDireccionPaciente2=StringVar()
eDireccionPaciente2=Entry(vModificarPaciente,textvariable=vsDireccionPaciente2,width=20)
eDireccionPaciente2.pack()
lOcupacionPaciente2=Label(vModificarPaciente,font=('Cambria',14),bg="lightblue",text="Digite la ocupacion del Paciente")
lOcupacionPaciente2.pack()
vsOcupacionPaciente2=StringVar()
eOcupacionPaciente2=Entry(vModificarPaciente,textvariable=vsOcupacionPaciente2,width=20)
eOcupacionPaciente2.pack()
bGuardarCambiosPaciente=Button(vModificarPaciente,text="Guardar Cambios",command=lambda:modificarInfoPaciente(vsNombrePaciente2.get(),vsIdentificacionPaciente2.get(),vsCorreoPaciente1_2.get(),vsCorreoPaciente2_2.get(),vsCorreoPaciente3_2.get(),vsTelefonoPaciente1_2.get(),vsTelefonoPaciente2_2.get(),vsTelefonoPaciente3_2.get(),vsfnacimientoPaciente2.get(),vsDireccionPaciente2.get(),vsOcupacionPaciente2.get()) or ocultar(vModificarPaciente))
bGuardarCambiosPaciente.pack()
bVolverPacientes2=Button(vModificarPaciente,text="Volver a Informacion de Pacientes",command=lambda:olvidarGrids(listaObjetosInfoPaciente) or mostrar(vPacientes) or ocultar(vModificarPaciente))
bVolverPacientes2.pack()

vPacienteModificado=Toplevel(v0)
vPacienteModificado.config(bg="lightblue")
vPacienteModificado.title("Paciente Modificado")
vPacienteModificado.geometry("500x150")
vPacienteModificado.withdraw()

lPacienteModificado=Label(vPacienteModificado,font=('Cambria',14),bg="lightblue",text="La informacion ha sido modificada")
lPacienteModificado.pack()

bPacienteModificado=Button(vPacienteModificado,text="Aceptar",command=lambda:olvidarGrids(listaObjetosInfoPaciente) or actualizarListboxPacientes() or ocultar(vPacienteModificado))
bPacienteModificado.pack()

vFaltaInfoPaciente=Toplevel(v0)
vFaltaInfoPaciente.config(bg="lightblue")
vFaltaInfoPaciente.title("Falta Informacion")
vFaltaInfoPaciente.geometry("500x150")
vFaltaInfoPaciente.withdraw()

lFaltaInfoPaciente=Label(vFaltaInfoPaciente,font=('Cambria',14),bg="lightblue",text="Complete todos los espacios")
lFaltaInfoPaciente.pack()

bAceptarFaltaInfoPaciente=Button(vFaltaInfoPaciente,text="Aceptar",command=lambda:mostrar(vAgregarPaciente) or ocultar(vFaltaInfoPaciente))
bAceptarFaltaInfoPaciente.pack()

vFaltaInfoPaciente2=Toplevel(v0)
vFaltaInfoPaciente2.config(bg="lightblue")
vFaltaInfoPaciente2.title("Falta Informacion")
vFaltaInfoPaciente2.geometry("500x150")
vFaltaInfoPaciente2.withdraw()

lFaltaInfoPaciente2=Label(vFaltaInfoPaciente2,font=('Cambria',14),bg="lightblue",text="Complete todos los espacios")
lFaltaInfoPaciente2.pack()

bAceptarFaltaInfoPaciente2=Button(vFaltaInfoPaciente,text="Aceptar",command=lambda:mostrar(vModificarPaciente) or ocultar(vFaltaInfoPaciente2))
bAceptarFaltaInfoPaciente2.pack()

vPacienteRepetido=Toplevel(v0)
vPacienteRepetido.config(bg="lightblue")
vPacienteRepetido.title("Paciente existente")
vPacienteRepetido.geometry("500x150")
vPacienteRepetido.withdraw()

lPacienteRepetido=Label(vPacienteRepetido,font=('Cambria',14),bg="lightblue",text="Ya existe un Paciente con esta identificacion")
lPacienteRepetido.pack()

bPacienteRepetido=Button(vPacienteRepetido,text="Aceptar",command=lambda:mostrar(vAgregarPaciente) or ocultar(vPacienteRepetido))
bPacienteRepetido.pack()

vNombrePacienteRepetido=Toplevel(v0)
vNombrePacienteRepetido.config(bg="lightblue")
vNombrePacienteRepetido.title("Paciente existente")
vNombrePacienteRepetido.geometry("500x150")
vNombrePacienteRepetido.withdraw()

lNombrePacienteRepetido=Label(vNombrePacienteRepetido,font=('Cambria',14),bg="lightblue",text="Ya existe un Paciente con este nombre")
lNombrePacienteRepetido.pack()

bNombrePacienteRepetido=Button(vNombrePacienteRepetido,text="Aceptar",command=lambda:mostrar(vAgregarPaciente) or ocultar(vNombrePacienteRepetido))
bNombrePacienteRepetido.pack()

vNombrePacienteRepetido2=Toplevel(v0)
vNombrePacienteRepetido2.config(bg="lightblue")
vNombrePacienteRepetido2.title("Paciente existente")
vNombrePacienteRepetido2.geometry("500x150")
vNombrePacienteRepetido2.withdraw()

lNombrePacienteRepetido2=Label(vNombrePacienteRepetido2,font=('Cambria',14),bg="lightblue",text="Ya existe un Paciente con este nombre")
lNombrePacienteRepetido2.pack()

bNombrePacienteRepetido2=Button(vNombrePacienteRepetido2,text="Aceptar",command=lambda:mostrar(vModificarPaciente) or ocultar(vNombrePacienteRepetido2))
bNombrePacienteRepetido2.pack()

vPacienteRepetido2=Toplevel(v0)
vPacienteRepetido2.config(bg="lightblue")
vPacienteRepetido2.title("Paciente existente")
vPacienteRepetido2.geometry("500x150")
vPacienteRepetido2.withdraw()

lPacienteRepetido2=Label(vPacienteRepetido2,font=('Cambria',14),bg="lightblue",text="Ya existe un Paciente con esta identificacion")
lPacienteRepetido2.pack()

bPacienteRepetido2=Button(vPacienteRepetido2,text="Aceptar",command=lambda:mostrar(vModificarPaciente) or ocultar(vPacienteRepetido2))
bPacienteRepetido2.pack()

vInfoPacienteRepetida=Toplevel(v0)
vInfoPacienteRepetida.config(bg="lightblue")
vInfoPacienteRepetida.title("Informacion Repetida")
vInfoPacienteRepetida.geometry("500x150")
vInfoPacienteRepetida.withdraw()

lInfoPacienteRepetida=Label(vInfoPacienteRepetida,font=('Cambria',14),bg="lightblue",text="Ha digitado informacion repetida")
lInfoPacienteRepetida.pack()

bInfoPacienteRepetida=Button(vInfoPacienteRepetida,text="Aceptar",command=lambda:mostrar(vAgregarPaciente) or ocultar(vInfoPacienteRepetida))
bInfoPacienteRepetida.pack()

vInfoPacienteRepetida2=Toplevel(v0)
vInfoPacienteRepetida2.config(bg="lightblue")
vInfoPacienteRepetida2.title("Informacion Repetida")
vInfoPacienteRepetida2.geometry("500x150")
vInfoPacienteRepetida2.withdraw()

lInfoPacienteRepetida2=Label(vInfoPacienteRepetida2,font=('Cambria',14),bg="lightblue",text="Ha digitado informacion repetida")
lInfoPacienteRepetida2.pack()

bInfoPacienteRepetida2=Button(vInfoPacienteRepetida2,text="Aceptar",command=lambda:mostrar(vModificarPaciente) or ocultar(vInfoPacienteRepetida2))
bInfoPacienteRepetida2.pack()

vPacienteAgregado=Toplevel(v0)
vPacienteAgregado.config(bg="lightblue")
vPacienteAgregado.title("Paciente Agregado")
vPacienteAgregado.geometry("500x150")
vPacienteAgregado.withdraw()

lPacienteAgregado=Label(vPacienteAgregado,font=('Cambria',14),bg="lightblue",text="Paciente Agregado Exitosamente!")
lPacienteAgregado.pack()

bAceptarPacienteAgregado=Button(vPacienteAgregado,text="Aceptar",command=lambda:limpiarEntryPacientes() or mostrar(vPacientes) or ocultar(vPacienteAgregado))
bAceptarPacienteAgregado.pack()

vConfirmarEliminarPaciente=Toplevel(v0)
vConfirmarEliminarPaciente.config(bg="lightblue")
vConfirmarEliminarPaciente.title("Confirmar")
vConfirmarEliminarPaciente.geometry("500x150")
vConfirmarEliminarPaciente.withdraw()

lConfirmarEliminarPaciente=Label(vConfirmarEliminarPaciente,font=('Cambria',14),bg="lightblue",text="Estas seguro que deseas eliminar toda la informacion de este Paciente?")
lConfirmarEliminarPaciente.pack()

bAceptarEliminarPaciente=Button(vConfirmarEliminarPaciente,text="Aceptar",command=lambda:eliminarPaciente() or ocultar(vConfirmarEliminarPaciente))
bAceptarEliminarPaciente.pack()

bCancelarEliminarPaciente=Button(vConfirmarEliminarPaciente,text="Cancelar",command=lambda:mostrar(vPacientes) or ocultar(vConfirmarEliminarPaciente))
bCancelarEliminarPaciente.pack()

vPacienteEliminado=Toplevel(v0)
vPacienteEliminado.config(bg="lightblue")
vPacienteEliminado.title("Paciente Eliminado")
vPacienteEliminado.geometry("500x150")
vPacienteEliminado.withdraw()

lPacienteEliminado=Label(vPacienteEliminado,font=('Cambria',14),bg="lightblue",text="Paciente Eliminado Correctamente")
lPacienteEliminado.pack()

bAceptarPacienteEliminado=Button(vPacienteEliminado,text="Aceptar",command=lambda:mostrar(vPacientes) or ocultar(vPacienteEliminado))
bAceptarPacienteEliminado.pack()

vPacienteEncontrado=Toplevel(v0)
vPacienteEncontrado.config(bg="lightblue")
vPacienteEncontrado.title("Paciente Encontrado")
vPacienteEncontrado.geometry("500x150")
vPacienteEncontrado.withdraw()

lPacienteEncontrado=Label(vPacienteEncontrado,font=('Cambria',14),bg="lightblue",text="Paciente Encontrado")
lPacienteEncontrado.pack()

bPacienteEncontrado=Button(vPacienteEncontrado,text="Aceptar",command=lambda:mostrarInfoPaciente(PacienteTemporal) or limpiar(vsIdentificacionBuscarPaciente) or  ocultar(vPacienteEncontrado))
bPacienteEncontrado.pack()

vPacienteNoEncontrado=Toplevel(v0)
vPacienteNoEncontrado.config(bg="lightblue")
vPacienteNoEncontrado.title("No existe ningun Paciente con esa Identificacion")
vPacienteNoEncontrado.geometry("500x150")
vPacienteNoEncontrado.withdraw()

lPacienteNoEncontrado=Label(vPacienteNoEncontrado,font=('Cambria',14),bg="lightblue",text="No existe ningun Paciente con esa Identificacion")
lPacienteNoEncontrado.pack()

bPacienteNoEncontrado=Button(vPacienteNoEncontrado,text="Aceptar",command=lambda:mostrar(vPacientes) or limpiar(vsIdentificacionBuscarPaciente) or ocultar(vPacienteNoEncontrado))
bPacienteNoEncontrado.pack()

vVerInfoPaciente=Toplevel(v0)
vVerInfoPaciente.config(bg="lightblue")
vVerInfoPaciente.title("Informacion del Paciente")
vVerInfoPaciente.geometry("500x500")
vVerInfoPaciente.withdraw()

bRegresarVerInfoPaciente=Button(vVerInfoPaciente,text="Regresar",command=lambda:olvidarGrids(listaObjetosInfoPaciente) or mostrar(vPacientes) or ocultar(vVerInfoPaciente))
bRegresarVerInfoPaciente.pack()

bModificarInfoPaciente2=Button(vVerInfoPaciente,text="Modificar la Informacion",command=lambda:mostrarDatosPacienteModificar() or ocultar(vVerInfoPaciente))
bModificarInfoPaciente2.pack()

bVerListaTratamientos=Button(vVerInfoPaciente,text="Ver tratamientos",command=lambda:mostrarTratamientos() or ocultar(vVerInfoPaciente))
bVerListaTratamientos.pack()

bVerCitas=Button(vVerInfoPaciente,text="Ver Citas",command=lambda:mostrarCitasPaciente(PacienteTemporal) or ocultar(vVerInfoPaciente))
bVerCitas.pack()

lVerInfoPaciente=Label(vVerInfoPaciente,font=('Cambria',14),bg="lightblue",text="Informacion del Paciente")
lVerInfoPaciente.pack()

vBuscarPaciente=Toplevel(v0)
vBuscarPaciente.config(bg="lightblue")
vBuscarPaciente.title("Buscar Paciente")
vBuscarPaciente.geometry("500x500")
vBuscarPaciente.withdraw()

lBuscarPaciente=Label(vBuscarPaciente,font=('Cambria',14),bg="lightblue",text="Digite la identificacion del Paciente a buscar")
lBuscarPaciente.pack()

vsIdentificacionBuscarPaciente=StringVar()
eBuscarPaciente=Entry(vBuscarPaciente,textvariable=vsIdentificacionBuscarPaciente,width=20)
eBuscarPaciente.pack()

bAceptarBuscarPaciente=Button(vBuscarPaciente,text="Aceptar",command=lambda:buscar_paciente(vsIdentificacionBuscarPaciente.get()) or ocultar(vBuscarPaciente))
bAceptarBuscarPaciente.pack()

bRegresarBuscarPaciente=Button(vBuscarPaciente,text="Regresar",command=lambda:mostrar(vPacientes) or ocultar(vBuscarPaciente))
bRegresarBuscarPaciente.pack()

vOpcionCitas=Toplevel(v0)
vOpcionCitas.config(bg="lightblue")
vOpcionCitas.title("Citas")
vOpcionCitas.geometry("500x500")
vOpcionCitas.withdraw()

bAgregarCita=Button(vOpcionCitas,text="Agregar Una Nueva Cita",command=lambda:mostrar(vAgregarCita) or ocultar(vOpcionCitas))
bAgregarCita.pack()

bCitasPorDia=Button(vOpcionCitas,text="Mostrar Citas por Dia",command=lambda:mostrar(vCitasPorDia) or ocultar(vOpcionCitas))
bCitasPorDia.pack()

bCitasPendientes=Button(vOpcionCitas,text="Mostrar Todas las citas pendientes",command=lambda:mostrarCitasPendientes() or ocultar(vOpcionCitas))
bCitasPendientes.pack()

bCitasRealizadas=Button(vOpcionCitas,text="Mostrar Todas las citas realizadas",command=lambda:mostrarCitasRealizadas() or ocultar(vOpcionCitas))
bCitasRealizadas.pack()

bVolverInicioCitas=Button(vOpcionCitas,text="Volver al Inicio",command=lambda:mostrar(v0) or ocultar(vOpcionCitas))
bVolverInicioCitas.pack()

vAgregarCita=Toplevel(v0)
vAgregarCita.config(bg="lightblue")
vAgregarCita.title("Agregar Cita")
vAgregarCita.geometry("500x500")
vAgregarCita.withdraw()

lSeleccioneDoctor=Label(vAgregarCita,text="Seleccion un Doctor",font=('Cambria',14),bg="lightblue")
lSeleccioneDoctor.pack()

ListBoxDoctores2=Listbox(vAgregarCita)
ListBoxDoctores2.pack()

bSeleccionarDoctorCita=Button(vAgregarCita,text="Seleccionar",command=lambda:seleccionarDoctor(ListBoxDoctores2.get(ListBoxDoctores2.curselection()),ListBoxDoctores2.curselection()) or mostrar(vAgregarCita2) or ocultar(vAgregarCita))
bSeleccionarDoctorCita.pack()

bVolverInfoCitas1=Button(vAgregarCita,text="Volver a Citas",command=lambda:mostrar(vOpcionCitas) or ocultar(vAgregarCita))
bVolverInfoCitas1.pack()

vAgregarCita2=Toplevel(v0)
vAgregarCita2.config(bg="lightblue")
vAgregarCita2.title("Agregar Cita")
vAgregarCita2.geometry("500x500")
vAgregarCita2.withdraw()

lSeleccionePaciente=Label(vAgregarCita2,text="Seleccion un Paciente",font=('Cambria',14),bg="lightblue")
lSeleccionePaciente.pack()

ListBoxPacientes2=Listbox(vAgregarCita2)
ListBoxPacientes2.pack()

bSeleccionarPacienteCita=Button(vAgregarCita2,text="Seleccionar",command=lambda:seleccionarPaciente(ListBoxPacientes2.get(ListBoxPacientes2.curselection()),ListBoxPacientes2.curselection()) or mostrar(vAgregarCita3) or ocultar(vAgregarCita2))
bSeleccionarPacienteCita.pack()

bVolverInfoCitas2=Button(vAgregarCita2,text="Volver a Citas",command=lambda:mostrar(vOpcionCitas) or ocultar(vAgregarCita2))
bVolverInfoCitas2.pack()

vAgregarCita3=Toplevel(v0)
vAgregarCita3.config(bg="lightblue")
vAgregarCita3.title("Agregar Cita")
vAgregarCita3.geometry("500x500")
vAgregarCita3.withdraw()

lDigiteFecha=Label(vAgregarCita3,text="Digite la fecha (dd/mm/aaaa)",font=('Cambria',14),bg="lightblue")
lDigiteFecha.pack()

vsFechaCita=StringVar()
eFechaCita=Entry(vAgregarCita3,textvariable=vsFechaCita,width=20)
eFechaCita.pack()

lDigiteHora=Label(vAgregarCita3,text="Digite la Hora",font=('Cambria',14),bg="lightblue")
lDigiteHora.pack()

vsHoraCita=StringVar()
eHoraCita=Entry(vAgregarCita3,textvariable=vsHoraCita,width=20)
eHoraCita.pack()

bAgregarCita=Button(vAgregarCita3,text="Agregar Cita",command=lambda:agregarCita(vsFechaCita.get(),vsHoraCita.get(),PacienteTemporal,DoctorTemporal,listaCitas) or ocultar(vAgregarCita3))
bAgregarCita.pack()

bVolverInfoCitas3=Button(vAgregarCita3,text="Volver a Citas",command=lambda:mostrar(vOpcionCitas) or ocultar(vAgregarCita3) or limpiarEntryCitas())
bVolverInfoCitas3.pack()

vFaltaInfoCita=Toplevel(v0)
vFaltaInfoCita.config(bg="lightblue")
vFaltaInfoCita.title("Complete Todos los Espacios")
vFaltaInfoCita.geometry("500x300")
vFaltaInfoCita.withdraw()

lFaltaInfoCita=Label(vFaltaInfoCita,text="Complete Todos los Espacios!",font=('Cambria',14),bg="lightblue")
lFaltaInfoCita.pack()

bAceptarFaltaInfoCita=Button(vFaltaInfoCita,text="Aceptar",command=lambda:mostrar(vAgregarCita3) or ocultar(vFaltaInfoCita))
bAceptarFaltaInfoCita.pack()

vDoctorOcupado=Toplevel(v0)
vDoctorOcupado.config(bg="lightblue")
vDoctorOcupado.title("Doctor Ocupado")
vDoctorOcupado.geometry("500x300")
vDoctorOcupado.withdraw()

lDoctorOcupado=Label(vDoctorOcupado,text="El Doctor Seleccionado ya tiene una cita en esa Fecha y Hora",font=('Cambria',14),bg="lightblue")
lDoctorOcupado.pack()

bAceptarDoctorOcupado=Button(vDoctorOcupado,text="Aceptar",command=lambda:mostrar(vOpcionCitas) or ocultar(vDoctorOcupado))
bAceptarDoctorOcupado.pack()

vPacienteOcupado=Toplevel(v0)
vPacienteOcupado.config(bg="lightblue")
vPacienteOcupado.title("Paciente Ocupado")
vPacienteOcupado.geometry("500x300")
vPacienteOcupado.withdraw()

lPacienteOcupado=Label(vPacienteOcupado,text="El Paciente Seleccionado ya tiene una cita en esa Fecha y Hora",font=('Cambria',14),bg="lightblue")
lPacienteOcupado.pack()

bAceptarPacienteOcupado=Button(vPacienteOcupado,text="Aceptar",command=lambda:mostrar(vOpcionCitas) or ocultar(vPacienteOcupado))
bAceptarPacienteOcupado.pack()

vCitaAgregada=Toplevel(v0)
vCitaAgregada.config(bg="lightblue")
vCitaAgregada.title("Cita Agregada")
vCitaAgregada.geometry("500x300")
vCitaAgregada.withdraw()

lCitaAgregada=Label(vCitaAgregada,text="La cita ha sido agregada!",font=('Cambria',14),bg="lightblue")
lCitaAgregada.pack()

bAceptarCitaAgregada=Button(vCitaAgregada,text="Aceptar",command=lambda:mostrar(vOpcionCitas) or ocultar(vCitaAgregada))
bAceptarCitaAgregada.pack()

vCitasPorDia=Toplevel(v0)
vCitasPorDia.config(bg="lightblue")
vCitasPorDia.title("Seleccione Fecha")
vCitasPorDia.geometry("500x500")
vCitasPorDia.withdraw()

lSeleccioneFecha=Label(vCitasPorDia,text="Seleccione una fecha",font=('Cambria',14),bg="lightblue")
lSeleccioneFecha.pack()

ListBoxFechas=Listbox(vCitasPorDia)
ListBoxFechas.pack()

bSeleccionarFechaCita=Button(vCitasPorDia,text="Seleccionar",command=lambda:mostrarCitasPorDia(ListBoxFechas.get(ListBoxFechas.curselection()))or ocultar(vCitasPorDia))
bSeleccionarFechaCita.pack()

bVolverInfoCitas4=Button(vCitasPorDia,text="Volver a Citas",command=lambda:mostrar(vOpcionCitas) or ocultar(vCitasPorDia))
bVolverInfoCitas4.pack()

vCitas=Toplevel(v0)
vCitas.config(bg="lightblue")
vCitas.title("Citas")
vCitas.geometry("500x500")
vCitas.withdraw()

bVolverInfoCitas5=Button(vCitas,text="Volver Informacion de Citas",command=lambda:mostrar(vOpcionCitas) or ocultar(vCitas) or olvidarObjetos(listaObjetosInfoCita) or olvidarGrids(listaObjetosInfoPaciente) or olvidarGrids(listaObjetosInfoDoctor))
bVolverInfoCitas5.grid()

vConfirmarCambiarEstadoCita=Toplevel(v0)
vConfirmarCambiarEstadoCita.config(bg="lightblue")
vConfirmarCambiarEstadoCita.title("Cambiar Estado")
vConfirmarCambiarEstadoCita.geometry("450x300")
vConfirmarCambiarEstadoCita.withdraw()

lConfirmarCambiarEstadoCita=Label(vConfirmarCambiarEstadoCita,text="Desea cambiar del estado de la cita a realizada?",font=('Cambria',14),bg="lightblue")
lConfirmarCambiarEstadoCita.pack()

bConfirmarCambiarEstadoCita=Button(vConfirmarCambiarEstadoCita,text="Si",command=lambda:CambiarEstadoCita() or ocultar(vConfirmarCambiarEstadoCita) or olvidarObjetos(listaObjetosInfoCita))
bConfirmarCambiarEstadoCita.pack()
                                   
bConfirmarCambiarEstadoCita2=Button(vConfirmarCambiarEstadoCita,text="No",command=lambda:mostrar(vCitas) or ocultar(vConfirmarCambiarEstadoCita))
bConfirmarCambiarEstadoCita2.pack()

vDeseaAsignarTratamiento=Toplevel(v0)
vDeseaAsignarTratamiento.config(bg="lightblue")
vDeseaAsignarTratamiento.title("Ingresar Tratamiento")
vDeseaAsignarTratamiento.geometry("450x300")
vDeseaAsignarTratamiento.withdraw()

lDeseaIngresarTratamiento=Label(vDeseaAsignarTratamiento,text="Desea Ingresarle un tratamiento al paciente?",font=('Cambria',14),bg="lightblue")
lDeseaIngresarTratamiento.pack()

bDeseaIngresarTratamiento=Button(vDeseaAsignarTratamiento,text="Si",command=lambda:mostrar(vAsignarTratamiento) or ocultar(vDeseaAsignarTratamiento))
bDeseaIngresarTratamiento.pack()
                                   
bDeseaIngresarTratamiento2=Button(vDeseaAsignarTratamiento,text="No",command=lambda:mostrar(vOpcionCitas) or ocultar(vDeseaAsignarTratamiento))
bDeseaIngresarTratamiento2.pack()

vAsignarTratamiento=Toplevel(v0)
vAsignarTratamiento.config(bg="lightblue")
vAsignarTratamiento.title("Asignar Tratamiento")
vAsignarTratamiento.geometry("500x500")
vAsignarTratamiento.withdraw()

lAsignarDescripcionTratamiento=Label(vAsignarTratamiento,text="Digite la descripcion del tratamiento",font=('Cambria',14),bg="lightblue")
lAsignarDescripcionTratamiento.pack()

vsDescripcionTratamiento=StringVar()
eDescripcionTratamiento=Entry(vAsignarTratamiento,textvariable=vsDescripcionTratamiento,width=20)
eDescripcionTratamiento.pack()

bAceptarAsignarTratamiento=Button(vAsignarTratamiento,text="Aceptar",command=lambda:asignarTratamiento(vsDescripcionTratamiento.get()) or ocultar(vAsignarTratamiento) or limpiarEntry(vsDescripcionTratamiento))
bAceptarAsignarTratamiento.pack()

vTratamientoAsignado=Toplevel(v0)
vTratamientoAsignado.config(bg="lightblue")
vTratamientoAsignado.title("Ingresar Tratamiento")
vTratamientoAsignado.geometry("500x300")
vTratamientoAsignado.withdraw()

lTratamientoAsignado=Label(vTratamientoAsignado,text="El Tratamiento ha sido Asignado",font=('Cambria',14),bg="lightblue")
lTratamientoAsignado.pack()

bTratamientoAsignado=Button(vTratamientoAsignado,text="Aceptar",command=lambda:mostrar(vOpcionCitas) or ocultar(vTratamientoAsignado))
bTratamientoAsignado.pack()

vFaltaInfoDescripcion=Toplevel(v0)
vFaltaInfoDescripcion.config(bg="lightblue")
vFaltaInfoDescripcion.title("Falta Info")
vFaltaInfoDescripcion.geometry("500x300")
vFaltaInfoDescripcion.withdraw()

lFaltaInfoDescripcion=Label(vFaltaInfoDescripcion,text="Falta Informacion",font=('Cambria',14),bg="lightblue")
lFaltaInfoDescripcion.pack()

bFaltaInfoDescripcion=Button(vFaltaInfoDescripcion,text="Aceptar",command=lambda:mostrar(vAsignarTratamiento) or ocultar(vFaltaInfoDescripcion))
bFaltaInfoDescripcion.pack()

vModificarCita=Toplevel(v0)
vModificarCita.config(bg="lightblue")
vModificarCita.title("Modificar Cita")
vModificarCita.geometry("500x500")
vModificarCita.withdraw()

lModificarFechaCita=Label(vModificarCita,text="Digite la fecha (dd/mm/aaaa)",font=('Cambria',14),bg="lightblue")
lModificarFechaCita.pack()

vsFechaCita2=StringVar()
eFechaCita2=Entry(vModificarCita,textvariable=vsFechaCita2)
eFechaCita2.pack()

lModificarHoraCita=Label(vModificarCita,text="Digite la Hora",font=('Cambria',14),bg="lightblue")
lModificarHoraCita.pack()

vsHoraCita2=StringVar()
eHoraCita2=Entry(vModificarCita,textvariable=vsHoraCita2)
eHoraCita2.pack()

bGuardarCambiosCita=Button(vModificarCita,text="Guardar Cambios",command=lambda:modificarCita(vsFechaCita2.get(),vsHoraCita2.get()) or ocultar(vModificarCita))
bGuardarCambiosCita.pack()

vDoctorOcupado2=Toplevel(v0)
vDoctorOcupado2.config(bg="lightblue")
vDoctorOcupado2.title("Doctor Ocupado")
vDoctorOcupado2.geometry("500x300")
vDoctorOcupado2.withdraw()

lDoctorOcupado2=Label(vDoctorOcupado2,text="El Doctor Seleccionado ya tiene una cita en esa Fecha y Hora",font=('Cambria',14),bg="lightblue")
lDoctorOcupado2.pack()

bAceptarDoctorOcupado2=Button(vDoctorOcupado2,text="Aceptar",command=lambda:mostrar(vModificarCita) or ocultar(vDoctorOcupado2))
bAceptarDoctorOcupado2.pack()

vPacienteOcupado2=Toplevel(v0)
vPacienteOcupado2.config(bg="lightblue")
vPacienteOcupado2.title("Paciente Ocupado")
vPacienteOcupado2.geometry("500x300")
vPacienteOcupado2.withdraw()

lPacienteOcupado2=Label(vPacienteOcupado2,text="El Paciente Seleccionado ya tiene una cita en esa Fecha y Hora",font=('Cambria',14),bg="lightblue")
lPacienteOcupado2.pack()

bAceptarPacienteOcupado2=Button(vPacienteOcupado2,text="Aceptar",command=lambda:mostrar(vModificarCita) or ocultar(vPacienteOcupado2))
bAceptarPacienteOcupado2.pack()

vFaltaInfoCita2=Toplevel(v0)
vFaltaInfoCita2.config(bg="lightblue")
vFaltaInfoCita2.title("Complete Todos los Espacios")
vFaltaInfoCita2.geometry("500x300")
vFaltaInfoCita2.withdraw()

lFaltaInfoCita2=Label(vFaltaInfoCita2,text="Complete Todos los Espacios!",font=('Cambria',14),bg="lightblue")
lFaltaInfoCita2.pack()

bAceptarFaltaInfoCita2=Button(vFaltaInfoCita2,text="Aceptar",command=lambda:mostrar(vModificarCita) or ocultar(vFaltaInfoCita2))
bAceptarFaltaInfoCita2.pack()

vCitaModificada=Toplevel(v0)
vCitaModificada.config(bg="lightblue")
vCitaModificada.title("Cita Modificada")
vCitaModificada.geometry("500x300")
vCitaModificada.withdraw()

lCitaModificada=Label(vCitaModificada,text="La Cita ha sido Modificada",font=('Cambria',14),bg="lightblue")
lCitaModificada.pack()

bCitaModificada=Button(vCitaModificada,text="Aceptar",command=lambda:mostrar(vOpcionCitas) or ocultar(vCitaModificada) or olvidarObjetos(listaObjetosInfoCita))
bCitaModificada.pack()

vCitaEliminada=Toplevel(v0)
vCitaEliminada.config(bg="lightblue")
vCitaEliminada.title("Cita Eliminada")
vCitaEliminada.geometry("500x300")
vCitaEliminada.withdraw()

lCitaEliminada=Label(vCitaEliminada,text="La Cita ha sido Eliminada",font=('Cambria',14),bg="lightblue")
lCitaEliminada.pack()

bCitaEliminada=Button(vCitaEliminada,text="Aceptar",command=lambda:mostrar(v0) or ocultar(vCitaEliminada) or olvidarObjetos(listaObjetosInfoCita))
bCitaEliminada.pack()

vVerTratamientos=Toplevel(v0)
vVerTratamientos.config(bg="lightblue")
vVerTratamientos.title("Ver Tratamientos")
vVerTratamientos.geometry("500x500")
vVerTratamientos.withdraw()

bVerTratamientos=Button(vVerTratamientos,text="Volver",command=lambda:mostrar(vPacientes) or ocultar(vVerTratamientos))
bVerTratamientos.grid()

vTratamientoCancelado=Toplevel(v0)
vTratamientoCancelado.config(bg="lightblue")
vTratamientoCancelado.title("Tratamiento Cancelado")
vTratamientoCancelado.geometry("500x300")
vTratamientoCancelado.withdraw()

lLabel=Label(vTratamientoCancelado,text="El tratamiento ha sido cancelado",font=('Cambria',14),bg="lightblue")
lLabel.pack()

bTratamientoCancelado=Button(vTratamientoCancelado,text="Aceptar",command=lambda:mostrar(vPacientes) or ocultar(vTratamientoCancelado) or olvidarObjetos(listaObjetosInfoTratamientos) or olvidarGrids(listaObjetosInfoPaciente))
bTratamientoCancelado.pack()

cargarArchivoDoctores()
mostrarDoctores()
cargarArchivoPacientes()
mostrarPacientes()
cargarArchivoCitas()
mostrarFechas()
v0.mainloop()
