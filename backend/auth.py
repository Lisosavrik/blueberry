from sql_class import SQLClass


my_SQL = SQLClass("blueberry.db")

def console_training():
    my_SQL.db_connect()

    training_today = my_SQL.training_now()
    if training_today == []:
        print("nothing for today")


    for card in training_today:
        card_id = card[0]

        nxt_well = card[5]
        nxt_very_well = card[6]

        d = {
        "not at all": 0,
        "not well": 1,
        "well": nxt_well,
        "very well": nxt_very_well, 
        }
            


        print(f'Item: {card[1]}')
        input("what is your answer?\n")
        print(f'Meaning: {card[2]}')
        reaction = input('how it was? Not at all, not well, well, very well\n')
        reaction = reaction.lower()
        term = d.get(reaction, 0)

        my_SQL.update_well(term, card_id)
        my_SQL.update_card (term, card_id)
    my_SQL.close_db()


console_training()