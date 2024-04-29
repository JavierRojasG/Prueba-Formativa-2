## Javier Rojas Guerrero ##

def main():
    precios = {
        1: 4500, # Pikachu Roll
        2: 5000, # Otaku Roll
        3: 5200, # Pulpo Venenoso Roll
        4: 4800 # Anguila Eléctrica Roll
    }
    nombres = {
        1: "Pikachu Roll",
        2: "Otaku Roll",
        3: "Pulpo Venenoso Roll",
        4: "Anguila Eléctrica Roll"
    }
    
    pedido = {1: 0, 2: 0, 3: 0, 4: 0}
    
    while True:
        print("Seleccione el Sushi que desea agregar al pedido:")
        for id, nombre in nombres.items():
            print(f"{id}. {nombre} - ${precios[id]}")
        seleccion = int(input("Introduzca el número del roll (1-4): "))
        
        if seleccion in pedido:
            pedido[seleccion] += 1
        else:
            print("Opción no válida, por favor intente de nuevo.")
            continue
        
        continuar = input("¿Desea agregar otro roll? (si/no): ").lower()
        if continuar == 'no':
            break

    descuento_aplicado = 0
    while True:
        tiene_codigo = input("¿Tiene un código de descuento? (si/no): ").lower()
        if tiene_codigo == 'si':
            codigo = input("Introduzca su código de descuento: ")
            if codigo == "soyotaku":
                descuento_aplicado = 0.10 # 10% de descuento
                break
            else:
                print("Código no válido")
                opcion = input("Presione 'X' para cancelar o cualquier otra tecla para reintentar: ").lower()
                if opcion == 'x':
                    break
        else:
            break

    total_productos = sum(pedido.values())
    subtotal = sum(precios[k] * v for k, v in pedido.items())
    descuento = subtotal * descuento_aplicado
    total = subtotal - descuento

    print("******************************")
    print(f"TOTAL PRODUCTOS: {total_productos}")
    print("******************************")
    for k, v in pedido.items():
        if v > 0:
            print(f"{nombres[k]}: {v}")
    print("******************************")
    print(f"Subtotal por pagar: ${subtotal}")
    print(f"Descuento por código: ${descuento:.2f}")
    print(f"TOTAL: ${total:.2f}")
    print("******************************")
    
    repetir = input("¿Desea realizar otro pedido? (si/no): ").lower()
    if repetir == 'si':
        main() 
    else:
        print("Gracias por su pedido. ¡Hasta luego!")

if __name__ == "__main__":
    main()