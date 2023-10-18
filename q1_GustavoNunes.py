accounts_data = {
    '123456': 1000,
    '234567': 2000,
    '345678': 1500,
}

account_handler = lambda account_number, data: (
    (
        lambda result: result if result == "Conta não encontrada!" else (
            (
                lambda action, amount, balance: (
                    f"Saldo atual: R${balance + amount}"
                    if action == "depositar"
                    else (
                        "Saque não permitido!"
                        if amount > balance
                        else f"Saldo atual: R${balance - amount}"
                    )
                ) if action in ["depositar", "sacar"] else "Comando inválido"
            )(
                input("Gostaria de depositar ou sacar seu dinheiro?: ").lower(),
                float(input("Insira o valor: ")),
                data.get(account_number, 0)
            )
        )
    )(
        "Conta não encontrada!" if account_number not in data else None
    )
)

account_number = input("Insira o número da sua conta: ")
result = account_handler(account_number, accounts_data)
print(result)
