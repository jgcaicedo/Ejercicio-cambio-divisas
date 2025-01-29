import requests
import sys

def obtener_tasas(api_key):
    """Obtiene las tasas de cambio desde la API."""
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["data"]
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener las tasas de cambio: {e}")
        sys.exit()

def mostrar_menu():
    """Muestra el menú principal de la aplicación."""
    print("\n=== Convertidor de Divisas ===")
    print("1. Mostrar lista de monedas")
    print("2. Mostrar tasas de cambio")
    print("3. Establecer monedas a convertir")
    print("4. Convertir cantidad")
    print("5. Ver historial de conversiones")
    print("6. Salir")

def mostrar_monedas(tasas):
    """Muestra la lista de monedas disponibles."""
    print("\nMonedas disponibles:")
    for moneda in tasas:
        print(moneda)

def mostrar_tasas(tasas):
    """Muestra las tasas de cambio."""
    print("\nTasas de cambio:")
    for moneda, tasa in tasas.items():
        print(f"1 USD = {tasa} {moneda}")

def convertir_cantidad(tasas, moneda_origen, moneda_destino, cantidad):
    """Convierte una cantidad de una moneda a otra."""
    if moneda_origen not in tasas or moneda_destino not in tasas:
        print("Moneda no válida.")
        return None

    tasa_origen = tasas[moneda_origen]
    tasa_destino = tasas[moneda_destino]
    cantidad_en_usd = cantidad / tasa_origen
    cantidad_convertida = cantidad_en_usd * tasa_destino
    return round(cantidad_convertida, 2)

def main():
    api_key = "fca_live_NpkganDTrtF3OhxS3zcA9YzUjgKlThkzsmDCcBho"  # Reemplaza con tu clave de FreeCurrencyAPI
    tasas = obtener_tasas(api_key)
    historial = []
    moneda_origen = None
    moneda_destino = None

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_monedas(tasas)

        elif opcion == "2":
            mostrar_tasas(tasas)

        elif opcion == "3":
            moneda_origen = input("Ingrese la moneda de origen (código, ej. USD): ").upper()
            moneda_destino = input("Ingrese la moneda de destino (código, ej. EUR): ").upper()

            if moneda_origen not in tasas or moneda_destino not in tasas:
                print("Moneda no válida.")
                moneda_origen, moneda_destino = None, None
            else:
                print(f"Monedas establecidas: {moneda_origen} -> {moneda_destino}")

        elif opcion == "4":
            if not moneda_origen or not moneda_destino:
                print("Primero debe establecer las monedas a convertir.")
                continue

            try:
                cantidad = float(input("Ingrese la cantidad a convertir: "))
                if cantidad < 0:
                    raise ValueError("La cantidad debe ser positiva.")
            except ValueError as e:
                print(f"Entrada no válida: {e}")
                continue

            resultado = convertir_cantidad(tasas, moneda_origen, moneda_destino, cantidad)
            if resultado is not None:
                print(f"{cantidad} {moneda_origen} = {resultado} {moneda_destino}")
                historial.append(f"{cantidad} {moneda_origen} -> {resultado} {moneda_destino}")

        elif opcion == "5":
            print("\nHistorial de conversiones:")
            if not historial:
                print("No hay conversiones registradas.")
            else:
                for registro in historial:
                    print(registro)

        elif opcion == "6":
            print("Saliendo del programa. ¡Adiós!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
