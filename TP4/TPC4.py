import json

with open("stock.json", "r", encoding="utf-8") as f:
    stock = json.load(f)

print("maq: 2024-03-08, Stock carregado, Estado atualizado.")
print("maq: Bom dia. Estou disponível para atender o seu pedido.")

total_e = 0
total_c = 0

while True:
    input_string = input()

    if input_string.startswith("LISTAR"):

        print("maq:")
        print("cod  | nome                 | quantidade | preço")
        print("------------------------------------------------")

        for produto in stock:
            print(f"{produto['cod']:4} | {produto['nome']:<20} | {produto['quant']:<10} | {produto['preco']:.2f}")

    elif input_string.startswith("MOEDA "):

        lista = input_string.split(" ", 1)
        moedas_str = lista[1]
        moedas = moedas_str.split(",")
        moedas = [m.strip() for m in moedas]
        moedas_validas = ["2e", "1e", "50c", "20c", "10c", "5c", "2c", "1c"]


        for m in moedas:
            if m not in moedas_validas:
                print("Moedas inválidas")
                break
            else: 
                if m[-1] == "e":
                    total_e += int(m[:-1])
                elif m[-1] == "c":
                    total_c += int(m[:-1])
        
        total_e += total_c // 100
        total_c = total_c % 100
        
        print(f"maq: Saldo {total_e}e{total_c}c")

    elif input_string.startswith("SELECIONAR "):
        lista_strs = input_string.split(" ")
        codigo = lista_strs[1]
        codigos_validos = [p["cod"] for p in stock]
        saldo = total_e + total_c / 100
        if len(lista_strs) != 2 or codigo not in codigos_validos:
            print("Seleciona novamente um codigo valido")
        else: 
            codigo = lista_strs[1]
            for produto in stock:
                if produto["cod"] == codigo:
                    if saldo >= produto["preco"]:
                        produto["quant"] -= 1
                        print(f"maq: Pode retirar o produto dispensado {produto['nome']}")
                        saldo = saldo - float(produto["preco"])
                        total_e = int(saldo)
                        total_c = int((saldo - total_e)*100)
                        print(f"maq: Saldo = {total_e}e{total_c}c")
                    else:
                        print("maq: Saldo insuficiente para satisfazer o seu pedido")
                        total_e = int(saldo)
                        total_c = int((saldo - total_e) * 100)
                        pedido_total = produto["preco"]
                        pedido_e = int(pedido_total)
                        pedido_c = int(round((pedido_total - pedido_e) * 100))
                        if pedido_e > 0:
                            pedido_str = f"{pedido_e}e{pedido_c}c"
                        else: 
                            pedido_str = f"{pedido_c}c"
                        print(f"maq: Saldo = {total_e}e{total_c}c; Pedido {pedido_str}")

    elif input_string.startswith("SAIR"):
       
        total_centimos = total_e * 100 + total_c

        moedas_valores = [200, 100, 50, 20, 10, 5, 2, 1]
        moedas_devolvidas = []

        for valor in moedas_valores:
            quantidade = total_centimos // valor
            if quantidade > 0:
                moedas_devolvidas.append((quantidade, valor))
                total_centimos = total_centimos % valor

        troco_str_lista = []
        for q, v in moedas_devolvidas:
            if v >= 100:
                troco_str_lista.append(f"{q}x {v//100}e")
            else:
                troco_str_lista.append(f"{q}x {v}c")

        troco_str = ", ".join(troco_str_lista)

        if troco_str:
            print(f"maq: Pode retirar o troco: {troco_str}.")
        else:
            print("maq: Sem troco a devolver.")

        with open("stock.json", "w", encoding="utf-8") as f:
            json.dump(stock, f, ensure_ascii=False, indent=4)

        print("maq: Até à próxima.")
        break

        

