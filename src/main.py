from logsProcedure import LogsProcedure


# Manejo el error en caso de que no exista el archivo
def main():
    hay_archivo = True
    try:
        archivo = open("logs/http_access_200304.log", "r")
        logs = archivo.readlines()
        archivo.close()
    except Exception as e:
        print(e)
        print("No se encuentra el archivo")

    if hay_archivo:
        logsProcedure = LogsProcedure(logs)
        logsProcedure.calculate()
        logsProcedure.show_data()

main()



