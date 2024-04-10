class row:
    def __init__(self, root):
        try:
            self.serie = root.attrib['Serie']
        except KeyError:
            self.serie = ''
        try:
            self.folio = root.attrib['Folio']
        except KeyError:
            self.folio = ''
        try:
            self.rfc = root[0].attrib['Rfc']
        except KeyError:
            self.rfc = root[1].attrib['Rfc']
        try:
            self.nombre = root[0].attrib['Nombre']
        except KeyError:
            self.nombre = root[1].attrib['Nombre']
        self.fecha = root.attrib['Fecha']
        self.subtotal = float(root.attrib['SubTotal'])
        try:
            self.descuento = float(root.attrib['Descuento'])
        except KeyError:
            self.descuento = 0.00
        self.iva = round((float(self.subtotal) - float(self.descuento)) * .16, 2)
        self.total = float(root.attrib['Total'])

        self.descripcion = ''

        for i in range(0,11):
            for j in range(0,11):
                #print(root.attrib['Descripcion'])
                try:
                    self.descripcion += root[i][j].attrib['Descripcion'] + '    '
                except IndexError:
                    pass
                except KeyError:
                    pass

    def to_dict(self):
        return {
                'Serie': str(self.serie),
                'Folio': str(self.folio),
                'RFC': str(self.rfc),
                'Nombre': str(self.nombre),
                'Fecha': str(self.fecha),
                'Subtotal': self.subtotal,
                'Descuento': self.descuento,
                'IVA': self.iva,
                'Total': self.total,
                'Descripcion': str(self.descripcion)
                }