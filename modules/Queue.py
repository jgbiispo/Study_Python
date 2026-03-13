from collections import deque


def simulate_queue(customers: list[tuple[str, bool]]) -> list[str]:
    customers_order = []
    vip_count = 0

    for customer, is_vip in customers:
        if is_vip:
            customers_order.insert(vip_count, customer)
            vip_count += 1
        else:
            customers_order.append(customer)

    return customers_order


def run_testes():
    customers = [
        ("João", False),
        ("Maria", True),
        ("Pedro", False),
        ("Ana", True),
    ]

    print(simulate_queue(customers))
