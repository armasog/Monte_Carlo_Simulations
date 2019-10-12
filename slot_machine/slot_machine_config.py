lines = 5
symbols = [[1, 2, 3, 4, 5, 6], [4, 5, 6, 1, 2, 3], [3, 5, 6, 1, 2, 4]]

pay_table = {
    # Specifies scenario and the payout as a multiple of the bet
    "2_of_a_kind_any": 0,
    "2_of_a_kind_bronze": 0,
    "2_of_a_kind_silver": 0,
    "2_of_a_kind_gold": 0,
    "3_of_a_kind_any": 5,
    "3_of_a_kind_bronze": 10,
    "3_of_a_kind_silver": 25,
    "3_of_a_kind_gold": 30,
    "special_symbol_bronze": 0,
    "special_symbol_silver": 0,
    "special_symbol_gold": 0,
}

pay_symbols = {
    # Specifies which symbols should be used for payouts
    "gold": 6,
    "silver": 5,
    "bronze": 4,
}
