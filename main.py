from game import Game

def main():
    rony_game = Game()
    rony_game.start()






# cuando importamos un módulo, python lo ejecuta. Sólo con poner "from directorio import mi_modulo" python ya ejecutó el código contenido en el archivo,
# aunque no hayamos llamado ninguno de los métodos que ahí se encuentren (creo que se debe a que es un lenguaje interpretado, puedes buscar más info sobre eso).
# Entonces, para evitar que se ejecute código que no queremos que se ejecute (todavía), usamos el if name == 'main':
# Esto funciona porque todo archivo de python tiene un atributo name por defecto. Nosotros no lo creamos, python lo hace. Su valor cambia dependiendo de 
# cómo fue ejecutado el archivo. Si el archivo fue ejecutado directamente (cuando hacemos "python mi_archivo.py" en la terminal) el valor de name 
# es "main", en cambio, si el archivo fue ejecutado porque fue importado el valor de name es el nombre del archivo.
# Entonces al hacer if name == 'main': nos aseguramos de que ese código que se esté ejecutando en ese momento sea porque lo
# hayamos llamado y no porque se esté importando.
if __name__ == '__main__':
    main()