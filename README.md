<h1 align="center" id="title">AddressSQL</h1>

<p id="description">Este script automatiza la obtención y generación de archivos con información de estados ciudades y códigos postales.</p>

<h2>🛠️ Installation Steps:</h2>

<p>1. Instalar los requerimientos para ejecutar el script</p>

```
 pip install -r .\requirements.txt
```

## Argumentos

### `-t, --type`
- **Descripción**: Especifica el tipo de archivo de salida.
- **Valores posibles**: `csv` o `sql`.
- **Valor por defecto**: `sql`.
- **Ejemplo de uso**:
  - Para generar archivos CSV: `--type csv`
  - Para generar archivos SQL: `--type sql`

### `-of, --only-file`
- **Descripción**: Indica si solo se debe generar un archivo con la información.
- **Tipo**: `booleano` (se activa si está presente en la línea de comandos).
- **Ejemplo de uso**: 
  - Si deseas generar un único archivo de salida: `--only-file`

### `-p, --path`
- **Descripción**: Especifica el directorio de origen donde se encuentran los archivos CSV de entrada.
- **Valor por defecto**: `src\files\csv`.
- **Ejemplo de uso**: 
  - Para cambiar el directorio de origen: `--path "ruta/a/tu/directorio"`

### `-o, --output`
- **Descripción**: Define el directorio de salida donde se generarán los archivos resultantes.
- **Valor por defecto**: `src\exports`.
- **Ejemplo de uso**: 
  - Para cambiar la ruta de exportación: `--output "ruta/a/directorio/output"`

### `-e, --engine`
- **Descripción**: Especifica el motor de base de datos para el cual se generarán los scripts SQL.
- **Valores posibles**: `mysql`, `postgres`.
- **Valor por defecto**: `postgres`.
- **Ejemplo de uso**: 
  - Para generar archivos compatibles con MySQL: `--engine mysql`
  - Para PostgreSQL: `--engine postgres`

## Ejemplo de Uso

```bash
python tool-cmd.py --type sql --engine mysql --path "ruta/a/entrada" --output "ruta/a/salida" --only-file