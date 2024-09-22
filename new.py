git clone https://github.com/ferchoroller2112/CalculoDescuentoPython.git


# Función que calcula el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Esta función calcula el descuento dado un monto total y un porcentaje de descuento.
    Parámetros:
    monto_total (float): El monto total de la compra.
    porcentaje_descuento (float): El porcentaje de descuento a aplicar. Por defecto es 10%.

    Retorna:
    float: El monto del descuento.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Programa principal
def main():
    # Primera llamada con el porcentaje de descuento predeterminado
    monto1 = 100.0
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    print(f"Monto total: ${monto1:.2f}, Descuento: ${descuento1:.2f}, Monto final a pagar: ${monto_final1:.2f}")

    # Segunda llamada con un porcentaje de descuento personalizado
    monto2 = 200.0
    porcentaje_descuento2 = 15
    descuento2 = calcular_descuento(monto2, porcentaje_descuento2)
    monto_final2 = monto2 - descuento2
    print(f"Monto total: ${monto2:.2f}, Descuento: ${descuento2:.2f}, Monto final a pagar: ${monto_final2:.2f}")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
