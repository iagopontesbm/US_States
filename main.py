import turtle as tt
import pandas as pd

screen = tt.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # Adciona imagem as opções de shape
tt.shape(image)  # Vincula o novo shape
map_text = tt.Turtle()  # Texto no mapa

data = pd.read_csv("50_states.csv")  # Leitura e armazenado dados csv
states_list = []  # Lista de estados a serem preenchidos

while len(states_list) != 50:  # Enquanto lista não estiver preenchida
    answer_state = screen.textinput(title=f"{len(states_list)}/50 States Correct",  # Informa numero de acertos
                                    prompt="What's another state's name.").title()  # Conveerte texto para title case
    us_state = data[data.state == answer_state]  # Armazena a series do estado informado
    state_name = False if us_state.empty else us_state.state.item()  # Nome do estado se for encontrado no DataFrame
    if answer_state == state_name:  # Compara resposta informada e Dataframe
        states_list.append(state_name)  # adiciona lista
        x_pos = us_state.x.item()  # Posição X no mapa
        y_pos = us_state.y.item()  # Posição Y no mapa
        # Gerando texto no mapa
        map_text.color("black")
        map_text.penup()
        map_text.goto(x_pos, y_pos)
        map_text.hideturtle()
        map_text.write(answer_state, align="center")
    else:
        continue

print("Congratulations!")

tt.mainloop()
