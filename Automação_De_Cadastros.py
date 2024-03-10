import pandas as pa
import pyautogui as pg
import time

pg.PAUSE = 2.5

pg.press("win")
pg.write("microsoft edge")
pg.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pg.write(link)
pg.press("enter")

time.sleep(4)

pg.click(x=477, y=356)
pg.write("Fefeimpressionador2@gmail.com")

pg.press("tab")
pg.write("fefe04")

pg.click(x=677, y=534)

time.sleep(2)

pg.click(x=548, y=239)

tabela = pa.read_csv("produtos.csv")
print(tabela)

time.sleep(2)

for linha in tabela.index:

    pg.click(x=553, y=248)

    codigo = tabela.loc[linha, "codigo"]
    pg.write(codigo)
    pg.press("tab")

    pg.write(tabela.loc[linha, "marca"])
    pg.press("tab")

    pg.write(tabela.loc[linha, "tipo"])
    pg.press("tab")

    pg.write(str(tabela.loc[linha, "categoria"]))
    pg.press("tab")

    pg.write(str(tabela.loc[linha, "preco_unitario"]))
    pg.press("tab")

    pg.write(str(tabela.loc[linha, "custo"]))
    pg.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pa.isna(obs):
        pg.write(obs)
    pg.press("tab")

    pg.press("enter")
    pg.scroll(675)
