# Convertidor de Divisas

Este es un programa en Python que permite convertir una cantidad especificada de una moneda a otra utilizando datos de la API FreeCurrencyAPI.

## Características
- Obtener tasas de cambio en tiempo real.
- Mostrar una lista de monedas disponibles.
- Mostrar las tasas de cambio actuales.
- Establecer monedas de origen y destino.
- Convertir cantidades con precisión hasta los centavos.
- Historial de conversiones dentro de la sesión.
- Interfaz de consola con menú interactivo.

## Requisitos
- Python 3.7 o superior
- Una cuenta en [FreeCurrencyAPI](https://freecurrencyapi.com/) para obtener una clave de API.
- Biblioteca `requests` instalada (`pip install requests`).

## Instalación
1. Clona el repositorio o descarga el código fuente:
   ```bash
   git clone https://github.com/tuusuario/convertidor-divisas.git
   cd convertidor-divisas
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
3. Agrega tu clave de API en el archivo `convertidor_divisas.py` reemplazando `TU_API_KEY_AQUI`.

## Uso
Ejecuta el programa con el siguiente comando:
```bash
python convertidor_divisas.py
```
Sigue las instrucciones en pantalla para seleccionar las monedas y realizar conversiones.

## Ejemplo de Conversión
```
=== Convertidor de Divisas ===
1. Mostrar lista de monedas
2. Mostrar tasas de cambio
3. Establecer monedas a convertir
4. Convertir cantidad
5. Ver historial de conversiones
6. Salir
Seleccione una opción: 3
Ingrese la moneda de origen (código, ej. USD): USD
Ingrese la moneda de destino (código, ej. EUR): EUR
Monedas establecidas: USD -> EUR
Seleccione una opción: 4
Ingrese la cantidad a convertir: 100
100 USD = 92.50 EUR
```

## Autor
Juan Guillermo Caicedo Delgado
