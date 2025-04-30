from num2words import num2words


CONST_PLAZOS_DE_PAGO={"Mensual":1,
                      "Semestral":2,
                      "Vencimiento":3}


CONST_PLAZOS_DE_PAGO_INVERTED = {1: "Mensual", 2: "Semestral", 3: "Vencimiento"}


class Certificado:
    def __init__(self, monto_base,plazo_de_pago=1,plazo_en_meses_vigencia=12,tasa_de_interes=0):
        self.monto_base = monto_base
        self.plazo_de_pago = plazo_de_pago
        self.plazo_en_meses_vigencia=plazo_en_meses_vigencia
        self.tasa_de_interes=tasa_de_interes
        self.intereses = 0
        self.impuestos = 0
        self.intereses_despues_de_deducciones=0
        self.pago_por_periodo=0
        
        

    def calcular_total(self):
         return self.monto_base + self.intereses - self.impuestos

    def calcular_intereses_y_deducciones(self):
        self.intereses=self.monto_base*self.tasa_de_interes/100
        self.impuestos=self.intereses*15/100
        self.intereses_despues_de_deducciones=self.intereses-self.impuestos

        #redonde
        self.intereses=round(self.intereses,2)
        self.impuestos=round(self.impuestos,2)
        self.intereses_despues_de_deducciones=round(self.intereses_despues_de_deducciones,2)

    def deposito_a_realizarse(self):
        if self.plazo_de_pago==1:
            self.pago_por_periodo=self.intereses_despues_de_deducciones/self.plazo_en_meses_vigencia
        elif self.plazo_de_pago==2:
            numero_de_semestres=self.plazo_en_meses_vigencia/6 #6 meses
            self.pago_por_periodo=self.intereses_despues_de_deducciones/numero_de_semestres
        else:
            self.pago_por_periodo=self.intereses_despues_de_deducciones
        self.pago_por_periodo=round(self.pago_por_periodo,2)

    def muestra_datos_del_certificado(self)->None:
        self.calcular_intereses_y_deducciones()
        self.deposito_a_realizarse()
        data=""
        data+=f"\nMonto base del certificado: \u20A1{self.monto_base} {num2words(self.monto_base, lang='es')}\n"
        data+=f"Tasa de interes: {self.tasa_de_interes}%\n"
        data+=f"Intereses acumulados: \u20A1{self.intereses}\n"
        data+=f"Deducciones de impuestos: \u20A1{self.impuestos}\n"
        data+=f"Intereses despues de deducciones: \u20A1{self.intereses_despues_de_deducciones}\n\n"
        data+=f"Plazo de vigencia: {self.plazo_en_meses_vigencia} meses\n"
        data+=f"Periodicidad de los pagos de intereses: {CONST_PLAZOS_DE_PAGO_INVERTED[self.plazo_de_pago]}\n"
        data+=f"Pago por periodo: \u20A1{self.pago_por_periodo}\n"
        print(data)


certificado=Certificado(monto_base=25000000,plazo_de_pago=CONST_PLAZOS_DE_PAGO["Mensual"],
                        plazo_en_meses_vigencia=12,
                        tasa_de_interes=6.5)
certificado.muestra_datos_del_certificado()