import os

class Empresa:
    def __init__(self, nomb='', direc='', telef= '', ruc=''):
        self.nombre = nomb
        self.direccion = direc
        self.telefono = telef
        self.ruc = ruc
    def mostrar(self):   
        print(' Nombre: {}\n Ruc : {}\n Teléfono : {}\n Dirección: {} '.format(self.nombre,self.ruc, self.direccion, self.telefono))


class Departamento:
    def __init__(self, nombre='', id=0):
        self.area = nombre
        self.id = id
    def mostrarDepart(self):
        print('>> DEPARTAMENTO DE {}'.format(self.area))


class Empleado: 
    def __init__(self, nomb='',cedu='', puesto='', dire='',telef=''):
        self.nombre = nomb
        self.cedula = cedu
        self.telefono = telef
        self.puesto = puesto
        self.direccion = dire

    def mostrarEmpleado(self):
        print(' Empleado : {}\n Puesto : {}\n Cedula: {}'.format(self.nombre,self.puesto,self.cedula))


class PagoSobretiempo():   
    def __init__(self, horasexT, pagoH):
        self.horasextrasTrabajadas = horasexT
        self.pagoHoraextras = pagoH
        
    def calculoPago(self):
        cal = self.horasextrasTrabajadas * self.pagoHoraextras
        return cal
        

class PagoNomina:
    def __init__(self,sueldobase):
        self.sueldoBase = sueldobase

    def mostrarPagoNomina(self):
        sobre = sobretiempo.calculoPago()
        print(' Sueldo base: ${}\n Pago Sobretiempo: ${}'.format(self.sueldoBase, sobre))
        print(' NETO A PAGAR: $',self.sueldoBase + sobre )

os.system('cls')
print('Recolección de datos......')
nomEmp = input('Ingrese NOMBRE de empresa: ').upper()
rucEmp = input('Ingrese RUC de empresa: ')
telefEmp = input('Ingrese TELEFONO de empresa: ')
direEmp = input('Ingrese DIRECCION de empresa: ').capitalize()
print('')
nomEmplea = input('Ingrese NOMBRE de empleado: ').capitalize()
nomDepartamento = input('Ingrese nombre de departamento al que pertenece: ').upper()
puestEmplea = input('Ingrese PUESTO de empleado: ').capitalize()
teleEmplea = input('Ingrese CEDULA de empleado: ')
print('')
while True:
    try:
        sueldo = int(input('Ingrese sueldo base: '))
        break
    except ValueError:
        print('Ingrese valor válido.')
ingreso = input(' El empleado a trabajado horas extras? [SI/NO]: ').upper()
if ingreso =='SI':
    while True:
        try:
            hextra = int(input('Ingrese horas extras trabajadas: '))
            pagoh = int(input('Ingrese pago por hora extra: '))
            break
        except ValueError:
            print('Ingrese valor válido.')
else:
    hextra=0
    pagoh=0

os.system('cls')
print('------------------------------------------')
print('    N O M I N A   D E   P A G O')
print('------------------------------------------')
print('>> DATOS DE EMPRESA')
emp = Empresa(nomEmp,direEmp, telefEmp, rucEmp)
emp.mostrar()
print('------------------------------------------')
dep = Departamento(nomDepartamento, id = 1)
dep.mostrarDepart()    
emple = Empleado(nomEmplea,teleEmplea, puestEmplea, dire='Sin dirección', telef='Sin teléfono')
emple.mostrarEmpleado()
print('------------------------------------------')
sobretiempo = PagoSobretiempo(hextra,pagoh)
sobretiempo.calculoPago()
nomina = PagoNomina(sueldo)
nomina.mostrarPagoNomina()
print('------------------------------------------')