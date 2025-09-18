def extract_date_in_sequence(text: str) -> list[str]:
    months = ("январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август",
              "сентябрь", "октябрь", "ноябрь", "декабрь")
    correct_datapiece = ['', '', '']
    result = []
    i = 0
    pieces = text.split(' ')
    for piece in pieces:
        if i==0 and piece.isdigit() and 1 <= int(piece) <= 31:
            correct_datapiece[i] = piece
            i += 1
        elif i==1 and piece.lower() in months:
            correct_datapiece[i] = piece
            i += 1
        elif i==2 and piece.isdigit() and  1000 <= int(piece)<= 9999:
            correct_datapiece[i] = piece
            i = 0
            result.append(' '.join(correct_datapiece))
            correct_datapiece = ['', '', '']
        else:
            i = 0
            correct_datapiece = ['', '', ''] 
    return result 
