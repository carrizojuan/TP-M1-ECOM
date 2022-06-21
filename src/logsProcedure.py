from tabulate import tabulate
from log import Log


class LogsProcedure(object):
    def __init__(self, logs):
        self.logs = logs
        self.ips = []
        self.status_codes = []
        self.cant_bytes = 0
        self.menor_bytes = int(logs[0].split(" ")[9])
        self.mayor_bytes = 0
        self.cant_peticiones = 0

    def calc_bytes(self, b):
        return 0 if b == "-" else int(b)

    def add_statuscode(self, s_code):
        hay_code = False
        for s in self.status_codes:
            # Si hubo un log con ese status_code aumento en 1 su cantidad
            if s["code"] == s_code:
                s["cant"] += 1
                hay_code = True
                break
            # Si no hubo un log con ese status code lo inicializo con cantidad 1
        if not hay_code:
            s = {
                "code": s_code,
                "cant": 1
            }
            self.status_codes.append(s)

    def calculate(self):

        for log in self.logs:
            linea = log.split(" ")
            # Seteo variables del log
            ip = linea[0]
            status_code = linea[8]
            bytes = self.calc_bytes(linea[9])
            log = Log(ip, status_code, bytes)

            # Hago el calculo de cantidad de status_code para cada codigo y lo guardo en la lista status_codes
            if status_code.isnumeric():
                self.add_statuscode(log.get_status_code())

            # Solo agrego la ip si no se encuentra en la lista de ips
            if ip not in self.ips:
                self.ips.append(ip)

            # Calculo el menor y mayor byte entre todos los logs
            if log.get_bytes() < self.menor_bytes:
                self.menor_bytes = log.get_bytes()

            if log.get_bytes() > self.mayor_bytes:
                self.mayor_bytes = log.get_bytes()

            self.cant_bytes += log.get_bytes()
            self.cant_peticiones += 1

    def show_data(self):
        print("")
        print(self.get_ip_data())
        print("")
        print(self.get_bytes_data())
        print("")
        print(self.get_status_data())

    def get_bytes_data(self):
        d = [[str(round(self.cant_bytes / self.cant_peticiones, 2)) + " B",
              str(self.mayor_bytes) + " B", str(self.menor_bytes) + " B"]]
        return tabulate(d, headers=["Promedio Bytes", "Mayor valor de bytes", "Menor valor de bytes"])

    def get_status_data(self):
        d = []
        for s in self.status_codes:
            porc = round((s["cant"] / self.cant_peticiones) * 100, 2)
            sd = [s["code"], s["cant"], str(porc) + " %"]
            d.append(sd)
        return tabulate(d, headers=["Status code", "Cant peticiones", "Porcentaje"])

    def get_ip_data(self):
        d = [[len(self.ips)]]
        return tabulate(d, headers=["Cant IPs distintas"])