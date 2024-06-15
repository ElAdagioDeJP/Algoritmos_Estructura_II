class Proyectos:
    def __init__(self, id,nombre,descripcion,fecha_inicio,fecha_fin,estado,empresa,gerente,equipo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.empresa = empresa
        self.gerente = gerente
        self.equipo = equipo
        listilla = []
    def __str__(self):
        return f'{self.id} {self.nombre} {self.descripcion} {self.fecha_inicio} {self.fecha_fin} {self.estado} {self.empresa} {self.gerente} {self.equipo}'
    def listaentre(self):
        listilla = []
        listilla.append(self.id)
        listilla.append(self.nombre)
        listilla.append(self.descripcion)
        listilla.append(self.fecha_inicio)
        listilla.append(self.fecha_fin)
        listilla.append(self.estado)
        listilla.append(self.empresa)
        listilla.append(self.gerente)
        listilla.append(self.equipo)
        return listilla
proyecto1 = Proyectos(1,"Proyecto 1","Proyecto de prueba","2021-01-01","2021-12-31","Activo","Empresa 1","Gerente 1","Equipo 1")
print(proyecto1.listaentre())